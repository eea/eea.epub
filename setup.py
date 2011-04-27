""" EEA EPub Installer
"""
from setuptools import setup, find_packages
import os
from os.path import join

name = 'eea.epub'
path = name.split('.') + ['version.txt']
version = open(join(*path)).read().strip()


setup(name='eea.epub',
      version=version,
      description="Publish Plone content in epub form",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='epub plone import',
      author='Per Thulin, David Ichim (eaudeweb), Tiberiu Ichim (eaudeweb), '
             'Antonio De Marinis (EEA), European Environment Agency (EEA)',
      author_email='webadmin@eea.europa.eu',
      url='https://svn.eionet.europa.eu/projects/Zope',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      namespace_packages=['eea'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'BeautifulSoup',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
