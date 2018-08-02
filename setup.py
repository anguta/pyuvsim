# -*- mode: python; coding: utf-8 -*
# Copyright (c) 2018 Radio Astronomy Software Group
# Licensed under the 2-clause BSD License

from setuptools import setup
import glob
import os
from os import listdir
import io
import json
from pyuvsim import version

data = [version.git_origin, version.git_hash, version.git_description, version.git_branch]
with open(os.path.join('pyuvsim', 'GIT_INFO'), 'w') as outfile:
    json.dump(data, outfile)

with io.open('README.md', 'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()


setup_args = {
    'name': 'pyuvsim',
    'author': 'Radio Astronomy Software Group',
    'url': 'https://github.com/RadioAstronomySoftwareGroup/pyuvsim',
    'license': 'BSD',
    'description': 'A radio interferometer simulator',
    'long_description': readme,
    'long_description_content_type': 'text/markdown',
    'package_dir': {'pyuvsim': 'pyuvsim'},
    'packages': ['pyuvsim', 'pyuvsim.tests'],
    'scripts': glob.glob('scripts/*'),
    'version': version.version,
    'include_package_data': True,
    'install_requires': ['numpy>=1.10', 'astropy>=1.2', 'pyuvdata'],
    'classifiers': ['Development Status :: 2 - Pre-Alpha',
                    'Intended Audience :: Science/Research',
                    'License :: OSI Approved :: BSD License',
                    'Programming Language :: Python :: 2.7',
                    'Topic :: Scientific/Engineering :: Astronomy'],
    'keywords': 'radio astronomy interferometry'
}

if __name__ == '__main__':
    apply(setup, (), setup_args)
