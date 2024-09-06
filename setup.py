from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT=" -e ."

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()   
        requirements=[req.replace("\n","") for req in requirements if req.strip() and not req.startswith("-e")]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)        # use when ther is a -e . in requirements
        
        return requirements




setup(
    name="src",
    version="0.0.1",
    author="meraj",
    author_email="merajsheikh202@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages()    
    
)