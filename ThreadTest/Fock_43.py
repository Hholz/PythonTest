'''多进程'''
from multiprocessing import Process
import os


# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    p2 = Process(target=run_proc, args=('test2',))
    print('Child process will start.')
    p.start()
    p2.start()
    p.join()  # 方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print('Child process end.')
