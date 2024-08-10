from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView
class NotebookApp(App):
    def build(self):
        self.title = "Simple Notebook"
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.text_input = TextInput(size_hint_y=0.8, font_size='20sp', multiline=True)
        layout.add_widget(self.text_input)
        button_layout = BoxLayout(size_hint_y=0.2, spacing=10)
        save_button = Button(text="Save", on_press=self.save_note)
        load_button = Button(text="Load", on_press=self.load_note)
        button_layout.add_widget(save_button)
        button_layout.add_widget(load_button)
        layout.add_widget(button_layout)
        return layout
    def save_note(self, instance):
        content = self.text_input.text
        if not content:
            self.show_popup("Error", "Note is empty!")
            return
        filechooser = FileChooserIconView()
        filechooser.bind(on_submit=self._save_file)
        popup = Popup(title="Save Note", content=filechooser, size_hint=(0.8, 0.8))
        popup.open()
    def _save_file(self, filechooser, selection, *args):
        if selection:
            filepath = selection[0]
            with open(filepath, 'w') as file:
                file.write(self.text_input.text)
            self.show_popup("Success", f"Note saved to {filepath}.")
    def load_note(self, instance):
        filechooser = FileChooserIconView()
        filechooser.bind(on_submit=self._load_file)
        popup = Popup(title="Load Note", content=filechooser, size_hint=(0.8, 0.8))
        popup.open()
    def _load_file(self, filechooser, selection, *args):
        if selection:
            filepath = selection[0]
            with open(filepath, 'r') as file:
                self.text_input.text = file.read()
            self.show_popup("Success", f"Note loaded from {filepath}.")
    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical', padding=10)
        content.add_widget(Label(text=message))
        close_button = Button(text="Close", size_hint_y=0.2)
        content.add_widget(close_button)
        
        popup = Popup(title=title, content=content, size_hint=(0.5, 0.5))
        close_button.bind(on_press=popup.dismiss)
        popup.open()
if __name__ == '__main__':
    NotebookApp().run()
