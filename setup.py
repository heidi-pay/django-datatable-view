# -*- encoding: utf-8 -*-
"""setup.py: Django django-datatables-view"""

from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(name='django-datatable-view',
      version='0.9.1',
      description='This package is used in conjunction with the jQuery plugin '
                  '(http://http://datatables.net/), and supports state-saving detection'
                  ' with (http://datatables.net/plug-ins/api).  The package consists of '
                  'a class-based view, and a small collection of utilities for rendering'
                  ' table data from models.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Autumn Valenta',
      author_email='avalenta@pivotalenergysolutions.com',
      url='https://github.com/pivotal-energy-solutions/django-datatable-view',
      download_url='https://github.com/pivotal-energy-solutions/django-datatable-view/tarball/django-datatable-view-0.9.0',
      license='Apache License (2.0)',
      classifiers=[
           'Development Status :: 2 - Pre-Alpha',
           'Environment :: Web Environment',
           'Framework :: Django',
           'Intended Audience :: Developers',
           'License :: OSI Approved :: Apache Software License',
           'Operating System :: OS Independent',
           'Programming Language :: Python',
           'Topic :: Software Development',
      ],
      packages=find_packages(exclude=['tests', 'tests.*']),
      package_data={'datatableview': ['static/js/*.js', 'templates/datatableview/*.html']},
      include_package_data=True,
      install_requires=['django>=1.11', 'python-dateutil>=2.1'],
)
