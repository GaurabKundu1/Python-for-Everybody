# Get method for dictionaries
counts = dict()
names = ['csev' , 'cwen' , 'csev', 'zqian' , 'cwen']
for name in names :
    if name in counts :
        x = counts[name]
    else :
        x = 0
    x = counts.get(name, 0)