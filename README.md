This python script will apply the requested ciphers to the input string in the order provided.

Input message is not case sensitive - will be converted to all uppercase for output. Any non-letter characters in input will be left unchanged by the cipher. For added security, remove spaces and punctuation from message before input.

example usage: cipher.py -e -c C3N -m bill is watching
                  ouput: 05121515 1222 2604230611121710
INPUT FLAGS:

  -e, --encode (default)  Encode input text with given ciphers

  -d, --decode  Decode input text with given ciphers. (If text was encoded with multiple ciphers, you will need to reverse the order of encoding to decode properly).
        If decoding an A1Z26 cipher remember to add leading zeros for numbers 1-9 or you will get some weird output.

  -c, --ciphers  Choose which ciphers to apply and in which order to apply them. The string of letters and numbers that follows the -c will be used to determine which ciphers to use and the order in which to apply them.
        The available ciphers are:
          C[1-25] - Caesar cipher - replaces the original letter with the nth letter AFTER it in the alphabet REQUIRES A NUMBER FROM 1 to 25 INCLUSIVE AFTER THE C (a Caesar Cipher of 0 or 26 is the original text and numbers outside that range can be reduced to a number from 1 to 25)
          A - Atbash cipher - reverses the alphabet (so A becomes Z, B becomes Y and so on)
          N - A1Z26 cipher - replaces the nth letter of the alphabet with a 2 digit version of the number n (A becomes 01, J becomes 10, etc)
          V - Vigenère cipher - uses a series of Caesar ciphers and a key word to encode the input text. NB: USING THIS CIPHER REQUIRES THE -k FLAG AND A KEYWORD!!! The keyword is used to "mask" the text by determining the Caesar shift of each letter in the original text.
                The following table is used to encode the letter of the original text (top row) with the corresponding letter in that column based on the letter from the keyword (left-most column) see example below the table for clarification
                     A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
                  -------------------------------------------------------------------------------
                  A| A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
                  B| B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A
                  C| C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B
                  D| D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C
                  E| E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D
                  F| F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E
                  G| G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F
                  H| H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G
                  I| I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H
                  J| J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I
                  K| K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J
                  L| L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K
                  M| M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L
                  N| N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M
                  O| O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N
                  P| P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O
                  Q| Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P
                  R| R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q
                  S| S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R
                  T| T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S
                  U| U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T
                  V| V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U
                  W| W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V
                  X| X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W
                  Y| Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X
                  Z| Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y 

              Message:  MABELEATSSPRINKLES
              Key:      GRAVITYGRAVITYGRAV (keyword "GRAVITY" is entered as many times as necessary to fit the length of the message)
              Cipher:   SRBZTXYZJSKZBLQCEN

  -k, --keyword  Keyword for a Vignère cipher. Can be any word or phrase with no spaces and no special characters.

  -m, --message  Input message to encode. (can be given as last input without the flag)

  -v  Verbose mode. Will output the intermediary encodings/decodings as they are completed when using multiple successive ciphers

  -h, --help print this information

Will output the final encoded message to stdout.
