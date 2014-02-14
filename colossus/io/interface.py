__author__ = 'sleibman'

import colossus

class Storage(object):

    @property
    def name(self):
        raise NotImplementedError()

    @property
    def width(self):
        raise NotImplementedError()

    @property
    def height(self):
        raise NotImplementedError()

    @property
    def zoomlevels(self):
        raise NotImplementedError()

    @property
    def tile_width(self):
        raise NotImplementedError()

    @property
    def tile_height(self):
        raise NotImplementedError()

    def write(self, image, x=0, y=0):
        raise NotImplementedError()

    def read(self, xmin=0, xmax=None, ymin=0, ymax=None):
        if xmax is None:
            xmax = self.height
        if ymax is None:
            ymax = self.height
        raise NotImplementedError()
    



