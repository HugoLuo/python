str1="JustdoIt"

#将字符串变成全部变成小写
result1=str1.lower()
print(result1)

#将字符串变成全部变成大写
result2=str1.upper()
print(result2)

#判断字符串开头是否是指定的内容。
# result3=str1.startswith("Just")
result3=str1.startswith("just")
print(result3)

result4=str1.endswith("It")
print(result4)


#查找字符串：找到返回索引，找不到返回-1
# result5=str1.find("do")
result5=str1.find("xxx")
print(result5)

#字符串转列表，根据指定的分割符将字符串拆分出来放到一个列表里
result6=str1.split("do")
print(result6)

#列表转字符串，将列表用指定的符号(字符串)连接起来组成一个字符串
names=["Jimbo","Hugo","Boss","Cici"]
one_string="|".join(names)
print(one_string)


#删除指定的字符串,返回一个新的字符串
# result7="JustdoIt999".strip("999")
result7="JustdoIt".strip("It")
print(result7)

#替换字符串
result8="JustDoIt999".replace("999","666")
print(result8)