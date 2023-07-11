from PyQt5 import QtWidgets
import datetime
import os
import cv2
import numpy as np
import math


def select_file(title, dir_path, file_filter):
    """
    function: this function is fot selected file
        title: the title window
        dir_path: the path directory file stored
        file_filter: the filter to selected file on the directory
    """
    options = QtWidgets.QFileDialog.DontUseNativeDialog
    file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, title, dir_path,
                                                         file_filter,
                                                         options=options)
    return file_path


def read_image(image_path):
    """
    read image function
    """
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError("`{}` not cannot be loaded".format(image_path))
    return img


def saveImage(filename, image):
    ss = datetime.datetime.now().strftime("%H_%M_%S")
    name = "../result/Images/" + filename + "_" + str(ss) + ".png"
    os.makedirs(os.path.dirname(name), exist_ok=True)
    cv2.imwrite(name, image)
    QtWidgets.QMessageBox.information(None, "Information", "Image saved !!")


def drawPoint(image, heightImage, coordinatePoint):
    if heightImage >= 1000:
        cv2.circle(image, coordinatePoint, 10, (0, 255, 0), 20, -1)
    else:
        cv2.circle(image, coordinatePoint, 6, (0, 255, 0), 12, -1)
    return image


def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    """ function for resize image and keep ratio"""
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)

    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation=inter)
    return resized


def corner_detect(image, sigma=1, threshold=0.01):
    # height, width = image.shape
    # shape = (height, width)
    # Calculate the dx,dy gradients of the image (np.gradient doesnt work)
    dx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    dy = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
    # Get angle for rotation
    _, ang = cv2.cartToPolar(dx, dy, angleInDegrees=True)
    # Square the derivatives (A,B,C of H) and apply apply gaussian filters to each
    sigma = (sigma, sigma)
    Ixx = cv2.GaussianBlur(dx * dx, sigma, 0)
    Ixy = cv2.GaussianBlur(dx * dy, sigma, 0)
    Iyy = cv2.GaussianBlur(dy * dy, sigma, 0)

    H = np.array([[Ixx, Ixy], [Ixy, Iyy]])
    # Find the determinate
    num = (H[0, 0] * H[1, 1]) - (H[0, 1] * H[1, 0])
    # Find the trace
    denom = H[0, 0] + H[1, 1]
    # Find the response using harmonic mean of the eigenvalues (Brown et. al. variation)
    R = np.nan_to_num(num / denom)

    # Adaptive non-maximum suppression, keep the top 1% of values and remove non-maximum points in a 9x9 neighbourhood
    R_flat = R[:].flatten()
    # Get number of values in top threshold %
    N = int(len(R_flat) * threshold)
    # Get values in top threshold %
    top_k_percentile = np.partition(R_flat, -N)[-N:]
    # Find lowest value in top threshold %
    minimum = np.min(top_k_percentile)
    # Set all values less than this to 0
    R[R < minimum] = 0
    # Set non-maximum points in an SxS neighbourhood to 0
    s = 9
    for h in range(R.shape[0] - s):
        for w in range(R.shape[1] - s):
            maximum = np.max(R[h:h + s + 1, w:w + s + 1])
            for i in range(h, h + s + 1):
                for j in range(w, w + s + 1):
                    if R[i, j] != maximum:
                        R[i, j] = 0

    # Return harris corners in [H, W, R] format
    features = list(np.where(R > 0))
    features.append(ang[np.where(R > 0)])
    corners = zip(*features)
    return list(corners)


def draw_corners(corners, image):
    i = 0
    for h, w in corners:
        cv2.circle(image, (w, h), 3, (0, 0, 255), -1)
        # caption = '{},{}'.format(h, w)
        cv2.putText(image, str(i), (w - 5, h + 10), cv2.FONT_HERSHEY_COMPLEX, 0.3, (0, 255, 0))
        i += 1
    return image


def get_corner_list(corners):
    coor = []
    for h, w, r in corners:
        caption = '{},{}'.format(h, w)
        res = tuple(map(int, caption.split(',')))
        coor.append(res)
    return coor


def distance(point_a, point_b):
    """Returns the distance between two points."""
    x0, y0 = point_a
    x1, y1 = point_b
    return math.fabs(x0 - x1) + math.fabs(y0 - y1)


def draw_matches(matches, img_left, img_right, verbose=False):
    # Determine the max height
    height = max(img_left.shape[0], img_right.shape[0])
    # Width is the two images side-by-side
    width = img_left.shape[1] + img_right.shape[1]

    img_out = np.zeros((height, width, 3), dtype=np.uint8)
    # Place the images in the empty image
    img_out[0:img_left.shape[0], 0:img_left.shape[1], :] = img_left
    img_out[0:img_right.shape[0], img_left.shape[1]:, :] = img_right

    # The right image coordinates are offset since the image is no longer at (0,0)
    ow = img_left.shape[1]

    # Draw a line between the matched pairs in green
    for p1, p2 in matches:
        p1o = (int(p1[1]), int(p1[0]))
        p2o = (int(p2[1] + ow), int(p2[0]))
        color = list(np.random.random(size=3) * 256)
        cv2.line(img_out, p1o, p2o, color, thickness=2)

    if verbose:
        print("Press enter to continue ... ")
        cv2.imshow("matches", img_out)
        cv2.waitKey(0)