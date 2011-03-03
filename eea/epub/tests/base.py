""" Base module for epub tests
"""
from Products.PloneTestCase import PloneTestCase
from Products.PloneTestCase.layer import onsetup
from Products.Five import zcml
from Products.Five import fiveconfigure
#from Products.CMFPlone.interfaces import IPloneSiteRoot
#from Products.GenericSetup import EXTENSION, profile_registry


PRODUCTS = ['ATVocabularyManager', 'FiveSite']
PROFILES = ['eea.epub:default']


@onsetup
def setup_epub():
    """ setup epub test
    """
    fiveconfigure.debug_mode = True
    import Products.Five
    import Products.FiveSite
    import eea.soer
    zcml.load_config('meta.zcml', Products.Five)
    zcml.load_config('configure.zcml', Products.Five)
    zcml.load_config('configure.zcml', Products.FiveSite)
    zcml.load_config('configure.zcml', eea.soer)
    fiveconfigure.debug_mode = False

    PloneTestCase.installProduct('Five')
    for product in PRODUCTS:
        PloneTestCase.installProduct(product)

setup_epub()
PRODUCTS.append('eea.epub')
PloneTestCase.setupPloneSite(products=PRODUCTS)


class EpubFunctionalTestCase(PloneTestCase.FunctionalTestCase):
    """ EpubFunctionalTestCase class
    """
    pass
