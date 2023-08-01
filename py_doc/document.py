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
