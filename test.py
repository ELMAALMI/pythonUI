#2  j < 2

# 1 )  i = 0 , j = 0
#      i = 0 , j = 1
    # t [0][0] = 5
    # t [0][1] = 6

    
# 2 )  i = 1 , j = 0
#      i = 1 , j = 1
    # t [1][0] = 9
    # t [1][1] = 10
    
# [ [5,6],[9,10] ] 

# a = 2
# i = 0 j = 0
#matrice = [] # [ [1,2,3], [4,5,6] ]
#for i in range(a):
#    t=[] # 1 2 3 4 5 6
#    for j in range(a):
#        t.append(int(input("enter matrice [" +str(i)+ "][" +str(j)+ "] : "))    # ===> [ int(input("enter t["+str(i)+"]["+str(j)+"] : ")) for i in range (a) ]
#    matrice.append(t)
# "meryam " + "blala" + "hhhh" => "meryam blala hhhh"  => enter t[0][1] : 4

a = int(input("taille de la matrice & vector  = "))
mat = [ [ int(input("enter matrice ["+str(i)+"]["+str(j)+"] : ")) for i in range (a) ] for j in range(a) ]

vec = [ int(input("enter vector ["+str(i)+"]: ")) for i in range (a) ] 

print("matrice ----------------- ")
print(mat)

# 1 2 3
# 0 3 6
# 0 0 2

print("vector  ----------------- ")
print(vec)

solution = []
 
def remontree (i):
    if(i == a):
        return vec[a-1] / mat[a-1][a-1]
    return (vec[a-i] - ( mat[a-i][a-1] * remontree(a) )) / mat[a-i][a-i]

for i in reversed ( range(a) ):  
    somme = 0
    for j  in range(i+1,a):
        somme = somme + mat[i][j] * remontree(j)
        print(somme)
    
        
        
