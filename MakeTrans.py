import os
import string
alphabets=string.ascii_lowercase
value="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
new_value=""
y=0;
for i in alphabets:
    if i in alphabets:
        print ('hi')
        y=alphabets.index(i)+2
        print (y)
        if (y > 25):
            y=y-26
        i=alphabets[y]
    new_value+=i
print (new_value)   
table=value.maketrans(alphabets,new_value)
print ((table))
print (value.translate(table))
