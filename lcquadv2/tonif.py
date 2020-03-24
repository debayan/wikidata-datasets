from pynif import NIFCollection
import sys,os,json,re


d = json.loads(open('test.json').read())

collection = NIFCollection(uri="http://sda.tech/lcquadv2")

for item in d:
    if not item['question']:
        continue
    uid = item['uid']
    context = collection.add_context(uri="http://sda.tech/lcquadv2/%s"%uid,
    mention=item['question'])
    entities = re.findall( r'wd:([Q][0-9]*)', item['sparql_wikidata'])
    for entity in entities:
        context.add_phrase(taIdentRef='http://www.wikidata.org/entity/'+entity, beginIndex=0, endIndex=1)

generated_nif = collection.dumps(format='turtle')
f = open('lcquad2.0.test.nif','w')
f.write(generated_nif)
f.close()

