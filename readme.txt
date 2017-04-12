w2v-train.py 参数说明：--ch 语料中是否只保留中文，默认为中英文全部包含
                    --nlp 新增额外nlpcc训练语料，需要添加的次数
                    --folder_name 存放原始语料的文件夹，不需要输入路径，路径已经写入到程序
                    --vec_name 生成词向量文件的名字，不需要输入路径，路径已经写入到程序
	运行示例：python w2v-train.py --ch --nlp 10 --folder_name wiki/ --vec_name wiki-test :语料中只保留中文，nlpcc额外训练语料增加10次，原始语料使用的是wiki，生成词向量的名字为wiki-test
	python w2v-train.py --nlp 10 --folder_name wiki/ --vec_name wiki-test :语料中中英文全部包含，nlpcc额外训练语料增加10次，原始语料使用的是wiki，生成词向量的名字为wiki-test
	注意：最后一共会生成两个词向量文件，一个是以二进制存储的，一个是txt形式存储的
test-word-vector.py 一个用来简单比较两个词向量的demo，一共有三个参数，前两个是要比较的词向量的文件（二进制形式），第三个是用来计算相似度的词对文件(例如：word-pairs.txt)。
word-pairs.txt:每一行为要比较的两个词，中间用tab隔开