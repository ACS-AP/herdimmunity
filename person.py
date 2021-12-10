import random
from virus import Virus



class Person(object):

    def __init__(self, _id, is_vaccinated, virus=None):
 
        self._id = _id  
        self.is_alive = True  
        self.natural_immunity = False  
        self.is_vaccinated = is_vaccinated  
        self.virus = virus  

    def did_survive_infection(self):
        if self.virus: 
            random_mortality = random.random()
            if random_mortality < self.virus.mortality_rate:
                print(f'{self._id} died')
                self.is_alive = False
                return False
            else:
                self.natural_immunity = True
                self.virus = None
                return True
        


def test_vacc_person_instantiation():
    person = Person(1, True)
    assert person._id == 1
    assert person.is_alive is True
    assert person.is_vaccinated is True
    assert person.virus is None

def test_not_vacc_person_instantiation():
    person = Person(2, False)
    assert person._id == 2
    assert person.is_alive is True
    assert person.is_vaccinated is False
    assert person.virus is None

def test_sick_person_instantiation():
    virus = Virus("Dysentery", 0.7, 0.2)
    person = Person(3, False, virus)
    assert person._id == 3
    assert person.is_alive is True
    assert person.is_vaccinated is False
    assert person.virus is virus

def test_did_survive_infection():
    virus = Virus("Dysentery", 0.7, 0.2)
    person = Person(4, False, virus) 
    assert person._id == 4
    assert person.is_alive is True
    assert person.is_vaccinated is False
    assert person.virus is virus

    survived = person.did_survive_infection()
    
    if survived:
        assert person.is_alive is True
        assert person.natural_immunity is True

    else:
        assert person.is_alive is False
    

# print(person.did_survive_infection())
# print(person.did_survive_infection())
# print(person.did_survive_infection())



# print(test_vacc_person_instantiation())
# print(test_not_vacc_person_instantiation())
# print(test_sick_person_instantiation())

# print(f'test: {test_sick_person_instantiation()}')