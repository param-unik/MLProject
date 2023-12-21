from typing import List

from setuptools import setup, find_packages


def get_requirements(file_path: str) -> List[str]:
    """
    This function returns the list of package requirements
    :param file_path: str
    :return: List
    """
    requirements = []

    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements


setup(
    name="mlProject",
    version="0.0.1",
    author="param-unik",
    author_email="param.unik@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
