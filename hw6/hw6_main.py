# Name: Adam Klingler
# Section: AB
# Description:

# imports here
import numpy as np
import matplotlib.pyplot as plt
import imageio

# constants here

# functions here


def invert_colors(img):
    '''
    This function takes in a color image and returns an image with inverted
    color.
    '''
    height, width, depth = img.shape()
    inverter = np.ones((height, width, depth)) * 255  # max value of a pixel

    return inverter - img


def blur(img, patch_size):
    '''
    Takes in a black and white and image and a patch size, and returns an image
    that is the original image blurred, which is proportional to the patch
    size.
    '''
    img_h, img_w = img.shape
    result_h = img_h - patch_size + 1
    result_w = img_w - patch_size + 1

    kernel = np.ones((patch_size, patch_size)) / patch_size ** 2
    result = np.zeros((result_h, result_w))

    for i in range(result_h):
        for j in range(result_w):
            window = img[i:i+patch_size, j:j+patch_size]
            result[i, j] = np.multiply(window, kernel)

    return result


def template_match(img, template):
    '''
    '''
    pass
