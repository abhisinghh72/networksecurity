'''
The Setup.py file is an Essential part of packaging and distributing Python Projects.
 It is used by setuptools (or distutils in older versions) to define the configuration of 
 your project, such as metadata, dependencies, and more
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
        """
        This Functon will return the list of requirements
        """

        requirement_lst:List[str]= []
        try:
            with open('requirements.txt',"r") as file:
                # Read lines from the file
                lines = file.readlines()
                ## Process each line
                for line in lines:
                    requirement = line.strip()
                    ## ignore empty line and -e .
                    if requirement and requirement != '-e .':
                        requirement_lst.append(requirement)

        except FileNotFoundError:
            print("requirements.txt file not found.")

        return requirement_lst
    

setup(
     name= "NetworkSecurity",
     version= "0.0.1",
     author = "Abhishek Singh",
     author_email ="abhishek.singhh712@gmail.com",
     packages = find_packages(),
     install_requires = get_requirements()
)
