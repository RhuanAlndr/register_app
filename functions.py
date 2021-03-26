import PySimpleGUI as sg

def seepeoples(f):
    name = list()
    age = list()
    data = name, age

    # open the file
    try:
        file = open(f, 'rt')
    except:
        file = open(f, 'wt+')
        file.close()
        file = open(f, 'rt')

    # make the data
    try:
        for reader in file:
            new_reader = reader.replace('\n', '').split(';')
            name.append(new_reader[0])
            age.append(new_reader[1])
    except:
        return "don't make the people"

    # verifying if data exists
    if not name:
        data = (['Not data', ''], [''])

    file.close()
    return data


def new_register(name, age, file):
    try:
        f = open(file, 'at')

        f.write(name.title() + ';' + age + '\n')
        f.close()
    except:
        print('Algo deu errado!')


def pop_up(m):
    sg.theme('DarkAmber')

    sg.popup_quick_message(m, location=(500, 480))
