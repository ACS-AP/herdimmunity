class Virus(object):

    def __init__(self, virus_name, repro_rate, mortality_rate):
        self.virus_name = virus_name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate

#TESTING-------------------------------------------

def test_virus_instantiation():
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

def test_virus_instantiation():
    virus = Virus("Bubonic Plague", 0.8, 0.7)
    assert virus.name == "Bubonic Plague"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.7

def test_virus_instantiation():
    virus = Virus("Ebola", 0.25, 0.7)
    assert virus.name == "Ebola"
    assert virus.repro_rate == 0.25
    assert virus.mortality_rate == 0.7
