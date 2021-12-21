# -*- coding: UTF-8 -*-
import random
class NormalPoet:
    def __init__(self, grammar, vocabulary):
        '''这里把grammar, vocabulary保存成对象的属性'''
        self.grammar = grammar
        self.vocabulary = vocabulary
    def get_random_word(self, wordlist):
        '''这里传入一个list，然后返回这个list中的任意元素'''
        # self.wordlist = wordlist
        return random.choice(wordlist) #引用了错误的函数 random.choices
    def nianshi(self):
        '''这里通过get_random_word随机取一种grammar，然后用string.replace替换grammar中的成分'''
        shi = self.get_random_word(grammar)
        for i in vocabulary:
            while i in shi:
                shi = shi.replace(i, self.get_random_word(vocabulary[i]), 1) #括号没封死 找语法报错找了半天lol
        return shi # 这个地方很奇怪，在12行 18行报错之前提示我这里缩进错误，但修改过后就无法正常替换list里的字符，改回之前的缩进就正常了
    def __iter__(self):
        '''返回一个迭代器'''
        #self.nianshi = 1
        #return self
    def __next__(self):
        '''返回一句诗'''
        #self.nianshi
        #self.nianshi += 1
        #return self
        #test bug

if __name__ == '__main__':
    # init grammar and vocabulary
    grammar = ['MM在DD', 'XX的MM在DD', 'MM是XX的', 'TTXX的MM', '从MM到MM']
    vocabulary = {}
    vocabulary['DD'] = ['蒸发', '磁化', '撕杀', '氧化', '互相残杀', '升华', '雾化', '自杀', '挥发', '被磁化', '自杀', '谈话', '磨擦', '说梦话', '说胡话']
    vocabulary['DJ'] = ['刺杀', '喝下', '咒骂', '磨擦', '轰炸', '刮', '溶化', '痛打', '磁化', '淡化', '大骂', '谋杀', '锤打', '攻打', '冲刷', '润滑', '暗杀', '拧开']
    vocabulary['TT'] = ['啊！', '噢！', '嘘！', '唉！', '呀！', '天啊！', '哈哈哈哈！']
    vocabulary['XX'] = ['哗哗啦啦', '宏大', '无穷大', '高大', '光滑', '无限大']
    vocabulary['MM'] = ['爸爸', '犹大', '大坝', '火把', '蒙娜丽莎', '尾巴', '酒吧']
    # create a poet
    poet = NormalPoet(grammar, vocabulary)
    # use loop to nianshi
    for i in range(10):
        print(poet.nianshi())
