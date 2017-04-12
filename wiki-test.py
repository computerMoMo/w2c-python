# -*- coding:utf-8 -*-
import jieba
import sys
if __name__ == '__main__':
    train_file_path = '/data/cn_corpus/wiki/wiki_cn'
    write_file_path = '/data/cn_corpus/wiki/wiki_test.txt'
    wiki_reader = open(train_file_path, 'r')
    wiki_writer = open(write_file_path, 'w')
    sum = 0
    while True:
        line = wiki_reader.readline().decode(encoding='utf-8', errors='ignore')
        if not line:
            break
        # line_list = jieba.lcut(line, cut_all=True)
        # wiki_writer.write(" ".join(line_list).encode(encoding='utf-8'))
        wiki_writer.write(line.encode(encoding='utf-8', errors='ignore'))
        sum += 1
        if sum % 10000 == 0:
            print sum
    wiki_reader.close()
    wiki_writer.close()
