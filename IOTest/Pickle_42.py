'''序列化'''
import pickle

d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))  # 方法把任意对象序列化成一个bytes
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'wb')
dict_d = pickle.load(f)
print(dict_d)
f.close()