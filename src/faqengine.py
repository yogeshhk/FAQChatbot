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


class FaqEngine:
    def __init__(self, faqslist, type='tfidf'):
        self.faqslist = faqslist
        self.stemmer = LancasterStemmer()
        self.le = LE()
        self.classifier = None
        #self.doc_emb = None
        self.build_model(type)

    def cleanup(self, sentence):
        word_tok = nltk.word_tokenize(sentence)
        stemmed_words = [self.stemmer.stem(w) for w in word_tok]
        return ' '.join(stemmed_words)

    def build_model(self, type):
        self.vectorizer = get_vectoriser(type)  # TfidfVectorizer(min_df=1, stop_words='english')
        dataframeslist = [pd.read_csv(csvfile).dropna() for csvfile in self.faqslist]
        
        # Data preprocessing and question embedding generation using Pandas apply function
        # Ideally we need to replace this with vector database implementation in future.
        self.data = pd.concat(dataframeslist, ignore_index=True)
        self.data['Clean_Question'] = self.data['Question'].apply(lambda x : self.cleanup(x))
        self.data['Question_embeddings'] = list(self.vectorizer.vectorize(self.data['Clean_Question'].tolist()))
        self.questions = self.data['Question'].values
        X = self.data['Question_embeddings'].tolist()

        #self.vectorizer = get_vectoriser(type)  # TfidfVectorizer(min_df=1, stop_words='english')
        #dataframeslist = [pd.read_csv(csvfile).dropna() for csvfile in self.faqslist]
        
        
        
        # questions_cleaned = []
        # for question in self.questions:
        #     questions_cleaned.append(self.cleanup(question))

        # X = self.vectorizer.vectorize(questions_cleaned)
        # self.doc_emb = self.vectorizer.vectorize(questions_cleaned)
        
        

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
            
            # Instead of loop trying vectorized implementation of cosine similarity with Panda dataframe for fast execution
            cos_sims = cosine_similarity(questionset['Question_embeddings'].tolist(), t_usr_array)
            
            # for question in questionset['Question']:
            #     cleaned_question = self.cleanup(question)
            #     question_arr = self.vectorizer.query(cleaned_question)
            #     sims = cosine_similarity(question_arr, t_usr_array)
            #     # if sims > threshold:
            #     cos_sims.append(sims)

            # print("scores " + str(cos_sims))
            if len(cos_sims) > 0:
                ind = np.argmax(cos_sims)
                return self.data['Answer'][questionset.index[ind]] 
                
                #cos_sims.index(max(cos_sims))
                # print(ind,cos_sims[ind],max(cos_sims))
                # print(questionset.index[ind])
                #return self.data['Answer'][questionset.index[ind]]
        except Exception as e:
            print(e)
            return "Could not follow your question [" + usr + "], Try again"


if __name__ == "__main__":
    base_path = os.path.join(os.path.dirname(os.path.abspath( __file__ )),"data")
    faqslist = [os.path.join(base_path,"Greetings.csv"), os.path.join(base_path,"GST FAQs 2.csv")]
    faqmodel = FaqEngine(faqslist, 'tfidf')
    response = faqmodel.query("Hi")
    print(response)
