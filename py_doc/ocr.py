import pytesseract


class OCR:

    def __init__(self, image):
        self.image = image

    def get_text(self):
        """
        Get text from image using OCR

        :param image: The input image
        :type image: numpy.ndarray or PIL.JpegImagePlugin.JpegImageFile

        :return: The text from the image
        :rtype: str
        """
        return pytesseract.image_to_string(self.image, lang='eng')
