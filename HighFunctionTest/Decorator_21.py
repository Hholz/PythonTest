"""装饰器"""

# 代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
import time


def now():
    print("2018-01-19")


f = now
print(f())
print(now.__name__)
print(f.__name__)


# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
# 但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
def log(func):
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now2():
    print("2018-01-19")


print(now2())
print('================')
now3 = log(now)
now3()


# 可以自定义文本
def log_with_text(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log_with_text('execute')
def now4():
    print('2018-01-19')


now4()

# 我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，
# 再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
# 以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，
# 它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经
# 从原来的'now'变成了'wrapper'：

now5 = log_with_text('execute2')(now)
now5()
print(now5.__name__)


# 打印一个方法执行的时间
def metric(fn):
    def wrapper(*args, **kw):
        start = time.time()
        fv = fn(*args, **kw)
        end = time.time()
        print("%s executed used %s" % (fn.__name__, end - start))
        return fv

    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;


f = fast(11, 22)
s = slow(11, 22, 33)
metric(now)
metric_f = metric(now)
print('metric_f=', metric_f)


if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
