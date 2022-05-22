import cv2
import mahotas as mt
import numpy as np
import pyfeats
import skimage.feature.texture
import mahotas


def get_glcm(image):
    data = []
    img = cv2.imread(image)
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
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
    data = []
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features, labels = pyfeats.zernikes_moments(gray)
    features = mahotas.features.zernike_moments(gray, 9)
    means, std = cv2.meanStdDev(gray)
    hist = np.concatenate((features, means.transpose().flatten(), std.transpose().flatten()), axis=0)
    data.append(hist)
    cols = ['Zernikes_Moments {}'.format(i) for i in range(0, 25)]
    return cols, data


def get_lbp(image):
    data = []
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    patterns = skimage.feature.texture.local_binary_pattern(gray, 8, 1)
    hist, _ = np.histogram(patterns, bins=np.arange(2 ** 8 + 1), density=True)
    means, std = cv2.meanStdDev(img)
    #hist = np.concatenate((hist, means.transpose().flatten(), std.transpose().flatten()), axis=0)
    data.append(hist)
    cols = ['lbp_feat{}'.format(i) for i in range(0, 256)]
    #channel = ['R-mean', 'G-mean', 'B-mean', 'R-std', 'G-std', 'B-std']
    #cols.extend(channel)
    return cols, data


def get_law(image):
    data = []
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features, labels = pyfeats.lte_measures(gray, None, l=5)
    means, std = cv2.meanStdDev(img)
    hist = np.concatenate((features, means.transpose().flatten(), std.transpose().flatten()), axis=0)
    data.append(hist)
    cols = labels
    return cols, data


def get_hu(image):
    data = []
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features, labels = pyfeats.hu_moments(gray)
    means, std = cv2.meanStdDev(img)
    hist = np.concatenate((features, means.transpose().flatten(), std.transpose().flatten()), axis=0)
    data.append(hist)
    cols = ['Hu_Moment{}'.format(i) for i in range(0, 7)]
    return cols, data


def get_fos(image):
    data = []
    img = cv2.imread(image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features, labels = pyfeats.fos(img, None)
    hist = features
    data.append(hist)
    cols = labels
    return cols, data