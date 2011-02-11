EEA Epub makes the following assumptions:

1. You don't use unicode or other special characters into the name of the epub, images, or links

2. You've created the epub with Indesign which uses some standards for the following:

    * The table of contents is named toc.ncx and is placed inside OEBPS
    * Book text & images are placed inside the folder OEBPS or other folders that are children 
    of OEBPS
    * Items ids doesn't contain the following characters . / \ ( if possible stick to letters,
    numers and - _ )

Best practices when creating an epub:

    * Chapter names should not be all uppercase or use special characters
    * Image names should not contain spaces, periods, / or other special characters

Epubs that were created with Indesign but failed to upload:
    
    * At this moment any errors that would appear on the site are surpressed by the info message:
    "Please Upload only Epubs that were made with Adobe Indesign"
    If you've made the epub with Indesign and yet you get this info message then please reopen this 
    ticket and upload there the troubleing epub:
    https://svn.eionet.europa.eu/projects/Zope/ticket/3883


More details about how to use this package can be found at the following link:
http://svn.eionet.europa.eu/projects/Zope/wiki/HowToEpub
