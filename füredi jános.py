# ITMP tanfolyam 2020.10.10
# https://github.com/green-fox-academy/http-info-syllabus/blob/master/python.md
#
# Author: Füredi János
#

print("\n"+"="*12,"2020.10.10. ITMP Python tanfolyam feladatok megoldása")
print("Készítette: Füredi János")
print("\nJavaslom a repli.it Settings / Layout / stacked beállítást.")

print("\n"+"="*12,"Feladat 1")

print("Mutasd be magad változók segítségével! Hozz létre három változót egyet a nevednek, egyet a korodnak és egyet a kedvenc gyümölcsödnek. Írd ki a konzolra a következőket a változók használatával:")

nev = "John"
kor = 18
gyumolcs = "banán"

print("\nSziasztok,",nev,"vagyok",kor,"éves!")
print("A kedvenc gyümölcsöm a",gyumolcs+".")

print("\n"+"="*12,"Feladat 2")
print("Írd ki a konzolra százszor, hogy \"Nem fogok csalni a vizsgán.\"")

for i in range(100):
  print("Nem fogok csalni a vizsgán.")

print("\n"+"="*12,"Feladat 3")

print("Írd ki a konzolra a számokat 1-től 100-ig úgy, hogy ha a szám osztható 3-mal, akkor azt írod a szám helyett, hogy \"Piff\", ha osztható 7-tel, akkor azt, hogy \"Puff\", ha mindkettővel, akkor pedig azt, hogy \"PiffPuff\".")
for i in range(1,101):
  if i%3==0 and i%7==0:
    print("PiffPuff")
  elif i%3==0 :
    print("Piff")
  elif i%7==0 :
    print("Puff")
  else:
    print(i)

print("\n"+"="*12,"Feladat 4")
print("Hozz létre egy változót sorokSzama néven, amit tölts fel értékkel, pl. 4. Készíts programot, amely ezt rajzolja ki a konzolra, úgy hogy pont annyi sor legyen, amennyi épp a változó értéke:")
print("    *\n   ***\n  *****\n *******\n")

sorokSzama = int(input("Hány sort írjak ki:"))
# 
for i in range(1,sorokSzama+1):
  space = " "*(sorokSzama-i)
  star = "*"*(2*i-1)
  print(space+star)

print("\nNehéz feladatok, ne izgulj ha nem mennek magadtól, azoknak van akik jól haladnak.")


print("\n"+"="*12,"Feladat 5")

print("Írj egy függvényt, ami egy szám-listát vesz be paraméterként, és visszaadja a számok átlagát.")
def atlag(szamok):
  ossz= 0
  for a in szamok:
    ossz+=a
  return ossz/len(szamok)

# sum() függvény használatával
def atlag2nd(szamok):
  return sum(szamok)/len(szamok)

szamLista = [1,2,3,4,5]
print(szamLista)
print(atlag(szamLista))
print(atlag2nd(szamLista))

print("\n"+"="*12,"Feladat 6")
print("Írj egy függvényt, ami egy számok mátrix-át veszi be paraméterül (szám-listák listája), és a mátrixot elforgatja 90 fokkal balra.\n")

""" Example
Input
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Output
[
    [3, 6, 9],
    [2, 5, 8],
    [1, 4, 7]
]
"""

def rotate(myInput):
  row = len(myInput)
  col = len(myInput[0])

  # Create new empty matrix
  myOutput = []
  for i in range(col):
    myOutput.append([0]*row)

  # Copy items from myInput
  for i in range(row):
    for j in range(col):
      # print(i," ",j," ",myInput[i][j])
      myOutput[col-1-j][i]=myInput[i][j]

  return myOutput

myList = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

myList = [
    [1, 2, 3, 10],
    [4, 5, 6, 11],
    [7, 8, 9, 12]
]

print("Bemenet:")
for item in myList: print(item)

print("\nElforgatott:")
for item in rotate(myList): print(item)


print("\n"+"="*12,"Feladat 7")
print("Írj egy függvényt, ami paraméterként átvesz egy szöveget, és visszatér egy listával, ami a 3 leggyakoribb karaktert tartalmazza a szövegből csökkenő sorrendben.")

def betu3(s):
  betuk = {}
  for c in s:
    if c in betuk:
      betuk[c] += 1
    else:
      betuk[c] = 1

  betukRendezett = sorted(betuk.items(), key=lambda x: x[1], reverse=True) 
  # print(betukRendezett)
  return betukRendezett[:3]


str = "3 leggyakoribb karaktert tartalmazza a szövegből"
print("\""+str+"\"")
print(betu3(str))


print("\n"+"="*12,"Feladat 8")
print("Írj egy függvényt, ami palindromokat keres egy szövegben. Paraméterként vegyen át szöveget, és térjen vissza egy listával, ami tartalmazza a szovegben legalább 3 betűs palindromokat.\n")

def palindrom(mystr):
  pali = []
  # Step over the input string
  for p in range(len(mystr)):
    s=mystr[p::]

    # Substring check
    for i in range(3,len(s)+1):
      substr = s[:i:]
      revstr = substr[::-1]
      if substr == revstr:
        # print(substr)
        pali.append(substr)

  return pali

# === Start ===
str = "dog goat dad duck doodle never"
# ["og go", "g g", " dad ", "dad", "d d", "dood", "eve"]
# str = "apple"
#  [] 
# str = "racecar"
# ["racecar", "aceca", "cec"]
# str =  ""
# []

print("Bemenet:")
print(str)
print("\nPalindromok:")
print(palindrom(str))

print("\n"+"="*12,"Feladat 9")
print("Írj egy függvényt, ami egy bemeneti számról eldönti, hogy Armstrong-szám-e?")
# Teszteléshez 153, 370, 371, 407, 1634, 8208

def armstrong(a):
  szamjegyek = []
  aa = a
  while(aa!=0):
    szamjegyek.append(aa%10)
    aa//=10
    # print(szamjegyek)
  
  ossz=0;
  for szam in szamjegyek:
    ossz+=szam**len(szamjegyek)
    # print(ossz)
  return ossz==a

szam = int(input("Szam: "))
print(armstrong(szam))

print("\n"+"="*12,"Feladat 10")
print("Írj egy függvényt, ami megvalósítja Conway életjátékának egy körét. A bemenete legyen egy szám mátrix, ahol az élő sejtek 1-es, a halottak pedig 0-ás értéket vesznek fel. A kimenete legyen egy új mátrix.")
# https://hu.wikipedia.org/wiki/%C3%89letj%C3%A1t%C3%A9k

def gameOfLife(inMatrix):
  row = len(inMatrix)
  col = len(inMatrix[0])

  # Create new empty matrix for counting neighbours
  nbMatrix = []
  for i in range(row):
    nbMatrix.append([0]*col)
  
  # Segédmátrix a szomszédszámoláshoz
  # A mátrix önmagával érintkezik
  # Plusz oszlop bal és jobb oldalon az inMatrix utolsó és első elemével
  workMatrix = []
  for line in inMatrix:
    newLine = line[:]
    newLine.insert(0, line[-1])
    newLine.append(line[0])
    workMatrix.append(newLine)
  # Plusz sor ez ejején és a végén     
  # first row
  workMatrix.insert(0,workMatrix[-1:][0])
  # last row (Az első sor beszúrása után most már a második sor lesz a szomszéd!!!)
  workMatrix.append(workMatrix[1:2][0])
  # corners: Szembe sarkok 
  workMatrix[0][0]=inMatrix[-1][-1]
  workMatrix[0][-1]=inMatrix[-1][0]
  workMatrix[-1][0]=inMatrix[0][-1]
  workMatrix[-1][-1]=inMatrix[0][0]

  # Teszteléshez
  # print("\nSegédmátrix:")
  # for line in workMatrix: print(line)
  # print()

  # Szomszédok számolása és tárolása az nbMatrix-ban
  for i in range(1,len(workMatrix)-1):
    for j in range(1,len(workMatrix[0])-1):
      # 8 lehetséges sejtszomszéd megszámolása
      for ii in range(i-1, i+2):
        for jj in range(j-1, j+2):
          nbMatrix[i-1][j-1]+=workMatrix[ii][jj]
      # Saját magát ne számolja be!
      nbMatrix[i-1][j-1] -= workMatrix[i][j]      

      # Favágó megoldás, de legalább átlátható
      # nbMatrix[i-1][j-1]+=workMatrix[i-1][j-1]      
      # nbMatrix[i-1][j-1]+=workMatrix[i-1][j]
      # nbMatrix[i-1][j-1]+=workMatrix[i-1][j+1]
      # nbMatrix[i-1][j-1]+=workMatrix[i][j-1]
      # nbMatrix[i-1][j-1]+=workMatrix[i][j+1]      
      # nbMatrix[i-1][j-1]+=workMatrix[i+1][j-1]      
      # nbMatrix[i-1][j-1]+=workMatrix[i+1][j]
      # nbMatrix[i-1][j-1]+=workMatrix[i+1][j+1]

  # Teszteléshez
  # print("\nSzomszédok száma:")
  # for line in nbMatrix: print(line)
  # print()

  # Segédmátrix most már felesleges kiegészítő sorainak és oszlopainak eltávolítása
  workMatrix.pop(0)
  workMatrix.pop(-1)
  for i in range(0,len(workMatrix)):
    workMatrix[i].pop(0)
    workMatrix[i].pop(-1)

  # Az életjáték következő körének szerkesztése az alábbi szabályok szerint:

  # A sejt túléli a kört, ha két vagy három szomszédja van.
  # A sejt elpusztul, ha kettőnél kevesebb (elszigetelődés), vagy háromnál több (túlnépesedés) szomszédja van.
  # Új sejt születik minden olyan cellában, melynek környezetében pontosan három sejt található.

  # Az elhaló sejtek megjelölése
  # A születő sejtek elhelyezése
  # A megjelölt sejtek eltávolítása

  for i in range(0,row):
    for j in range(0,col):
      if nbMatrix[i][j]<2 or nbMatrix[i][j]>3:
        workMatrix[i][j]=0
      elif nbMatrix[i][j]==3:
        workMatrix[i][j]=1

  return workMatrix
  # End of gameOfLife(inMatrix) function

myConway = [
    [1, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 1],    
    [0, 0, 1, 1, 0, 0]
]

# Kapott tesztadatok
myConway = [
  [1, 1, 1, 0, 0],
  [0, 0, 0, 1, 1], 
  [1, 1, 1, 1, 1],
  [0, 1, 0, 0, 1],
  [0, 1, 0, 0, 1]
]

eredmeny = [
  [0, 1, 1, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 1, 1]
]

print("\nBemenet:")
for line in myConway:
  print(line)

print("\nÉletjáték egy köre:")
for line in gameOfLife(myConway):
  print(line)

print("\nThe end of exercise. Goodbye!")
