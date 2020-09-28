#example data types
a=type('A') # string
b=type(3)  #int
c=type(3.)  #float
d=type(float(3)) # float
f=type('True') # string  ; ''means string
g=type(True) # T만 대문자인 경우가 Boolean type TRUE(X)
h=type([1,2,3,4]) # list
j=type({1:'a',2:'b',3:'c',4:'d'}) # dictionary

print(a,b,c,d,f,g,h,j)

list_a =[1,2,3,4]
list_b = list_a +list_a   #[1,2,3,4,1,2,3,4] ; 그대로 이어 붙여 나옴
print (list_b)

print(list_a *2)  # [1,2,3,4,1,2,3,4] ; n번 반복됨

## Operations for Sequence
student_id =[1,3,2,4]
print(len(student_id)) # 4 ; 1,2,3,4 으로 총 4임
print(student_id[0:2])  # [1,3] ; a:b이면 a에서부터 b-1까지 가져옴

print('before sorting', student_id) # [1,3,2,4] # data type 달라서 ,사용
student_id.sort()
print('after sorting',student_id) # [1,2,3,4]


a = 1
a += 1 # == a=a+1
print(a)


# Operations for changeable squences

student_id.append(5)
print(student_id) # [1,2,3,4,5] ; 5가 새로 들어감

student_id.insert(0,6)
print(student_id)  # [6, 1, 2, 3, 4, 5]

student_id.reverse()
print(student_id )# [5, 4, 3, 2, 1, 6]



