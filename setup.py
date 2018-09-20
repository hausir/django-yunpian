# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name='django-yunpian',
    version='0.0.1',
    description='Django extension for YunPian API',
    long_description=readme,
    author='hausir',
    author_email='hausir@icloud.com',
    url='https://github.com/hausir/django-yunpian',
    license='MIT',
    install_requires=[
        'requests',
        'django',
    ],
    packages=find_packages(),
)
