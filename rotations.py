#! /usr/bin/env python
"""Module for general rotations library."""

from math import *
import math_extensions as math2
#import physical_constants as const
import quaternion as quat
import random

EARTH_OBLIQUITY = 23.43929 * math2.D2R  #Obliquity of Earth's orbit, in radians to support transforms to ecliptic coordinates.

class GalacticPole (object):
    """Represents coordinates of galactic pole."""
    
    def __init__ (self, latitude, longitude, ascending_node):
        """Initializes the coordinates of the galactic pole.
        
        latitude = latitude of pole, in degrees
        longitude = longitude of pole, in degrees
        ascending_node = ascending node of pole, in degrees."""
        
        #Arguments specified in degrees, but values represented in radians.
        self.latitude = radians(latitude)
        self.longitude = radians(longitude)
        self.anode = radians(ascending_node)
        
    def __str__ (self):
        """Returns string representation of the galactic pole."""
        
        #Convert attributes back into degrees for readability.
        return('GalacticPole: latitude: %.3fD, longitude: %.3fD, anode: %.3fD'\
        %(degrees(self.latitude), degrees(self.longitude), degrees(self.anode)))
        
NGP = GalacticPole(192.859508, 27.128336, 32.932)   #supports transformation to galactic coordinates

class NumericList (list):
    """List class that supports multiplication.  Only valid for numbers."""
    
    def __mul__ (L1, L2):
        """Take the dot product of two numeric lists.
        Not using Vector for this because it is limited to three dimensions.
        Lists must have the same number of elements."""
        
        return(sum(map(lambda x,y: x*y, L1, L2)))


class Matrix (list):    
    """Class to encapsulate matrix data and methods.
   
    A matrix is simply a list of lists that correspond to rows of the matrix.
    This is just intended to handle simple multiplication and vector rotations.
    For anything more advanced or computationally intensive, Python library routines
    should be used."""
   
    def __init__(self, rows):
        """Constructor for a matrix.
      
        This accepts a list of rows.
        It is assumed the rows are all of the same length."""
        
        for row in rows:
            self.append(NumericList(row))  #copy list       
        
    def __str__(self):
        """Returns a string representation of the matrix."""
        
        return_str = 'Matrix:'
            
        for row_index in range(len(self)):
            row_str = 'Row %d: ' %(row_index + 1)
            row = self[row_index]
            
            for col_index in range(len(row)):
                #row_str = row_str + '%6.3f  ' % (row[col_index])
                row_str = row_str + '%12.8f  ' % (row[col_index])
            
            return_str = return_str + '\n' + row_str
            
        return(return_str)

    def element(self, row_index, col_index):
        """Returns an element of the matrix indexed by row and column.

        Indices begin with 0."""
        
        return ((self[row_index])[col_index])
     
    def row(self, row_index):
        """Returns a specified row of the matrix."""
         
        return(self[row_index])
        
    def column(self, col_index):
        """Returns a specified column of the matrix as a numeric list."""
        
        return(NumericList([row[col_index] for row in self]))
        
    def num_rows(self):
        """Returns the number of rows in the matrix."""
        
        return(len(self))
        
    def num_cols(self):
        """Returns the number of columns in the matrix."""
        
        return (len(self[0]))  #assumes all rows of equal length
        
    def get_cols (self):
        """Returns list of all columns in a matrix."""
        
        return ([self.column(col_index) for col_index in range(0, self.num_cols())])
         
    def __mul__(m1, m2):
        """Multiplies two Matrix objects and returns the resulting matrix.
    
           Number of rows in m1 must equal the number of columns in m2."""
       
        result_rows = []
        
        #Iterate over the rows in m1.  The first column of row i is formed by
        #multiplying the ith row of m1 by the first column of m2.  The second
        #column is formed by muliplying the ith row of m1 by the second column
        #of m2, etc.
        for row in m1:
            new_row = []
            
            for col in m2.get_cols():
                new_row.append(row * col)
                
            result_rows.append(new_row)
        
        return (Matrix(result_rows))     
        
            
class Vector (object):
    "Class to encapsulate vector data and operations."
     
    def __init__(self,x=0.0,y=0.0,z=0.0):
        """Constructor for a three-dimensional vector.
      
        Note that two-dimensional vectors can be constructed by omitting one of 
        the coordinates, which will default to 0."""
         
        self.x = x     #Cartesian x coordinate
        self.y = y     #Cartesian y coordinate
        self.z = z     #Cartesian z coordinate
      
    def __str__(self):  #Called when used in print statement
        """Returns a string representation of the vector."""
        return('Vector: x: %.3f, y: %.3f, z: %.3f'\
                % (self.x, self.y, self.z))

    def set_eq(self, x=None, y=None, z=None):
        """Assigns new value to vector.
      
        Arguments are now optional to permit this to be used with 2D vectors
        or to modify any subset of coordinates."""
      
        if (x != None):
            self.x = x
        if (y != None):
            self.y = y
        if (z != None):
            self.z = z
      
    def length(self):
        """Returns magnitude of the vector """ 
        return(sqrt(self.x * self.x + self.y * self.y + self.z * self.z))
       
    def normalize(self):
        """Returns copy of the normalized vector """ 
        mag = self.length()
      
        if (mag == 0.0):
            return(Vector(self.x, self.y, self.z))
        else:
            return (Vector(self.x/mag,self.y/mag,self.z/mag))

    def __mul__(self,rs):
        """Implements Vector * scalar.  Can then use '*' syntax in multiplying a vector by a scalar rs. """ 
        x = self.x * rs
        y = self.y * rs
        z = self.z * rs
        return (Vector(x,y,z))
      
    def __rmul__(self,ls):
        """Implements float * Vector """ 
        x = self.x * ls
        y = self.y * ls
        z = self.z * ls
        return (Vector(x,y,z))
      
    def __add__(self,rs):
        """Implements Vector + Vector """ 
        x = self.x + rs.x
        y = self.y + rs.y
        z = self.z + rs.z
        return (Vector(x,y,z))
      
    def __sub__(self,rs):
        """Implements Vector - Vector """ 
        x = self.x - rs.x
        y = self.y - rs.y
        z = self.z - rs.z
        return (Vector(x,y,z))
      
    def __div__(self,rs):
        """Implements Vector / float """ 
        x = self.x / rs
        y = self.y / rs
        z = self.z / rs
        return (Vector(x,y,z))
      
    def __imul__(self,rs):
        """Implements Vector *= float """ 
        self.x *= rs
        self.y *= rs
        self.z *= rs
        return (self)
      
    def __iadd__(self,rs):
        """Implements Vector += vector """ 
        self.x += rs.x
        self.y += rs.y
        self.z += rs.z
        return (self)
      
    def __isub__(self,rs):
        """Implements Vector -= vector """ 
        self.x -= rs.x
        self.y -= rs.y
        self.z -= rs.z
        return (self)
      
    def __idiv__(self,rs):
        """Implements Vector /= float """ 
        self.x /= rs
        self.y /= rs
        self.z /= rs
        return (self)
      
    def create_matrix(self):
         """Converts a Vector into a single-column matrix."""
       
         column = [self.x, self.y, self.z]
         return(Matrix([[element] for element in column]))  #singleton list
       
    def compute_ra (self):
         """Returns the right ascension of a vector (must be unit vector) in radians."""
       
         ra = atan2(self.y, self.x)       #RA is arctan of y/x
         return(math2.normalize_2pi(ra))   #normalize from 0-2pi
       
    def compute_dec (self):
         """Returns the declination of a vector (must be unit vector) in radians."""
              
         return(math2.asin2(self.z))   #DEC is arcsin of z
          
    def set_xyz(self,ra,dec):
        """Creates a unit vector from spherical coordinates """ 
        self.x = cos(dec) *cos(ra)
        self.y = cos(dec) *sin(ra)
        self.z = sin(dec)
    def rotate_about_eigenaxis(self, angle, eigenaxis):
        """rotates a vector about arbitrary eigenaxis.
        
        eigenaxis = Vector object (axis about which to rotate).
        angle = angle to rotate by in radians.
        Rotation is counterclockwise looking outward from origin along eigenaxis.
        Function uses rotation matrix from Rodrigues formula.
        
        Note: This function is more general than rotate_about_axis above and
        could be used in its place.  However, rotate_about_axis is faster and
        clearer when the rotation axis is one of the Cartesian axes."""
        
        cos_ang = cos(angle)    #Used repeatedly below
        sin_ang = sin(angle)
        
        #Fill out the Rodrigues rotation matrix
        R11 = cos_ang + eigenaxis.x**2 * (1 - cos_ang)
        R12 = eigenaxis.x * eigenaxis.y * (1 - cos_ang) - eigenaxis.z * sin_ang
        R13 = eigenaxis.x * eigenaxis.z * (1 - cos_ang) + eigenaxis.y * sin_ang
        R21 = eigenaxis.x * eigenaxis.y * (1 - cos_ang) + eigenaxis.z * sin_ang
        R22 = cos_ang + eigenaxis.y**2 * (1 - cos_ang)
        R23 = eigenaxis.y * eigenaxis.z * (1 - cos_ang) - eigenaxis.x * sin_ang
        R31 = eigenaxis.x * eigenaxis.z * (1 - cos_ang) - eigenaxis.y * sin_ang
        R32 = eigenaxis.y * eigenaxis.z * (1 - cos_ang) + eigenaxis.x * sin_ang
        R33 = cos_ang + eigenaxis.z**2 * (1 - cos_ang)
        
        rot_matrix = Matrix([[R11, R12, R13], [R21, R22, R23], [R31, R32, R33]])
        new_matrix = rot_matrix * self.create_matrix()
        new_vector = new_matrix.column(0)
        #result = CelestialVector()  #initialize with Cartesian coordinates
        #result.update_cartesian(x=new_vector[0], y=new_vector[1], z=new_vector[2])
        return(Vector(new_vector[0],new_vector[1],new_vector[2]))
                
      
NULL_3D_VECTOR = Vector(0,0,0)    #this can be reused as needed


class CelestialVector (Vector):
    "Class to encapsulate a unit vector on the celestial sphere."
    
    def __init__(self, ra=0.0, dec=0.0, frame='eq', degrees=True):
        """Constructor for a celestial vector.
        
        There are two spherical coordinates, a longitudinal coordinate (called
        right ascension), and a latitudinal coordinate (called declination).
        The RA is defined as the counterclockwise angle from a reference direction 
        on the equatorial plane; it ranges from 0-360 degrees.  The DEC is the angle
        between the vector and the equatorial plane; it ranges from -90 to 90 degrees.
        Angles are specified in degrees but represented internally as radians.
        
        The frame attribute indicates the coordinate frame of the vector, which may be 
        'eq' (equatorial, default), 'ec' (ecliptic), or 'gal' (galactic).  In equatorial
        coordinates, the equatorial plane is the celestial equator (extension of the Earth's
        equator) and the reference axis is the vernal equinox.  In ecliptic coordiantes,
        the equatorial plane is the ecliptic (the Earth's orbital plane) and the reference
        axis is usually defined relative to the Sun.  In galactic coordinates, the equatorial
        plane is the plane of the Galaxy.
        
        The degrees attribute should be True if the RA,DEC inputs are in degrees.
        Otherwise radians is assumed.  
        
        The coordinates "ra" and "dec" may be used in all three systems.  Other names for
        coordinates in different frames may be defined for clarity.
        
        A CelestialVector is also an ordinary unit vector, with Cartesian coordinates defined
        relative to the equatorial plane."""
      
        if (degrees):
            ra = math2.D2R * ra
            dec = math2.D2R * dec
        
        self.ra = ra
        self.dec = dec
        self.frame = frame

        #Initialize standard vector with translated Cartesian coordinates
        Vector.__init__(self, x=cos(ra)*cos(dec), y=sin(ra)*cos(dec), z=sin(dec))
        
    def __str__(self, verbose=True):
        """Returns a string representation of the vector.  Displays angles in degrees."""
        celest_info = 'RA: %.3fD, DEC: %.3fD, frame: %s'\
        % (math2.R2D*self.ra, math2.R2D*self.dec, self.frame)
        
        if (verbose):
            celest_info = 'CelestialVector: ' + celest_info + '\n' + super(CelestialVector, self).__str__()
        return(celest_info)
    
    def set_eq(self, ra, dec, degrees=False):
        """Modifies a celestial vector with a new RA and DEC.
        
        degrees = True if units are degrees.  Default is radians."""
        
        if (degrees):
            ra = math2.D2R * ra
            dec = math2.D2R * dec
        
        self.ra = ra 
        self.dec = dec
    
        #Update Cartesian coordinates as well.
        super(CelestialVector, self).set_eq(cos(ra)*cos(dec), sin(ra)*cos(dec), sin(dec))
        
    def update_cartesian(self, x=None, y=None, z=None):
        """Modifies a celestial vector by specifying new Cartesian coordinates.
        
    Any subset of the Cartesian coordinates may be specifed."""
        
        if (x != None):
           self.x = x
        if (y != None):
           self.y = y
        if (z != None):
         self.z = z
            
        self.ra = self.compute_ra()
        self.dec = self.compute_dec()
        
    def rotate_about_axis (self, angle, axis):
        """This rotates a vector about an axis by the specified angle
        by using a rotation matrix.
        A new vector is returned.
        
        Axis must be 'x', 'y', or 'z'.
        The x-rotation rotates the y-axis toward the z-axis.
        The y-rotation rotates the z-axis toward the x-axis.
        The z-rotation rotates the x-axis toward the y-axis."""
        
        if (axis == 'x'):
            rot_matrix = Matrix([[1,0,0],[0,cos(angle),-sin(angle)],\
            [0, sin(angle), cos(angle)]])
            
        elif (axis == 'y'):
            rot_matrix = Matrix([[cos(angle), 0, sin(angle)], [0,1,0],\
            [-sin(angle), 0, cos(angle)]])
            
        elif (axis == 'z'):
            rot_matrix = Matrix([[cos(angle), -sin(angle), 0],\
            [sin(angle), cos(angle), 0], [0,0,1]])
            
        else:
            print ('Error')
            return
            
        new_matrix = rot_matrix * self.create_matrix()
        new_vector = new_matrix.column(0)
        result = CelestialVector()  #initialize with Cartesian coordiantes
        result.update_cartesian(x=new_vector[0], y=new_vector[1], z=new_vector[2])
        return(result)
        
    def rotate_about_eigenaxis(self, angle, eigenaxis):
        """rotates a vector about arbitrary eigenaxis.
        
        eigenaxis = Vector object (axis about which to rotate).
        angle = angle to rotate by in radians.
        Rotation is counterclockwise looking outward from origin along eigenaxis.
        Function uses rotation matrix from Rodrigues formula.
        
        Note: This function is more general than rotate_about_axis above and
        could be used in its place.  However, rotate_about_axis is faster and
        clearer when the rotation axis is one of the Cartesian axes."""
        
        cos_ang = cos(angle)    #Used repeatedly below
        sin_ang = sin(angle)
        
        #Fill out the Rodrigues rotation matrix
        R11 = cos_ang + eigenaxis.x**2 * (1 - cos_ang)
        R12 = eigenaxis.x * eigenaxis.y * (1 - cos_ang) - eigenaxis.z * sin_ang
        R13 = eigenaxis.x * eigenaxis.z * (1 - cos_ang) + eigenaxis.y * sin_ang
        R21 = eigenaxis.x * eigenaxis.y * (1 - cos_ang) + eigenaxis.z * sin_ang
        R22 = cos_ang + eigenaxis.y**2 * (1 - cos_ang)
        R23 = eigenaxis.y * eigenaxis.z * (1 - cos_ang) - eigenaxis.x * sin_ang
        R31 = eigenaxis.x * eigenaxis.z * (1 - cos_ang) - eigenaxis.y * sin_ang
        R32 = eigenaxis.y * eigenaxis.z * (1 - cos_ang) + eigenaxis.x * sin_ang
        R33 = cos_ang + eigenaxis.z**2 * (1 - cos_ang)
        
        rot_matrix = Matrix([[R11, R12, R13], [R21, R22, R23], [R31, R32, R33]])
        new_matrix = rot_matrix * self.create_matrix()
        new_vector = new_matrix.column(0)
        result = CelestialVector()  #initialize with Cartesian coordinates
        result.update_cartesian(x=new_vector[0], y=new_vector[1], z=new_vector[2])
        return(result)
        
    def rotate_using_quaternion(self, angle, eigenaxis):
        """Rotates a vector about arbitrary eigenaxis using quaternion.
        
        This is an alternative formulation for rotate_about_eigenaxis.
        Interface is the same as rotate_about_eigenaxis."""
        
        q = quat.Quaternion(eigenaxis, 0.0)
        
        ##Need to negate here because set_values performs a negative rotation  Quaternion definition updated.
        #q.set_values(eigenaxis, -angle)   #quaternion now represents the rotation
        return(make_celestial_vector(q.cnvrt(self)))
        
    def transform_frame(self, new_frame):
        """Transforms coordinates between celestial and ecliptic frames

        and returns result as a new CelestialVector.
        If new coordinate frame is the same as the old, a copy of the vector
        is returned."""
        
        result = None
        
        #Equatorial to ecliptic: rotate z-axis toward y-axis.
        if ((new_frame == 'ec') and (self.frame == 'eq')):
            result = self.rotate_about_axis(-EARTH_OBLIQUITY, 'x')
        
        #Ecliptic to equatorial: rotate y-axis toward z-axis.
        elif ((new_frame == 'eq') and (self.frame == 'ec')):
            result = self.rotate_about_axis(EARTH_OBLIQUITY, 'x')
            
        elif ((new_frame == 'gal') and (self.frame == 'eq')):
            #Use formula from Wayne Kinzel's book, adjusted for J2000 coordinates.
            b = math2.asin2(cos(self.dec) * cos(NGP.longitude) * cos(self.ra - NGP.latitude)\
            + sin(self.dec) * sin(NGP.longitude))
            
            l = atan2(sin(self.dec) - sin(b) * sin (NGP.longitude),\
            cos (self.dec) * sin(self.ra - NGP.latitude) * cos(NGP.longitude)) + NGP.anode
            
            result = CelestialVector(l, b, degrees=False)
            
        elif ((new_frame == 'eq') and (self.frame == 'gal')):
            l = self.ra   #use l,b notation here for clarity
            b = self.dec
            
            dec = math2.asin2(cos(b) * cos(NGP.longitude) * sin(l - NGP.anode) + sin(b) * sin(NGP.longitude))
            
            ra = atan2(cos(b) * cos(l - NGP.anode),\
            sin(b) * cos(NGP.longitude) - cos(b) * sin(NGP.longitude) * sin(l - NGP.anode)) + NGP.latitude
            
            result = CelestialVector(ra, dec, degrees=False)
                        
        elif (((new_frame == 'gal') and (self.frame == 'ec')) or ((new_frame == 'ec') and (self.frame == 'gal'))):
            print("Error: Direct conversion between ecliptic and galactic coordinates not supported yet")
            
        elif (new_frame != self.frame):
            print("Error: unrecognized coordinate frame.")

        #If there was an error, return a copy of the initial vector.            
        if (result is None):
            result = CelestialVector(self.ra, self.dec, self.frame, False)

        else:
            result.frame = new_frame  #record new frame
            
        return (result)
        
    def rotate_by_posang (self, pa):
        """Returns the vector that results from rotating the self vector
        
        counterclockwise from the North projection onto the plane
        orthogonal to that vector by the specified position angle
        (in radians).
        See "V3-axis Position Angle", John Isaacs, May 2003 for
        further discussion."""
        
        x_coord = -cos(self.ra) * sin(self.dec) * cos(pa) - sin(self.ra) * sin(pa)
        y_coord = -sin(self.ra) * sin(self.dec) * cos(pa) + cos(self.ra) * sin(pa)
        z_coord = cos(self.dec) * cos(pa)
        result = CelestialVector()
        result.update_cartesian(x_coord, y_coord, z_coord)
        return(result)
        
    def position_angle (self, v):
        """Returns the position angle of v at the self vector, in radians.
        
        v is an arbitrary vector that should be a CelestialVector object.
        The position angle is the angle between the North vector on the
        plane orthogonal to the self vector and the projection of v onto
        that plane, defined counterclockwise.
        See "V3-axis Position Angle", John Isaacs, May 2003 for
        further discussion."""
        
        y_coord = cos(v.dec) * sin(v.ra - self.ra)
        x_coord = sin(v.dec) * cos(self.dec) - cos(v.dec) * sin(self.dec) * cos (v.ra - self.ra)
        pa = atan2(y_coord, x_coord)
        
        if (pa < 0):
            pa += (2 * pi)  #PA has range 0-360 degrees
            
        return(pa)
        
        
class Attitude (CelestialVector):
    "Defines an Observatory attitude by adding a position angle."""
    
    def __init__(self, ra=0.0, dec=0.0, pa=0.0, frame='eq', degrees=True):
        """Constructor for an Attitude.
        
        pa = position_angle in degrees(default) or radians if degrees=False is specified.
        Other arguments are the same as with CelestialVector."""
        
        super(Attitude, self).__init__(ra=ra, dec=dec, frame=frame, degrees=degrees)
    
        if (degrees):   #convert into radians
            pa = math2.D2R * pa
        
        self.pa = pa
    
    def __str__ (self, verbose=True):
        """Returns a string representation of the attitude.
        
        verbose (optional) = flag indicating whether detailed Vector information should be included."""
        
        att_info = 'PA: %.3fD' %(math2.R2D * self.pa)
        
        if (verbose):
           att_info = att_info + '\n' + super(Attitude, self).__str__(verbose=True)
        else:
           att_info = att_info + ', ' + super(Attitude, self).__str__(verbose=False)
           
        return(att_info)
        
        
class SpacecraftPointing (Vector):
    """A 2-dimensional vector to represent a V2/V3 pointing on a telescope focal plane."""
    
    def __init__ (self, v2=0.0, v3=0.0):
        """Constructor for the V2/V3 pointing.
        
        v2 = v2 coordinate (arcsec).
        v3 = v3 coordinate (arcsec)."""
        
        #Call Vector constructor to set up x/y attributes, which set up infrastructure for vector arithmetic.
        #V2,V3 methods are just syntactic sugar.
        Vector.__init__(self, x=v2, y=v3)
        
    def v2 (self):
        """Returns V2 coordinate."""
         
        return(self.x)
         
    def v3 (self):
        """Returns V3 coordinate."""
         
        return(self.y)
        
    def __str__ (self):
        """Inspector function for the V2/V3 pointing."""
        
        return('SpacecraftPointing: v2: %.3f, v3: %.3f arcsec' %(self.v2(), self.v3()))
        
    def __add__ (self, v2):
        """Implements SpacecraftPointing + SpacecraftPointing."""
        
        x = self.x + v2.x
        y = self.y + v2.y
        
        return(SpacecraftPointing(x,y))
        
    def __sub__ (self, v2):
        """Implements SpacecraftPointing - SpacecraftPointing."""
        
        x = self.x - v2.x
        y = self.y - v2.y
        
        return(SpacecraftPointing(x,y))

         
#Functions that operate on vectors but are not methods.

NEP_ECI = (CelestialVector(0.0, 90.0, 'ec')).transform_frame('eq')  #useful as a safe attitude

def get_tuple (v):
    """Returns the vector as a tuple, but checks for None.

    v = Vector object to represent, or None if there is no vector."""

    result = None

    if (v is not None):
        result = (v.x, v.y, v.z)

    return(result)

def dot(v1,v2):
    """returns dot product between two vectors, non class member """ 
    return(v1.x * v2.x + v1.y * v2.y + v1.z * v2.z)
   
def cross(v1,v2):
    """returns cross product between two vectors, non class member """ 
    x = v1.y*v2.z - v1.z*v2.y
    y = v1.z*v2.x - v1.x*v2.z
    z = v1.x*v2.y - v1.y*v2.x
    return Vector(x,y,z)
   
def separation(v1, v2, norm=False):
    """Returns angle between two unit vectors in radians.
       
    The angle between two normalized vectors is the arc-cosine of the dot product.
    Unless the norm attribute is set to True, it is assumed the vectors are 
    already normalized (for performance)."""
    
    if (norm):
        v1 = v1.normalize()
        v2 = v2.normalize()

    separation = math2.acos2(dot(v1, v2))
    
    #For very small angles, cos and acos behave poorly as the cosine of a very small angle is
    #interpreted as 1.0.  Therefore, recompute using the cross product if the result is less than 1 degree.
    if (separation < math2.D2R):
        vcross = cross(v1,v2)
        separation = math2.asin2(vcross.length())
        
    return(separation)
    
def ra_delta (v1, v2):
    """Returns difference in right ascension between two CelestialVectors."""
    
    delta_ra = v1.ra - v2.ra
    
    #Check for zero crossings.  If the difference exceeds 180 degrees, adjust by 360 in opposite direction.
    
    if (delta_ra < -pi):
        delta_ra = delta_ra + 2*pi
    elif (delta_ra > pi):
        delta_ra = delta_ra - 2*pi
        
    return(delta_ra)
    
def ra_separation(v1, v2):
    """Returns separation in right ascension between two CelestialVectors.
    This is accurate only if the difference in declination is small.
    
    |sep| = DELTA-RA cos DEC."""
    
    delta_ra = ra_delta(v1, v2)
    dec = math2.avg2(v1.dec, v2.dec)  #use average of the two declinations.
    return(delta_ra * cos(dec))
    
def dec_separation(v1, v2):
    """Returns difference in declination between two CelestialVectors."""
    
    return(v1.dec - v2.dec)    #simply take the difference in declination
    
def make_celestial_vector(v):
    """Takes a Vector object and creates an equivalent CelestialVector.
    
    Input vector v must be a unit vector."""
    
    result = CelestialVector()
    result.update_cartesian(v.x, v.y, v.z)
    return(result)
    
def random_direction_vector (mag=1.0):
    """Creates a vector in a random direction with the requested magnitude.

    mag = magnitude of the vector (default 1.0)."""

    #The objective here is to generate a point in a random direction on a sphere,
    #so that any region of the sphere of a given area is expected to contain the
    #same number of randomly generated points.  The algorithm is to generate two
    #random numbers on [0,1], u and v.  Then
    #
    # RA = 2 * pi * u [range 0-2pi]
    # DEC = asin(2v - 1) [range -pi - pi]
    #
    #This algorithm is taken from http://mathworld.wolfram.com/SpherePointPicking.html.
    #That article uses spherical coordinates THETA and PHI, where THETA is the
    #azimuthal angle (equivalent to RA) and PHI is the zenith angle.  The conversion
    #between zenith angle and declination is PHI = PI/2 - DEC, so cos PHI = sin DEC.
    #Therefore, the acos in the Wolfram formula is replaced by asin here.
    #
    #Also note that the solid angle of an annulus on the celestial sphere scales as
    #sin DEC_MAX - sin DEC_MIN (a result which can easily be proved by integrating over the sphere),
    #which is consistent with this formula.
        
    u = random.random()
    v = random.random()
    ra = 2 * pi * u
    dec = math2.asin2(2*v - 1)
    vec = Vector()
    vec.set_xyz(ra, dec)   #convert to Cartesian coordinates
    vec *= mag       #scale by magnitude
    return(vec)
      
def projection (v, axis):
    """Returns projection of vector v on plane normal to axis.
    
    First take cross-product of v and the axis and normalize it.
    Then cross the axis with the result and return a CelestialVector.
    See http://www.euclideanspace.com/maths/geometry/elements/plane/lineOnPlane/index.htm."""
    
    return(make_celestial_vector(cross(axis, (cross(v, axis)).normalize())))

def pos_V_to_ra_dec(V):
    """Returns tuple of spherical angles from unit direction Vector """ 
    ra = atan2(V.y,V.x)
    dec = math2.asin2(V.z)
    if ra < 0.:
        ra += 2. * pi
    return(ra,dec)

def pos_V_to_v2_v3(V):
    """Returns tuple of spherical angles from unit direction Vector """ 
    ra = atan2(V.y,V.x)
    dec = math2.asin2(V.z)
    #if ra < 0.:
    #    ra += 2. * pi
    return(ra,dec)

#Numerical integration routines

def Vector_trapzd (a, b, n, old_s, the_func):
    """This is used in conjunction with Vector_integration below to perform an iteration of trapezoidal integration.
    
    a = lower limit of range (float)
    b = upper limit of range (float)
    n = iteration number for this iteration (integer >= 1).
    old_s = the vector returned by the previous iteration of Vector_trapzd.
    On the first iteration (n=1), a zero vector should be provided.
    
    the_func = the function being integrated (must return a Vector)."""
    
    #For the basics of trapezoidal integration, see http://en.wikipedia.org/wiki/Trapezoidal_rule.
    #The trapezoidal method approximates the area under the function as a trapezoid, whose area
    #is the width (b-a) times the average value of the function over the interval.
    #In its simplest form (N=1), the entire integral is approximated as a single trapezoid, using
    #average of the function's value at the two endpoints.  This is not very accurate, especially
    #for a complex function.
    
    #Now let the range be subdivided into N equal subintervals of width h = (b-a)/N.  The interval
    #then consists of N+1 points: x0, x1, ..., xN.  The average of the first interval is (f(x0) + f(x1))/2,
    #the average of the second is (f(x1) + f(x2))/2, etc.  The sum, as given in the Wikipedia article
    #under "Uniform Grid", is S = h/2 SUM(i=0..N-1) [f(x(i)) + f(x(i+1))].  Note that all the interior
    #points are counted twice in this summation, while the endpoints are counted only once:
    #S = ((b-a)/2n) [f(x0) + 2f(x1) + 2f(x2) + ... + 2f(x(N-1)) + f(x(N))].
    
    #This function is used as part of an iterative loop where Vector_integration repeatedly calls it
    #with successively larger increments of n, starting at n=1.  The number of subintervals N = 2**(n-1).
    #To avoid repeating computations, the sum returned from the previous iteration is passed on the
    #next one as old_s and reused.  The previous iteration, when N was equal to N/2, generated data
    #for N/2 + 1 points.  To this we now want to add N/2 interior points, each spaced halfway between
    #two of the points from the last iteration (say i and i+1).  For each such interior point j,
    #the function is evaluated in two places: at (i+j)/2, and at (j+(i+1))/2.  The sum of these is 
    #not exactly equal to 2 f(j), but should approach this value as the interval width becomes smaller.
    #The sum of these interior points is added to the previous sum, and since twice as many intervals
    #are now involved, the result is divided by an additional factor of 2.
    
    #For example, suppose n=2.  Then old_s = ((b-a)/2) (f(x0) + f(x2)).
    #The first and only interior point is the midpoint x1 = (b-a)/2.
    #The function is evaluated twice, at (a+x1)/2 and (x1+b)/2.  Adding these gives an approximation
    #of 2f(x1).  This is added to the previous sum and the result is divided by 2,
    #which approximates ((b-a)/4) (f(x0) + 2f(x1) + f(x2)).
    
    #Now suppose n=4.  There are now two interior points, x1 and x3.  Again the function is evaluated on
    #opposite sides of each interior point to approximate 2f(x1) and 2f(x3).  Combining this with
    #the previous sum gives S ~ ((b-a)/8) (f(x0) + 2f(x1) + 2f(x2) + 2f(x3) + f(x4)), and so forth.
    
    #Note that the_func returns a Vector.  The resulting sum is also a vector, using scalar-vector
    #arithmetic to combine results as needed.
     
    Vsum = Vector()
    #s = Vector()
    if n == 1:
        s=0.5*(b-a)*(the_func(a) + the_func(b))  #pure trapezoidal rule with one interval
    else:
        it = 1     #this is the number of intervals (N above).
        
        #The left shift multiplies by 2.  Presumably this is faster than just using 2**(n-1).
        for j in range(1,n-1):
            it <<= 1
        tnm=float(it)
        adel=(b-a)/tnm    #this is the interval width h = (b-a)/N
        
        #Add half the interval width to find the midpoint between a and the first interior point.
        x=a+0.5*adel
        
        Vsum *= 0.    #remember Vsum is a vector, so this initializes each element to zero.
        for j in range(it):
            Vsum += the_func(x)
            x+=adel    #increment by the full width of the new interval
            
        #Mutiply the sum by the interval width h = (b-a)/N.  This takes care of the interior points.
        #Add the old sum to include the original points, then divide by another factor of 2.
        s=0.5*(old_s+(b-a)*Vsum*(1./tnm))
    return s

def Vector_integration (a,b,the_func, rel_tolerance=1.0e-03, abs_tolerance=1.0e-5):
    """Performs a trapezoidal integration of a vector function.
    
    a = lower limit of range (float)
    b = upper limit of range (float)
    the_func = the function to be integrated (must return a Vector).
    rel_tolerance = minimum relative tolerance (default 0.1%).
    abs_tolerance = minimum absolute tolerance (default 1.0E-05)."""
    
    JMAX=30 #Maximum number of iterations; normally 20
    old_s = Vector()   #This holds the result of the previous iteration; initialize to zero vector
    
    #Repeatedly call Vector_trapzd to refine the integration using 2**(j-1) intervals.
    #Compare each result to the previous one to check for convergence.
    #When the result of an iteration is sufficiently close to the previous one, the
    #result is considered to have converged and can be returned.
      
    for j in range(JMAX):
        s = Vector_trapzd(a,b,j+1,old_s,the_func)
        if j > 2:    #Don't bother to check for convergence until the fourth iteration.
            #For convergence, either each element of the new vector must be within the tolerance of
            #the corresponding element of the old one, or the absolute differences must
            #all be very small.
            if (( abs(s.x - old_s.x) < rel_tolerance*abs(old_s.x)  and
                  abs(s.y - old_s.y) < rel_tolerance*abs(old_s.y)  and
                  abs(s.z - old_s.z) < rel_tolerance*abs(old_s.z)) or
                ( abs(s.x - old_s.x) <= abs_tolerance and
                  abs(s.y - old_s.y) <= abs_tolerance and
                  abs(s.z - old_s.z) <= abs_tolerance )
                ):
                return s
        old_s.set_eq(s.x,s.y,s.z)
        
    #If we got to this point, the integration failed to converge after the maximum number of iterations.
    #Complain and return the zero vector.s
    print("Too many steps in routine qtrap")
    return Vector()
           




          
