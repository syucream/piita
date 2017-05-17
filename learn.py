# -*- coding: utf-8 -*-
#
# Learn Doc2Vec model.
#

import json
import sys
import gensim
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
import piita_parser

MODEL_FILENAME = 'piita.model'

if __name__ == '__main__':
    stdin = sys.stdin.read()
    items = json.loads(stdin)
    docs = [TaggedDocument(words=piita_parser.get_words(i['body']), tags=str(i['label'])) for i in items]
    model = Doc2Vec(documents=docs, size=100, min_count=3)
    model.save(MODEL_FILENAME)
