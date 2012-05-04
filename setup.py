import sys, os
from setuptools import setup, find_packages

version = '0.0.2'
long_description = open('README.rst').read() + '\n\n' + \
                   open('CHANGES.rst').read()

setup(
    name='django_logtail',
    version=version,
    description='A log viewing and tailing utility accessible via a Django ' \
                'admin panel',
    long_description=long_description,
    keywords='django admin logfile viewer tail log',
    author='Alex Holmes',
    author_email='alex.holmes@isotoma.com',
    url='https://github.com/alex2/django_logtail',
    license='The MIT License',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Django',
    ],
)
