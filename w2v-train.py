# -*- coding:utf-8 -*-
import sys
import re
import gensim
import os
import multiprocessing
import jieba
import argparse
from gensim.models import Word2Vec


# 提取文本中的中文字符
def get_chinese(str_lines):
    re_chinese = re.compile(u'[\u4e00-\u9fa5]+')
    re_str_list = re_chinese.findall(str_lines)
    return "".join(re_str_list).encode('utf-8')


# 对中文文本进行分词
def cut_words(str_lines):
    word_list = jieba.lcut(str_lines, cut_all=True)
    return word_list


# 文本迭代器
class TextReader(object):
    # 初始化函数
    def __init__(self, data_file_path, chinese_only=True, add_nlpcc_data=False, nlpcc_data_file="", nlpcc_iteration=0):
        self.data_file_path = data_file_path
        self.chinese_only = chinese_only
        self.add_nlpcc_data = add_nlpcc_data
        self.nlpcc_data_file = nlpcc_data_file
        self.nlpcc_iteration = nlpcc_iteration

    # 跌代器每次返回带训练文本的一行
    def __iter__(self):
        # 打开nlpcc训练文件
        if self.add_nlpcc_data:
            epochs = 0
            while epochs < self.nlpcc_iteration:
                try:
                    nplcc_data_reader = open(self.nlpcc_data_file, 'r')
                    while True:
                        line = nplcc_data_reader.readline()
                        if not line:
                            break
                        line = line.decode(encoding='utf-8', errors='ignore')
                        # 提取文本中的中文
                        if self.chinese_only:
                            line = get_chinese(line)
                        # 分词
                        word_list = cut_words(line)
                        yield word_list
                except:
                    print "error in opening nlpcc data file!"
                    break
                epochs += 1

        # 打开预料库文件
        for file_name in os.listdir(self.data_file_path):
            try:
                with open(self.data_file_path+file_name, 'r') as file_reader:
                    while True:
                        line = file_reader.readline()
                        if not line:
                            break
                        line = line.decode(encoding='utf-8', errors='ignore')
                        # 提取文本中的中文
                        if self.chinese_only:
                            line = get_chinese(line)
                        # 分词
                        word_list = cut_words(line)
                        yield word_list
            except:
                print "error in opening "+self.data_file_path+file_name+"!"


if __name__ == '__main__':
    # 数据文件路径
    train_file_path = '/data/cn_corpus/'
    vectors_store_path = '/data/cn_corpus/'
    nlpcc_data_file = '/data/cn_corpus/nlpcc-dbqa/nlpcc-iccpol-2016.dbqa.training-data'

    # 语料参数设置
    parser = argparse.ArgumentParser()
    parser.add_argument('--ch', action='store_true', default=False, dest='chinese_only')
    parser.add_argument('--nlp', action='store', type=int, dest='nlp')
    parser.add_argument('--folder_name', action='store', dest='train_file_name')
    parser.add_argument('--vec_name', action='store', dest='vectors_file_name')
    w2v_command = parser.parse_args()
    train_file_name = w2v_command.train_file_name
    vectors_file_name = w2v_command.vectors_file_name
    nlpcc_iterations = w2v_command.nlp
    chinese_only = w2v_command.chinese_only
    if nlpcc_iterations > 0:
        add_nlpcc_data = True
    else:
        add_nlpcc_data = False

    # word2vec参数设置
    word_dim = 300
    word_min_count = 5
    model_workers = multiprocessing.cpu_count()-8
    if model_workers <= 0:
        model_workers = 8

    # 读取语料
    ch_text = TextReader(train_file_path+train_file_name, chinese_only=chinese_only, add_nlpcc_data=add_nlpcc_data,
                         nlpcc_data_file=nlpcc_data_file, nlpcc_iteration=nlpcc_iterations)

    print "training......"
    w2v_model = Word2Vec(ch_text, size=word_dim, min_count=word_min_count, workers=model_workers)

    print "store word vectors"
    w2v_model.wv.save_word2vec_format(vectors_store_path + vectors_file_name + '.txt', binary=False)
    w2v_model.wv.save_word2vec_format(vectors_store_path + vectors_file_name + '.bin', binary=True)
    print "program finished!"
