#!/usr/bin/python3

print('hello world!!!')

cnt = 6
for x in range(cnt):
    print(f"打{cnt}次第{x}次")
else:
    print("finish!")

new_list = [1, 2, 3, 4, 5, 6]
print(new_list)
new_list = list()
print("新的空list:", new_list)

tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = ('one', 'two', 'three', 'four', 'five')
print(tuple1 + tuple2)

a, b = 0, 1
while b < 1000:
    print(b, end=" ")
    a, b = b, a + b
else:
    print('finish!')

# 推导式
# [out_exp_res for out_exp in input_list if condition]
# out_exp_res 可以是表达式 也可以是一个函数（列表元素当入参）
names = ['wangyafei', 'lidandan', 'yangyang', 'huanghongyi']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

# { key_expr : value_expr for value in collection if condition }
listDemo = ['google', 'taobao', 'baidu', 'huawei']
new_dict = {key: len(key) for key in listDemo}
print(new_dict)

new_dict1 = {x: x ** 2 for x in [2, 4, 6]}
print(new_dict1)

# { expression for item in Sequence if conditional }
new_set = {x ** 2 for x in [1, 2, 3]}
print(new_set)

new_set2 = {x ** 2 for x in new_set}
print(new_set2)

new_set1 = {x for x in 'abracadabra' if x not in 'abc'}
print(new_set1)

new_set3 = {x for x in range(3) if x % 2 == 0}
print(new_set3)

# (expression for item in Sequence if conditional )
# 元组推导式返回的结果是一个生成器对象
generator = (x for x in range(10))
print(type(generator))
new_tuple = tuple(generator)
print(new_tuple)
