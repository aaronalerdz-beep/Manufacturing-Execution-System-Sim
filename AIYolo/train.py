from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt") 

    model.train(
        data="./Welding.v13i.yolov8/data.yaml", 
        epochs=50,                
        imgsz=640,                
        device="cpu",             
        workers=2                   
    )

if __name__ == '__main__':
    main()