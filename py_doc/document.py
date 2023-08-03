import cv2

from py_doc.yolov7.document_detection import detect_document

class Document:
    """
    A class for representing documents.

    :param name: The name of the document.
    :type name: str
    """

    def __init__(self, name):
        self.name = name

    def get_name(self):
        """
        Get the name of the document.

        :return: The name of the document.
        :rtype: str
        """

        return self.name

    def get_bounding_box(self):
        """
        Use an object detection model to get bounding boxes for titles, text, figures, lists, and tables in the document.

        :return: A list of bounding boxes of the document.
        :rtype: list
        """
        image = cv2.imread(self.name)
        return detect_document(image)

    def draw_classifications(self, file):
        """
        Draw the bounding boxes on the document.

        :param file: The output file to save the image to.
        :type file: str

        :return: Boolean indicating if the image was saved.
        :rtype: bool
        """
        
        image = cv2.imread(self.name)
        bboxes = detect_document(image)

        classes = ["text", "title", "list", "table", "figure"]
        colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0), (0, 255, 255)]

        for bbox in bboxes:
            x1, y1, x2, y2, class_id = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3]), int(bbox[5])
            color = colors[class_id]
            cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
            cv2.putText(image, classes[class_id], (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1)

        cv2.imwrite(file, image)

        return True 



if __name__ == "__main__":
    document = Document("/home/connor/Development/MachineLearning/document-platform/py-doc/py_doc/yolov7/test.jpg")
    print(document.get_bounding_box())
    