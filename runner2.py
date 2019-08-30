# coding=utf-8
import time
import unittest
from BeautifulReport import BeautifulReport
import os


nowtime = time.strftime("%Y%m%d%H%M%S")
# 获取路径
curpath = os.path.dirname(os.path.realpath(__file__))
casepath = os.path.join(curpath, ".")
if not os.path.exists(casepath):
    print("测试用例需放到‘case’文件目录下")
    os.mkdir(casepath)
reportpath = os.path.join(curpath, "./report")
if not os.path.exists(reportpath): os.mkdir(reportpath)


def add_case(case_path=casepath, rule="test_manila_1*.py"):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,
                                                  top_level_dir=None)
    return discover


def run(test_suit):
    result = BeautifulReport(test_suit)
    result.report(filename=f'Bangkok Report.html', description='Automation Test', log_path='./report')

if __name__ == "__main__":
    # 用例集合
    run(add_case())
