from setuptools import find_packages, setup
from typing import List

from pathlib import Path
this_dir = Path(__file__).parent
long_des = (this_dir / "README.md").read_text()

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = [req.replace("\n","") for req in file_obj.readlines()]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name="movie_recommender",
    version="0.0.1",
    description="Movie Recommender Streamlit Application",
    long_description=long_des,
    long_description_content_type="text/markdown",
    author="Anishka Mukherjee",
    author_email="anishkamukherjee237@gmail.com",
    url="https://github.com/anishka07/movie_recommender",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)