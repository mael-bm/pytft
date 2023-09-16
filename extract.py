from PIL import Image, ImageGrab
import pytesseract
import cv2
import numpy as np

SHOP_COORDS = (480, 1040, 1480, 1070)
GOLD_COORDS = (868, 885, 910, 910)
STREAK_COORDS = (984, 876, 1025, 908)
LOSE_COLOR = (15, 59, 70)
STAGE_COORDS = (770, 12, 860, 33)

class Tesseract:
    pytesseract.pytesseract.tesseract_cmd = "tesseract"

    @staticmethod
    def to_gray(d):
        image = np.asarray(d)
        gry = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        return Image.fromarray(cv2.cvtColor(gry, cv2.COLOR_BGR2RGB))

    @staticmethod
    def clean(d):
        image = np.asarray(d)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (3, 3), 0)
        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        # Morph open to remove noise and invert image
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
        invert = 255 - opening

        return Image.fromarray(cv2.cvtColor(invert, cv2.COLOR_BGR2RGB))

    @staticmethod
    def image_to_string(data):
        result = pytesseract.image_to_string(data, config = r"--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        return result

    @staticmethod
    def get_shop():
        im = ImageGrab.grab(bbox=SHOP_COORDS)
        im = Tesseract.to_gray(im)
        im.save("gray.png")
        unit_length = im.size[0] / 5
        units = []
        for x in range(0, 5):
            box = (x * unit_length, 0, (x + 1) * unit_length - 50, im.size[1])
            #print(box)
            new = im.crop(box)
            text = Tesseract.image_to_string(new).replace("\n","")
            units.append(text)
        return units

    @staticmethod
    def gold_balance():
        im = ImageGrab.grab(bbox=GOLD_COORDS)
        im = Tesseract.to_gray(im)
        gold_count = Tesseract.image_to_string(im)
        return gold_count

    @staticmethod
    def streak_value():
        im = ImageGrab.grab(bbox=STREAK_COORDS)
        im.save("streak.png")
        color = im.getpixel((2, 23))
        side = (-1 if color[2] > 17 else 1)  # check if blue channel of rgb is higher 17, if so its lose streak
        try:
            val = int(Tesseract.image_to_string(im))
        except ValueError:
            val = 0
        return val*side

    @staticmethod
    def stage_value():
        im = ImageGrab.grab(bbox=STAGE_COORDS)
        im = Tesseract.to_gray(im)
        im.save("stage.png")
        stage = Tesseract.image_to_string(im)
        return stage

u = Tesseract.get_shop()
print(u)