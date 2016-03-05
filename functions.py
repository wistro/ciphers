#!/usr/bin/python

#Function definitions for cipher.py

import classdef, re

#Prints the README file from the local directory as extended help
#FOR LATER: Implement 'less' style scrolling print
def printREADME():
  README = open("README.md")
  print README.read()
  README.close()
  return

def dothething(ciphers, message, keyword = "", verbose = False, encode = True):
  #regular expression for matching the first cipher code listed by user
  #will be used recursively to match successive ciphers, perform the
  #cipher and then remove that cipher from the beginning of the string
  #matches a single character for A N or V cipher
  #matches C and a number from 1-25 for caesar cipher
  p = re.compile('^[ANV]|^C1[0-9]|^C2[0-5]|^C[1-9]') 
  tehMessage = message
  #print tehMessage
  while (ciphers != ""):
    m = p.search( ciphers )
    #print ciphers
    cipher = classdef.Cipher( m.group() )
    if ( encode ):
      cipher.encode(tehMessage, keyword)
    else:
      cipher.decode(tehMessage, keyword)
    if( verbose ):
      print cipher.output
    tehMessage = cipher.output
    del cipher
    ciphers = ciphers[m.end():]
  if ( encode ):
    print "The final encoded message is: " + tehMessage
  else:
    print "The final decoded message is: " + tehMessage
  return
