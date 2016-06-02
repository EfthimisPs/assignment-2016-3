import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', help='name',default='musical_rythms.json')
parser.add_argument('-n', '--SLOTS', type=int)
parser.add_argument('-k', '--PULSES', type=int )
parser.add_argument('-r', '--RECOGNIZE', type=int)
parser.add_argument('-l', '--LIST_RYTHMS', type=int)

args = parser.parse_args()


filename=args.filename

f=open(filename)
#diavazw thn eisodo kai kanw thn arxikh lista
def metatrduad(k,n):
    seira=[]
    for x in range(0, n):
        if x<k:
            seira.append('1')
        else:
            seira.append('0')
    flag=True
    seira1=[]
    seira2=[]
    seirama=[]
    while (flag==True):
        l=0
        j=0
        z=0
        for i in seira:
            if i==seira[-1]:
                z=z+1
            if len(i)==len(seira[-1]):
                l=l+1
        if (l>1 and z<len(seira)) :

            seira1=seira[:len(seira)-z]
            seira2=seira[len(seira)-z:]
            ma=max(len(seira1),len(seira2))
            if len(seira1)>len(seira2):
                seirama=seira1
            else:
                seirama=seira2
            mi=min(len(seira1),len(seira2))
            del seira[:]
            for x in range(0, ma):
                if x<mi:
                    seira.insert(x,seira1[x]+''+ seira2[x])
                else:
                    seira.insert(x,seirama[x])
        else:
            flag=False
    telseira=''
    for  i in seira:
        telseira=telseira+i
    return (telseira)
#elegxw an uparxei
def anazhthsh(k,n):
    key='"E(' +str(k)+ ',' +str(n)+ ')"'
    flag=True
    for line in f:
        if key in line:
            keim = (line[14:-4])
            flag=False
    f.seek(0)
    if flag==True:
        return ('')
    else:
        return (keim)
def metatrarith(telseira):
    #ftiaxnw ton 2o tropo me athrisma
    i=0
    newtelseira=''
    mhden=1
    teltel=str(telseira)
    while i < len(teltel):
        flag=True
        while flag==True:
            i+=1
            if i < len(teltel):
                if teltel[i]=='0':
                    mhden+=1
                else:
                    newtelseira=newtelseira+str(mhden)
                    mhden=1
                    flag=False
            else:
                flag=False
    newtelseira=newtelseira+str(mhden)
    return (newtelseira)
#ftiaxnw to rythmo
def euclid(newtelseira):
    #elegxw an einai Euclidean string
    pr='1'
    for i in range(1,k):
        pr=pr+'0'
    eunewtelseira=(int(newtelseira)-1)+int(pr)
    flag=True
    if int(eunewtelseira) == int(newtelseira[::-1]) and len(newtelseira)>1:
        return('\nIt is a Euclidean string.')
        flag=False
    #elegxw an einai reverse Euclidean string
    reunewtelseira=(int(newtelseira[::-1])-1)+int(pr)
    if int(newtelseira) == int(reunewtelseira) and len(newtelseira)>1:
        return('\nIt is a reverse Euclidean string.')
        flag=False
    if flag==True:
        return ('')
#to 1o toy r
def metatre(telseira):
    n=len(str(telseira))
    k=0
    i=0
    teltel=str(telseira)
    while i < n:
        k=k+int(teltel[i])
        i+=1
    return (n,k)

def hamstring(s1,s2): 
    sum=0
    s1=str(s1)
    s2=str(s2)
    for i in range (0,len(s1)):
        if s1[i]!=s2[i]:
            sum=sum+1
    return (sum)

if args.SLOTS and args.PULSES:
    n=args.SLOTS
    k=args.PULSES
    telseira=metatrduad(k,n)
    keimeno=anazhthsh(k,n)
    newtelseira=metatrarith(telseira)
    euc=euclid(newtelseira)
    print ('E(' +str(k)+ ',' +str(n)+ ') = ['+telseira+'] = ('+newtelseira+') '+keimeno+euc)
if args.RECOGNIZE:
    telseira=args.RECOGNIZE
    n,k=metatre(telseira)
    telseira2=metatrduad(k,n)
    if int(telseira2)==telseira:
        keimeno=anazhthsh(k,n)
        newtelseira=metatrarith(telseira)
        euc=euclid(newtelseira)
        print ('E(' +str(k)+ ',' +str(n)+ ') = ['+str(telseira)+'] = ('+newtelseira+') '+keimeno+euc)
    else:
        print ('Not a Euclidean rythm.')
if args.LIST_RYTHMS:
    telseira=args.LIST_RYTHMS
    n,k=metatre(telseira)
    ham={}
    for i in range (1,n):
        if i!=k:
            itelseira=metatrduad(i,n)
            dist=hamstring(telseira,itelseira)
            ham.setdefault(dist,[])
            ham[dist].append(i)
    print ('Distance = 0')
    keimeno=anazhthsh(k,n)
    newtelseira=metatrarith(telseira)
    euc=euclid(newtelseira)
    print ('E(' +str(k)+ ',' +str(n)+ ') = ['+str(telseira)+'] = ('+newtelseira+') '+keimeno+euc)

    for keys in ham:
        for k in ham[keys]:
            print ('Distance = '+str(keys))
            telseira=metatrduad(k,n)
            keimeno=anazhthsh(k,n)
            newtelseira=metatrarith(telseira)
            euc=euclid(newtelseira)
            print ('E(' +str(k)+ ',' +str(n)+ ') = ['+str(telseira)+'] = ('+newtelseira+') '+keimeno+euc)
