l = [1, 2, [1, 5, 3, 2], {1: 'Hello, World', 2: 'Hi'}] # python은 리스트의 원소가 data type 이 다달라도 상관x
print(type(l)) # <class 'list'>
print(type(l[0]),type(l[1]),type(l[2]),type(l[3])) # <class 'int'> <class 'int'> <class 'list'>  <class 'dict'>

print(l[len(l)-1]) # 마지막 idex 에 있는 값을 가져옴  # == print(l[-1])
print(l[-1])  # {1: 'Hello, World', 2: 'Hi'} ; 마지막 idex 에 있는 값을 가져옴

# list
print(len(l)) # 4  ;#  1 and 2 and [1,5,3,2] and {1: 'Hello, World', 2: 'Hi'}
print(l[0], l[-3]) # 1,2  ;#  0: 1 and 1: 2 and 2: [1,5,3,2] and 3: {1: 'Hello, World', 2: 'Hi'} ; -3은 거꾸로

print(l.index(2)) # 1  ; 2값의 index를 출력하세요->1번방
print(l.index(1)) #0
print(l.index([1,5,3,2])) #2


print('hihihihi')

del l[l.index(2)]  # delete 2 from list l ;
print(l)  # [1, [1, 5, 3, 2], {1: 'Hello, World', 2: 'Hi'}]

l[1].append(4)  # add 4 to list [1, 5, 3, 2]
print(l) # [1, [1, 5, 3, 2, 4], {1: 'Hello, World', 2: 'Hi'}]

l[1].sort()  #  ;  sort list [1, 5, 3, 2, 4]
print(l) # [1, [1, 2, 3, 4, 5], {1: 'Hello, World', 2: 'Hi'}]


print('hi')

# dictionary
print(l[2].items())  # dict_items([(1, 'Hello, World'), (2, 'Hi')])
print(l[2].keys())  # dict_keys([1, 2])
print(l[2].values())  # dict_values(['Hello, World', 'Hi']


print(l[2]) # {1: 'Hello, World', 2: 'Hi'} #; 리스트에서 인덱스로 접근하는 대괄호[]
print(l[2][2]) # Hi ; {1: 'Hello, World', 2: 'Hi'}의 key값이 2인것 출력
del l[2][2]  #; 리스트에서 key값으로 보는 대괄호[]  ; 'Hi' remove
print(l) #[1, [1, 2, 3, 4, 5], {1: 'Hello, World'}]

print(2 in l[2])  #False # has_key method deprecated in version 3 #; l에 key가 2인값 있어? false


# string


print(l[2].get(1))  #Hello, World
print(len(l[2].get(1))) #12 ; Hello, World의 길이 =12

print(l[2].get(1)[1:4]) # ell
print(l[2].get(1).count('l')) #3
