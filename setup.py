from setuptools import setup, find_packages

setup(
    name='glassvector',
    packages=find_packages(include=['glassvector']),
    version='1.0.0',
    description='A simple in-memory vector database',
    author='Arshin Albab',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.4.2'],
    test_suite='tests',
)