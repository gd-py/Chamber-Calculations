"""Find the chamber pressure and thrust of a solid rocket motor."""
from proptools import solid, nozzle
import numpy as np

Mpa_PSI = 145.037738 #conversion from Mpa to PSI

d_o = 50e-3 # solid fuel outer dia
d_i = 12.7e-3 # solid fuel inner dia
l = 42e-2 # chamber length
burn_area = np.pi*l*(d_o+d_i)/2 # Average of inner and outer area

# Propellant properties
gamma = 1.0468    # Exhaust gas ratio of specific heats [units: dimensionless].
rho_solid = 1890.    # Solid propellant density [units: kilogram meter**-3].
n = 0.319    # Propellant burn rate exponent [units: dimensionless].
a =  15.29e-3 * (6.9e6)**(-n)    # Burn rate coefficient, such that the propellant
# burns at 2.54 mm s**-1 at 6.9 MPa [units: meter second**-1 pascal**-n].
c_star = 919.    # Characteristic velocity [units: meter second**-1].

# Motor geometry
A_t = 295.32e-6    # Throat area [units: meter**2].
d_o = 50e-3 # solid fuel outer dia
d_i = 12.7e-3 # solid fuel inner dia
l = 42e-2 # chamber length
A_b = np.pi*l*(d_o+d_i)/2 # Burn area, Average of inner and outer area [units: meter**2].

# Nozzle exit pressure [units: pascal].
p_e = 101325

# Compute the chamber pressure [units: pascal].
p_c = solid.chamber_pressure(A_b / A_t, a, n, rho_solid, c_star)

# Compute the sea level thrust [units: newton].
F = nozzle.thrust(A_t, p_c, p_e, gamma)

print('Chamber pressure = {:.1f} PSI'.format(p_c * 1e-6 * Mpa_PSI))
print('Thrust (sea level) = {:.1f} kN'.format(F * 1e-3))