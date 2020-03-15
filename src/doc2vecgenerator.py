import gensim
from gensim import utils
from gensim.models.doc2vec import TaggedDocument
from gensim.models import Doc2Vec
import numpy as np
    
class Doc2VecGenerator:
    
    def vectorize(self, clean_questions):
        prefix = "FAQ"
        taggedDocs = []
        for item_no,question in enumerate(clean_questions):
            tagd = TaggedDocument(gensim.utils.simple_preprocess(question), [prefix + '_%s' % item_no])
            taggedDocs.append(tagd)    
        self.model = Doc2Vec(min_count=1, window=10, size=100, sample=1e-4, negative=5, workers=2)
        self.model.build_vocab(taggedDocs)
        for i in range(800): # 10 if good machine
            print("Iteration {}...".format(i))
            self.model.train(taggedDocs,total_examples=self.model.corpus_count, epochs=self.model.iter)
    
        transformed_X = []
        for item_no,question in enumerate(clean_questions):
            vec = self.model[prefix + '_%s' % item_no] # or model.docvecs[]
            transformed_X.append(vec)
            
        return np.array(transformed_X)
        
    def query(self, clean_usr_msg):
        t_usr_array= None
        try:
            clean_usr_msg = gensim.utils.simple_preprocess(clean_usr_msg)
            t_usr = self.model.infer_vector(clean_usr_msg)
        except Exception as e:
            print(e)
            return "Could not follow your question [" + usr + "], Try again"
            
        return np.array([t_usr])