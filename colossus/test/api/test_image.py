__author__ = 'sleibman'

import nose
import colossus
import numpy
import tempfile
import os
from PIL import Image
import shutil


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


def element_array_to_abgr(array):
    """
    Converts a 4-element array of integers to an ABGR (alpha;blue;green;red) integer.
    Example: array_to_rgba([255,0,255,16]) returns 0x10FF00FF
    """
    # r =reloaded_array.reshape(40,4)
    # numpy.apply_along_axis(array_to_rgba,1,r)
    return 0x00000000 | (array[3] << 6*4) | (array[2] << 4*4) | (array[1] << 2*4) | (array[0])


def image_array_to_abgr(array):
    """
    Converts a 3D numpy array (a 2D array of 4-element ABGR arrays) to a 2D array of ints that
    have AABBGGRR values.
    """
    (h, w, e) = array.shape
    a = array.reshape(h*w, e)
    a = numpy.apply_along_axis(element_array_to_abgr, 1, a)
    return a.reshape(h, w)


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
        nose.tools.assert_true(numpy.alltrue(array == image_array_to_abgr(reloaded_array)))


class TestImage():
    def setup(self):
        (fd, filename) = tempfile.mkstemp(suffix='.png')
        self.tmp_png_filename = filename

        script_dir = os.path.dirname(os.path.realpath(__file__))
        test_dir = os.path.dirname(script_dir)
        self.stored_test_image = os.path.join(test_dir, 'images', 'jace.png')

        self.temp_dir = tempfile.mkdtemp()

    def teardown(self):
        try:
            os.remove(self.tmp_png_filename)
            shutil.rmtree(self.temp_dir)
        except OSError:
            pass

    def test_import_file(self):
        array = sample_small_array()
        image = create_image(array)
        image.save(self.tmp_png_filename)
        li = colossus.LargeImage.import_file(self.tmp_png_filename)
        nose.tools.assert_true(isinstance(li, colossus.LargeImage))

    def test_imported_size(self):
        li = colossus.LargeImage.import_file(self.stored_test_image)
        nose.tools.assert_equal(li.size, (1202, 762))

    def test_default_patch_size(self):
        li = colossus.LargeImage()
        nose.tools.assert_equal(li.patch_size, (256, 256))

    def test_checkin(self):
        li = colossus.LargeImage.import_file(self.stored_test_image)
        li.checkin(self.temp_dir, zoomlevel=0)

        # image.checkin('~/tmp/bigmap_colossus', zoomlevel=0)
