import requests
import collections

class cool_dictionary(dict):
  def __init__(self):
    self = dict()
  
  def add(self, key, value):
    self[key] = value

r = requests.get('http://167.71.246.232:8080/rabbit_hole.php?page=cE4g5bWZtYCuovEgYSO1')

allinfo = cool_dictionary()

key = int(r.text[r.text.find('[')+1:r.text.find(',')])
value = r.text[r.text.find(',')+3:r.text.find(']')-1]

allinfo.add(key,value)


# first ran this loop as a while loop with the status code 200 and watched the output until it stopped printing out a page
for i in range(1581):
  page = r.text[r.text.find(']')+3:]
  r = requests.get('http://167.71.246.232:8080/rabbit_hole.php?page='+page)
  print(page +"{"+str(i)+"}")
  key = int(r.text[r.text.find('[')+1:r.text.find(',')])
  value = r.text[r.text.find(',')+3:r.text.find(']')-1]
  allinfo.add(key,value)

#ordered the keys
ol = collections.OrderedDict(sorted(allinfo.items()))


flag = ""
for k, v in ol.items(): flag += v

print(flag)