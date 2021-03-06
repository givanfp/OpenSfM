#!/usr/bin/env python

from __future__ import print_function
from setuptools import setup
import os
import errno
import subprocess
import sys

"""
def mkdir_p(path):
    '''Make a directory including parent directories.
    '''
    try:
        os.makedirs(path)
    except os.error as exc:
        if exc.errno != errno.EEXIST or not os.path.isdir(path):
            raise


print("Configuring...")
mkdir_p('cmake_build')
cmake_command = ['cmake', '../opensfm/src']
if sys.version_info >= (3, 0):
    cmake_command.extend([
        '-DBUILD_FOR_PYTHON3=ON',
        '-DBOOST_PYTHON3_COMPONENT=python-py{}{}'.format(
            sys.version_info.major,
            sys.version_info.minor)])
subprocess.Popen(cmake_command, cwd='cmake_build').wait()

print("Compiling extension...")
subprocess.Popen(['make', '-j4'], cwd='cmake_build').wait()

print("Building package")
"""
setup(
    name='OpenSfM',
    version='0.1',
    description='A Structure from Motion library',
    url='https://github.com/mapillary/OpenSfM',
    author='Mapillary',
    license='BSD',
    scripts=['bin/opensfm_run_all', 'bin/opensfm', 'bin/export_bundler'],
	packages=['opensfm', 'opensfm.commands', 'opensfm.large'],
    #package_dir={'opensfm':  'opensfm/src/build/Release', 'opensfm.commands': 'opensfm/src' },
	package_data={'opensfm': ['csfm.pyd', 'data/sensor_data.json']}
)
