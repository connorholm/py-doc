import fitz
import os
from py_doc import Image
import cv2
import numpy as np

class PDF:
    """
    A class for representing PDFs.

    :param name: The name of the document.
    :type name: str
    """

    def __init__(self, name) -> None:
        self.name = name
        self.doc = fitz.open(name)
        self.images = [] 

    def get_name(self):
        """
        Get the name of the document.

        :return: The name of the document.
        :rtype: str
        """

        return self.name
    
    def store_images_from_doc(self, output_path):
        """
        Turn a PDF into images and stores them on your local machine using the provided document from the constructor.

        :param output_path: The path of the folder where the images should be stored. 
        :type output_path: string with folder name

        :return: None
        :rtype: None
        """

        directory = output_path
        path = os.path.join(directory)
        if not os.path.exists(path): 
            os.mkdir(path)
        for page in self.doc:
            pix = page.get_pixmap(dpi=150)  
            pix.save(os.path.join(directory,"image_%04i.png" % page.number))

    def store_images(self, output_path, images = None):
        """
        Turn a PDF into images and stores them on your local machine using the class attribute images if a list of images is not provided.

        :param output_path: The path of the folder where the images should be stored. 
        :type output_path: string with folder name

        :return: None
        :rtype: None
        """

        # checks if images is None, if it is, it uses the class attribute images
        # additionally, if the class attribute images is empty, it will call convert_to_images to populate it
        if images is None:
            images = self.images
            if len(images) == 0:
                images = self.convert_to_images()

        directory = output_path
        path = os.path.join(directory)
        if not os.path.exists(path): 
            os.mkdir(path)
        index = 0
        for page in images:
            # get just the name of the pdf file
            name = os.path.basename(self.name)
            file_name = name.split(".")[0] + "_%04i.png" % index
            cv2.imwrite(os.path.join(directory, file_name), page.bytes)
            index += 1

    def convert_to_images(self):
        """
        Turn a PDF into an array of Image objects.

        :return: A list of images.
        :rtype: list
        """
        images = []
        index = 0
        for page in self.doc:
            pix = page.get_pixmap(dpi=150)
            img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, pix.n)
            images.append(Image("image_%04i.png" % index, img))
            index += 1

        self.images = images
        return self.images

    def draw_classifications(self, output_file):
        """
        Draw the bounding boxes on the images and merge them into a single PDF.

        :param output_file: The path of the folder where the images should be stored. 
        :type output_file: string

        :return: None
        :rtype: None
        """

        image_list = []
        if (len(self.images) == 0):
            self.convert_to_images()
        for image in self.images:
            image_list.append(image.draw_classifications())

        directory = os.path.dirname(output_file)
        path = os.path.join(directory, "images")
        if not os.path.exists(path): 
            os.mkdir(path)
        self.store_images(path, image_list)
        
        doc = fitz.open()
        imglist = os.listdir(path)
        for i, f in enumerate(imglist):
            img = fitz.open(os.path.join(path, f))
            rect = img[0].rect
            pdfbytes = img.convert_to_pdf()
            img.close()
            imgPDF = fitz.open("pdf", pdfbytes)
            page = doc.new_page(width = rect.width, height = rect.height)
            page.show_pdf_page(rect, imgPDF, 0)
            page.insert_image(rect, filename = os.path.join(path, f))
        doc.save(output_file)
