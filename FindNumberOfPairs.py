def sockMerchant(n,ar):

""" arrange by color
and find if its odd, minus one and devide by 2
if even devide by 2 
You call it pair when you have two things which looks same 
iterate through the array, 

"""


 pairs={}
  for i in ar:
   if i not in pairs.items(): 
    pairs[i]=1
   else:
    pairs[i]+=1
  for key,value in pairs.items():
   last=0
   if value%2 == 0:
    last=last+value/2;
   else:
    value-=1;
    last=last+value/2;
  print(last)
