__author__ = 'sleibman'

import nose
import colossus
import numpy
import tempfile
import os
from PIL import Image


def create_image(img):
    """
    Example numpy/PIL image creation code from http://jehiah.cz/a/creating-images-with-numpy
    """
    (h, w) = img.shape
    pilImage = Image.frombuffer('RGBA', (w, h), img, 'raw', 'RGBA', 0, 1)
    return pilImage
    #pilImage.save(filename)


def sample_small_array():
    w, h = 5, 8
    img = numpy.empty((w, h), numpy.uint32)
    img.shape = h, w
    img[:, :] = 0xFFFFFFFF  # All white
    img[0, 0] = 0xFF0000FF  # Top left pixel to red (ABGR)
    img[:, 3:5] = 0xFFFF0000  # Columns 3 & 4 to blue
    return img


class TestPilBasics():
    def setup(self):
        (fd, filename) = tempfile.mkstemp(suffix='.png')
        self.tmp_png_filename = filename

    def teardown(self):
        try:
            os.remove(self.tmp_png_filename)
        except OSError:
            pass

    def test_write_read_image(self):
        array = sample_small_array()
        image = create_image(array)
        image.save(self.tmp_png_filename)
        reloaded_image = Image.open(self.tmp_png_filename)
        reloaded_array = numpy.asarray(reloaded_image)
        nose.tools.assert_true(numpy.alltrue(array == reloaded_array))


class TestImage():
    def setup(self):
        (fd, filename) = tempfile.mkstemp(suffix='.png')
        self.tmp_png_filename = filename

    def teardown(self):
        try:
            os.remove(self.tmp_png_filename)
        except OSError:
            pass


    def test_import_file(self):
        create_image(self.tmp_png_filename)
        colossus.LargeImage.import_file(self.tmp_png_filename)
        x=1