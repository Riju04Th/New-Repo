from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
class MyApp(App):
    def build(self):
        self.title = "Kivy Simple App"
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Hello, Kivy!", font_size='40sp')
        btn = Button(text="Click Me", font_size='30sp')
        # Bind the button's on_press event to the update_label method
        btn.bind(on_press=self.update_label)
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout
    def update_label(self, instance):
        self.label.text = "Button Clicked!"
if __name__ == '__main__':
    MyApp().run()
# This is a simple Kivy app that creates a vertical layout with a label and a button. When the button is clicked, the label changes to "Button Clicked!".
