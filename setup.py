"""Setup module for Robot Framework RabbitMq Library package."""

# To use a consistent encoding
from codecs import open
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Get install requires from requirements.txt
with open(path.join(here, 'requirements.txt')) as f:
    requirements = f.read().splitlines()

setup(
    name='robotframework-rabbitmq',
    version='3.0.1',
    description='A Robot Framework RabbitMq Library',
    long_description=long_description,
    url='https://github.com/Thibuko/robotframework-rabbitmq',
    author='Matthieu Flemal',
    author_email='matthieu.flemal@gmail.com',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.10',
        'Framework :: Robot Framework :: Library',
    ],
    keywords='testing testautomation robotframework rabbitmq amqp',
    package_dir={'': 'src'},
    py_modules=['RabbitMq'],
    install_requires=requirements,
)
