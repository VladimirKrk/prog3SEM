# используется для сортировки
from operator import itemgetter


class Program:
    """Program"""

    def __init__(self, id, name, version, comp_id):
        self.id = id
        self.name = name # name of the program
        self.version = version #version of the program
        self.comp_id = comp_id # id of the computer


class Computer:
    """Computer"""

    def __init__(self, id, model):
        self.id = id #computer's id
        self.model = model #model of the computer

#
class ProgramComputer:
    """
    'Computer's programs' for many-to-many realisation
    """

    def __init__(self, comp_id, program_id):
        self.comp_id = comp_id #computer id
        self.program_id = program_id # program id


# Computer info
computers = [
    Computer(1, 'Macbook Pro M2'),
    Computer(2, 'Lenovo ThinkPad 1'),
    Computer(3, 'Asus E210'),

    Computer(11, 'Lenovo Yoga Slim 7x'),
    Computer(22, 'Macbook Pro M1'),
    Computer(33, 'Asus X510'),
]

# Programs
programs = [
    Program(1, 'Microsoft Ofiice', 2012, 1),
    Program(2, 'Adobe Photoshop', 2021, 2),
    Program(3, 'GoogleChrome', 2023, 3),
    Program(4, 'Visual Studio', 2022, 3),
    Program(5, 'Intellij IDEA', 2024, 1),
]

programs_computers = [
    ProgramComputer(1,1),
    ProgramComputer(1,5),
    ProgramComputer(2, 2),
    ProgramComputer(3, 3),
    ProgramComputer(3, 4),
    ProgramComputer(2, 1),
    ProgramComputer(11, 3),
    ProgramComputer(22, 3),
    ProgramComputer(33, 3),
]


def main():
    """Main Function"""

    # Соединение данных один-ко-многим
    one_to_many = [(p.name, p.version, c.model)
                   for c in computers
                   for p in programs
                   if p.comp_id == c.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.model, pc.comp_id, pc.program_id)
                         for c in computers
                         for pc in programs_computers
                         if c.id == pc.comp_id]

    many_to_many = [(p.name, p.version, comp_model)
                    for comp_model, comp_id,program_id in many_to_many_temp
                    for p in programs
                    if p.id == program_id]

    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)

    #Sorting the Computers by the most recent version
    print('\nЗадание А2')
    res_12_unsorted = []
    for c in computers:
        c_progs = list(filter(lambda i: i[2] == c.model, one_to_many))
        if len(c_progs) > 0:
            versions = [ver for _, ver, _ in c_progs]
            res_12_unsorted.append((c.model, max(versions)))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    #Sorting the computers by the "Pro" part inside of it
    print('\nЗадание А3')
    res_13 = {}
    for c in computers:
        if 'Pro' in c.model:
            c_progs = list(filter(lambda i: i[2] == c.model, many_to_many))
            prog_names = [x for x, _, _ in c_progs]
            res_13[c.model] = prog_names

    print(res_13)


if __name__ == '__main__':
    main()
