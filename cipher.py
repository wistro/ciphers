#!/usr/bin/python

import sys, getopt, classdef, functions

def main(argv) :
  encode = True
  verbose = False
  keyword = ""
  message = ""
  ciphers = ""
  try:
    opts, args = getopt.getopt(argv, "edc:k:m:vh", ["encode", "decode", "ciphers=", "keyword=", "message=", "help"])
  except getopt.GetoptError:
    print 'cipher.py -[vhed] -c [C[1-25]ANV] -m [message] -k [keyword]'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print """cipher.py -edvh -c [C[1-25]ANV] -k [keyword] -m [message]
        For more help use cipher.py --help"""
      sys.exit()
    elif opt == '--help':
      functions.printREADME()

if __name__ == "__main__":
  main(sys.argv[1:])
