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

def encode(ciphers, message, keyword = "", verbose = False, encode = True):
  #regular expression for matching the first cipher code listed by user
  #will be used recursively to match successive ciphers, perform the
  #cipher and then remove that cipher from the beginning of the string
  #matches a single character for A N or V cipher
  #matches C and a number from 1-25 for caesar cipher
  p = re.compile('^[ANV]|^C[1-9]|^C1[0-9]|^C2[0-5]') 
  tehMessage = message
  while (ciphers != ""):
    m = p.search( ciphers )
    cipher = classdef.Cipher( m.group() )
    if ( encode ):
      cipher.encode(tehMessage, keyword)
    else
      cipher.decode(tehMessage, keyword)
    if( verbose ):
      print cipher.message
    tehMessage = cipher.message
    del cipher
    ciphers = ciphers[m.end():]
  if ( encode ):
    print "The final encoded message is: " + tehMessage
  else
    print "The final decoded message is: " + tehMessage
  return
