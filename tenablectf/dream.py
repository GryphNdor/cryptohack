with open('speech.txt', 'r') as file:
    data = file.read().replace('\n', '')
    data = data.replace(' ','')

f = open('dreamoutput.txt','a')

f.write(data)

with open('dreamoutput.txt','r') as file:
  data2 = file.read()

print(data2[8972])

#flag{8337,669,8972,3621,8898,5581,8720,1900,5208}
#flag{E#}