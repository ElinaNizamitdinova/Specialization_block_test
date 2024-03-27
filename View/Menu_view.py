import Model.menu

class Menu_view:
    def show_menu():
        menu =Model.menu.Menu.get_menu()
        numer = 1
        for i in menu:
            if i =='Заметки:':
                print(i)
            else:
                print(numer,i)
                numer+=1