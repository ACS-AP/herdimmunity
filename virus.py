# virus class
class Virus(object):
    ''' Properties and attributes of the virus used in Simulation. '''

    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
# Testing virus class

def test_virus_instantiation():
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

def test_virus_instantiation():
    virus = Virus("Dysentery", 0.3, 0.4)
    assert virus.name == "Dysentery"
    assert virus.repro_rate == 0.3
    assert virus.mortality_rate == 0.4

def test_virus_instantiation():
    virus = Virus("Fever", 0.98, 0.02)
    assert virus.name == "Fever"
    assert virus.repro_rate == 0.98
    assert virus.mortality_rate == 0.02
