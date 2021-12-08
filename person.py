import random
random.seed(42)
from virus import Virus

class Person(object):
    def __init__(self, _id, is_vaccinated, infection=None):
        ''' 
        If person is chosen to be infected when the population is created, the simulation
        should instantiate a Virus object and set it as the value
        self.infection. Otherwise, self.infection should be None.
        '''
        self._id = _id # int
        self.is_alive = True  # bool
        self.is_vaccinated = is_vaccinated  # bool
        self.infection = infection  # Virus object or None

    def did_survive_infection(self):
        if self.virus: 
            died = random.random()
            if died < self.virus.died:
                print(f'{self._id} has Died :(')
                self.is_alive = False
                return False
            else:
                self.virus = None
                return True

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
# Testing person class

def test_vacc_person_instantiation():
    person = Person(1, True)

    assert person._id == 1
    assert person.is_alive is True
    assert person.is_vaccinated is True
    assert person.infection is None

def test_not_vacc_person_instantiation():
    person = Person(2, False)

    assert person._id == 2
    assert person.is_alive is True
    assert person.is_vaccinated is False
    assert person.infection is None

def test_sick_person_instantiation():
    person = Person(3, False, virus)

    assert person._id == 3
    assert person.is_alive is True
    assert person.is_vaccinated is False
    assert person.infection == virus

def test_did_survive_infection():
    person = Person(4, False, virus)
    survived = person.did_survive_infection()

    if survived:
        assert person.is_alive is True
        assert person._id == 4
        assert person.is_vaccinated == True
        assert person.infection == None
        print('Survived: True')
    else:
        assert person.is_alive is False
        assert person._id == 4
        assert person.is_vaccinated == False
        assert person.infection == virus
        print('Surived: False')

if __name__ == '__main__':
    virus = Virus('Ebola', .8, .3)

    test_vacc_person_instantiation()
    test_not_vacc_person_instantiation()
    test_sick_person_instantiation()
    test_did_survive_infection()
    