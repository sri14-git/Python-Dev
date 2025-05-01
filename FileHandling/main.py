# This is a sample Python script.
import time

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



file=open("hello.txt",'w')
file.write("Hello worl")
file.close()
# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
a=[1,2,3,4]
b=[1,2,3]
print(list(zip(a,b)))
# print(help(time))
print(time.strftime("%Y"))
print(ord("A"))