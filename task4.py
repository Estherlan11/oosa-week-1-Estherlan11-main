def color():
    x=y=8   #set up 8*8 range of square 
    for i in range(1,x+1):    #set a loop of x
        for j in range(1,y+1):     #set a loop of y
            if i%2 == 1:    #set a condition, if x is an odd number
                if j%2 == 1:      # x is an odd number, and y is also an odd number
                    print(i,j,'black')     #x and y are both odd, the color of square is black
                else:
                    print(i,j,'white')    #if x is an odd number, and y is not an odd number, the color of square is white
            else:
                i%2 == 0       #if x is an even number
                if j%2 == 1:     # y is an odd number
                    print(i,j,'black')    # if x is an even number, y is an odd number, print the color is black
                else:
                    print(i,j,'white')    #x and y are both even number, print the color is white


if __name__== '__main__':
    color()