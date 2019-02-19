import os
from setuptools import setup

base = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(base, 'README.md')).read()

setup(
    name='l298n-pyfirmata',
    version='0.1',
    packages=['l298n'],
    description = '''
    A library for controlling module L298n ardunio
    ''',
    long_description=README,
    author='Komang Suryadana',
    author_email='suryadana80@gmail.com',
    url='https://github.com/suryadana/L298N-pyfirmata',
    license='MIT',
    install_requires=[
        'pyfirmata'
    ]
)
