# Ref: https://github.com/hanxiao/bert-as-service#building-a-qa-semantic-search-engine-in-3-minutes
# need to have bert server running in a separate window
# bert-serving-start -num_worker=1 -model_dir=D:/Yogesh/Education/DataScience/Datasets/uncased_L-12_H-768_A-12 

from bert_serving.client import BertClient
import numpy as np
    
class BertGenerator:
    
    def __init__(self):
        self.bc = BertClient(port=5555, port_out=5556,max_seq_len=None)
            
    def vectorize(self, clean_questions):
        return self.bc.encode(clean_questions)
        
    def query(self, clean_usr_msg):
        t_usr_array= None
        try:
            t_usr_array = self.bc.encode([clean_usr_msg])[0]
        except Exception as e:
            print(e)
            return "Could not follow your question [" + usr + "], Try again"
            
        return np.array([t_usr_array])