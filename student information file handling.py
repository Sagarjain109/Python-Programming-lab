f= open('info.txt','w')
name = input('Enter name: ')
section = input('Enter section: ')
roll= int(input('Enter roll number: ')
college = input('Enter college name : ')
st = f'''
    Name : {name}
    Section : {section}
    Roll number : {roll}
    College : {college}'''
f.write(st)
f.close()
