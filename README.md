# Handwritten-Grocery-List-Detection
Introduction
The objective of this project is to design and implement an order generation application that detects a 
hand written grocery shopping list and converts it to a digital item list using linear SVM algorithm coupled with
HOG feature extraction. The data set contains different 62 different characters (English alphabets capital and small,
Digits 0-9) written in 55 different styles. In particular, we apply the tools of machine learning to detect the handwritten 
characters.
We have used segmentation, HOG feature extraction and linear SVM model to obtain better performance from any of the 
constituent machine learning algorithms.

Problem Definition and Algorithm
The input here is the images of characters written in 55 different styles. The algorithm learns the original character 
for the different styles of characters in the phase by using the HOG features to label the characters. This is later used
when a character in a different style unseen by the algorithm is given as input. The final output, the digitalized form of
the recognized characters, is obtained by extracting its HOG features and detecting the characters by matching the HOG 
features from the trained linear SVM model.

Tools Used:
OpenCV2
Python 3.0
Libraries:  Scikit Learn for HOG, SVM, KNN

Dataset:
The Chars74K dataset
http://www.ee.surrey.ac.uk/CVSSP/demos/chars74k/EnglishHnd.tgz

Experiment Evaluation
We experimented the recognition with SVM and KNN classifiers.
Accuracy of SVM is approximately 60% whereas KNN accuracy was very low. 

KNN is slow because the model cannot be trained and saved, every time it trains based    on the feature generated. Linear SVM saves the trained model and uses it for training directly. SVM gives good better performance than KNN classifier.
 
