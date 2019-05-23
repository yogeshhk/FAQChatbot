import pandas as pd
import numpy as np
import pickle
import operator
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split as tts
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder as LE
from sklearn.metrics.pairwise import cosine_similarity
import random
import nltk
from nltk.stem.lancaster import LancasterStemmer
from tfidfvectorgenerator import TfidfVectorGenerator
from doc2vecgenerator import Doc2VecGenerator



class FaqEngine:
    def __init__(self, faqslist):
        self.faqslist = faqslist
        self.stemmer = LancasterStemmer()
        self.le = LE()
        self.vectorizers = {"tfidf":TfidfVectorGenerator(),"doc2vec":Doc2VecGenerator()}
        self.build_model()
        
        
    def cleanup(self, sentence):
        word_tok = nltk.word_tokenize(sentence)
        stemmed_words = [self.stemmer.stem(w) for w in word_tok]
        return ' '.join(stemmed_words)
        
    def build_model(self):
        
        self.vectorizer = self.vectorizers["doc2vec"]#TfidfVectorizer(min_df=1, stop_words='english')   
        
        dataframeslist = [pd.read_csv(csvfile).dropna() for csvfile in self.faqslist]
        self.data = pd.concat(dataframeslist,  ignore_index=True)
        self.questions = self.data['Question'].values 
                
        questions_cleaned = []
        for question in self.questions:
            questions_cleaned.append(self.cleanup(question)) 
            
        X = self.vectorizer.vectorize(questions_cleaned)
                 
        y = self.data['Class'].values.tolist()
        y = self.le.fit_transform(y)
         
        trainx, testx, trainy, testy = tts(X, y, test_size=.25, random_state=42)
        
        self.model = SVC(kernel='linear')
        self.model.fit(trainx, trainy)
        # print("SVC:", self.model.score(testx, testy))        
        
    def query(self, usr):
        #print("User typed : " + usr)
        try:
            cleaned_usr = self.cleanup(usr)
            t_usr_array = self.vectorizer.query(cleaned_usr)
            prediction = self.model.predict(t_usr_array)[0]
            class_ = self.le.inverse_transform([prediction])[0]
            #print("Class " + class_)
            questionset = self.data[self.data['Class']==class_]
            
            #threshold = 0.7
            cos_sims = []
            for question in questionset['Question']:
                cleaned_question = self.cleanup(question)
                question_arr = self.vectorizer.query(cleaned_question)
                sims = cosine_similarity(question_arr, t_usr_array)
                #if sims > threshold:
                cos_sims.append(sims)
                
            #print("scores " + str(cos_sims))                
            if len(cos_sims) > 0:
                ind = cos_sims.index(max(cos_sims)) 
                #print(ind)
                #print(questionset.index[ind])
                return self.data['Answer'][questionset.index[ind]]
        except Exception as e:
            print(e)
            return "Could not follow your question [" + usr + "], Try again"
    
if __name__ == "__main__":
    faqslist = ["faqs/Greetings.csv", "faqs/GSTFAQs.csv"]
    faqmodel = FaqEngine(faqslist)
    response = faqmodel.query("Hi")
    print(response)
