# Face Annotation Tool

## Create a bounding box around a face present in the image and save the cropped face automatically

Opens the image named `dog.jpg` in a new OpenCV window and saves the selected region to the directory. Select the top left region and drag to the bottom right to select.

## Install

This project was setup to work with virtual environments. To reproduce the environment:

- Activate a new virtual environment

```bash
python3 -m venv ./venv
```

```bash
source ./venv/bin/activate
```

- Install dependencies

```bash
pip install -r requirements.txt
```

#### Note: Open CV is the only 3rd party dependency. This project may run if `opencv-python@^4.2` is installed already

## Usage

The root file for this project is `submission.py`. From the command line on a system that support windowed environments, run:

```bash
python submission.py
```

image source:
dog.jpg - https://www.piqsels.com/en/public-domain-photo-ovxve
Creative Commons Zero - CC0
