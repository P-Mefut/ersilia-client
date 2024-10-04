from setuptools import setup, find_packages
import sys

print("WARNING: setup.py is deprecated. Please use `pip install -e .` instead.")

setup(
    name='Ersilia Client',
    version='0.1.0',
    url='https://github.com/ersilia-os/ersilia-client',
    author='Ersilia Open Source Initiative',
    author_email='hello@ersilia.io',
    description='Interact with served Ersilia models through a simple Python client',
    packages=find_packages(),    
    install_requires=[
        'requests',
        'pandas'
    ],
)
