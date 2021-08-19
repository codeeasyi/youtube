# Gesichtserkennung mit Deep Learning(dlib)
# pip install numpy dlib

import argparse
from time import sleep
import dlib

parser = argparse.ArgumentParser()
parser.add_argument("-img_path", "-p", required=True, help="Path to file")
parser.add_argument("-delay", "-d", type=int, default=4)
args = parser.parse_args()

detector = dlib.get_frontal_face_detector()
popup_window = dlib.image_window()

image_array = dlib.load_rgb_image(args.img_path)

faces = detector(image_array, 1)
print(f"{len(faces)} faces detected on the image")

popup_window.set_image(image_array)
popup_window.add_overlay(faces)
sleep(args.delay)
popup_window.clear_overlay()
