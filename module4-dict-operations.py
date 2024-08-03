grades = {}
grades ['John'] = 'A-'
grades ['Anne'] = 'B'

grades ['Anne'] = 'A'

grades.update ({'John':'A'})

len (grades)

if 'John' in grades:
    print ('John got:', grades ['John'])

    
del grades ['John']
print (grades)

for el in grades:
    print (el)

for el in grades.keys ():
    print (el)

for el in grades.values ():
    print (el)

for person, grade in grades.items ():
    print (person, 'got', grade)