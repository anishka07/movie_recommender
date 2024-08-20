from paths import Paths

movies_dictionary = Paths.MOVIE_LIST_FROM_PKL.get("title")
cosine_similarity = Paths.COSINE_SIMILARITY_FROM_PKL


def get_movie_list():
    return movies_dictionary.values()


def recommend_movie(movie):
    movie_idx = None
    for idx, title in movies_dictionary.items():
        if title == movie:
            movie_idx = idx
            break
    if movie_idx is None:
        raise ValueError(f"{movie} not in list")
    distances = cosine_similarity[movie_idx]
    sorted_values = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = [movies_dictionary[i[0]] for i in sorted_values]
    return recommended_movies


class Settings:
    GET_MOV_LIST = get_movie_list()