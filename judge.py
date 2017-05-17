# -*- coding: utf-8 -*-
#
# Judge a doc is poem or not.
#

import json
import sys
import gensim
from gensim import models
import piita_parser

MODEL_FILENAME = 'piita.model'
TAG2MSG = {'0': 'Its NOT poem.', '1': 'Its maybe poem!'}

def search_doctag(model, words):
    vec = model.infer_vector(words)
    similarities = model.docvecs.most_similar([vec])
    return similarities[0][0]

if __name__ == '__main__':
    doc = sys.stdin.read()
    words = piita_parser.get_words(doc)
    model = models.Doc2Vec.load(MODEL_FILENAME)
    tag = search_doctag(model, words)
    print(TAG2MSG[tag])
