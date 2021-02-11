import string
arr = string.ascii_letters
pl = input("Please enter message ")
key=input("key gap")
iq=""

for item in pl:
    if item.isalpha():
        iq+=arr[(arr.index(item)+int(key))%26]
    else:
        iq+=item
print(iq)