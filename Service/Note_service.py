import Model.note

class Note_Service:
    def create_note(numder_id):
        title = input('Введите название заметки: ')
        note_body = input('Введите текст заметки: ')
        return Model.note.Note(numder_id,title, note_body)
