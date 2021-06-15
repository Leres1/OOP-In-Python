class Point:
    'class comment(__doc__)'
    x = 1
    y = 1
# class announcement


pt = Point()
pt.x = 4
pt.y = 10 # initialization of new variables in the object
print( pt.x, pt.y )


print('----------[ __dict__ ]----------')

print( pt.__dict__ )
print( Point.__dict__ ) # displays the attributes of the object

print('----------[ getattr ]----------')

print( getattr(pt, "x") )
print( getattr(pt, "z", False) ) # checks for an attribute( if do not add False it will give an ERROR )

print('----------[ hasattr ]----------')

print( hasattr(pt, "z") ) # checks for an attribute

print('----------[ setattr ]----------')

print( setattr( pt, 'z', 7) ) # initializes a new variable
print( getattr(pt, "z") )

print('----------[ delattr ]----------')

print( delattr( pt, 'z') ) # removes the variable
print( pt.__dict__ )

print('----------[ isinstance ]----------')

print( isinstance( pt, Point ) ) # checks the presence of an object to classroom


print('----------[ __doc__ ]----------')
print(Point.__doc__) # displays a comment left in class