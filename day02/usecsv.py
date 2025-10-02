import csv
import re

def opencsv(filename) :
  f = open(filename, 'r')
  reader = csv.reader(f)
  output = []
  for i in reader :
    output.append(i)
  return output

def deletecoma(output) :
  for i in output :
    for j in i :
      try :
        i[i.index(j)] = float(re.sub(',','',j))
      except :
        pass
  return output