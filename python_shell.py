import os

# os.system 获取shell 脚本的返回码
# response_code=os.system('pwd')
# print(response_code)

# os.popen 获取shell 脚本的输出 
# CMD='touch ttt.txt'
# response_content=os.popen(CMD)
# print("Response content is {0}".format(response_content))



# subprocess.getstatusoutput 获取 shell的返回码和输出
import subprocess
# (status,output)=subprocess.getstatusoutput('ls -ltr /')
# print("status is {0}".format(status))
# print("output is {0}".format(output))

# response_content=subprocess.getoutput('pwd')

response_content=subprocess.getoutput('ls -ltr')
print("response content is {0}".format(response_content))

#能用 python实现的尽量不调用shell脚本



