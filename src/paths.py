import os 
import pickle
import numpy as np 


def get_src_path():
    return os.path.abspath(os.getcwd())


def get_project_dir():
    src_path = get_src_path()
    return os.path.dirname(src_path)


class Paths:
    GET_PROJ_DIR = get_project_dir()
    MOVIE_LIST_FROM_PKL = pickle.load(open(os.path.join(GET_PROJ_DIR, "models/movie_dict.pkl"), "rb"))
    COSINE_SIMILARITY_FROM_PKL = pickle.load(open(os.path.join(GET_PROJ_DIR, "models/cosine_similarity.pkl"), "rb"))