import sys,os,json

d = json.loads(open('graph.train.entities.json').read())
c = 0
for item in d:
    c += len(item['entities'])
print(c)
d = json.loads(open('graph.test.entities.json').read())
c1 = 0
for item in d:
    c1 += len(item['entities'])
print(c,c1,c+c1)
