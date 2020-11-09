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
    long_description=open(path.join(here, "README.md")).read(),
    url='https://github.com/wdecoster/nanopack',
    author='Wouter De Coster',
    author_email='decosterwouter@gmail.com',
    license='GPLv3',
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
    python_requires='>=3',
    install_requires=[
        'NanoPlot>=1.30.0',
        'NanoStat>=1.2.1',
        'NanoFilt>=2.7.1',
        'NanoLyse>=1.1.3',
        'nanoget>=1.13.2',
        'nanomath>=0.23.3',
        'NanoComp>=1.11.2',
        'nanoQC>=0.9.3'
    ],
    package_data={'nanopack': []},
    package_dir={'nanopack': 'nanopack'},
    include_package_data=True,

)
