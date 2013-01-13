import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    ]

setup(name='sample csv creator',
      version='0.1',
      description='sample csv creator',
      classifiers=[
        "Programming Language :: Python",
        ],
      author='',
      author_email='',
      url='',
      keywords='',
      packages=find_packages('src'),
      package_dir={'':'src'},
      include_package_data=True,
      zip_safe=False,      
      install_requires = requires,
      )
