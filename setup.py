import pathlib

from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
REQUIREMENTS = (HERE / "requirements.txt").read_text()
CLASSIFIERS = """
Development Status :: 3 - Alpha
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Programming Language :: Python :: 3.10
Programming Language :: Python :: 3.11
Framework :: Robot Framework
Framework :: Robot Framework :: Library
Topic :: Software Development :: Testing
Topic :: Software Development :: Quality Assurance
Topic :: Utilities
Intended Audience :: Developers
""".strip().splitlines()

setup(
    name='robotframework-rabbitmq',
    version='3.0.1',
    description='A Robot Framework RabbitMq Library',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/Thibuko/robotframework-rabbitmq',
    author='Matthieu Flemal',
    author_email='matthieu.flemal@gmail.com',
    license='Apache License 2.0',
    classifiers=CLASSIFIERS,
    keywords='testing testautomation robotframework rabbitmq amqp',
    package_dir={'': 'src'},
    install_requires=REQUIREMENTS
)
