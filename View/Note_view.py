import Task1.Model.note

class Note_view:
    def show_note(new_note):
         string_note =Task1.Model.note.Note.to_string(new_note)
         print("Запись содержит следующие данные: ",string_note)