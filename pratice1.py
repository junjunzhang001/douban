
def filterchar(string):
    import re
    pattern = r'heike'
    sub=re.sub(pattern,"baike",string)


pattern = r'(h)|(e)'
string = "Hello, World1!"
match = re.match(r"Hello1", string)

if match:
    print("Matched")
else:
    print("Not Matched")