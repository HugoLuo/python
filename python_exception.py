try:
   file5=open("/Users/luohaitao/python3_demo/onefile.txt","r") 
   i=1/0
except FileNotFoundError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    file5.close()