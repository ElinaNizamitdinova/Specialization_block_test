import Service.Note_service
import Model.note
import Model.menu
import Controller
import View.Menu_view
import csv
import random

class Controller:
    def start_app():
        input_from_user = ''
        while input_from_user != '5':
            View.Menu_view.Menu_view.show_menu()
            input_from_user = input().strip()
            if input_from_user == '1':
                Controller.show('all')
            if input_from_user == '2':
                Controller.add()            
            if input_from_user == '4':
                Controller.show('all')
                Controller.note_operation('del')
            if input_from_user == '3':
                Controller.show('all')
                Controller.note_operation('edit')
            if input_from_user == '5':
                print("Выход из программы")
                break

    id_number = random.randint(100,1000)

    def show(text):
        logic = True
        array = Controller.read_file()
        for notes in array:
            if text == 'all':
                logic = False
                print(Model.note.Note.to_string(notes))
            if text == 'id':
                logic = False
                print('ID: ' + Model.note.Note.get_id(notes))
            if text == 'date':
                logic = False
                if "date" in Model.note.Note.get_date(notes):
                    print(Model.note.Note.map_note(notes))
        if logic == True:
            print('Нет заметок')



    def add():
        note = Service.Note_service.Note_Service.create_note(Controller.id_number)
        Controller.id_number+=1
        array =Controller.read_file()
        for notes in array:
            if Model.note.Note.get_id(note) == Model.note.Note.get_id(notes):
                Model.note.Note.set_id(note)
        array.append(note)
        Controller.write_file(array, 'a')
        print('Запись сохранена')

    def write_file(array, mode):
        file = open("notes.csv", mode='w', encoding='utf-8')
        file.close()
        file = open("notes.csv", mode=mode, encoding='utf-8')
        for notes in array:
            file.write(Model.note.Note.to_string(notes))
            file.write('\n')
        file.close

    def read_file():
        try:
            array = []
            file = open("notes.csv", "r", encoding='utf-8')
            notes =file.read().strip().split("\n")
            for n in notes:
                split_n = n.split(';')
                note = Model.note.Note(split_n[0],split_n[1],split_n[2],split_n[3])
                array.append(note)
            return array
        except Exception:
            print("Запись не найдена")
            return array




    def note_operation(text):
        id = input('Введите id необходимой заметки: ')
        array = Controller.read_file()
        logic = True
        for notes in array:
            if id == Model.note.Note.get_id(notes):
                logic = False
                if text == 'edit':
                    note = Service.Note_service.Note_Service.create_note(Controller.id_number)
                    Model.note.Note.set_title(notes, note.get_title())
                    Model.note.Note.set_note_body(notes, note.get_note_body())
                    Model.note.Note.set_last_interaction_time(notes)
                    print('Заметка изменена.')
                if text == 'del':
                    array.remove(notes)
                    print('Заметка удалена.')
                if text == 'show':
                    print(Model.note.Note.map_note(notes))
        if logic == True:
            print('Заметка не найдена, возможно, вы ввели неверный id')
        Controller.write_file(array, 'a')
