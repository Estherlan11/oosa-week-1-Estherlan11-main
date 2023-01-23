from math import sqrt   #import a calculation function from	the	maths package
def distanced():
    x=y=8     #set up the range of square 8*8
    for i in range(1,x+1):     #set a loop of x1
       for j in range (1,y+1):    #set a nested loop of y1
            for m in range(1,x+1):    #set a nested loop of x2
                for n in range(1,y+1):     #set a nested loop of y2
                    if((i == m)&(j == n)):   #set a condition, if x1=x2, y1=y2, skip the calculation
                        continue
                    distance=sqrt((m-i)**2+(n-j)**2)   #calculate the distance
                    print(i,j ,'to', m,n, 'distance',distance)   #set the contents of print       

if __name__== '__main__':
    distanced()