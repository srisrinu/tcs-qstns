def base17Conversion(n):
    sum=0
    k=len(n)-1
    for i in n:
        if(i.upper() in base17d):
            sum+=base17d[i]*17**k
        else:
            sum+=int(i)*17**k
        k-=1
    return(sum)
if __name__=="__main__":
    n=input()
    base17d={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16}   
    print(base17Conversion(n))        