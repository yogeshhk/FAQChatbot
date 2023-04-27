# need to OpenAI api key in to environmental variable.We recommend that you set the name of the variable to OPENAI_API_KEY
from langchain.embeddings import OpenAIEmbeddings
import numpy as np

class OpenAIGenerator:
    
    def __init__(self, model_dir, size=300):
        self.embed = OpenAIEmbeddings()

    def vectorize(self, clean_questions):
        return self.embed.embed_documents(clean_questions)
        
    def query(self, clean_usr_msg):
        t_usr_array= None
        try:
            t_usr_array = self.embed.embed_query(clean_usr_msg)
        except Exception as e:
            print(e)
            return "Could not follow your question [" + t_usr_array + "], Try again"
        return np.array([t_usr_array])
