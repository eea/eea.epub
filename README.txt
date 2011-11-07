EEA Epub product
================
A product which allows you to import in Plone epub files.

Contents
========

.. contents::


Introduction
============

EEA Epub product allows you to import in Plone epub files. On upload,
Epub content will imported as Plone folders, files, images and documents.

Export to Epub is also available.

Note that only epub files created with "Adobe InDesign CS4" are supported for import.


Main features
=============

EEA Epub features:

   1. Import epub files as Plone content.
   2. Export into epub format.

Installation
============

The easiest way to get eea.epub support in Plone 4 using this
package is to work with installations based on `zc.buildout`_.
Other types of installations should also be possible, but might turn out
to be somewhat tricky.

To get started you will simply need to add the package to your "eggs" and
"zcml" sections, run buildout, restart your Plone instance and install the
"eea.epub" package using the quick-installer or via the "Add-on
Products" section in "Site Setup".

  .. _`zc.buildout`: http://pypi.python.org/pypi/zc.buildout/

You can download a sample buildout at:

  https://svn.eionet.europa.eu/repositories/Zope/trunk/eea.epub/buildouts

Getting started
===============

From "Add new" menu select "EpubFile" and upload an epub file.

Dependecies
===========

  1. Plone 4.x
  2. BeautifulSoup


Live demo
=========

Here some live production demos at EEA (European Environment Agency)

   1. http://www.eea.europa.eu/soer/synthesis


Source code
===========

Latest source code (Plone 4 compatible):
   https://svn.eionet.europa.eu/repositories/Zope/trunk/eea.epub/branches/plone4/

Plone 2 and 3 compatible:
   https://svn.eionet.europa.eu/repositories/Zope/trunk/eea.epub/trunk/


Copyright and license
=====================
The Initial Owner of the Original Code is European Environment Agency (EEA).
All Rights Reserved.

The EEA Faceted Navigation (the Original Code) is free software;
you can redistribute it and/or modify it under the terms of the GNU
General Public License as published by the Free Software Foundation;
either version 2 of the License, or (at your option) any later
version.

Contributor(s): Per Thulin (Valentine Web Systems),
                Antonio De Marinis (European Environment Agency),
                Alec Ghica (Eau de Web),
                David Ichim (Eau de Web),
                Tiberiu Ichim (Eau de Web)

More details under docs/License.txt


Links
=====

   1. EEA Epub wiki page: https://svn.eionet.europa.eu/projects/Zope/wiki/HowToEpub#HowtocreateanduploadanEpub


Funding
=======

  EEA_ - European Enviroment Agency (EU)

.. _EEA: http://www.eea.europa.eu/