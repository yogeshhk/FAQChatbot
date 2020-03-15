from sklearn.feature_extraction.text import TfidfVectorizer

    
class TfidfVectorGenerator:
    
    def vectorize(self, clean_questions):
        self.vectorizer = TfidfVectorizer(min_df=1, stop_words='english')  
        self.vectorizer.fit(clean_questions)
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
            return "Could not follow your question [" + usr + "], Try again"
            
        return t_usr_array