'''collections'''
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p, p.x, p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))
# namedtuple('名称', [属性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
q = deque(['a', 'b', 'c'])
q.append('a')
q.appendleft(1)
print(q)

# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
dd = defaultdict(lambda: 'N/A')
print(dd['key1'])

# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict：
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])  #OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
print(od)
print(od.keys())

# Counter
# Counter是一个简单的计数器，例如，统计字符出现的个数：

c = Counter
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)