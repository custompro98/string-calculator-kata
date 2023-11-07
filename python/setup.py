# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='string calculator',
    version='0.1.0',
    description='String Calculator Kata in Python',
    long_description=readme,
    author='Mitch Joa',
    author_email='mitchjoa@gmail.com',
    url='https://github.com/custompro98/string-calculator-kata/tree/master/python',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
