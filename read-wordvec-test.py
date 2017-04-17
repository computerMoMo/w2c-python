# -*- coding:utf-8 -*-
import gensim
import sys
import os
import numpy as np
from gensim.models import keyedvectors

if __name__ == '__main__':
    word_vectors1_file_path = sys.argv[1]
    word_vectors1 = keyedvectors.KeyedVectors.load_word2vec_format(word_vectors1_file_path, binary=True)
    word_array = np.asarray(word_vectors1.word_vec('的'.decode(encoding='utf-8')))
    print word_array.shape
    print "words in vectors: "+len(word_vectors1.vocab)
