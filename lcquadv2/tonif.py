from pynif import NIFCollection
import sys,os,json,re


d = json.loads(open('train.json').read())

collection = NIFCollection(uri="http://lc-quad2.sda.tech")

for item in d:
    if not item['question']:
        continue
    uid = item['uid']
    context = collection.add_context(uri="http://lc-quad2.0.sda.tech/%s"%uid,
    mention=item['question'])
    entities = re.findall( r'wd:([Q][0-9]*)', item['sparql_wikidata'])
    for entity in entities:
        context.add_phrase(taIdentRef='http://www.wikidata.org/entity/'+entity, beginIndex=0, endIndex=1)

generated_nif = collection.dumps(format='turtle')
f = open('lcquad2.0.train.nif','w')
f.write(generated_nif)
f.close()

