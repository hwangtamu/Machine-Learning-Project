# This is code is for computing the features
import math
from numpy import *
from numpy.linalg import *
import string
import re
import urlparse

# This function takes a url and returns
# a vector of feature values
def features_url(url,dim):

  # ulr is the string containing the url
  # dim is the number of features

  # the declaration of feature vector
  vec=zeros(dim)
  
  # computing the length of url
  length=len(url)
  vec[0]=length

  # counting the number of dots
  vec[1]=url.count('.')

  # counting number of digits
  mystr=url
  digits=re.findall('[0-9]+', mystr)
  num_digits=0
  for digit in digits:
    num_digits+=len(digit)
  vec[2]=num_digits
    
  # computing the length of the hostname
  hostname = urlparse.urlparse(url).hostname
  vec[3]=len(hostname)

  # counting the number of IP addresses contained
  # in the url
  ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', url )
  vec[4]=len(ip)

  # counting the numbers of subdomains
  vec[5]=url.count('/')

  # counting the number of '?'
  vec[6]=url.count('?')

  # counting number of '_'
  vec[7]=url.count('_')

  # counting number of '-'
  vec[8]=url.count('-')

  # counting number of '='
  vec[9]=url.count('=')

  # counting number of ';'
  vec[10]=url.count(';')
  
 # counting number of '&'
  vec[11]=url.count('&')

 # counting number of '%'
  vec[12]=url.count('%')

 # counting number of '#'
  vec[13]=url.count('#')

  # counting numbers of 'http'
  vec[14]=url.count('http')
  
  # counting numbers of 'www'
  vec[15]=url.count('www')

  return vec























