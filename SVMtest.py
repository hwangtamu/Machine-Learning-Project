# This code is to train and test the data using Support 
# Vector machine (SVM) classifier
import math
from numpy import *
from numpy.linalg import *
import string
import re
import urlparse
from sklearn import svm
from features import *

# reading training data
f = open('training_data1.txt')
urls1 = f.readlines()
f.close()
dim=16 # number of features
size=len(urls1) # the data size
data1=zeros(size*dim).reshape((size, dim))
for i in range(0,size):
  data1[i]=features_url(urls1[i],dim)

# class values for the training data
target1=zeros(size)
for i in range(0,size/2):
   target1[i]=0
for i in range(size/2,size):
   target1[i]=1

# reading testing data
f = open('testing_data1.txt')
urls2 = f.readlines()
f.close()

size=len(urls2) # the data size
data2=zeros(size*dim).reshape((size, dim))
for i in range(0,size):
  data2[i]=features_url(urls2[i],dim)

# the definition of SVM
clf = svm.SVC(kernel='rbf',C=2.0)  # you can change this
clf.fit(data1,target1)

y_pred=clf.predict(data2)

count1=0
count2=0
for i in range(0,size/2):
  if (y_pred[i]==1):
    count1+=1

for i in range(size/2,size):
  if (y_pred[i]==0):
    count2+=1

precision = float(size/2-count2)/float(size/2-count2+count1)
recall = float(size/2-count2)/float(size/2)
f1 = 2*precision*recall/(precision+recall)
print 'false positive = ', count1
print 'false negative = ', count2
print 'precision = ', precision
print 'recall = ', recall
print 'f-measure = ', f1
