# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

exec(open('nanopack/version.py').read())

setup(
    name='nanopack',
    version=__version__,
    description='Install all Oxford Nanopore scrips and modules for processing and analysis',
    long_description=open(path.join(here, "README.rst")).read(),
    url='https://github.com/wdecoster/nanopack',
    author='Wouter De Coster',
    author_email='decosterwouter@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='nanopore sequencing processing analysis',
    packages=find_packages(),
    install_requires=[
        'NanoPlot',
        'NanoStat',
        'NanoFilt',
        'NanoLyse',
        'nanoget',
        'nanomath',
        'nanoplotter'
    ],
    package_data={'nanopack': []},
    package_dir={'nanopack': 'nanopack'},
    include_package_data=True,

)
