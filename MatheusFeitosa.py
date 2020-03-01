def convhextonum(letra):
  hexa = {"0" : 0,
           "1" : 1,
           "2" : 2,
           "3" : 3,
           "4" : 4,
           "5" : 5,
           "6" : 6,
           "7" : 7,
           "8" : 8,
           "9" : 9,
           "a" : 10,
           "b" : 11,
           "c" : 12,
           "d" : 13,
           "e" : 14,
           "f" : 15,
  }
  return hexa[letra]

def convnumtohexa(numero):
  num = { 0 : "0",
           1 : "1",
           2 : "2",
           3 : "3",
           4 : "4",
           5 : "5",
           6 : "6",
           7 : "7",
           8 : "8",
           9 : "9",
           10 : "a",
           11 : "b",
           12 : "c",
           13 : "d",
           14 : "e",
           15 : "f",
  }
  return num[numero]

def convnumto64(letra):
  num = { 0 : "A",
           1 : "B",
           2 : "C",
           3 : "D",
           4 : "E",
           5 : "F",
           6 : "G",
           7 : "H",
           8 : "I",
           9 : "J",
           10 : "K",
           11 : "L",
           12 : "M",
           13 : "N",
           14 : "O",
           15 : "P",
           16 : "Q",
           17 : "R",
           18 : "S",
           19 : "T",
           20 : "U",
           21 : "V",
           22 : "W",
           23 : "X",
           24 : "Y",
           25 : "Z",
           26 : "a",
           27 : "b",
           28 : "c",
           29 : "d",
           30 : "e",
           31 : "f",
           32 : "g",
           33 : "h",
           34 : "i",
           35 : "j",
           36 : "k",
           37 : "l",
           38 : "m",
           39 : "n",
           40 : "o",
           41 : "p",
           42 : "q",
           43 : "r",
           44 : "s",
           45 : "t",
           46 : "u",
           47 : "v",
           48 : "w",
           49 : "x",
           50 : "y",
           51 : "z",
           52 : "0",
           53 : "1",
           54 : "2",
           55 : "3",
           56 : "4",
           57 : "5",
           58 : "6",
           59 : "7",
           60 : "8",
           61 : "9",
           62 : "+",
           63 : "/",
  }
  return num[letra]

def converte64(mensagem):
  mensagem = mensagem[::-1]
  i = 0
  resultado = ""
  while(len(mensagem)>(i*3)): 
    if(len(mensagem)>((i*3)+2)):
      a = mensagem[0 + 3*i]
      b = mensagem[1 + 3*i]
      c = mensagem[2 + 3*i]
      d = convhextonum(a) + 16*convhextonum(b) + 16*16*convhextonum(c)
      e = d%64
      d = (d - e)/64
      resultado = resultado + convnumto64(d) + convnumto64(e)
    elif(len(mensagem)>((i*3)+1)):
      a = mensagem[0 + 3*i]
      b = mensagem[1 + 3*i]
      d = convhextonum(a) + 16*convhextonum(b)
      e = d%64
      d = (d - e)/64
      resultado = resultado + convnumto64(d) + convnumto64(e)
    else:
      a = mensagem[0 + 3*i]
      d = convhextonum(a)
      e = d%64
      d = (d - e)/64
      resultado = resultado + convnumto64(e) + convnumto64(d)
    i = i + 1
  print(resultado[::-1])

def fazxor(primeiro, segundo):
  i = 0
  resultado = ""
  while(len(primeiro)>i):
    a = convhextonum(primeiro[i])
    b = convhextonum(segundo[i])
    c = 0
    if(a>=8):
      if(b<8):
        c = c + 8
        a = a - 8
      else:
        a = a - 8
        b = b - 8
    else:
      if(b>=8):
        c = c + 8
        b = b - 8
        
    if(a>=4):
      if(b<4):
        c = c + 4
        a = a - 4
      else:
        a = a - 4
        b = b - 4
    else:
      if(b>=4):
        c = c + 4
        b = b - 4

    if(a>=2):
      if(b<2):
        c = c + 2
        a = a - 2
      else:
        a = a - 2
        b = b - 2
    else:
      if(b>=2):
        c = c + 2
        b = b - 2

    if(a>=1):
      if(b<1):
        c = c + 1
        a = a - 1
      else:
        a = a - 1
        b = b - 1
    else:
      if(b>=1):
        c = c + 1
        b = b - 1
        
    resultado = resultado + convnumtohexa(c)
    i = i+1
  
  print(resultado)
    

converte64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
fazxor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")


#https://colab.research.google.com/drive/1DcLI-Gala78YKhg3IwX6z4PhB9EHWsfJ