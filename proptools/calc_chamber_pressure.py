"""Illustrate the chamber pressure equilibrium of a solid rocket motor."""

from matplotlib import pyplot as plt
import numpy as np

Mpa_PSI = 145.037738

p_c = np.linspace(1e6, 10e6)    # Chamber pressure [units: pascal].

# KNSU Propellant properties
gamma = 1.0468    # Exhaust gas ratio of specific heats [units: dimensionless].
rho_solid = 1890    # Solid propellant density [units: kilogram meter**-3].
n = 0.319    # Propellant burn rate exponent [units: dimensionless].
a = 15.29e-3 * (6.9e6)**(-n)    # Burn rate coefficient, such that the propellant
# burns at 0.602 in s**-1 at 1000 PSI [units: meter second**-1 pascal**-n] (Taken from Nakka's KNSU data).
c_star = 919    # Characteristic velocity [units: meter second**-1].

# Motor geometry
A_t = 295.32e-6    # Throat area [units: meter**2].
d_o = 50e-3 # solid fuel outer dia
d_i = 12.7e-3 # solid fuel inner dia
l = 42e-2 # chamber length
A_b = np.pi*l*(d_o+d_i)/2 # Burn area, Average of inner and outer area [units: meter**2].
    

# Compute the nozzle mass flow rate at each chamber pressure.
# [units: kilogram second**-1].
m_dot_nozzle = p_c * A_t / c_star

# Compute the combustion mass addition rate at each chamber pressure.
# [units: kilogram second**-1].
m_dot_combustion = A_b * rho_solid * a * p_c**n

# Plot the mass rates
plt.plot(p_c * 1e-6 * Mpa_PSI, m_dot_nozzle, label='Nozzle')
plt.plot(p_c * 1e-6 * Mpa_PSI, m_dot_combustion, label='Combustion')
plt.xlabel('Chamber pressure [PSI]')
plt.ylabel('Mass rate [kg / s]')

# Find where the mass rates are equal (e.g. the equilibrium).
i_equil = np.argmin(abs(m_dot_combustion - m_dot_nozzle))
m_dot_equil = m_dot_nozzle[i_equil]
p_c_equil = p_c[i_equil]
print("Required pressure is: ", p_c_equil * 1e-3, "Kpa")
p_c_equil *= Mpa_PSI
print("Required pressure is: ", p_c_equil * 1e-6, "PSI")

# Plot the equilibrium point.
plt.scatter(p_c_equil * 1e-6, m_dot_equil, marker='o', color='black', label='Equilibrium')
plt.axvline(x=p_c_equil * 1e-6, color='grey', linestyle='--')

plt.title('Chamber pressure: stable equilibrium, $n =$ {:.1f}'.format(n))
plt.legend()
plt.show()
