# YOLOv5 for Mask Detection based on IoT

This project uses YOLOv4 for mask wearing detection and is implemented using PyTorch. At the same time, we combine it with IoT and deploy it on edge devices.

## Environment Setup
- Python >= 3.7
- PyTorch >= 1.4.0
- opencv-python >= 4.2.0.32
- Pillow >= 7.0.0

## How to Run model

### detect objects
Use *Jupyter Notebook* to open *predict.ipynb*, set the file path, and run the *detect_video()* function.
### traing
Use *Jupyter Notebook* to open *train.ipynb*, and after setting the data path, model path, and hyperparameters, you can train.

### Test
Use *Jupyter Notebook* to open *eval.ipynb*, set the test set path, and run to generate *detection-results* and *ground-truth*.

Then run *main.py* in the *mAP* directory to calculate *mAP* and other results.

## Reference
- Datasets：
  - https://github.com/hikariming/virus-mask-dataset
  - https://www.kesci.com/home/dataset/5e958c69e7ec38002d033362
  - For more, please refer to [this](https://github.com/CH-YellowOrange/YOLOv5-for-Object-Tracking-based-on-IoT/blob/-main/More%20Information.pdf).


