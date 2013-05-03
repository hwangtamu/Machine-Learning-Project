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
Mali = []
Ben = []
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
a = []
for i in range(5):
    a.append(float(0.1+0.2*(i)))

for g in a:
    clf = svm.SVC(kernel='rbf', gamma=g, C=1.0)  # you can change this
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
    print 'For the malicious URLs'
    print 'false positive = ', count1
    print 'false negative = ', count2
    print 'precision = ', precision
    print 'recall = ', recall
    print 'f-measure = ', f1
    print '-------------------------------------'

    precision1 = float(size/2-count1)/float(size/2-count1+count2)
    recall1 = float(size/2-count1)/float(size/2)
    f11 = 2*precision1*recall1/(precision1+recall1)
    print 'For the benign URLs'
    print 'false positive = ', count2
    print 'false negative = ', count1
    print 'precision = ', precision1
    print 'recall = ', recall1
    print 'f-measure = ', f11
    Mali.append(str(g)+' '+str(count1)+' '+str(count2)+' '+str(precision)+' '+str(recall)+' '+str(f1))
    Ben.append(str(g)+' '+str(count2)+' '+str(count1)+' '+str(precision1)+' '+str(recall1)+' '+str(f11))
f = open('./mali.txt', 'w')
for i in Mali:
    f.write(i+'\n')
ff = open('./ben.txt', 'w')
for j in Ben:
    ff.write(j+'\n')