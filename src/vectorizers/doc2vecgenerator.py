import os

import gensim
import numpy as np
from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
import pickle

class Doc2VecGenerator:

    def __init__(self, model_dir, size=300):
        filename = 'doc2vec.pkl'

        self.model_dir = model_dir
        if not os.path.exists(model_dir):
            os.makedirs(model_dir)
        self.model_file_path = os.path.join(self.model_dir, filename)
        self.vec_size = size
        self.vectorizer = None

    def vectorize(self, clean_questions):
        # type: (List) -> List

        if os.path.exists(self.model_file_path):
            with open(self.model_file_path, "rb") as input_file:
                self.vectorizer = pickle.load(input_file)
        else:
            prefix = "FAQ"
            taggedDocs = []
            for item_no,question in enumerate(clean_questions):
                tagd = TaggedDocument(gensim.utils.simple_preprocess(question), [prefix + '_%s' % item_no])
                taggedDocs.append(tagd)
            self.vectorizer = Doc2Vec(min_count=1, window=10, vector_size=self.vec_size, sample=1e-4, negative=5, workers=2)
            self.vectorizer.build_vocab(taggedDocs)
            for i in range(self.vectorizer.iter): # 5, try 10 if good machine
                print("Iteration {}...".format(i))
                self.vectorizer.train(taggedDocs,total_examples=self.vectorizer.corpus_count, epochs=self.vectorizer.iter)
            with open(self.model_file_path, 'wb') as output_file:
                pickle.dump(self.vectorizer, output_file)

        transformed_X = []
        # Getting memory error
        for item_no,question in enumerate(clean_questions):
            clean_usr_msg = gensim.utils.simple_preprocess(question)
            vec = self.vectorizer.infer_vector(clean_usr_msg)#[prefix + '_%s' % item_no] # or model.docvecs[]
            transformed_X.append(vec)
            
        return np.array(transformed_X)
        
    def query(self, clean_usr_msg):
        t_usr= None
        try:
            clean_usr_msg = gensim.utils.simple_preprocess(clean_usr_msg)
            t_usr = self.vectorizer.infer_vector(clean_usr_msg)
        except Exception as e:
            print(e)
            return "Could not follow your question [" + t_usr + "], Try again"
            
        return np.array([t_usr])