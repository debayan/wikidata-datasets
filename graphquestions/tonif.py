from pynif import NIFCollection
import sys,os,json,re


gold = []
f = open('input/graph.train.entities.json')
d = json.loads(f.read())

for item in d:
    unit = {}
    unit['uid'] = int(item['question_id'])
    unit['question'] = item['utterance']
    unit['entities'] = item['entities']
    gold.append(unit)


collection = NIFCollection(uri="http://sda.tech/graphquestions")

for item in gold:
    uid = item['uid']
    context = collection.add_context(uri="http://sda.tech/graphquestions/%s"%uid,
    mention=item['question'])
    for entity in item['entities']:
        if entity is None:
            continue
        context.add_phrase(taIdentRef='http://www.wikidata.org/entity/'+entity, beginIndex=0, endIndex=1)

generated_nif = collection.dumps(format='turtle')
f = open('graphquestions.train.nif','w')
f.write(generated_nif)
f.close()

