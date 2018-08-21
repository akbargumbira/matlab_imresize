# coding=utf-8
"""Setup file for distutils / pypi."""
try:
    from ez_setup import use_setuptools
    use_setuptools()
except ImportError:
    pass

from setuptools import setup, find_packages

setup(
    name='matlab_imresize',
    version='0.1',
    author='fatheral',
    py_modules=['imresize'],
    description=('Python implementation of MatLab imresize() function.'),
    long_description=open('README.md').read(),
    install_requires=[
        "numpy"
    ]
)
