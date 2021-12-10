class Logger(object):

    def __init__(self, file_name):
        
        self.file_name = file_name
        self.file = f'main_{self.file_name}.txt'
        self.microlog = f'details_{self.file_name}.txt'

    def write_metadata(self, virus_name, repro_rate, mortality_rate, population, percentage_vaccinated, initial_infected):

        repro_rate = repro_rate * 100
        mortality_rate = mortality_rate * 100
        percentage_vaccinated = percentage_vaccinated * 100


        
        file = open(self.file, 'a')

        file.write('HERD IMMUNITY SIMULATION\n\n')
        file.write('----- Virus Info -----\n')
        file.write(f'Virus: {virus_name}\n')
        file.write(f'Reproduction Rate: {repro_rate}%\n')
        file.write(f'Mortality Rate: {mortality_rate}%\n')
        file.write('\n--- Population Info ---\n')
        file.write(f'Population: {population}\n')
        file.write(f'Vaccination Rate: {percentage_vaccinated}%\n')
        file.write(f'Initial Infections: {initial_infected}\n')

        file.write('\n\n------------------------------------------------------------- \n\n')
                   
        file.close()
        
 
        

    def log_interaction(self, person, random_person, infected=False):
        
        
        file = open(self.microlog, 'a')
        file.write('\n\n')
        file.write('--------INTERACTIONS--------\n')
        
        if random_person.is_vaccinated:
            file.write(f'{person._id} Did Not Infect {random_person._id}. REASON: Vaccinated\n')
        elif random_person.natural_immunity: 
            file.write(f'{person._id} Did Not Infect {random_person._id}. REASON: Natural Immunity\n')
        elif random_person.virus != None: 
            file.write(f'{person._id} Did Not Infect {random_person._id}. REASON: Already Infected\n')
        elif infected: 
            file.write(f'{person._id} Infected {random_person._id}.\n')
        else: 
            file.write(f'{person._id} Did Not Infect {random_person._id}.\n')

        file.close()


    def log_infection_survival(self, person, did_die_from_infection=False):
        file = open(self.microlog, 'a')
        file.write('\n')
        file.write('     INFECTION OUTCOME:\n')
        if did_die_from_infection:
            file.write(f'{person._id} Died\n')
        else:
            file.write(f'{person._id} Survived. Achieved Immunity\n')

        file.close()

    def log_time_step(self, time_step, time_step_infections, time_step_deaths, total_infections, total_deaths, total_immune, total_population, herd_immunity):
    
        file = open(self.microlog, 'a')
        file.write('\n')
        file.write(f'------------ TIME STEP {time_step} ENDED ----------------\n')

        file.close()

        file = open(self.file, 'a')
        file.write(f'\nTIME STEP {time_step} ENDED\n')
        file.write(f'>> Infections: {time_step_infections} \n')
        file.write(f'>> Deaths: {time_step_deaths} \n\n')
        file.write(f'CUMULATIVE TOTAL \n')
        file.write(f'Infections: {total_infections} \n')
        file.write(f'Deaths: {total_deaths} \n\n')
        file.write(f'IMMUNITY STATS: \n')
        file.write(f'Total Immune: {total_immune}/{total_population} \n')
        file.write(f'Current Immunity Rate: {round((total_immune/total_population*100),2)}% \n')
        file.write(f'Herd Immunity Rate: {round(herd_immunity*100, 2)}% \n\n')
        file.write('\n\n------------------------------------------------------------- \n\n')

        file.close()

    def Final_data(self, conclusion, total_dead, total_alive, total_immune):
        file = open(self.file, 'a')
        file.write(f'FINAL OUTCOME: \n\n')
        if conclusion == 'herd immunity':
            file.write(f'>> SIMUlATION TERMINATED. HERD IMMUNITY ACHIEVED\n')
        elif conclusion == 'no infections':
            file.write(f'>> SIMUlATION TERMINATED. NO MORE INFECTIONS\n')
        else:
            file.write(f'>> SIMUlATION TERMINATED. POPULATION DIED\n')

        file.write(f'\nTotal Survivors: {total_alive}')
        file.write(f'\nTotal Deaths: {total_dead}')
        file.write(f'\nTotal Immune: {total_immune}')

        file.close()
        

    