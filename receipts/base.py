#!/usr/bin/env python
import os
from fastai.vision import *


def main():
    def image_classifier(path):
        """
        Run classifier to determine whether image contains a receipt
        or not. Returns boolean value.
        """
        learner = load_learner('.', 'receipt_classifier.pkl')
        image_path = path
        image = open_image(image_path)
        pred_class, _, _ = learner.predict(image)
        if str(pred_class) == "receipts":
            # return True
            print(True)
        else:
            # return False
            print(False)

    return image_classifier('receipts/images/example.jpg')
