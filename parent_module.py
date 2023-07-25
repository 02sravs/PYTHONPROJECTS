#! D:\pythonprojects\myenv\Scripts\python.exe

n=10
print(n)

def func():
    global n
    n=8
    print(n)

func()


