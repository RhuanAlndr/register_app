import menus
import functions
import PySimpleGUI as sg

# database
file = 'database.txt'

while True:
    # first window and main menu
    while True:
        window = menus.main_menu()
        event, values = window.read()
        if event or event == sg.WIN_CLOSED:
            break

    if event == sg.WIN_CLOSED or event == 'Sair':
        window.close()
        break
    else:
        window.close()
        del window

    # second window
    if event == 'Ver Pessoas':
        peoples = functions.seepeoples(file)
        window = menus.seepeoples_menu(file, peoples)
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                window.close()
                del window
                break
    
    # third window
    elif event == 'Cadastrar pessoas':
        window = menus.register_menu()
        while True:
            event, value = window.read()
            if event in (sg.WINDOW_CLOSED, 'Sair'):
                window.close()
                break
            elif event == 'Salvar' and not value[0].isalpha() or value[0] == '':
                functions.pop_up('ERRO! Favor digitar letras em nome!')
            elif event == 'Salvar' and not value[1].isnumeric() or value[1] == '':
                functions.pop_up('ERRO! Favor digitar número inteiro válido!')
            else:
                functions.new_register(value[0], value[1], file)
                functions.pop_up('Deu certo!')
