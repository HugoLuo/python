import random

#generate random 0~1
randomNumber1=random.random()
print(str(randomNumber1))

#generate random from 1 to 10
randomNumber2=random.randint(1,10)
print(str(randomNumber2))


#generate random in range from A to B(not include B), and every change is C(default is 1)

list1 = random.randrange(1,10,2)

print(list1)

list2 = ['关羽','张飞','刘备','赵云','黄忠']
randomOne=random.choice(list2)
print(randomOne)

print("current list sort is: ",list2)
random.shuffle(list2)
print("after the list sort is ",list2)