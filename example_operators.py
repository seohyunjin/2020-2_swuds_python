# example operators
a = 10+100  #110;  add
b = 21-23  #-2; subtract
c = 4*5  #20;  multiply
# 4* 5.0 = 20.0

d = 10/3  #3.3333333333333335 ; divide
# 10/2 = 5.0 ; 나누기 연산은 항상 값이 float으로 나옴
e = 10/3.  #3.3333333333333335
f = 10/float(3)  #3.3333333333333335
g = 10//3 # 3; 몫
h = 10 % 3  # 1;  mod operation ; 나머지

print(a, b, c, d, e, f, g, h)

a = True
b = False

print(a == b) # False
print(a or b) #True; 둘중 하나가 true이므로 true

l = [1, 2, [1, 5, 3, 2], {1: 'Hello, World', 2: 'Hi'}] # True

print(l[0] in l[2])
