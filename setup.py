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
    python_requires='>=3',
    install_requires=[
        'NanoPlot>=1.29.0',
        'NanoStat>=1.2.0',
        'NanoFilt>=2.6.0',
        'NanoLyse>=1.1.0',
        'nanoget>=1.21.1',
        'nanomath>=0.23.1',
        'NanoComp>=1.10.1',
        'nanoQC>=0.9.2'
    ],
    package_data={'nanopack': []},
    package_dir={'nanopack': 'nanopack'},
    include_package_data=True,

)
