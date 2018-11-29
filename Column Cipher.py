import math

try:
  with open('code.txt', 'r') as file:
    code = file.read()

except:
  print('Please create text file called code.txt with your encoded text')
  input()
  exit()

code = code.replace(' ', '');

print('--- Columnar Transposition Cipher tool ---')
print('--- by Sam Medwell >>>')

print()
print('This program will take the length of the key and put the encoded text into the form before it was read down the columns');
print()

keyLength = int(input('Enter the length of the key to test: '))
columnLength = math.ceil(len(code)/keyLength)

print('Column length: {}'.format(columnLength))


characterTable = [[] for i in range(0, columnLength)]

character = 0
for i in range(1,keyLength+1):
  rowNum = 0
  for row in characterTable:
    try:
      rowNum += 1
      row.append(code[character])
      print('Character {} column {} Row {} {} '.format(character, i, rowNum, row))
      character += 1
    except IndexError:
       break

print(characterTable)

invertedText = ''
for row in characterTable:
    for character in row:
        invertedText += character

print()
print(invertedText)
