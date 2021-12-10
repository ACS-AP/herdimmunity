from simulation import Simulation
from virus import Virus
from check import check

print('\n\nWelcome to the Herd Immunity Simulator!')
print('-------------------------------------------------------------')
print('Enter the required Data to run the Simulation')
print('Please enter all rates as an integer between 1-100.')
print('Data will be accesible in the output files. Enjoy!')
print('-------------------------------------------------------------')



virus_name = check('Virus Name:  ', str)
repro_rate = check('Reproductive Rate:  ')/100
mortality_rate = check('Mortality Rate:  ')/100
population_size = check('Population Size:  ')
percentage_vaccinated = check('Percentage Population Already Vaccinated:  ')/100
initial_infected = check('# of Initial Infections:  ')
avg_interactions = check('Interactions each Infected Person Has:  ')

virus = Virus(virus_name, repro_rate, mortality_rate)

sim = Simulation (virus, population_size, percentage_vaccinated, initial_infected, avg_interactions)

sim.run()