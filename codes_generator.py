import random
ch=''
n=int(input("type the lenth of your code : "))
f=open("liste.txt",'w') ## make the file in the same directory as the script
i=0
while i<1000: 
    for j in range(n):
        c=random.random()
        if c > 0.66 :
    	      ch=ch+chr(random.randint(48,57))
        elif c < 0.33:
            ch=ch+chr(random.randint(65,90))
        else :
            ch=ch+chr(random.randint(97,122))
    ch=ch+'\n'
    f.write(ch)
    i+=1
f.close()
