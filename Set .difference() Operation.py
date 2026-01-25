n=int(input())
a=set(map(int,input().split()))
m=int(input())
b=set(map(int,input().split()))
x=a-b
print(len(x))
