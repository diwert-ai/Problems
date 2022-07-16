n = 5
a = [[i+n*j+1 for i in range(n)] for j in range(n)]
s = "{:2d} "*n
for r in a:
    print(s.format(*r))
print('')

d0 = [[row[i+j] for i,row in enumerate(a) if i+j < len(row)] for j in range(len(a)-3)]
d1 = [[row[i-j] for i,row in enumerate(a) if i-j > -1] for j in range(1,len(a)-3)]

d2 = [[row[-i+j-1] for i,row in enumerate(a) if -i+j-1 < 0] for j in range(len(a)-3)]
d3 = [[row[-i-j-1] for i,row in enumerate(a) if -i-j-1 > -len(row)-1] for j in range(1,len(a)-3)]

print(*(d0+d1+d2+d3),sep='\n')



