def showinfo(c,d):
    dct={'Name': 0,'Course': 0}
    dct['Name']= c
    dct['Course']= d
    out = dct
    return out    

    





#main code
a= input("Enter name: ")
b= input('Enter course: ',Default= 'BTECH')
print(showinfo(a,b))