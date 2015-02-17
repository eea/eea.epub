""" Async job
"""
import logging
from eea.converter.job import AsyncJob
logger = logging.getLogger('eea.epub')

class EpubJob(AsyncJob):
    """ Asynchronous generate ePub
    """
    def run(self, **kwargs):
        """ Run job
        """
        safe = kwargs.get('safe', True)
        # retry = kwargs.pop('retry', 0)
        errors = []

        with open(self.path, 'w') as ofile:
            ofile.write('Not implemented error')

        # Finish
        for error in errors:
            if not safe:
                raise error
            logger.exception(error)
