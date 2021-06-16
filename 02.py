print('----------[ Point2D ]----------')


class Point:
    def __init__( self, x = 0, y = 0 ):
        self.x = x
        self.y = y
        print( 'A new instance has been created' )

    def __del__( self ):
        print('Delete instance' + str(self.__str__()))

    def setCoords( self, x, y ): # self is an instance of the class( in this case "pt`s" )
        self.x = x
        self.y = y


pt1 = Point()
pt2 = Point(11)
pt3 = Point(21)
pt1.setCoords(5, 10)

print( pt1.__dict__, pt2.__dict__, pt3.__dict__ )


print('----------[ Point3D ]----------')


class Point3D:
    def __init__( self, point = 0 ):  # point - object of class Point3D
        if point:
            self.x = point.x
            self.y = point.y
            self.z = point.z
        else:
            self.x = 0
            self.y = 0
            self.z = 0
    
    def setPoint3D( self, x, y, z ):
        self.x = x
        self.y = y
        self.z = z

    def getPoint3D( self ):
        return ( self.x, self.y, self.z, )


pt3D = Point3D()
print(pt3D.__dict__)

pt3D.setPoint3D( 10, 20, 30 )
print(pt3D.__dict__)

pt3D_2 = Point3D( pt3D )
print(pt3D.__dict__)

pt3D_2.setPoint3D( pt3D_2.x, 30, pt3D_2.z )
print(pt3D_2.getPoint3D())


print('----------[ __del__ ]----------')