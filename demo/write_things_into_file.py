"""
step 1 :open the file
"""

"""
mode有几种模式
w 只能操作写入（如果文件中有数据，再次写入内容，会把原来的覆盖掉）
r只能读取 a向文件追加
w+ 可读可写  r+可读可写  a+可读可追加
wb+ 写入进制数据
"""
# file_handle = open("../data/data_language.txt",mode="a")
# file_handle.write("hello world1 \n")
# file_handle.close()
with open("../data/data_language.txt","a") as f:
    for i in  range(10):
        f.write("hello world \n")