# -*- coding: utf-8 -*-

midict = {
    'Name': 'Zara',
    'Age': 7,
    'Class': 'First'
}

print("dict['Name']: ", midict['Name'])
print("dict['Age']: ", midict['Age'])


midict['Age'] = 8  # update existing entry
midict['School'] = "DPS School"  # Add new entry
midict['Last Name'] = "Petterson"

print(midict)

print(midict['Last Name'])

for clave in midict:
    print(midict[clave])


midict['miarray'] = [1, 2]

del midict['Name']  # remove entry with key 'Name'
print(midict)
midict.clear()     # remove all entries in dict
print(midict)
del midict       # delete entire dictionary


midict = {'Name': 'Zara', 'Age': 7}
print (len(midict))

midict['Apellidos'] = {
    'primero': "Luces",
    'segundo': "Apagadas"
}

print(midict)
