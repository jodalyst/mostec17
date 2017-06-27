#!/usr/bin/env python3

from setuptools import setup, find_packages

EXCLUDED = ['*.tests', '*.tests.*', 'tests.*', 'tests']


setup(name='python-espeak',
      version='0.1.0',
      description='Python interface for espeak',
      classifiers=[
          'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis',
          'Topic :: Multimedia :: Sound/Audio :: Speech',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
          ],
      platforms='Linux',
      license='GPLv3',
      package_dir={'espeak': 'espeak'},
      test_suite='tests',
      packages=find_packages('.', EXCLUDED)
      )
