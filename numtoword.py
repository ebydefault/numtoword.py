"""

numtoword.py

Yet another number to words in Python


Copyright 2021 Wardhana <ellam.bydefault@gmail.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

def numtoword(num):
  digit = {
    0: "nol",
    1: "satu",
    2: "dua",
    3: "tiga",
    4: "empat",
    5: "lima",
    6: "enam",
    7: "tujuh",
    8: "delapan",
    9: "sembilan"
  }

  # Only official wording is listed.
  #
  # Reference:
  #
  # Pedoman Umum Pembentukan Istilah Edisi Ketiga, pp. 55-56
  # https://badanbahasa.kemdikbud.go.id/lamanbahasa/sites/default/files/Pedoman_Umum%20Pembentukan_Istilah_PBN_0.pdf
  #
  # Accessed: 6 December 2021
  tenpow = {
    1:  "puluh",
    2:  "ratus",
    3:  "ribu",
    6:  "juta",
    9:  "miliar",
    12: "triliun",
    15: "kuadriliun",
    18: "kuintiliun",
    21: "sekstiliun",
    24: "septiliun",
    27: "oktiliun",
    30: "noniliun",   # Not listed in KBBI.
    33: "desiliun"
  }

  # alias order matters:
  alias = {
    "satu puluh"       : "sepuluh",
    "sepuluh satu"     : "sebelas",
    "sepuluh dua"      : "dua belas",
    "sepuluh tiga"     : "tiga belas",
    "sepuluh empat"    : "empat belas",
    "sepuluh lima"     : "lima belas",
    "sepuluh enam"     : "enam belas",
    "sepuluh tujuh"    : "tujuh belas",
    "sepuluh delapan"  : "delapan belas",
    "sepuluh sembilan" : "sembilan belas",
    "satu ratus"       : "seratus",
    "satu ribu"        : "seribu"
  }

  point    = "koma"
  minus    = "minus"
  tooLarge = "angka terlalu besar"

  ### integer to words ###
  def itowords(inum):
    l = len(str(inum))
    w = []
    # t = 0

    for i in range(l):
      n = int(str(inum)[i])

      if n != 0:
        w.append(digit[n])
        t = 0
      elif (n == 0) and (i == 0):   # n is zero.
        w.append(digit[n])
        break

      # the main algorithm
      x = l - i - 1
      y = x % 3
      z = x if y == 0 else y

      if z > t:
        w.append(tenpow[z])
        t = z

    words = " ".join(w)

    for k,v in alias.items():
      words = words.replace(k,v)

    return words

  ### decimal to words ###
  def dtowords(dnum):
    w = []

    for i in str(dnum):
      w.append(digit[int(i)])

    return " ".join(w)

  ### process number ###
  minus  = (minus + " ") if num < 0 else ""
  numAry = str(num).split('.')

  if len(str(int(num))) > max(tenpow.keys()) + 3:
    return tooLarge
  elif len(numAry) == 1:                # num is integer.
    return minus + itowords(abs(num))
  else:                                 # num is float.
    inum = int(abs(num))
    dnum = int(numAry[1])

    return minus + " ".join([itowords(inum), point, dtowords(dnum)])

# vim: ts=2 sts=2 sw=2 et
