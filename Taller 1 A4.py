
def pt100_resistance(temperature):
    """Calculate the resistance of a PT100 RTD as a function of temperature."""
    r0 = 100.0  # resistance at 0 degrees Celsius
    alpha = 0.00385  # temperature coefficient
    return r0 * (1 + alpha * temperature)

# Example usage
temperature = 100.0  # in degrees Celsius
resistance = pt100_resistance(temperature)
print("Resistance at", temperature, "degrees Celsius:", resistance, "Ohms")