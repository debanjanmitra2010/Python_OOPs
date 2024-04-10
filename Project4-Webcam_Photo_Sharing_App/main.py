import time

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
import webbrowser

# Use this import when you implement Filesharer Class
# from filesharer import FileSharer

Builder.load_file('frontend.kv')


class CameraScreen(Screen):

    def start(self):
        """Starts camera and changes Button text"""
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera.texture

    def stop(self):
        """Stops camera and changes Button text"""
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        """Creates a filename with the current time stamp and captures
          and saves a photo image under that filename"""
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filepath = f"files/{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):

    def create_link(self):
        """ Accesses the photo filepath, uploads it to the web,
        and insert the link in the Label widget"""
        # Implement this when you generate an API key on FileShare
        # file_path = App.get_running_app().root.ids.camera_screen.filepath
        # filesharer = FileSharer(filepath=file_path)
        # url = filesharer.share()
        # self.ids.link.text = url
        self.ids.link.text = "This function is disabled, since File Share isn't setup."

    def copy_link(self):
        try:
            Clipboard.copy(self.filepath)
        except:
            self.ids.link.text = "Create a Link First"

    def open_link(self):
        try:
            webbrowser.open(self.filepath)
        except:
            self.ids.link.text = "Create a Link First"


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
