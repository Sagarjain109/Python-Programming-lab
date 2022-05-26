st = input("Enter the string: ")
c1=0
c2=0
c3=0
st_lower=st.lower()
vowel = 'aeiou'
for i in st_lower:
    if i in vowel:
        c1+=1
    elif i is ' ':
        c3+=1
    else:
        c2+=1
print(f'Number of Vowel is {c1}')
print(f'Number of Consonants is {c2}')
print(f'Number of Whitespace is {c3}')
