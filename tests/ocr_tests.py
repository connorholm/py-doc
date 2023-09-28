import os
import unittest
from py_doc import OCR

class OCRTestCase(unittest.TestCase):

    def setUp(self):
        self.image = OCR("tests/documents/ocr_test.png")

    def test_get_text(self):
        """Test get_text method"""

        # get_text method return the text of the document
        result = self.image.get_text()
        print(result)
        self.assertEqual(result, "It was the best of\ntimes, it was the worst\nof times, it was the age\nof wisdom, it was the\nage of foolishness...\n")