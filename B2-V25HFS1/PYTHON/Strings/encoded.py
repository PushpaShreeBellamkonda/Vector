s=input()
d={}
for i in s:
    d[i]=d.get(i,0)+1
print(d)
print(max(d.values()))   #to get max value
print(max(d, key=d.get)) #to get max key     