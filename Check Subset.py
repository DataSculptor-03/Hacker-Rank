# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(n):
    m=int(input())
    a=set(map(int,input().split()))
    n=int(input())
    b=set(map(int,input().split()))
    print(a.issubset(b))
