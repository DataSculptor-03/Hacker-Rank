# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
x1=set(map(int,input().split()))
m=int(input())
x2=set(map(int,input().split()))
a=x1.union(x2)
print(len(a))
