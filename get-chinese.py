# -*- coding:utf-8 -*-
import re
import sys
import argparse


def get_chinese_words(str_lines):
    re_chinese = re.compile(u'[\u4e00-\u9fa5]+')
    re_str_list = re_chinese.findall(str_lines)
    return "".join(re_str_list)

if __name__ == '__main__':
    input_file_path = '/data/cn_corpus/baidu_baike/part-r-00000'
    output_file_path = '/data/cn_corpus/baidu_baike/part-r-00000-chinese.txt'
    sum_line = 0
    file_writer = open(output_file_path, 'w')
    with open(input_file_path, 'r') as file_reader:
        while True:
            str_line = file_reader.readline().decode('utf-8', errors='ignore')
            if not str_line:
                break
            sum_line += 1
            if sum_line > 1000:
                break
            str_chinese = get_chinese_words(str_line)
            if len(str_chinese) > 0:
                file_writer.write(str_chinese.encode('utf-8') + '\n')
    file_reader.close()
    file_writer.close()
    print "done!"

