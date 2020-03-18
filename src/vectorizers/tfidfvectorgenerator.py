import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer


class TfidfVectorGenerator:

    def __init__(self, model_dir, size=100):
        filename = 'tfidf.pkl'

        self.model_dir = model_dir
        if not os.path.exists(self.model_dir):
            os.makedirs(self.model_dir)
        self.model_file_path = os.path.join(self.model_dir, filename)
        self.vec_size = size
        self.vectorizer = None

    def vectorize(self, clean_questions):
        # type: (List) -> List
        if os.path.exists(self.model_file_path):
            with open(self.model_file_path, "rb") as input_file:
                self.vectorizer = pickle.load(input_file)
        else:
            self.vectorizer = TfidfVectorizer(min_df=1, stop_words='english')
            self.vectorizer.fit(clean_questions)
            with open(self.model_file_path, 'wb') as output_file:
                pickle.dump(self.vectorizer, output_file)

        transformed_X = []
        # Getting memory error
        if self.vectorizer:
            # transformed_X = self.vectorizer.transform(clean_questions)
            transformed_X_csr = self.vectorizer.transform(clean_questions)
            transformed_X = transformed_X_csr.A # csr_matrix to numpy matrix
        return transformed_X
        
    def query(self, clean_usr_msg):
        t_usr_array= None
        try:
            t_usr = self.vectorizer.transform([clean_usr_msg])
            t_usr_array = t_usr.toarray()
        except Exception as e:
            print(e)
            return "Could not follow your question [" + t_usr_array + "], Try again"
            
        return t_usr_array