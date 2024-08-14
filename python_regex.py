# import re

# str1="Hugo boss"

# pattern_ID='/^[1-9]\d{5}(?:\d{2})(?:\d{2})\d{3}(?:\d|X)$/'
# ID_number='440981198204036132'

# pattern_phone=r'1\d{9}'
# phone_number='13760681998'

# match_result = re.match('[H]',str1)
# search_result = re.search('[u]',str1)
# findall_result = re.findall('[o]',str1)

# # print(match_result)
# # print(search_result)
# # print(findall_result)


# ID_match_result = re.match(pattern_ID,ID_number)
# print(ID_match_result)

# phone_match_result = re.match(pattern_phone,phone_number)
# print(phone_match_result)


# import re
# import requests

# msg = 'abcd1234abc'

# result = re.match(r'abc(\d+?)',msg)
# print(result)

# path='<img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=30a7526a9282d158bb8259b9b00b19d5/704bde177f3e67092893917b35c79f3dfadc55f5.jpg" size="2227636" changedsize="true" width="560" height="840" style="cursor: url(&quot;http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur&quot;), pointer;">'
# result = re.match(r'<img class="BDE_Image" src="(.*?)"',path)
# image_path=result.group(1)
# print(image_path)

# response=requests.get(image_path) 
# with open('aa.jpg','wb') as wstream:
#     wstream.write(response.content)
          


import re

msg="abcd1234abc234bcde"
parttrn =r'[ef]*'
result = re.match(parttrn,msg)
result.group()
print(result.group())