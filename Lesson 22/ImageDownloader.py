__author__ = 'Scott'

import random as Ran
import urllib.request as URL

def download(address):
    filename = str(Ran.randrange(25, 1000)) + 'a.jpg'
    URL.urlretrieve(address, filename)

download('http://hdnextyear.com/wp-content/uploads/2015/01/space-wallpaper-1920x1080-for-desktop-hd-wallpapers-aduphotocom-abstract-landscape-images-1920x1080-wallpaper.jpg')