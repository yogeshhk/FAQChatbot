# Ref: https://github.com/premrajnarkhede/sentence2vec/blob/master/plain%20average%20of%20word%20vectors%20example/sen2vec_plain_average_word_vectors.py

import spacy
import numpy as np

## Todo : this is still working on pretrained model, not corpus specific
class SpacySent2VecGenerator:
    
    def __init__(self, model_dir, size=300):
        self.nlp = spacy.load('en_core_web_sm')
            
    def vectorize(self, clean_questions):
        transformed_X = []
        for question in clean_questions:
            vec = self.nlp(question).vector
            transformed_X.append(vec)
            
        return np.array(transformed_X)
        
    def query(self, clean_usr_msg):
        t_usr= None
        try:
            t_usr = self.nlp(clean_usr_msg).vector
        except Exception as e:
            print(e)
            return "Could not follow your question [" + t_usr + "], Try again"
            
        return np.array([t_usr])