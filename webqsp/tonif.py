from pynif import NIFCollection
import sys,os,json,re


d = json.loads(open('input/webqsp.test.entities.with_classes.json').read())

collection = NIFCollection(uri="http://sda.tech/webquestions")

for item in d:
    if not item['utterance']:
        continue
    uid = item['question_id']
    context = collection.add_context(uri="http://sda.tech/webquestions/%s"%uid,
    mention=item['utterance'])
    beg = 0
    for entity in item['entities']:
        if entity is None:
            continue
        context.add_phrase(taIdentRef='http://www.wikidata.org/entity/'+entity, beginIndex=beg, endIndex=beg+1)
        beg+=1

generated_nif = collection.dumps(format='turtle')
f = open('webqsp.test.nif','w')
f.write(generated_nif)
f.close()

