from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT="-e ."

def get_package_names(file_path:str) -> List[str]:
    # THis function will return the list of requirements

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    print("Requirement list", requirements)
    return requirements

setup(
    name="ML_Pipeline",
    version="0.0.1",
    author="Piyush Vikas",
    author_email="piyushvikasdutta@gmail.com",
    maintainer="Nihal",
    maintainer_email="piyush.vikasde@gmail.com",
    packages= find_packages(),
    install_requires= get_package_names('requirement.txt')
)