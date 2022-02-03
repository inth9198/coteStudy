# 2시간 30분

def solution(name):
  alpha = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12,
   "N":13, "O":12, "P":11, "Q":10, "R":9, "S":8, "T":7, "U":6, "V":5, "W":4, "X":3, "Y":2, "Z":1, }
  
  splitName, stackA, listA = [], [], []
  result, start = 0, 0
  for i in range(len(name)):
    result += alpha[name[i]]

    if name[i] == 'A':
      if not stackA:
        splitName.append(name[start:i])
        start = i

      stackA.append('A') 

    elif name[i] != 'A' and stackA:
      splitName.append(name[start:i])
      listA.append(name[start:i])
      stackA = []
      start = i

  splitName.append(name[start:])
  if '' in splitName:
    splitName.remove('')

  if listA:
    maxA = max(listA, key=len)
    splitIdx = splitName.index(maxA)
    left, right = ''.join(splitName[:splitIdx]), ''.join(splitName[splitIdx+1:])
    delLen = len(splitName[splitIdx])
    
    if len(left) > len(right):
      cursor = len(name)-1
    else:
      cursor = len(name)-delLen+(len(left)-1)-1

  else:
    cursor = len(name)-1

  return result+cursor


print(solution("BBBBAABBB"))