__author__ = 'sleibman'

from PIL import Image
import os


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

    def xy_to_ij(self, x, y):
        """
        Finds the i,j patch containing specified absolute x,y coordinates in the full image.
        """
        return x / self.patch_size[0], y / self.patch_size[1]

    def ij_to_xy_min(self, i, j):
        """
        Returns the absolute coordinates of the min corner of the specified patch.
        """
        return i * self.patch_size[0], j * self.patch_size[1]

    def ij_to_xy_max(self, i, j):
        """
        Returns the absolute coordinates of the max corner of the specified patch.
        """
        return (i+1) * self.patch_size[0] - 1, (j+1) * self.patch_size[1] - 1

    def checkin(self, topdir, zoomlevel, x, y):
        """
        Creates patches, saves them in directory tree under dir.
        @param x: x offset for the checked-in subset in the full image. For a new checkin, set x=0
        @param y: y offset for the checked-in subset in the full image. For a new checkin, set y=0

        The directory convention is:
              zoom_level/i/j.jpg where i and j are tile indices starting with 0 at lower left.
        """

        # Create directory if necessary.
        if not os.path.exists(topdir):
            os.makedirs(topdir)

        max_x = x + self.size[0]
        max_y = y + self.size[1]


        (start_i, start_j) = self.xy_to_ij(x, y)
        (end_i, end_j) = self.xy_to_ij(max_x, max_y)

        # Determine set of patches that are only partially covered.
        patch_start_x, patch_start_y = self.ij_to_xy_min(start_i, start_j)
        patch_end_x, patch_end_y = self.ij_to_xy_max(end_i, end_j)

        function_array = [[self.ensure_exists if i<start_i or j<start_j else
                           self.partial_clobber if (i==start_i and patch_start_x != x) or
                                              (j==start_j and patch_start_y != y) or
                                              (i==end_i and patch_end_x != max_x) or
                                              (j==end_j and patch_end_y != max_y) else
                           self.full_clobber for j in range(end_j+1)] for i in range(end_i+1)]

        for i in range(end_i+1):
            for j in range(end_j+1):
                function_array[i][j](i, j)

        # For all partial cover patches:
        #   if patch exists on disk, import it, clobber the overlap
        #   if patch doesn't exist on disk, make the undefined section transparent.
        #   write to disk.

        # For all full cover patches, write to disk.

        # If offset was > 0,0 then make sure that patches exist starting at 0,0. If not, create transparent
        # patches to fill.