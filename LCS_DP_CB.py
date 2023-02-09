import time
#-------------------------------------------------------------------------------------------------------
#function for determining the length of LCS

def LCS_DP_CB(x, y):
    m = len(x) #row
    n = len(y) #col
    B = [[ ' ' for i in range(0, n+1)] for j in range(0, m+1)] #table B
    C = [[ [None] for i in range(0, n+1)] for j in range(0, m+1)] #table C
    for i in range(1,m+1):
        C[i][0] = 0
    for j in range(0, n+1):
        C[0][j] = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if  x[i-1] == y[j-1]:
                C[i][j] = C[i-1][j-1] + 1
                B[i][j] = "\\"
            elif C[i-1][j] >= C[i][j-1]:
                C[i][j] = C[i-1][j]
                B[i][j] = "^"
            else:
                C[i][j] = C[i][j-1]
                B[i][j] = "<"   
    return C,B
#-------------------------------------------------------------------------------------------------------
#  Function to store the LCS in an array

def printlcs(X, Y, m, n):
    L = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    lcs = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs += X[i-1]
            i -= 1
            j -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    lcs = lcs[::-1]
    return lcs

#-------------------------------------------------------------------------------------------------------
#  continuation of the program to display the output.
if __name__=="__main__":
    #reading file and saving in l
    with open("LCS1.txt") as file:
        l = file.readlines()

    for i in l:
        if "\n" in i:
            i = i[:-1]

        myList = i.split(',')
        X=(myList[0])
        Y=(myList[1])
        g = len(Y)+3
        print('\n')
        print('X =','\"'+X+'\"' , 'Y =', '\"'+Y+'\"')
        x=''
        y=''
        start = time.time()#Time calculation start at the call of first function
        a,k=LCS_DP_CB(X,Y)

        for i in Y:
            x=x+i+'   '
        
        print('----'*g)
        print('    |',end='')

        print('      ',1,end="")
        for i in range(2,len(Y)+1):
            print('  ',i,end="")
        print('\n    |   Y  ',x)
        print('----'*g)
        X1='X'+X
        
        for i in range(1,len(X1)+1):
            os=''
            os=''+X1[i-1]+' |'
            for j in range(0,len(Y)+1):
                os=os+'  '+str(k[i-1][j])
                os=os+''+str(a[i-1][j])
            if i-1==0:
                print(' ',os)
            else:                
                print(i-1,os)
            
        flcs=printlcs(X, Y,len(X),len(Y)) 
        end = time.time() #Time calculation stop at the completion of last function
        #printing final output
        print('----'*g)
        print("Length of the Longest Common Subsequence is: "+str(a[len(X)][len(Y)]))
        print("The Longest Common Subsequence of  "+'\"'+X+'\"'+" and "+'\"'+Y+'\"'+" is "'\"'+flcs+'\"')
        print('----'*g)