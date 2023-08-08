from setuptools import find_packages,setup
from typing import List

def get_requirements(filepath : str) -> List[str]:
    """
    This functions reads the names of all the required
    packages from requirements.txt and returns them as a list.
    """
    with open(filepath) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')
        
    return requirements


setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Jay Thanki',
    author_email = 'jayyoges@buffalo.edu',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)