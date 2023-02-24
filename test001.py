from numpy import array
def saisir():
    n=int(input("donner n :"))
    while not(2<=n<=15):
        n=int(input("donner n :"))
    return n
def remplir(M,nl,nc):
    for i in range(nl):
        for j in range(nc):
            M[i,j]=str(input("donner M["+str(i)+","+str(j)+"] :"))
            while not(0<len(M[i,j])):
                M[i,j]=str(input("donner M["+str(i)+","+str(j)+"] :"))
def affiche(M,nl,nc):
    print("matrice M :")
    for i in range(nl):
        print("")
        for j in range(nc):
            print("M[",i,",",j,"] est : ",M[i,j])
def remplir1(T1,M,nl,nc):
    for i in range(nl):
        T1[i]=voyelleligne(M,nc,i)
def voyelleligne(M,nc,i):
    T1[i]=""
    for j in range(nc):
        for z in range(len(M[i,j])):
            if ((M[i,j][z]).upper() in ["A","E","U","I","O","Y"]):
                T1[i]=T1[i]+M[i,j][z]
    return (T1[i])
def affiche2(T1,nl):
    print("le tableau T1 :")
    for i in range(nl):
            print("T1[",i,"] est : ",T1[i])
def remplir2(T2,M,nl,nc):
    for i in range(nl):
        T2[i]=0
        T2[i]=sommmechiffre(M,nc,i)
def sommmechiffre(M,nc,i):
    T2[i]=0
    for j in range(nc):
        for z in range(len(M[i,j])):
            if ((M[i,j][z]).isnumeric()):
                if (int(M[i,j][z]) in range (1,9)):
                    T2[i]=T2[i]+int(M[i,j][z])
    return T2[i]

def affiche3(T2,nl):
    print("le tableau T2 :")
    for i in range(nl):
            print("T2[",i,"] est : ",T2[i])
M=array([[str]*50]*50)
T1=array([str]*50)
T2=array([str]*50)
nl=saisir()
nc=saisir()
remplir(M,nl,nc)
affiche(M,nl,nc)
remplir1(T1,M,nl,nc)
remplir2(T2,M,nl,nc)
affiche2(T1,nl)
affiche3(T2,nl)
