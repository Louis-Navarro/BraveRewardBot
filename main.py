import sys
import time

from tqdm import trange
from PIL import Image
from PIL import ImageChops
import pyscreenshot as ImageGrab
import pyautogui


class All:
    def __init__(self, bbox, fp):
        self.bbox = bbox
        self.example = Image.open(fp)

        click_x = (bbox[0] + bbox[2]) // 2
        click_y = (bbox[1] + bbox[3]) // 2
        self.click = (click_x, click_y)

    def _check_notif(self):
        im = ImageGrab.grab(bbox=self.bbox)

        diff = ImageChops.difference(im, self.example)
        if not diff.getbbox():
            return True
        
        return False

    def _get_money(self):
        pyautogui.click(*self.click)
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'w')

    def loop(self, sleep=60):
        while 1:
            time.sleep(sleep)

            pyautogui.scroll(-10)
            time.sleep(1)
            pyautogui.scroll(10)
            time.sleep(1)
        
            if self._check_notif():
                self._get_money()

            pyautogui.moveTo(2800, 500)


if __name__ == '__main__':
    if sys.platform == 'linux':
        bbox = (2644, 50, 2672, 82)
        fp = 'example_linux.png'

    else:
        print('Only linux is supported at the moment')

    main = All(bbox, fp=fp)
    main.loop(sleep=600)
