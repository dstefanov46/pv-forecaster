# -*- coding: utf-8 -*-

# Copyright (c) 2016-2023 by University of Kassel and Fraunhofer Institute for Energy Economics
# and Energy System Technology (IEE), Kassel. All rights reserved.

from setuptools import setup, find_packages
import re

with open('README.rst', 'rb') as f:
    install = f.read().decode('utf-8')

#with open('CHANGELOG.rst', 'rb') as f:
#    changelog = f.read().decode('utf-8')

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3']

# with open('.github/workflows/github_test_action.yml', 'rb') as f:
    # lines = f.read().decode('utf-8')
    # versions = set(re.findall('3.[7-9]', lines)) | set(re.findall('3.1[0-9]', lines))
    # for version in sorted(versions):
        # classifiers.append('Programming Language :: Python :: %s' % version)

# long_description = '\n\n'.join((install, changelog))

setup(
    name='pv-forecaster',
    packages=find_packages(),
    include_package_data=True,
    classifiers=classifiers
)