# PyDoc
A library for interacting with pdf documents.

### Installation
```
pip install py-doc
```

### Get Started
How to use the library:

```python
from py_doc import Document 

# Instantiate a Document object 
image = Document('path/to/image.jpg')

# Use draw_classifications to find document classifications
image.draw_classifications("outupt.jpg")

# Additionally, if you just want the bounding boxes use get_bounding_box()
image.get_bounding_box()
```

### Documentation
The documentation for this library can be found [here](https://py-doc.readthedocs.io/en/latest/index.html#).

### Examples
This image is a sample of the output of the draw_classifications() method. The bounding boxes are drawn around the document classifications.
![Sample Output](tests/documents/output.jpg)


