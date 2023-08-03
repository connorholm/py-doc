import torch
from PIL import Image
import cv2

def get_yolov7():
    yolo_path = __file__.split("document_detection.py")[0]
    weights = yolo_path + "weights/yolov7-tiny.pt"
    torch.hub._validate_not_a_forked_repo=lambda a,b,c: True
    model = torch.hub.load(yolo_path, "custom", weights, force_reload=True, trust_repo=True, source='local')
    if isinstance(model, dict):
        model = model['ema' if model.get('ema') else 'model']
    model.conf = 0.5
    return model

def detect_document(image):
    model = get_yolov7()
    result = model(image).pred[0]
    if torch.cuda.is_available():
        result = result.cpu().numpy()
    else:
        result = result.numpy()
    return result