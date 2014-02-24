__author__ = 'sleibman'

class LargeImage(object):
    def __init__(self):
        pass

    @classmethod
    def import_file(cls, filename):
        """
        Takes a filename (png or jpg), reads in the image, and creates a LargeImage object.
        """
        print "hello"
        return cls()

    def export_file(self):
        print "goodbye"