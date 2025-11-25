d={}
fi=open("input.txt","r")
fo=open("output.txt","w")
for i in fi:
    i=i.strip()
    if len(i.split())==2:
        a=i.split()
        d[a[0]]=a[1]
    elif len(i.split())==1 and i.isalpha():
        if i in d.keys():
            print(d[i],file=fo)
        else:
            for j in list(d.keys()):
                if d[j]==i:
                    print(j,file=fo)
                    break
fo.close()

a=0