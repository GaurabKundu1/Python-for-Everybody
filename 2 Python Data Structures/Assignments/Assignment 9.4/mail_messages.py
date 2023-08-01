# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
name = input("Enter file:")
tekst = open(name)
dic = {}

for lines in tekst:
    if lines.startswith("From "):
        words = lines.split()
        email = words[1]
        dic[email] = dic.get(email, 0)+1
                   
i = None
j = None

for k, v in dic.items():
    if j is None or j < v:
        j = v
        i = k
print(i, j)