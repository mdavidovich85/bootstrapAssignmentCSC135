# CST 100 Assignment 6 - Rectangle Class 
# by Mike Davidovich
# Last modified 5/2/2016

class Rectangle:         #defines class rectangle

    def __init__(self,initX,initY,initWidth,initHeight):      #initizlizer method, passes four attributes to class
        self.x = initX
        self.y = initY
        self.width = initWidth
        self.height = initHeight

    def __str__(self):              # special string method to return rectangle as string
        return "Rectangle(" + str(self.x) + ", " + str(self.y) + ", " +  str(self.width) + ", " +  str(self.height) + ")" 
    
    def right(self):           # returns value of right edge
        r = self.x + self.width
        return r

    def bottom(self):       # returns value of bottom edge
        b = self.y + self.height
        return b

    def size(self):            # returns width and height of rectanlge
        return "(" + str(self.width) + ", " + str(self.height) + ")"

    def position(self):     # returns (x,y) coordinate of bottom left corner of triangle
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    
    def area(self):   # returns area of triangle
        a = self.width*self.height
        return a

    def expand(self, offset):     # expands triangle by offset factor, positve or negative
        self.xex = self.x - offset
        self.yex = self.y - offset
        self.widthex = self.width + offset*2
        self.heightex = self.height + offset*2
        return "Rectangle(" + str(self.xex) + ", " + str(self.yex) + ", " +  str(self.widthex) + ", " +  str(self.heightex) + ")" 

    def contains_point(self, p1, p2):     # tests to see if a point is contained in the triangle
        if p1 >= self.x and p1 <= self.x + self.width and p2 >= self.y and p2 <= self.y + self.height:
            return True
        else:
            return False

# end of program
