#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='nova_api_docs_tracker',
    version='0.1.0',
    description="Manage bugs in Launchpad for verification of Nova API Docs",
    long_description=readme + '\n\n' + history,
    author="Augustina Ragwitz",
    author_email='auggy@cpan.org',
    url='https://github.com/missaugustina/nova_api_docs_tracker',
    packages=[
        'nova_api_docs_tracker',
    ],
    package_dir={'nova_api_docs_tracker':
                 'nova_api_docs_tracker'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='nova_api_docs_tracker',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
