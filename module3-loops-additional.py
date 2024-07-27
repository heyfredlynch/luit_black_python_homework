for i in range (11):
    pass

for a in range (1,6):
    for b in range (1, 6):
        print (a, 'x', b, '=', a * b)

  # this next is rarely used, but you'll need to know it      
        i = 5
while i < 5:
    print (i)
    i += 1
else: 
    print ('else:', i)

# Remember: the else branch of a loop is always executed exactly once (execption: break statement) 
    i = 2
while i < 5:
    print (i)
    i += 1
else: 
    print ('else:', i)