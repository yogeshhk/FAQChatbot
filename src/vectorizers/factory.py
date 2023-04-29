"""
    Interfaces to core functions for Vectorisers docs functionality
"""
import os

from vectorizers.tfidfvectorgenerator import TfidfVectorGenerator
from vectorizers.doc2vecgenerator import Doc2VecGenerator
from vectorizers.spacysent2vecgenerator import SpacySent2VecGenerator
from vectorizers.bertgenerator import BertGenerator
from vectorizers.openaigenerator import OpenAIGenerator


def get_vectoriser(model_name, model_dir_path=os.path.join(os.path.dirname(os.path.abspath( __file__ )),"models")):
    vectoriser = None
    if model_name == "gensim":
        vectoriser = Doc2VecGenerator(model_dir_path)
    elif model_name == "tfidf":
        vectoriser = TfidfVectorGenerator(model_dir_path)
    elif model_name == "spacy":
        vectoriser = SpacySent2VecGenerator(model_dir_path)
    elif model_name == "bert":
        vectoriser = BertGenerator(model_dir_path)
    elif model_name == "openai":
        vectoriser = OpenAIGenerator(model_dir_path)

    return vectoriser
