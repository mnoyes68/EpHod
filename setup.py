from setuptools import setup, find_packages

with open("requirements.txt", "r") as req_file:
    requirements = [line.split("#")[0].strip() for line in req_file]
    requirements = [line for line in requirements if line]

setup(
    name='ephod',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        requirements
    ],
)
