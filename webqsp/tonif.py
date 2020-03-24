from pynif import NIFCollection
import sys,os,json,re


d = json.loads(open('input/webqsp.train.entities.json').read())

collection = NIFCollection(uri="http://sda.tech/webquestions")

for item in d:
    if not item['utterance']:
        continue
    uid = item['question_id']
    context = collection.add_context(uri="http://sda.tech/webquestions/%s"%uid,
    mention=item['utterance'])
    for entity in item['entities']:
        if entity is None:
            continue
        context.add_phrase(taIdentRef='http://www.wikidata.org/entity/'+entity, beginIndex=0, endIndex=1)

generated_nif = collection.dumps(format='turtle')
f = open('webqsp.train.nif','w')
f.write(generated_nif)
f.close()

