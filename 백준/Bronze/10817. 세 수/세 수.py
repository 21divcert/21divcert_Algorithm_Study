# 세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 
A,B,C = map(int,input().split())

a = [A,B,C]


a.sort()
result = a[1]
print(result)