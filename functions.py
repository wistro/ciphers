#!/usr/bin/python

#Function definitions for cipher.py

import classdef

#Prints the README file from the local directory as extended help
#FOR LATER: Implement 'less' style scrolling print
def printREADME():
  README = open("README.md")
  print README.read()
  README.close()
  return

def encode(ciphers, message, keyword = "", verbose = False):

def decode(ciphers, message, keyword = "", verbose = False):
