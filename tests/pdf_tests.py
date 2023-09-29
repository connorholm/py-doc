import unittest
import os
from py_doc import PDF

class PDFTestCase(unittest.TestCase):

    def setUp(self):
        self.pdf = PDF("tests/documents/attention.pdf")

    def test_get_name(self):
        """Test get_name method"""

        # get_name method return the name of the document
        result = self.pdf.get_name()
        self.assertEqual(result, "tests/documents/attention.pdf")

    def test_convert_to_images(self):
        """Test convert_to_images method"""

        # convert_to_images method returns a list of images
        result = self.pdf.convert_to_images()

        self.assertEqual(len(result), 11)

    def test_store_images(self):
        """Test store_images method"""

        self.pdf.store_images("tests/documents/pdf_testing/images")
        length = len(self.pdf.doc)
        items = os.listdir("tests/documents/pdf_testing/images")
        for item in items:
            os.remove(os.path.join("tests/documents/pdf_testing/images", item))
        self.assertTrue(len(items) == length)

    def test_draw_classifications(self):
        """Test draw_classifications method"""

        self.pdf.draw_classifications("tests/documents/pdf_testing/output.pdf")
        self.assertTrue(os.path.exists("tests/documents/pdf_testing/output.pdf"))