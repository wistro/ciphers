#!/usr/bin/python

import sys, getopt, classdef, functions

def main(argv) :
  encode = True #true for encode, false for decode
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
    elif opt == '-v':
      verbose = True
    elif opt in ('-c', '--ciphers'):
      ciphers = arg
    elif opt in ('-m', '--message'):
      message = arg
    elif opt in ('-k', '--keyword'):
      keyword = arg
    elif opt in ('-d', '--decode'):
      encode = False
    elif opt in ('-e', '--encode'):
      #check if user gave both 'e' and 'd' flags and send error
      if ( encode == False ):
        print 'please choose either encode (-e) or decode (-d) not both'
        sys.exit()
    else
      message = arg
  functions.encode(ciphers, message, keyword, verbose, encode)

if __name__ == "__main__":
  main(sys.argv[1:])
