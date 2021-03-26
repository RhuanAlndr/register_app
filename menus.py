import PySimpleGUI as sg

def main_menu():
    sg.theme('DarkAmber')
    main_layout = [[sg.Button('Ver Pessoas', size=(30, 1), button_color=('black', 'gray'))],
                   [sg.Button('Cadastrar pessoas', size=(30, 1), button_color=('black', 'gray'))],
                   [sg.Button(f'{"Sair"}', size=(7, 1))]]

    return sg.Window('Menu Principal', main_layout)


def seepeoples_menu(f, data):
    sg.theme('DarkAmber')

    seepeoples_layout = [[sg.Text(f'{data[0][counter]}', size=(30, 1)),
                          sg.Button(f'{age}', size=(5, 1))] for counter, age in enumerate(data[1])]

    return sg.Window('Ver Pessoas Cadastradas', seepeoples_layout)


def register_menu():
    sg.theme('DarkAmber')

    register_layout = [[sg.Text('Nome', size=(5, 1)), sg.InputText()],
                       [sg.Text('Idade', size=(5, 1)), sg.InputText()],
                       [sg.Button('Salvar'), sg.Button('Sair')]]

    return sg.Window('Tela de Cadastro', register_layout)

