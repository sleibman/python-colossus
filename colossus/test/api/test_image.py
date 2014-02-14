__author__ = 'sleibman'

import nose
import colossus

class TestImage():
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_import_file(self):
        colossus.LargeImage.import_file()
        x=1