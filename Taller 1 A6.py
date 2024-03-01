
import numpy as np
def cylinder_force(pressure, diameter, area, rod_diameter):
    """Calculate the force of a double-acting pneumatic cylinder."""
    rod_area = np.pi * (rod_diameter / 2)**2
    force_advance = pressure * (area - rod_area)
    force_retreat = pressure * rod_area
    return force_advance, force_retreat

# Example usage
pressure = 100000  # in Pascals
diameter = 0.05  # in meters
rod_diameter = 0.02  # in meters
area = np.pi * (diameter / 2)**2
force_advance, force_retreat = cylinder_force(pressure, diameter, area, rod_diameter)
print("Force of advance:", force_advance, "Newtons")
print("Force of retreat:", force_retreat, "Newtons")