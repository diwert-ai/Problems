a = ['1.cad', '1.bat', '1.aa', '.bat']



a.sort(key = lambda x: x[x.rfind('.'):] + x[:x.rfind('.')])

print(a)