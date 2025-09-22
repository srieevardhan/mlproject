from setuptools import find_packages,setup
from typing import List

hypen_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    it return reqirements
    '''
    requirement=[]
    with open (file_path) as file_object:
        requirement=file_object.readlines()
        requirement=[req.replace("\n","") for req in requirement]
        if hypen_dot in requirement:
            requirement.remove(hypen_dot)
    return requirement
        

setup(
    name='mlproject',
    version='0.0.1',
    author='srieevardhan',
    author_email='srieemadeshwaran@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)