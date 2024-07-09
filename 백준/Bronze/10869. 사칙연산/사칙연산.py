# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

A,B = input().split()

A= int(A)
B= int(B)

addition = A + B
subtraction = A - B
multiplication = A * B
division = int(A / B)  # 몫
modulus = A % B  # 나머지


print(addition)
print(subtraction)
print(multiplication)
print(division)
print(modulus)