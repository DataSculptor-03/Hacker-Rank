# Enter your code here. Read input from STDIN. Print output to STDOUT
a=set(map(int,input().split()))
m=int(input())
b=set(map(int,input().split()))
c=set(map(int,input().split()))
if((a.issuperset(b)and a!=b)and(a.issuperset(c)and a!=c)):
    print("True")
else:
    print("False")
