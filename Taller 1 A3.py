
import math

def rect_to_cyl(x, y, z):
    """Convert rectangular coordinates to cylindrical coordinates."""
    r = math.sqrt(x*2 + y*2)
    theta = math.atan2(y, x)
    return r, theta, z

def rect_to_sph(x, y, z):
    """Convert rectangular coordinates to spherical coordinates."""
    r = math.sqrt(x*2 + y*2 + z*2)
    theta = math.atan2(y, x)
    phi = math.acos(z / r)
    return r, theta, phi

# Example usage
x, y, z = 1, 1, 1
cyl = rect_to_cyl(x, y, z)
sph = rect_to_sph(x, y, z)
print("Cylindrical coordinates:", cyl)
print("Spherical coordinates:", sph)