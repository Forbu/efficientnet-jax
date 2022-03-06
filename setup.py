import os
from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "efficientnet_flax",
    version = "0.0.1",
    author = "Not Adrienb",
    description = ("Fork of the rwightman efficientnet flax"),
    license = "?",
    packages=find_packages(),
    package_dir="jeffnet",
    keywords = "Timm for flax",
    long_description=read('README.md'),
)
