__author__ = 'sleibman'

class LargeImage(object):
    def __init__(self):
        pass

    @classmethod
    def import_file(cls):
        print "hello"
        return cls()

    def export_file(self):
        print "goodbye"