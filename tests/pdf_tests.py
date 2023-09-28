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