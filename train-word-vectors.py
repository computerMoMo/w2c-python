# -*- coding:utf-8 -*-
import gensim
import sys
import os
import multiprocessing
from gensim.models import Word2Vec


class TextReader(object):
    def __init__(self, data_file_path):
        self.data_file_path = data_file_path

    def __iter__(self):
        for file_name in os.listdir(self.data_file_path):
            with open(self.data_file_path+file_name, 'r') as file_reader:
                while True:
                    line = file_reader.readline()
                    if not line:
                        break
                    yield line.split()

if __name__ == '__main__':
    train_file_path = 'corpus/'
    vectors_save_path = 'vectors/'
    word_dim = 100
    word_min_count = 1
    model_workers = multiprocessing.cpu_count()
    en_text = TextReader(train_file_path)
    w2v_model = Word2Vec(en_text, size=word_dim, min_count=word_min_count, workers=model_workers)
    w2v_model.wv.save_word2vec_format(vectors_save_path+'imdb.txt', binary=False)
    w2v_model.wv.save_word2vec_format(vectors_save_path+'imdb.bin', binary=True)
    print "done"
