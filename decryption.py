import string
arr = string.ascii_letters
pli = input("Message ")
key = input("gap")
iqe = ""
for item in pli:
    if item.isalpha():
        iqe+=arr[(arr.index(item)-int(key))%26]
    else:
        iqe+=item
print(iqe)