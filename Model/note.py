from datetime import datetime

class Note:
    def __init__(self,id, title, note_body, last_interaction_time = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title =title
        self.note_body = note_body
        self.last_interaction_time = last_interaction_time



    def set_id(note):
        note.id = id



    def set_title(note, title):
        note.title = title



    def set_note_body(note, note_body):
        note.note_body = note_body



    def set_last_interaction_time(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))


    def get_id(note):
        return note.id
    


    def get_title(note):
        return note.title
    


    def get_note_body(note):
        return note.note_body
    


    def get_last_interaction_time(note):
        return note.last_interaction_time
    

    def to_string(note):
        return str(note.id) + ';' + str(note.title) + ';' + str(note.note_body) + ';' + str(note.last_interaction_time) + "."
    


    def map_note(note):
        return '\nID: ' + str(note.id) + '\n' + 'Название: ' + str(note.title) + '\n' + 'Описание: ' +  str(note.note_body) + '\n' + 'Дата публикации: ' + str(note.last_interaction_time)