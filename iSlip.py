import random

#Εκτύπωση των requests
def printReq(r):
    print("Requests:")
    for i in range(4):
        for j in range(4):
            if r[i][j]!=[]:
                for k in range(len(r[i][j])): #Αν 1 είσοδος έχει πολλαπλά αιτήματα σε ουρά για την ίδια έξοδο
                    print("From Input {} towards Output {}".format(i,j))

#Grant Phase
def doGrant(r,g,grant):            
    print('\nGrant Phase')
    for i in range(4):
        for j in range(4):
            if r[(g[i]+j)%4][i]!=[]:
                print('Grant from output {} to input {}'.format(i,(g[i]+j)%4))
                grant[i]=((g[i]+j)%4)
                break
    return grant


#Accept Phase
def doAccept(acc,g,out,grant,r):
    print('\nAccept Phase')
    for i in range(4):
        for j in range(4):
            if grant[(acc[i]+j)%4]==i:
                try:
                    r[i][(acc[i]+j)%4].pop(0)
                    print('Input {} accepts the grant from output {}'.format(i,(acc[i]+j)%4))
                    out[(acc[i]+j)%4]=i
                    g[(acc[i]+j)%4]=i+1
                    acc[i]=(acc[i]+j+1)%4
                    break
                except: pass
    return[acc, g, out, r]

#ΆΦιξη νέων πακέτων
def addReq(r):
    for i in range(4):
        inp=random.randint(0,1)
        if inp==1:
            j=random.randint(0,3)
            r[i][j].append(1)
    return r

#Ορισμός κενού πίνακα των requests
def empReq():
    r=[[],[],[],[]]
    r[0]=[[],[],[],[]]
    r[1]=[[],[],[],[]]
    r[2]=[[],[],[],[]]
    r[3]=[[],[],[],[]]
    return r

#Iteration του αλγορίθμου
def doIteration(r,g,grant,acc,out,it):

    print("Iteration {}\n".format(it))
    it+=1
    printReq(r)
    grant=doGrant(r,g,grant)
    [acc,g,out,r]=doAccept(acc,g,out,grant,r)
    out2=[]
    in2=[]
    for i in range(4):
        if i not in out:
            in2.append(i)
        if out[i]==None:
            out2.append(i)
    remaining=empReq()
    remsum=0;
    for i in in2:
        for j in out2:
            if r[i][j]!=[]:
                remaining[i][j]=r[i][j].copy()
                remsum=1
    if remsum==1:
        print()
        doIteration(remaining,g,grant,acc,out,it)
    return [r,g,grant,acc,out]

#Αρχική κατάσταση
r=empReq()
acc=[0,2,1,3]
r[1][1].append(1)
r[1][3].append(1)
r[2][0].append(1)
r[2][2].append(1)
g=[0,1,2,0]

#Εκτέλεση    
cycle=0
while cycle<10:
    print('Cycle {}'.format(cycle))
    print('-------')
    it=0
    grant=[None,None,None,None]
    out=[None,None,None,None]
    
    [r,g,grant,acc,out]=doIteration(r,g,grant,acc,out,it)
    print('\nOutputs: {}'.format(out))
    print('----------------------------')
    input("\nPress enter to continue\n")
    print('\n\n')
    if cycle==0:
        r[1][0].append(1)
        r[3][1].append(1)
    else:
        r=addReq(r)
    cycle+=1
print('End')
