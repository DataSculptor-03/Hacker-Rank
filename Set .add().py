# Enter your code here. Read input from STDIN. Print output to STDOUT
s=set()
n=int(input())
if n>0 and n<1000:
    for i in range(n):
        s.add(input())
        
    print(len(s))
