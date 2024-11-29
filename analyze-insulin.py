"""
Your module description
"""
with open("preproinsulin-seq.txt") as origin:
    origin = origin.read()
    print(origin)

char = ["ORIGIN"," ","1","2","3","4","5","6","7","8","9","0","/","\n"]
for x in char:
    origin = origin.replace(x,"")
print(origin)
print(len(origin))

file = open("preproinsulin-seq-clean.txt", "w")
file.write(origin)

lsinsulin = origin[:24]
binsulin = origin[24:54]
cinsulin = origin[54:89]
ainsulin = origin[89:]
print(lsinsulin, binsulin, cinsulin, ainsulin)
print(len(lsinsulin))
print(len(binsulin))
print(len(cinsulin))
print(len(ainsulin))

ls = open("lsinsulin-seq-clean.txt", "w")
ls.write(lsinsulin)

b = open("binsulin-seq-clean.txt", "w")
b.write(binsulin)

c = open("cinsulin-seq-clean.txt", "w")
c.write(cinsulin)

a = open("ainsulin-seq-clean.txt", "w")
a.write(ainsulin)