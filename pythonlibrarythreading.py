#multi threading  - to reduce the time for program excecution
#dividing a large code set into piece of codes((units) such units is called 'THREAD' and that is excecute parallelly  to reduce
#  execution tyme we use multi threading

'''multi-threading--- in python allows concurrent excecution of multiple threads enabling efficient use of CPU resourses and improved performance in 
input output bound task'''


### without using thread 
#calculating tym

# import time
# def sqr(num):
#     for i in num:
#         time.sleep(1)
#         print("square is", i*i)

# def cube(num):
#     for j in num :
#         time.sleep(1)
#         print("cube is",j*j*j)

# a=[1,2,3,4,5]
# t1=time.time() #creating obj
# sqr(a)
# cube(a)
# print(time.time()-t1)

#so here after completion of square only cube is working

## by using threading

# import time
# import threading

# def sqr(num):
#     for i in num:
#         time.sleep(1)
#         print("square is", i*i)

# def cube(num):
#     for j in num :
#         time.sleep(1)
#         print("cube is",j*j*j)

# a=[1,2,3,4,5]
# t1=time.time() #creating obj
# thread1=threading.Thread(target=sqr,args=(a,))
# thread2=threading.Thread(target=cube,args=(a,))
# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# print(time.time()-t1)


######################################################################

# import threading
# import time

# def download_file(filename,duration):
#     print(f"start download:{filename}")
#     time.sleep(duration)
#     print(f"download completed:{filename}")

# files=[("file1.pdf",3),("file2.pdf",5),("file3.pdf",2)]
# threads=[]
# for filename,duration in files:
#     thread=threading.Thread(target=download_file,args=(filename,duration))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()

# print("all download is completed")

### if we are dwnloading one by one  multiple downloads will be simultaneously dowloaded for that here we are using threads

####################################################################################################################################

'''raise CONDITION'''

# IF WE AE ACCESSING OR MODIFYING MULTIPLE THREADS SOME TIMES SOME DATAS WILL BE LOST SO TO AVOID THAT WE USE lock concept

'''A raise condition occurs when multiple threads access and modify a shared resource at same time leading to unexpected or incorrect 
result due to unsynchronised execution'''
# for eg: imagine 2 threads trying to increment a shared variable simultaneously without synchronisation they may reda and
#  write incorrect values leading to data inconsistency

# eg occuring raise condition

# import threading

# counter=0
# def increment():
#     global counter
#     for i in range(100000):
#         counter+=1

# t1=threading.Thread(target=increment)
# t2=threading.Thread(target=increment)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(f"final counter value{counter}")

## both threads read the value of counter at the same time they increment it separately but write back outdated values
# causing data lose

## even though this code  has a raise condition u might still get the correct result this happens due to factors like thread scheduling
# pythons GIL(GLOBAL INTERPRETER LOCK)
#PYTHONS GIL  allows only one thrread to excecute python byte code at a tym since ur task is simple GIL may prevent 2 parallel execution
# making it appear like sequential execution


# import threading

# counter=0
# lock=threading.Lock()
# def increment():
#     global counter
#     for i in range(100000):
#         with lock:
#             counter+=1

# t1=threading.Thread(target=increment)
# t2=threading.Thread(target=increment)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(f"final counter value{counter}")

# to prevent raise condition use threading.Lock to ensure only one thread modifies counter at a time

# 1. import threading
#2. create a thread ( to create a new thread we create a object of the thread class it takes the target and args as the
#  parameters, target is the function to be exucuted by the thread, where as args is the arguments to be passed to the function)
# 3. start a thread (we use the start method of the thread class)
# 4. once the thread class end the thread execution , once the thread starts the current prgm also keeps on 
# executing inorder to stop the execution of the current prgm until a thread is complete we use the join method 

#############################################################################################################################################################

# import threading
# import time

# l=threading.Lock()
# def first (name,age):
#     for i in range(3):
#         l.acquire()
#         print("hello",name)
#         time.sleep(1)
#         print("age is",age)
#         l.release()

# t1=threading.Thread(target=first,args=("ammu",25))
# t2=threading.Thread(target=first,args=("achu",30))
# t1.start()
# t2.start()
# t1.join()
# t2.join()

#acquire and release to prevent a raise condition when multiple threads access a shared resources

###############################################################################################################################
'''Acquire'''
# a thread acquires the law blocking others from entering the critical session

'''release'''
# the lock is released allowing the next thread to proceed
################################################################################################################################
## 1.Write a Python program that creates two threads to find and print even and odd numbers from 30 to 50.


# import threading

# def print_even():
#     print("Even numbers:")
#     for num in range(30, 51):
#         if num % 2 == 0:
#             print(num, end=' ')
#     print()

# def print_odd():
#     print("Odd numbers:")
#     for num in range(30, 51):
#         if num % 2 != 0:
#             print(num, end=' ')
#     print()

# thread_even = threading.Thread(target=print_even)
# thread_odd = threading.Thread(target=print_odd)

# thread_even.start()
# thread_odd.start()

# thread_even.join()
# thread_odd.join()
