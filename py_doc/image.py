import cv2
import pytesseract
from py_doc.yolov7.document_detection import detect_document
from py_doc import utils
import os
import fitz

class Image:
    """
    A class for representing an image. Takes in a name and a image. If the image is not provided, the name is used to load the image.

    :param name: The name of the image.
    :type name: str
    """

    def __init__(self, name, bytes=None):
        self.name = name
        if bytes is None:
            self.bytes = cv2.imread(name)
        else:
            self.bytes = bytes
        self.bboxes = [] 

    def get_name(self):
        """
        Get the name of the image.

        :return: The name of the image.
        :rtype: str
        """

        return self.name

    def get_bboxes(self):
        """
        Use an object detection model to get bounding boxes for titles, text, figures, lists, and tables in the image.

        :return: A list of bounding boxes of the image.
        :rtype: list
        """
        if len(self.bboxes) == 0:
            self.bboxes = detect_document(self.bytes)
        return self.bboxes 

    def draw_classifications(self, output_file = None):
        """
        Draw the bounding boxes on the image. Contains the option to save the image to a file, otherwise it will just return the image.

        :param file: The output file to save the image to.
        :type file: str

        :return: If the file is provided, it will return a boolean based on the success, otherwise it will return the image.
        :rtype: bool or numpy.ndarray
        """
        
        if len(self.bboxes) == 0:
            bboxes = detect_document(self.bytes)

        classes = ["text", "title", "list", "table", "figure"]
        colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0), (0, 255, 255)]

        drawn_image = self.bytes.copy()

        for bbox in bboxes:
            x1, y1, x2, y2, class_id = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3]), int(bbox[5])
            color = colors[class_id]
            cv2.rectangle(drawn_image, (x1, y1), (x2, y2), color, 2)
            cv2.putText(drawn_image, classes[class_id], (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1)

        if output_file is not None:
            cv2.imwrite(output_file, drawn_image)
            return True
        else:
            return Image(self.name, drawn_image)


    def get_text(self):
        """
        Get the text from the image.

        :return: The text from the image.
        :rtype: str
        """

        return pytesseract.image_to_string(self.image, lang='eng')

    def get_text_from_bbox(self, bbox):
        """
        Get the text from the bounding box.

        :param bbox: The bounding box to get the text from.
        :type bbox: list with 4 elements [x1, y1, x2, y2]

        :return: The text from the bounding box.
        :rtype: str
        """

        x1, y1, x2, y2 = utils.reformat_bbox(bbox)
        cropped = self.bytes[y1:y2, x1:x2]
        return pytesseract.image_to_string(cropped, lang='eng')
