dictionary_if = {1:'a',2:'b',3:'c'}

if dictionary_if.get(3):
    print(dictionary_if.get(3))
elif dictionary_if.get(2):
    print(dictionary_if.get(2))
else:
    print(dictionary_if.get(1))
# key3에 'c'가 존재하므로 condition1이 참이므로 'c' 가 출력됨

del dictionary_if[3] # 키3값을 지움
print(dictionary_if) # {1: 'a', 2: 'b'}

if dictionary_if.get(3):
    print(dictionary_if.get(3))
elif dictionary_if.get(2):
    print(dictionary_if.get(2))
else:
    print(dictionary_if.get(1))
#b

del dictionary_if[2] # 키3값을 지움
print(dictionary_if) # {1: 'a'}

if dictionary_if.get(3):
    print(dictionary_if.get(3))
elif dictionary_if.get(2):
    print(dictionary_if.get(2))
else:
    print(dictionary_if.get(1))
#a