#!/usr/bin/python

from math import ceil

class Cipher:
  'Class that forms the paramaters of any cipher'
  __vigtable = (('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'),
      ('B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A'),
      ('C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B'),
      ('D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C'),
      ('E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D'),
      ('F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E'),
      ('G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F'),
      ('H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G'),
      ('I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'),
      ('J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'),
      ('K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'),
      ('L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'),
      ('M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'),
      ('N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'),
      ('O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'),
      ('P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'),
      ('Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'),
      ('R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q'),
      ('S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R'),
      ('T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S'),
      ('U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'),
      ('V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'),
      ('W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V'),
      ('X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W'),
      ('Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X'),
      ('Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y'))
  __atbash = ('Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A') 
  __num = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26')
  
  def __init__(self, cipher):
    self.cipher = cipher[0]
    if ( len(cipher) > 1 ):
      self.offset = int(cipher[1:])
    else:
      self.offset = 26
    self.replace = {}
    self.message = ""
    self.keyword = ""
    self.output = ""

#creates a dictionary with values in the form "input char": "output char" for encoding a cipher
#see _createDecodeDic for dictionary for decoding
  def _createEncodeDic(self) :
    if (self.cipher == "C") :
      self.replace = dict(zip(self.__vigtable[self.offset], self.__vigtable[0]))
    elif (self.cipher == "A") :
      self.replace = dict(zip(self.__vigtable[0], self.__atbash)) 
    elif ( (self.cipher == "N") or (self.cipher == "V") ):
      self.replace = dict(zip(self.__vigtable[0], self.__num))
    else :
      print "The cipher code supplied is invalid. Please use only 'C' 'A' 'N' or 'V'"
    return

#creates a dictionary with valuse in the form of "input char": "output char" for decoding a cipher
#the dictionary created will be the inverse of that created by _createEncodeDic()
#for example, in a Caesar cipher with offset 3, _createEncodeDic()'s first entry would be {'A': 'D'}
#whereas _createDecodeDic()'s first entry would be {'D': 'A'}
#given that dictionaries are unsorted "first entry" above refers to the first entry created by the function
  def _createDecodeDic(self) :
    if (self.cipher == "C") :
      self.replace = dict(zip(self.__vigtable[0], self.__vigtable[self.offset]))
    elif (self.cipher == "A") :
      self.replace = dict(zip(self.__atbash, self.__vigtable[0])) 
    elif (self.cipher == "N") :
      self.replace = dict(zip(self.__num, self.__vigtable[0]))
      #print self.replace
    elif (self.cipher == "V") :
      self.replace = dict(zip(self.__num, self.__vigtable[0]))
      self.replace.update(dict(zip(self.__vigtable[0], self.__num)))
    else :
      print "The cipher code supplied is invalid. Please use only 'C' 'A' 'N' or 'V'"
    return

  def encode(self, message, keyword = "NONE") :
    self.message = message.upper() #make sure message is all uppercase
    self.keyword = keyword.upper() #make sure keyword is all uppercase
    self._createEncodeDic() #create the necessary encoding dictionary
    if (self.cipher == "V") :
      #DO THE COMPLICATED VIGENERE THING
      self.__repeat() #repeats keyword such that it is the same length as message
      for index in range(len(self.message)) :
        self.output += self.__vigtable[self.replace[self.message[index]]][self.replace[self.keyword[index]]]
    else :
      for letter in self.message :
        self.output += self.replace[letter]
    return

  def decode(self, message, keyword = "NONE") :
    self.message = message.upper() #if message is letters, ensure it is all uppercase
    self.keyword = keyword.upper() #make sure keyword is all uppercase
    #print self.message
    self._createDecodeDic()
    #print self.replace
    if (self.cipher == "V") :
      self.__repeat() #repeat keyword such that it is the same length as the encoded message
      #print self.keyword
      for index in range(len(self.message)) :
        #print self.keyword[index]
        #print self.replace[self.keyword[index]]
        #print self.__vigtable[int(self.replace[self.keyword[index]])]
        thisTable = self.__vigtable[int(self.replace[self.keyword[index]]) - 1] #pull the row from vigTable that corresponds to the current letter in the keyword
        #then convert the tuple thisTable into a string so that we can use the string.find function
        thisString = ""
        for jndex in range(len(thisTable)) :
          thisString += thisTable[jndex]
        #print thisString
        #print self.message[index]
        #print thisString.find(self.message[index])
        pos = str(thisString.find(self.message[index]) + 1)
        if ( len(pos) == 1 ):
          pos = '0' + pos
        self.output += self.replace[pos]
        #print self.output
    elif (self.cipher == "N") :
      for index in range(0, len(self.message), 2) :
        self.output += self.replace[self.message[index:index+2]]
    else :
      for char in self.message :
        self.output += self.replace[char]
    return

  #repeats keyword such that it is the same length as message
  def __repeat(self) :
    self.keyword = (self.keyword * int(ceil(float(len(self.message)) / len(self.keyword))))[:len(self.message)]
    return
