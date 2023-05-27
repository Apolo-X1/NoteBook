import NOTES.notes as notes

class action_notes:

    def create_note(self, user):

        title = input("Write the title of the note: ")
        text = input("write: \n")

        note = notes.note(user[0], title, text)
        save = note.save()

        if save[0] >= 1:
            print("\n note saved successfully!")

        else:
            print(f"\n note not saved :( {user[1]}")

    def show_note(self, user):
        print(f"\n{user[1]}, here are all your notes: \n")

        note = notes.note(user[0])

        all_notes = note.show()
        
        for note in all_notes:
            print("//////////////////////////////////////////")
            print(f"TITLE: {note[2]}\n")
            print(f"CONTENT: {note[3]}")
            print("//////////////////////////////////////////\n \n")


    def delete_note(self, user):
        
        print(f"Hola {user[1]}, you gonna delete 1 note!")

        note_delete = input("write the title here: ")

        note = notes.note(user[0], note_delete)
        delete = note.delete()

        if delete[0] >= 1:
            print(f"Note delete '{note.title}' ")

        else:
            print("the note could not be deleted!")