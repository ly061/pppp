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


def run(city, case_path=casepath):
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=f"test_{city}_pencm.py",
                                                   top_level_dir=None)
    result = BeautifulReport(discover)
    result.report(filename=f'{city} Report.html', description='Automation Test', log_path='./report')

if __name__ == "__main__":
    # 用例集合
    citys = ['hongkong', 'beijing']
    # citys = ['hongkong', 'beijing', 'bangkok', 'beverly_hills', 'chicago', 'manila', 'newyork', 'paris', 'shanghai', 'tokyo']

    run('hongkong')
