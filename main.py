from operator import itemgetter
import unittest

class Program:
    def __init__(self, id, name, version, comp_id):
        self.id = id
        self.name = name
        self.version = version
        self.comp_id = comp_id

class Computer:
    def __init__(self, id, model):
        self.id = id
        self.model = model

class ProgramComputer:
    def __init__(self, comp_id, program_id):
        self.comp_id = comp_id
        self.program_id = program_id

# Данные
computers = [
    Computer(1, 'Macbook Pro M2'),
    Computer(2, 'Lenovo ThinkPad 1'),
    Computer(3, 'Asus E210'),
    Computer(11, 'Lenovo Yoga Slim 7x'),
    Computer(22, 'Macbook Pro M1'),
    Computer(33, 'Asus X510'),
]

programs = [
    Program(1, 'Microsoft Ofiice', 2012, 1),
    Program(2, 'Adobe Photoshop', 2021, 2),
    Program(3, 'GoogleChrome', 2023, 3),
    Program(4, 'Visual Studio', 2022, 3),
    Program(5, 'Intellij IDEA', 2024, 1),
]

programs_computers = [
    ProgramComputer(1, 1),
    ProgramComputer(1, 5),
    ProgramComputer(2, 2),
    ProgramComputer(3, 3),
    ProgramComputer(3, 4),
    ProgramComputer(2, 1),
    ProgramComputer(11, 3),
    ProgramComputer(22, 3),
    ProgramComputer(33, 3),
]

def get_one_to_many(computers, programs):
    return [(p.name, p.version, c.model)
            for c in computers
            for p in programs
            if p.comp_id == c.id]

def get_many_to_many(computers, programs, programs_computers):
    many_to_many_temp = [(c.model, pc.comp_id, pc.program_id)
                         for c in computers
                         for pc in programs_computers
                         if c.id == pc.comp_id]

    return [(p.name, p.version, comp_model)
            for comp_model, comp_id, program_id in many_to_many_temp
            for p in programs
            if p.id == program_id]

def task_a1(one_to_many):
    return sorted(one_to_many, key=itemgetter(2))

def task_a2(one_to_many, computers):
    res = []
    for c in computers:
        c_progs = list(filter(lambda i: i[2] == c.model, one_to_many))
        if c_progs:
            versions = [ver for _, ver, _ in c_progs]
            res.append((c.model, max(versions)))

    return sorted(res, key=itemgetter(1), reverse=True)

def task_a3(many_to_many, computers):
    res = {}
    for c in computers:
        if 'Pro' in c.model:
            c_progs = list(filter(lambda i: i[2] == c.model, many_to_many))
            prog_names = [x for x, _, _ in c_progs]
            res[c.model] = prog_names

    return res

# Модульные тесты
class TestTasks(unittest.TestCase):
    def setUp(self):
        self.one_to_many = get_one_to_many(computers, programs)
        self.many_to_many = get_many_to_many(computers, programs, programs_computers)

    def test_task_a1(self):
        expected = [('GoogleChrome', 2023, 'Asus E210'),
 ('Visual Studio', 2022, 'Asus E210'),
 ('Adobe Photoshop', 2021, 'Lenovo ThinkPad 1'),
 ('Microsoft Ofiice', 2012, 'Macbook Pro M2'),
 ('Intellij IDEA', 2024, 'Macbook Pro M2')]
        result = task_a1(self.one_to_many)
        self.assertEqual(result[:5], expected)

    def test_task_a2(self):
        expected = [('Macbook Pro M2', 2024), ('Asus E210', 2023), ('Lenovo ThinkPad 1', 2021)]
        result = task_a2(self.one_to_many, computers)
        self.assertEqual(result[:3], expected)

    def test_task_a3(self):
        expected = {
            'Macbook Pro M2': ['Microsoft Ofiice', 'Intellij IDEA'],
            'Macbook Pro M1': ['GoogleChrome']
        }
        result = task_a3(self.many_to_many, computers)
        self.assertEqual({k: v for k, v in result.items() if 'Pro' in k}, expected)

if __name__ == '__main__':
    unittest.main()
