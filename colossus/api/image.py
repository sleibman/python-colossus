__author__ = 'sleibman'

from PIL import Image


class LargeImage(object):
    def __init__(self):
        self._full_image = None

    @classmethod
    def import_file(cls, filename):
        """
        Takes a filename (png or jpg), reads in the image, and creates a LargeImage object.
        """
        li = cls()
        li._full_image = Image.open(filename)
        li._size = li._full_image.size
        return li

    def export_file(self):
        print "goodbye"

    @property
    def size(self):
        """
        (width, height) tuple representing the size of the checked out portion of the image, or the full image if
        imported from a traditional file type.
        """
        return self._size

    @property
    def patch_size(self):
        """
        (width, height) tuple of the standard patches comprising an image. All patches except edge patches will have the
         same size. Edge patches may be smaller if the full image size is not an even multiple of the patch size.
        """
        return 256, 256

    def checkin(self, dir, zoomlevel, x, y):
        """
        Creates patches, saves them in directory tree under dir.
        @param x: x offset for the checked-in subset in the full image. For a new checkin, set x=0
        @param y: y offset for the checked-in subset in the full image. For a new checkin, set y=0

        The directory convention is:
              zoom_level/i/j.jpg where i and j are tile indices starting with 0 at lower left.
        """

        # Create directory if necessary.

        # Determine set of patches that are only partially covered.

        # For all partial cover patches:
        #   if patch exists on disk, import it, clobber the overlap
        #   if patch doesn't exist on disk, make the undefined section transparent.
        #   write to disk.

        # For all full cover patches, write to disk.

        # If offset was > 0,0 then make sure that patches exist starting at 0,0. If not, create transparent
        # patches to fill.