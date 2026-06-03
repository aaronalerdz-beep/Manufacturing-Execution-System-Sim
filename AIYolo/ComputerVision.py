from ultralytics import YOLO
import random

def ImagesRandom():
    weight = [25, 25, 10, 25 ,15]
    imagesName = [1, 2, 3, 4, 5]
    return random.choices(imagesName, weights=weight, k=1)[0]
    

def ImageAnalysis():
    model = YOLO("/home/aaron/Desktop/AlienwareApps/Python/ManufacturaProyect/runs/detect/train-8/weights/best.pt") 
    num = ImagesRandom()
    results = model(f"AIYolo/{num}.jpeg")

    res = results[0]
    if len(res.boxes) > 0:
        match res.boxes.cls.item():
            case 0:
                return 0
            case 1:
                return 1
            case _:
                return 0
    print("images not detected")
    return 0
