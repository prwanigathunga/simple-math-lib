from setuptools import setup, find_packages

setup(
    name='simple-math-library',
    version='0.1',
    packages=find_packages(),
    author='Ranga Wanigathunga',
    author_email='prwanigathunga@gmail.com',
    description='A simple library for basic mathematical operations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/prwanigathunga/simple-math-lib',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
