# Parcing and Extracting
data = 'From stephen.maraquard@uct.ac.za Sat Jan 5 09:14;16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find('',atpos)

host = data[atpos+1 : sppos]
print(host)