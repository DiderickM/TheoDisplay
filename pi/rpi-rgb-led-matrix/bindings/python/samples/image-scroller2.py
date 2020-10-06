#!/usr/bin/env python
import time
from samplebase import SampleBase
from PIL import Image
import math

# Maybe een Theo T even laten staan of pulseren?


class ImageScroller(SampleBase):
    def __init__(self, *args, **kwargs):
        super(ImageScroller, self).__init__(*args, **kwargs)
        # self.parser.add_argument("-i", "--image", help="The image to display", default="THEO_GROOT.png")



    def run(self):
        folder = '/home/pi/rpi-rgb-led-matrix/bindings/python/samples/'
        theo_t_32_x_64 = Image.open(folder + 'test2_copy.png').convert('RGB').rotate(-90, expand=True)
        theo_198x64 = Image.open(folder + "THEO_GROOT.png").rotate(-90, expand=True)
        t_42x64 = Image.open(folder + "T.png").rotate(-90, expand=True)
        h_42x64 = Image.open(folder + "H.png").rotate(-90, expand=True)
        e_42x64 = Image.open(folder + "E.png").rotate(-90, expand=True)
        o_42x64 = Image.open(folder + "O.png").rotate(-90, expand=True)
        #
        
        o_resized = o_42x64.resize((60,30))
        self.matrix.SetImage(o_resized, 2, 1)
        time.sleep(7)
        self.matrix.Clear()
        #
        theo_array = [t_42x64,h_42x64,e_42x64,o_42x64]
        #
        # for letter in theo_array:
        #     letter_height, letter_width = letter.size
        #     print(letter_width)
        #     for p in range(1, 100, 1):
        #         size = math.sqrt(p)/10
        #         # print(size)
        #         width = round(letter_width * size/2)*2
        #
        #         height = round(letter_height * size/2)*2
        #         print(height)
        #         letter_resized = letter.resize((int(round(height)), int(round(width))))
        #         self.matrix.SetImage(letter_resized, -int(height / 2) + 32, -int(width / 2) + 16)
        #         time.sleep(0.01)
        #         self.matrix.Clear()
        #
        #
        # # Pulsating T
        # for p in range (10,1600,20):
        #     sleeptime = 1/math.sqrt(p)
        #     print(sleeptime)
        #     self.matrix.Clear()
        #     time.sleep(sleeptime)
       
        theo_array = [t_42x64,h_42x64,e_42x64,o_42x64]

        for letter in theo_array:
            letter_height, letter_width = letter.size
            print(letter_width)
            for p in range(1, 100, 1):
                size = math.sqrt(p)/10
                # print(size)
                width = round(letter_width * size/2)*2

                height = round(letter_height * size/2)*2
                print(height)
                letter_resized = letter.resize((int(round(height)), int(round(width))))
                self.matrix.SetImage(letter_resized, -int(height / 2) + 32, -int(width / 2) + 16)
                time.sleep(0.01)
                self.matrix.Clear()
        #
        #
        # Pulsating T
        #for p in range (10,1600,20):
        #    sleeptime = 1/math.sqrt(p)
        #    print(sleeptime)
        #    self.matrix.Clear()
        #    time.sleep(sleeptime)
        #    self.matrix.SetImage(theo_t_32_x_64, 0, 0)
        #    time.sleep(sleeptime)
        #    self.matrix.Clear()

        #self.matrix.SetImage(theo_t_32_x_64, 0, 0)
        #time.sleep(4)
        #self.matrix.Clear()
        #
        # # theo groot links naar rechts
        # for n in range(-200, 100, 1):
        #     self.matrix.SetImage(theo_198x64, 0, n)
        #     time.sleep(0.02)
        #     self.matrix.Clear()
        #
        # # theo groot rechts naar links
        # for n in range(-100, 200, 2):
        #     self.matrix.SetImage(theo_198x64, 0, -n)
        #     time.sleep(0.01)
        #     self.matrix.Clear()

        # im_new = add_margin(image, 10, 0, 100, (128, 0, 64))
        theo_t_8x16 = theo_t_32_x_64.resize((16,8))
        theo_t_8x16 = theo_t_8x16.rotate(45, expand=True)
        # im = im.setCanvas(img_width * 2, img_height * 2)
        theo_t_8x16_maxheight , theo_t_8x16_maxwidth = theo_t_8x16.size

        # 8 ts rotating
        for n in range(-45, 315, 6):
            self.matrix.Clear()
            theo_t_8x16_rotated = theo_t_8x16.rotate(n, center = (int(theo_t_8x16_maxwidth/2),int(theo_t_8x16_maxwidth/2)))
            self.matrix.SetImage(theo_t_8x16_rotated, 0, -2)
            self.matrix.SetImage(theo_t_8x16_rotated, 16, -2)
            self.matrix.SetImage(theo_t_8x16_rotated, 32, -2)
            self.matrix.SetImage(theo_t_8x16_rotated, 48, -2)
            self.matrix.SetImage(theo_t_8x16_rotated, 0, 14)
            self.matrix.SetImage(theo_t_8x16_rotated, 16, 14)
            self.matrix.SetImage(theo_t_8x16_rotated, 32, 14)
            self.matrix.SetImage(theo_t_8x16_rotated, 48, 14)
            time.sleep(0.05)
        
        # theo_t_8x16_rotated = theo_t_8x16.rotate(180, expand=True)
        # # 6 ts going down and rotating
        # for i in range(0,4):
        #     theo_t_8x16_rotated = theo_t_8x16_rotated.rotate(90, expand=True)
        #     for t in range(0, 120, 6):
        #         self.matrix.Clear()
        #         self.matrix.SetImage(theo_t_8x16_rotated, t, -2)
        #         self.matrix.SetImage(theo_t_8x16_rotated, t-32, -2)
        #         self.matrix.SetImage(theo_t_8x16_rotated, t-64, -2)
        #         self.matrix.SetImage(theo_t_8x16_rotated, t, 14)
        #         self.matrix.SetImage(theo_t_8x16_rotated, t-32, 14)
        #         self.matrix.SetImage(theo_t_8x16_rotated, t-64, 14)
        #         time.sleep(0.05)

        # theo_t_8x16_rotated = theo_t_8x16.rotate(90, expand=True)
        # for i in range(0,4):
        #     theo_t_8x16_rotated = theo_t_8x16_rotated.rotate(180, expand=True)
        #
        #     for t in range(0, 120, 3):
        #         self.matrix.Clear()
        #         self.matrix.SetImage(theo_t_8x16_rotated, t, t - 0)
        #         self.matrix.SetImage(theo_t_8x16_rotated, t - 16, t - 16)
        #         self.matrix.SetImage(theo_t_8x16_rotated, t - 32, t - 32)
        #         self.matrix.SetImage(theo_t_8x16_rotated, t, t-16)
        #         self.matrix.SetImage(theo_t_8x16_rotated, t-16, t-32)
        #         self.matrix.SetImage(theo_t_8x16_rotated, t-32, t-48)
        #         self.matrix.SetImage(theo_t_8x16_rotated, t + 16, t - 16)
        #         self.matrix.SetImage(theo_t_8x16_rotated, t - 0, t - 32)
        #         self.matrix.SetImage(theo_t_8x16_rotated, t - 16, t - 48)
        #         time.sleep(0.05)

        # theo_t_8x16_rotated = theo_t_8x16.rotate(90, expand=True)
        for i in range(0,4):
            theo_t_8x16_rotated = theo_t_8x16_rotated.rotate(180, expand=True)
        #
            for t in range(120, 0, -3):
                self.matrix.Clear()
                self.matrix.SetImage(theo_t_8x16_rotated, t, t - 0)
                self.matrix.SetImage(theo_t_8x16_rotated, t - 16, t - 16)
                self.matrix.SetImage(theo_t_8x16_rotated, t - 32, t - 32)
                self.matrix.SetImage(theo_t_8x16_rotated, t, t-16)
                self.matrix.SetImage(theo_t_8x16_rotated, t-16, t-32)
                self.matrix.SetImage(theo_t_8x16_rotated, t-32, t-48)
                self.matrix.SetImage(theo_t_8x16_rotated, t + 16, t - 16)
                self.matrix.SetImage(theo_t_8x16_rotated, t - 0, t - 32)
                self.matrix.SetImage(theo_t_8x16_rotated, t - 16, t - 48)
                time.sleep(0.05)



# Main function
# e.g. call with
#  sudo ./image-scroller.py --chain=4
# if you have a chain of four
if __name__ == "__main__":
    image_scroller = ImageScroller()
    if (not image_scroller.process()):
        image_scroller.print_help()
