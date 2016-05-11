#!/bin/sh

cd /home/vaishthiru/Downloads/FinalProject/tst
#cmake .
#make
./Segmentation /home/vaishthiru/Downloads/FinalProject/inputimage/input.png
cd /home/vaishthiru/Downloads/FinalProject/svmTrainTest/
#echo "Work on cv.."
#workon cv
#echo "Extract features and train for characters..."
#python hogForChar.py > hfc.out
echo "Test..."
python hogForTest.py  > hft.out


