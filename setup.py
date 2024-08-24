from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = '-e .'

def get_requirements(file_path:str)->List[str]:
    """This function will return all the list of libraries that are listed in requirements.txt file."""
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
            
    return requirements
    
# Setting up the project details
setup(
    name="Student-Performance-Indicator",
    version= "0.0.1",
    description= "Developing a Model that helps to predict the student performance from the given dataset.",
    author= "Anoop George",
    author_email= "anoopgeorge418@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)