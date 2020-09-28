student_dict = {1:'a',2:'b',3:'c',4:'d'}

print(student_dict.keys()) # dict_keys([1, 2, 3, 4])
print(student_dict.values()) # dict_values(['a', 'b', 'c', 'd'])
print(student_dict.items()) # dict_items([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')])
print('the name of student with id 2 is', student_dict.get(2))  # the name of student with id 2 is b
#; key에 해당하는 value를 가져옴 ; key가 없는 경우에는 None 출력됨