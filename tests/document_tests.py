
import unittest
import math
import numpy as np
from py_doc import Document


class DocumentTestCase(unittest.TestCase):

    def setUp(self):
        self.document = Document("documents/test.jpg") 

    def test_get_name(self):
        """Test get_name method"""

        # get_name method return the name of the document
        result = self.document.get_name()
        self.assertEqual(result, "documents/test.jpg")

    def test_bounding_box(self):
        """Test get_bounding_box method"""

        bbox = self.document.get_bounding_box()
        print(bbox)
        # check length is greater than 0
        self.assertGreater(len(bbox), 0)
        self.assertEqual(type(bbox), np.ndarray)


if __name__ == '__main__':
    unittest.main()