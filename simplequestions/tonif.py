from pynif import NIFCollection
import sys,os,json,re



gold = []
f = open('annotated_wd_data_train.txt')
for line in f.readlines():
    line = line.strip()
    s,p,o,q = line.split('\t')
    gold.append((s,q))

collection = NIFCollection(uri="http://sda.tech/simplequestions")

for idx,item in enumerate(gold):
    question = item[1]
    entity = item[0]
    uid = idx
    context = collection.add_context(uri="http://sda.tech/simplequestions/%s"%uid, mention=question)
    context.add_phrase(taIdentRef='http://www.wikidata.org/entity/'+entity, beginIndex=0, endIndex=1)

generated_nif = collection.dumps(format='turtle')
f = open('simplequestions.train.nif','w')
f.write(generated_nif)
f.close()

