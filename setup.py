# Always prefer setuptools over distutils
from setuptools import setup, find_packages


# To use a consistent encoding
from codecs import open
import os
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
requirements.append("py-doc")

# This call to setup() does all the work
setup(
    name="py-doc",
    version="0.1.2",
    description="Used for working with documentations in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/connorholm/py-doc",
    author="Connor Holm",
    author_email="connorjholm@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(),
    package_data={"": ["py_doc/yolov7/weights/yolov7-tiny.pt"], "": ["py_doc/yolov7/requirements.txt"]},
    include_package_data=True,
    install_requires=requirements
)
