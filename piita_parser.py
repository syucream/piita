# -*- coding: utf-8 -*-

import MeCab

def is_important(nodeval):
    f0 = nodeval.split(',')[0]
    return f0 == '名詞' or f0 == '動詞' or f0 == '形容詞' or f0 == '記号'

def get_words(str):
    mt = MeCab.Tagger('-Ochasen')
    mt.parse('') # To avoid unexpected UnicodeDecodeError ...
    node = mt.parseToNode(str)

    doc = []
    while node:
        if is_important(node.feature):
            doc.append(node.surface)
        node = node.next
    return doc
