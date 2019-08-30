import time
import unittest
from BeautifulReport import BeautifulReport
from multiprocessing import Pool

nowtime = time.strftime("%Y-%m-%d-%H-%M-%S")

def runner(city):
    discover = unittest.defaultTestLoader.discover(r"C:\Users\yan.liu\PycharmProjects\pppp\testcase", pattern=f"test_{city}_1*.py", top_level_dir=None)
    city1 = city.title()
    BeautifulReport(discover).report(filename=f"{city1} Test Report {nowtime}", description='Automation Test',
                                     log_path='./report')

if __name__ == '__main__':
    # li = ["manila","beijing","newyork","hongkong"]
    li = ["manila"]
    p = Pool(4)
    star_time = time.time()
    for i in li:
        p.apply_async(runner, args=(i,))
    p.close()
    p.join()
