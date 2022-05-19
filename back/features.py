import cv2
import mahotas as mt
import numpy as np
import pyfeats
import skimage.feature.texture


def get_glcm(image):
    data = []
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # gray = img
    hist = mt.features.haralick(img, compute_14th_feature=True, return_mean=True)
    means, std = cv2.meanStdDev(img)
    hist = np.concatenate((hist, means.transpose().flatten(), std.transpose().flatten()), axis=0)
    data.append(hist)
    cols = ['har_feat{}'.format(i) for i in range(0, 14)]
    channel = ['R-mean', 'G-mean', 'B-mean', 'R-std', 'G-std', 'B-std']
    cols.extend(channel)
    return cols, data


def get_zernikes(image):
    channel = ['R-mean', 'R-sd']
    data = []
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features, labels = pyfeats.zernikes_moments(gray)
    means, std = cv2.meanStdDev(gray)
    hist = np.concatenate((features, means.transpose().flatten(), std.transpose().flatten()), axis=0)
    data.append(hist)
    cols = ['Zernikes_Moments {}'.format(i) for i in range(0, 25)]
    cols.extend(channel)
    return cols, data


def get_lbp(image):
    channel = ['R-mean', 'G-mean', 'B-mean', 'R-std', 'G-std', 'B-std']
    data = []
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    patterns = skimage.feature.texture.local_binary_pattern(gray, 8, 1)
    hist, _ = np.histogram(patterns, bins=np.arange(2 ** 8 + 1), density=True)
    means, std = cv2.meanStdDev(img)
    hist = np.concatenate((hist, means.transpose().flatten(), std.transpose().flatten()), axis=0)
    data.append(hist)
    cols = ['lbp_feat{}'.format(i) for i in range(0, 256)]
    cols.extend(channel)
    return cols, data


def get_law(image):
    channel = ['R-mean', 'G-mean', 'B-mean', 'R-std', 'G-std', 'B-std']
    data = []
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features, labels = pyfeats.lte_measures(gray, None)
    means, std = cv2.meanStdDev(img)
    hist = np.concatenate((features, means.transpose().flatten(), std.transpose().flatten()), axis=0)
    data.append(hist)
    labels.extend(channel)
    cols = labels
    return cols, data


def get_hu(image):
    channel = ['R-mean', 'R-sd']
    data_hu = []
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features, labels = pyfeats.hu_moments(gray)
    means, std = cv2.meanStdDev(img)
    hist = np.concatenate((features, means.transpose().flatten(), std.transpose().flatten()), axis=0)
    data_hu.append(hist)
    cols = ['Hu_Moment{}'.format(i) for i in range(0, 7)]
    cols.extend(channel)