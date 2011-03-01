from setuptools import setup, find_packages
import os
from os.path import join

name = 'eea.epub'
path = name.split('.') + ['version.txt']
version = open(join(*path)).read().strip()


setup(name='eea.epub',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='epub plone import',
      author='David Ichim (Edw), Per Thulin, Antonio De Marinis (EEA), European Environment Agency (EEA)',
      author_email='webadmin@eea.europa.eu',
      url='https://svn.eionet.europa.eu/projects/Zope',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['eea'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
