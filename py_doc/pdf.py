import fitz
import os

class PDF:
    """
    A class for representing PDFs.

    :param name: The name of the document.
    :type name: str
    """

    def __init__(self, name) -> None:
        self.name = name
        self.doc = fitz.open(name)
    
    def convert_to_image(self, output_path):
        """
        Turn a PDF into images.

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
        self.doc.close()

