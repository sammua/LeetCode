#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
auther: mabin
date  : 2018-03-15 16:47
用来在每次写完题目后, 更新 README.md
题目都是按照 000.template.py 里的格式写的, 之后直接更新到上面
"""
import os
import re

program_dir = os.path.abspath(os.path.dirname(__file__))
root = os.path.join(program_dir, "../../")
readme_path = os.path.join(root, "README.md")

info_lineno = 7  # xxx.yyy.py 中 第七行

programs = {}
records = {}

records_template = "| {} | {} | [Python](./Algorithms/Python/{}) |\n"
excess = "description/"  # 一些地址是多出一部分的


class Pre(object):
    """用来做一些预处理, 检查等工作"""

    @classmethod
    def filter_files(cls, _list):
        """过滤文件名, 提取出 001~xxx 的程序文件名"""
        digit_files = filter(lambda x: x.split(".")[0].isdigit(), _list)
        digit_files.sort()  # 把 000 给去掉
        return digit_files[1:]

    @classmethod
    def get_num(cls, _string):
        """得到 001.two-sum.py 等程序的编号"""
        return int(_string.strip().split(".")[0])

    @classmethod
    def get_readme_info(cls, _string):
        """得到 readme 中的基本信息"""
        temp = _string.split("|")
        if len(temp) == 6:
            num, address = temp[1].strip(), temp[-2].strip()
            if num.isdigit():
                return num, address
        return False

    @classmethod
    def check_program_files(cls, _list):
        """确保程序文件号码是连续的"""
        print _list
        if int(_list[-1].split(".")[0]) == len(_list):
            for item in _list:
                programs[cls.get_num(item)] = item
                print item
            return True
        return False

    @classmethod
    def check_readme_files(cls):
        """检查 README.md 里面记录的程序文件名"""
        with open(readme_path, "r") as fr:
            for line in fr:
                line = line.strip()
                temp = cls.get_readme_info(line)
                if temp:
                    records[cls.get_num(temp[0])] = temp[1]

    @classmethod
    def get_new_ones(cls, _records, _programs):
        """取 两个列表的 异或"""
        out = list(set(_programs) - set(records))
        out.sort()
        return out


class Update(object):
    """生成 新 内容"""

    @staticmethod
    def get_program_dict():
        """获得要所有题目的列表
           {1: "文件名", 2: "文件名",,,}
        """
        # 获取程序文件名列表
        filenames = os.listdir(".")
        # 获取题目文件名列表
        program_files = Pre.filter_files(filenames)
        print program_files
        # 检查并更新 program_dict
        if Pre.check_program_files(program_files):
            print "[valid]program files are all right"
        else:
            raise ValueError("[invalid]something wrong with the program files")
        # print programs

    @staticmethod
    def get_readme_dict():
        """得到 readme 里面的 程序列表信息"""
        # 检查并更新 records
        Pre.check_readme_files()
        # print records

    @staticmethod
    def get_new_program_info(num):
        """通过文档编号, 找到新增文件, 得到要加入到readme 中的信息"""
        file_name = programs[num]
        file_path = os.path.join(program_dir, file_name)
        out = None
        with open(file_path, "r") as fr:
            count = 0
            for line in fr:
                count += 1
                if count == info_lineno:
                    line = line.strip()
                    num, _ = file_name.split(".", 1)
                    out = records_template.format(num, line, file_name)
                    out = out.replace("description/", "")
        return out

    @staticmethod
    def write(_string):
        with open(readme_path, "a") as fw:
            fw.write(_string)


def update_readme():
    # 得到程序列表
    Update.get_program_dict()
    # 得到当前readme 列表
    Update.get_readme_dict()
    # 得到 待添加 的程序列表
    new_ones = Pre.get_new_ones(records.keys(), programs.keys())
    print "[update_list]: {}".format(new_ones)
    # 得到带输入的文本
    for i in new_ones:
        _string = Update.get_new_program_info(i)
        print "added file: {}".format(i)
        Update.write(_string)


if __name__ == '__main__':
    # program
    # get_program_dict()
    # records
    # get_readme_dict()
    # update
    update_readme()
