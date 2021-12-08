import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    
    def __init__(self, virus, pop_size, num_vaccinated, initial_infected=1, avg_interactions=100):
        self.pop_size = pop_size 
        self.next_person_id = 0
        self.virus = virus 
        self.initial_infected = initial_infected 
        self.avg_interactions = avg_interactions
        self.total_infected = 0 
        self.current_infected = 0 
        self.total_immune = 0
        self.num_vaccinated = num_vaccinated
        self.population = []
        self.newly_dead = 0
        self.total_dead = 0 

        self._create_population() 
        for person in self.current_infected:
            print(f'Infected: {person._id}')
       
        self.newly_infected = []

        self.file_name = "{}_simulation_pop_{}.txt".format(virus.virus_name, pop_size)
        logger = Logger(self.file_name) 
        self.logger = logger

    def _create_population(self):
        
        person_id = 1

        while person_id < (self.pop_size + 1) :
            while person_id < (self.initial_infected + 1):
                person = Person(person_id, False, self.virus)
                self.population.append(person)
                self.current_infected.append(person)
                self.total_infected += 1
                person_id += 1
            is_vaccinated = ((random.random() < self.num_vaccinated))
            person = Person(person_id, is_vaccinated)
            self.population.append(person)
            person_id += 1
            if person.is_vaccinated:
                self.total_immune += 1 
        return self.population

    def _simulation_should_continue(self):
     
        pass

    def run(self):
        
        while self._simulation_should_continue() == True:
            self.time_step()
            self.current_infected = []
            self._infect_newly_infected()
            self.logger.log_time_step(len(self.newly_infected), self.newly_dead, self.total_infected, self.total_dead, self.total_immune, len(self.population), self.herd_immunity)
            self.newly_infected = []
            self.newly_dead = 0
            print(f'Population: {len(self.population)}')

    def time_step(self):
        
        for person in self.current_infected:
            print(f'Infected: {person._id}')

            random_people = random.sample(self.population, self.avg_interactions)
            for random_person in random_people:
                self.interaction(person, random_person)

    def interaction(self, person, random_person):
        
        assert person.is_alive == True
        assert random_person.is_alive == True

       
        pass

    def _infect_newly_infected(self):
        
        pass

if __name__ == "__main__":
    params = sys.argv[1:]

    name = str(params[0])
    pop_size = int(params[1])
    repro_rate = float(params[2])
    mortality_rate = float(params[3])
    num_vaccinated = int(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    virus = Virus(name, repro_rate, mortality_rate)
    # python3 simulation.py Ebola 100 0.9 0.7 25 1
    # python3 simulation.py Ebola 100000 0.9 0.7 25000 10
    sim = Simulation(virus, pop_size, num_vaccinated, initial_infected)

    sim.run()
    print(sim.pop_size)