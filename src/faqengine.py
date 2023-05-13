import os

import nltk
import pandas as pd
import numpy as np
from nltk.stem.lancaster import LancasterStemmer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import LabelEncoder as LE
from sklearn.svm import SVC

from vectorizers.factory import get_vectoriser

import faiss


class FaqEngine:
    def __init__(self, faqslist, type='tfidf'):
        self.faqslist = faqslist
        self.vector_store = None
        self.stemmer = LancasterStemmer()
        self.le = LE()
        self.classifier = None
        self.build_model(type)

    def cleanup(self, sentence):
        word_tok = nltk.word_tokenize(sentence)
        stemmed_words = [self.stemmer.stem(w) for w in word_tok]
        return ' '.join(stemmed_words)

    def build_model(self, type):

        self.vectorizer = get_vectoriser(type)  # TfidfVectorizer(min_df=1, stop_words='english')
        dataframeslist = [pd.read_csv(csvfile).dropna() for csvfile in self.faqslist]
        self.data = pd.concat(dataframeslist, ignore_index=True)
        self.data['Clean_Question'] = self.data['Question'].apply(lambda x : self.cleanup(x))
        self.data['Question_embeddings'] = list(self.vectorizer.vectorize(self.data['Clean_Question'].tolist()))
        self.questions = self.data['Question'].values
        X = self.data['Question_embeddings'].tolist()
        
        X = np.array(X)
        d = X.shape[1]
        index = faiss.IndexFlatL2(d)
        if index.is_trained :
            index.add(X)
        self.vector_store = index
        # Loop wise version for question embedding generation
        # questions_cleaned = []
        # for question in self.questions:
        #     questions_cleaned.append(self.cleanup(question))

        # X = self.vectorizer.vectorize(questions_cleaned)

        # Under following cases, we dont do classification
        # 'Class' column abscent
        # 'Class' column has same values
        if 'Class' not in list(self.data.columns):
            return

        y = self.data['Class'].values.tolist()
        if len(set(y)) < 2: # 0 or 1
            return

        y = self.le.fit_transform(y)

        trainx, testx, trainy, testy = tts(X, y, test_size=.25, random_state=42)

        self.classifier = SVC(kernel='linear')
        self.classifier.fit(trainx, trainy)
        # print("SVC:", self.model.score(testx, testy))        

    def query(self, usr):
        # print("User typed : " + usr)
        try:
            cleaned_usr = self.cleanup(usr)
            t_usr_array = self.vectorizer.query(cleaned_usr)
            if self.classifier:
                prediction = self.classifier.predict(t_usr_array)[0]
                class_ = self.le.inverse_transform([prediction])[0]
                # print("Class " + class_)
                questionset = self.data[self.data['Class'] == class_]
            else:
                questionset = self.data

            # threshold = 0.7
            
            # Vectorized implementation of cosine similarity usage for fast execution
            #cos_sims = cosine_similarity(questionset['Question_embeddings'].tolist(), t_usr_array)

            # Top most similar question
            top_k = 1
            
            #calling FAISS search
            D, I = self.vector_store.search(t_usr_array, top_k)
            
            question_index = int(I[0][0])
            return self.data['Answer'][question_index]
            
            # Loop wise implementation of cosine similarity usage
            # cos_sims = []
            # for question in questionset['Question']:
            #     cleaned_question = self.cleanup(question)
            #     question_arr = self.vectorizer.query(cleaned_question)
            #     sims = cosine_similarity(question_arr, t_usr_array)
            #     # if sims > threshold:
            #     cos_sims.append(sims)

            # print("scores " + str(cos_sims))
            # commenting this code as we use FAISS vector store. 
            '''if len(cos_sims) > 0:
                ind = np.argmax(cos_sims)
                return self.data['Answer'][questionset.index[ind]]'''
                # ind = cos_sims.index(max(cos_sims))
                # print(ind)
                # print(questionset.index[ind])
                
        except Exception as e:
            print(e)
            return "Could not follow your question [" + usr + "], Try again"


if __name__ == "__main__":
    base_path = os.path.join(os.path.dirname(os.path.abspath( __file__ )),"data")
    faqslist = [os.path.join(base_path,"Greetings.csv"), os.path.join(base_path,"GST FAQs 2.csv")]
    faqmodel = FaqEngine(faqslist, 'tfidf')
    response = faqmodel.query("Hi")
    print(response)
