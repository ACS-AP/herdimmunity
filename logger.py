class Logger(object):

    def __init__(self, file_name):
        self.file_name = file_name
        self.file = f'{self.file_name}.txt'

    def write_metadata(self, virus_name, repro_rate, mortality_rate, pop_size, num_vaccinated, initial_infected):

        repro_rate = repro_rate * 100
        mortality_rate = mortality_rate * 100
        num_vaccinated = num_vaccinated * 100

        
        file = open(self.file, 'a')
        file.write('Simulation\n\n\n')

        file.write('<---- Virus Information ---->\n')
        file.write(f'🦠 Virus: {virus_name}\n')
        file.write(f'🤒 Reproduction Rate: {repro_rate}%\n')
        file.write(f'💀 Mortality Rate: {mortality_rate}%\n')
        
        file.write('\n<--- Population Information --->\n')
        file.write(f'👥 Population: {pop_size}\n')
        file.write(f'💉 Vaccination Rate: {num_vaccinated}%\n')
        file.write(f'😷 Initial Infections: {initial_infected}\n')
         
        file.close()
        

    