# -*- coding:utf-8 -*-
import gensim
import sys
import os
from gensim.models import keyedvectors
reload(sys)
sys.setdefaultencoding('utf8')


# 读取测试所用的词对
def load_word_pairs(file_name):
    word_pairs_list = []
    with open(file_name) as file_reader:
        while True:
            str_line = file_reader.readline().decode(encoding='utf-8')
            if not str_line:
                break
            str_line = str_line.strip('\n')
            str_line = str_line.strip('\r\n')
            str_line_list = str_line.split('\t')
            word_pairs_list.append(str_line_list)
    return word_pairs_list


if __name__ == '__main__':
    word_vectors1_file_path = sys.argv[1]
    word_vectors2_file_path = sys.argv[2]
    word_pairs_file_path = sys.argv[3]
    print "load word pairs"
    word_pairs_list = load_word_pairs(word_pairs_file_path)

    print "load word vectors"
    word_vectors1 = keyedvectors.KeyedVectors.load_word2vec_format(word_vectors1_file_path, binary=True)
    word_vectors2 = keyedvectors.KeyedVectors.load_word2vec_format(word_vectors2_file_path, binary=True)

    vocab1 = word_vectors1.vocab
    vocab2 = word_vectors2.vocab
    print "vocab size of " + word_vectors1_file_path + " is: ", len(vocab1)
    print "vocab size of " + word_vectors1_file_path + " is: ", len(vocab2)

    # 计算每一对词的相似度
    print "compute similarity"
    acc1_list = []
    acc2_list = []
    for word_pairs in word_pairs_list:
        word1 = word_pairs[0]
        word2 = word_pairs[1]
        if (word1 in vocab1) and (word2 in vocab1):
            acc1 = word_vectors1.similarity(word1, word2)
        else:
            acc1 = -1.0
        acc1_list.append(acc1)
        if (word1 in vocab2) and (word2 in vocab2):
            acc2 = word_vectors2.similarity(word1, word2)
        else:
            acc2 = -1.0
        acc2_list.append(acc2)

    # 计算平均相似度
    sum = 0.0
    for acc in acc1_list:
        sum += float(acc)
    print "similarity on " + word_vectors1_file_path + ": ", sum/len(acc1_list)

    sum = 0.0
    for acc in acc2_list:
        sum += float(acc)
    print "similarity on " + word_vectors2_file_path + ": ", sum/len(acc1_list)
