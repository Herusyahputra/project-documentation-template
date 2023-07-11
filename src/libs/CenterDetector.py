"""
CENTER OF COLON

library for find the center
implementation Mask R-CNN model
written by haryanto
member of OIL-Lab
Ming Chi University of Technology
"""

import warnings
import os
import numpy as np
import cv2
from libs import model as modellib
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
import tensorflow.compat.v1 as tf

ROOT_DIR = os.path.abspath("./")
warnings.filterwarnings("ignore")

tf.disable_v2_behavior()
config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)


class Config:
    NAME = "polyp"  # Override in sub-classes
    CROP_SHAPE = np.array([256, 256, 3])
    IMAGE_COLOR = 'RGB'
    AUGMENT = True
    SCALE = True
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1
    bs = GPU_COUNT * IMAGES_PER_GPU
    STEPS_PER_EPOCH = 500 // bs
    VALIDATION_STEPS = 50 // bs
    BACKBONE = "resnet101"
    COMPUTE_BACKBONE_SHAPE = None
    BACKBONE_STRIDES = [4, 8, 16, 32, 64]
    FPN_CLASSIF_FC_LAYERS_SIZE = 1024
    TOP_DOWN_PYRAMID_SIZE = 256
    NUM_CLASSES = 1 + 1 # Override in sub-classes
    RPN_ANCHOR_SCALES = (8, 16, 32, 64, 128)
    RPN_ANCHOR_RATIOS = [0.5, 1, 2]
    RPN_ANCHOR_STRIDE = 1
    RPN_NMS_THRESHOLD = 0.7
    RPN_TRAIN_ANCHORS_PER_IMAGE = 320
    PRE_NMS_LIMIT = 6000
    POST_NMS_ROIS_TRAINING = 2048
    POST_NMS_ROIS_INFERENCE = 2048
    USE_MINI_MASK = True
    MINI_MASK_SHAPE = (56, 56)  # (height, width) of the mini-mask

    # Input image resizing
    # Generally, use the "square" resizing mode for training and predicting
    # and it should work well in most cases. In this mode, images are scaled
    # up such that the small side is = IMAGE_MIN_DIM, but ensuring that the
    # scaling doesn't make the long side > IMAGE_MAX_DIM. Then the image is
    # padded with zeros to make it a square so multiple images can be put
    # in one batch.
    # Available resizing modes:
    # none:   No resizing or padding. Return the image unchanged.
    # square: Resize and pad with zeros to get a square image
    #         of size [max_dim, max_dim].
    # pad64:  Pads width and height with zeros to make them multiples of 64.
    #         If IMAGE_MIN_DIM or IMAGE_MIN_SCALE are not None, then it scales
    #         up before padding. IMAGE_MAX_DIM is ignored in this mode.
    #         The multiple of 64 is needed to ensure smooth scaling of feature
    #         maps up and down the 6 levels of the FPN pyramid (2**6=64).
    # crop:   Picks random crops from the image. First, scales the image based
    #         on IMAGE_MIN_DIM and IMAGE_MIN_SCALE, then picks a random crop of
    #         size IMAGE_MIN_DIM x IMAGE_MIN_DIM. Can be used in training only.
    #         IMAGE_MAX_DIM is not used in this mode.

    IMAGE_RESIZE_MODE = "square"
    IMAGE_MIN_DIM = 512
    IMAGE_MAX_DIM = 512
    IMAGE_PADDING = True
    IMAGE_MIN_SCALE = 0
    IMAGE_CHANNEL_COUNT = 3
    MEAN_PIXEL = np.array([123.7, 116.8, 103.9])
    TRAIN_ROIS_PER_IMAGE = 200
    ROI_POSITIVE_RATIO = 0.33
    POOL_SIZE = 7
    MASK_POOL_SIZE = 14
    MASK_SHAPE = [28, 28]
    MAX_GT_INSTANCES = 20
    RPN_BBOX_STD_DEV = np.array([0.1, 0.1, 0.2, 0.2])
    BBOX_STD_DEV = np.array([0.1, 0.1, 0.2, 0.2])
    DETECTION_MAX_INSTANCES = 400
    DETECTION_MASK_THRESHOLD = 0.35
    DETECTION_MIN_CONFIDENCE = 0.7
    DETECTION_NMS_THRESHOLD = 0.3
    LEARNING_RATE = 0.001
    LEARNING_MOMENTUM = 0.9
    OPTIMIZER = 'ADAM'
    WEIGHT_DECAY = 0.0001
    LOSS_WEIGHTS = {
        "rpn_class_loss": 1.,
        "rpn_bbox_loss": 1.,
        "mrcnn_class_loss": 1.,
        "mrcnn_bbox_loss": 1.,
        "mrcnn_mask_loss": 1.
    }
    USE_RPN_ROIS = True

    # Train or freeze batch normalization layers
    #     None: Train BN layers. This is the normal mode
    #     False: Freeze BN layers. Good when using a small batch size
    #     True: (don't use). Set layer in training mode even when predicting
    TRAIN_BN = False  # Defaulting to False since batch size is often small
    GRADIENT_CLIP_NORM = 5.0

    def __init__(self):
        """Set values of computed attributes."""
        # Effective batch size
        self.BATCH_SIZE = self.IMAGES_PER_GPU * self.GPU_COUNT

        # Input image size
        if self.IMAGE_RESIZE_MODE == "crop":
            self.IMAGE_SHAPE = np.array([self.IMAGE_MIN_DIM, self.IMAGE_MIN_DIM,
                                         self.IMAGE_CHANNEL_COUNT])
        else:
            self.IMAGE_SHAPE = np.array([self.IMAGE_MAX_DIM, self.IMAGE_MAX_DIM,
                                         self.IMAGE_CHANNEL_COUNT])

        # Image meta data length
        # See compose_image_meta() for details
        self.IMAGE_META_SIZE = 1 + 3 + 3 + 4 + 1 + self.NUM_CLASSES

    def display(self):
        """Display Configuration values."""
        print("\nConfigurations:")
        for a in dir(self):
            if not a.startswith("__") and not callable(getattr(self, a)):
                print("{:30} {}".format(a, getattr(self, a)))
        print("\n")


inference_config = Config()
model_load = "../Model/center_colon.h5"
model = modellib.MaskRCNN(mode='inference',
                               config=inference_config,
                               model_dir=ROOT_DIR)
model.load_weights(model_load, by_name=True)
print("Loading weights from ", model_load)


class FindCenter:
    """
    this class is to find the coordinate of hollow
    """
    def center_coordinate(self, images):
        result = model.detect([images], verbose=0)
        r = result[0]
        coordinate = self.center_instances(images, r['rois'], r['scores'])
        return coordinate

    def center_instances(self, image, boxes, scores):
        """
        :param boxes: how many instance that detect by the model
        :param scores: the score of prediction
        :return: cx, cy
        """
        cx = []
        cy = []
        instance = boxes.shape[0]
        if not instance:
            print("no instance detect")
        else:
            assert boxes.shape[0]

        init_score = 0  # initial score of prediction
        for i in range(instance):
            if not np.any(boxes[i]):
                continue
            score = scores[i]
            if score > init_score:
                init_score = score
                # print(init_score)
                if init_score < 0.95:
                    continue
                else:
                    y1, x1, y2, x2 = boxes[i]
                    cx = int(round((x2 - x1) / 2) + x1)
                    cy = int(round((y2 - y1) / 2) + y1)
            else:
                continue

        return cx, cy
