# Using sorted()
d = {'a' : 10, 'b' : 1, 'c' : 22}
t = sorted(d.items())
t
for k,v in sorted(d.items()) :
    print(k,v)