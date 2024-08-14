import re

str1="Hugo boss"

pattern_ID='/^[1-9]\d{5}(?:\d{2})(?:\d{2})\d{3}(?:\d|X)$/'
ID_number='440981198204036132'

pattern_phone=r'1\d{9}'
phone_number='1376068199dfd8'

match_result = re.match('[H]',str1)
search_result = re.search('[u]',str1)
findall_result = re.findall('[o]',str1)

# print(match_result)
# print(search_result)
# print(findall_result)


ID_match_result = re.match(pattern_ID,ID_number)
print(ID_match_result)

phone_match_result = re.match(pattern_phone,phone_number)
print(phone_match_result)