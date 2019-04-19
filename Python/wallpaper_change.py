import ctypes
import os 
import random 
import time
import schedule

def is_img_file(f):
    return f.endswith('jpg') or f.endswith('png') or f.endswith('jpeg')

def job():
    wallpaper_dir = "path to folder containing wallpaper"

    img_files = os.listdir(wallpaper_dir)
    img_files = list(filter(is_img_file, img_files))
    # print("Img Files: {}".format(img_files))

    rand_num = random.randint(0, len(img_files)-1)
    desktop_wallpaper_img = wallpaper_dir + "\\" + str(img_files[rand_num])

    # print("Desktop Wallpaper:{}".format(desktop_wallpaper_img))

    ctypes.windll.user32.SystemParametersInfoW(20, 0, desktop_wallpaper_img, 0)

schedule.every().hour.do(job)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
