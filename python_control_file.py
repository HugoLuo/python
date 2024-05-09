#从某处以读取的方式打开一个文件
# onefile=open("/Users/luohaitao/python3_demo/onefile.txt","r")
#从该文件读取内容作为字符串返回
# file_content=onefile.read()  #返回文件的所有内容(字符串的类型)
# print(type(file_content))
# file_content=onefile.readlines()  #返回文件的所有内容(列表的类型)
# print(file_content1)
# file_content=onefile.read(1)  #返回文件内容里的前两个字符
# file_content=onefile.readlines(-1)  
# for i in file_content:
#     print(i)
# print(file_content)

# file2=open("/Users/luohaitao/python3_demo/onefile.txt","w")  #使用w参数表示以覆盖的方式写入内容
# file2.write("the first time write.")
# file2.write("the second time write.")
# file2.close()


# file3=open("/Users/luohaitao/python3_demo/onefile.txt","a")     #使用a参数表示以追加的方式写入内容
# file3.write("the sixth time write file \n") 
# file3.write("the seventh time write file \n") 
# file3.close()

# 使用with open 打开文件将自动close()

import time
with open("/Users/luohaitao/python3_demo/onefile.txt","w+") as file4:
    file4.write("GuangZhou\n")
    file4.write("Liwan \n")

try:
   file5=open("/Users/luohaitao/python3_demo/onefile2.txt","r") 
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
