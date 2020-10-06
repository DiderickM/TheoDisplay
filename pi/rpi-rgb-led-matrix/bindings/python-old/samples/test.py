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

        theo_t_32_x_64 = Image.open('test2_copy.png').convert('RGB').rotate(90, expand=True)
        theo_198x64 = Image.open("THEO_GROOT.png").rotate(90, expand=True)
        t_42x64 = Image.open("T.png").rotate(90, expand=True)
        h_42x64 = Image.open("H.png").rotate(90, expand=True)
        e_42x64 = Image.open("E.png").rotate(90, expand=True)
        o_42x64 = Image.open("O.png").rotate(90, expand=True)

        theo_t_8x16 = theo_t_32_x_64.resize((16,8))
        theo_t_8x16 = theo_t_8x16.rotate(45, expand=True)

        theo_t_8x16_maxheight , theo_t_8x16_maxwidth = theo_t_8x16.size



# Main function
# e.g. call with
#  sudo ./image-scroller.py --chain=4
# if you have a chain of four
if __name__ == "__main__":
    image_scroller = ImageScroller()
    if (not image_scroller.process()):
        image_scroller.print_help()

