"""API Blueprint from python docstring."""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyabp',
    version='0.1.0',
    description='API Blueprint from python docstring',
    long_description=long_description,
    url='https://github.com/HackerWilson/python-api-blueprint.git',
    author='HackerWilson',
    author_email='wenbinwb1@foxmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='api blueprint',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pyabp=src.__main__:cli',
        ],
    },
)
