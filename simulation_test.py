
   
from simulation import Simulation
from virus import Virus
from check import check

print('\n\nWelcome to the Herd Immunity Simulatiom!')
print('- - - - - - - - - - - - - - - - - - - - - - -  - - - - - - -')
print('You will be asked for data to input into your simulation.')
print('After running the simulation, you can access data in the output files. Enjoy!')
print('- - - - - - - - - - - - - - - - - - - - - - -  - - - - - - -')


virus_name = check('What is the virus name?  ', str)
repro_rate = check('What is the reproduction rate?  ')/100
mortality_rate = check('What is the mortality rate?  ')/100
population_size = check('What is the population size?  ')
vacc_percentage = check('What percentage of the population is vaccinated?  ')/100
initial_infected = check('How many people are initially infected?  ')
average_interactions = check('How many interactions should each infected person have?  ')


virus = Virus(virus_name, repro_rate, mortality_rate)


sim = Simulation (virus, population_size, vacc_percentage, initial_infected, average_interactions)


sim.run()