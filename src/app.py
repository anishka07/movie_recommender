from settings import Settings, recommend_movie

import streamlit as st
import numpy as np 

def main():
    st.title("Movie recommender system")
    selected_movie = st.selectbox("Select the movie you like.", Settings.GET_MOV_LIST)

    if st.button("Recommend"):
        recommendations = recommend_movie(selected_movie)
        for movie in recommendations:
            st.write(movie)


if __name__ == "__main__":
    main()
    