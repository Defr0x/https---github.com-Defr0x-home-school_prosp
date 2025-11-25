pr=[".",",",";",":","?","!"]
d={}
fi=open("input.txt","r")
fo=open("output.txt","w")

for i in fi:
    a=i.strip()
    for n in a:
        if n in pr:
            a=a.replace(n," ")
    a=a.lower()
    for j in a.split():
        d[j] = d.get(j, 0) + 1

for i in sorted(sorted(d), key=lambda x: d[x],reverse=True):
    print(i, d[i], file=fo)
fo.close()