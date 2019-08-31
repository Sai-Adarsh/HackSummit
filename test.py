# USAGE
# python test.py

# import the necessary packages
from __future__ import print_function
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from imutils import paths
import numpy as np
import argparse
import mahotas
import cv2
import pickle
from train import describe


def predict(filename):
	# test images path
	imagePaths1 = sorted(paths.list_images("test"))
	# reading model from pickle
	with open("classifier.cPickle", "rb") as f:
		model = pickle.load(f)
	image1 = cv2.imread(filename)
	show1 = cv2.resize(image1,(500,600))
	features = describe(image1)
	prediction = model.predict(features.reshape(1, -1))[0]
	return prediction

if __name__ == '__main__':
    # test images path
    imagePaths1 = sorted(paths.list_images("test"))

    # reading model from pickle
    with open("classifier.cPickle", "rb") as f:
        model = pickle.load(f)

    # loop over a few random images
    for imagepath1 in imagePaths1:
	    print (imagepath1)
	    image1 = cv2.imread(imagepath1)
	    show1 = cv2.resize(image1,(500,600))
	    features = describe(image1)
	    prediction = model.predict(features.reshape(1, -1))[0]

	    # show the prediction
	    print("[PREDICTION] {}".format(prediction))
	    cv2.putText(show1, prediction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
	    cv2.imshow("Image", show1)
	    cv2.waitKey(0)
