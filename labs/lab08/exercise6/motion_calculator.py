# Importing my own module and data                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
import physics_constants

initial_height = physics_constants.building_height
initial_velocity = physics_constants.initial_velocity
gravity = physics_constants.standard_gravity
mass = physics_constants.ball_mass

# Prorgam for Physics Calculator

time = 2

position = initial_height + (initial_velocity * time) - (0.5 * gravity * time * time)
velocity = initial_velocity - gravity * time
kinetic_energy = 0.5 * mass * velocity * velocity


print("Height:", initial_height, "\nVelocity:", initial_velocity, "\nMass:", mass)
print("Time-based calculations(postion, velocity):", position)
print("Energy analysis:", kinetic_energy)
print("Motion Status: Positive to the right.")




