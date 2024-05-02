import cv2
from skimage.exposure import equalize_adapthist
from skimage.filters.rank import enhance_contrast
from skimage.io import imsave
from skimage.restoration import denoise_bilateral
from skimage.util import img_as_ubyte
from skimage.morphology import disk


def process_img(src):
    # Access all images in the src directory
    img = cv2.imread(src)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_mean = gray_img.mean()
    adap_eq = equalize_adapthist(img, clip_limit=img_mean*0.0005)
    adap_eq = img_as_ubyte(adap_eq)
    adap_eq = cv2.cvtColor(adap_eq, cv2.COLOR_BGR2GRAY)
    adap_eq = denoise_bilateral(adap_eq, channel_axis=None)
    adap_eq = img_as_ubyte(adap_eq)
    enh = enhance_contrast(adap_eq, disk(1))

    imsave(f'temp/class1/temp.png', enh)
