def reformat_bboxes(bboxes):
    """
    Reformat the bounding boxes to the format expected by Document.get_text_from_bbox(). Removes last two elements of each bounding box and turns floats into ints.
    :param bboxes: Input the bounding boxes from Document.get_bounding_box(). Ex: [[x1, y1, x2, y2, conf, class_id], ...]
    :type bboxes: list

    :return: The reformatted bounding boxes. Ex: [[x1, y1, x2, y2], ...]
    :rtype: list
    """
    return [[int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])] for bbox in bboxes]

def reformat_bbox(bbox):
    """
    Reformat an individual bounding box. See reformat_bounding_boxes() for more details.

    :param bbox: [x1, y1, x2, y2, conf, class_id]
    :type bbox: list

    :return: bbox: [x1, y1, x2, y2]
    :rtype: list
    """

    return [int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])]