import tkinter as tk
import uuid
from abc import ABC, abstractmethod


class Model:
    uuid = []


class View(ABC):

    @abstractmethod
    def setup(self, controller):
        pass

    @abstractmethod
    def append_to_list(self, item):
        pass

    @abstractmethod
    def clear_list(self):
        pass

    @abstractmethod
    def start_main_loop(self):
        pass


class TkView(View):

    def setup(self, controller):
        """Setup the tkinter GUI."""
        # setup tkinter
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("UUIDGen")

        # create the gui
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=1)
        self.label = tk.Label(self.frame, text="Result:")
        self.label.pack()

        self.list = tk.Listbox(self.frame)
        self.list.pack(fill=tk.BOTH, expand=1)

        self.generate_uuid_button = tk.Button(self.frame, text="Generate UUID", command=controller.handle_click_generate_uuid)
        self.generate_uuid_button.pack()

        self.clear_button = tk.Button(self.frame, text="Clear list", command=controller.handle_click_clear_list)
        self.clear_button.pack()

    def append_to_list(self, item):
        """Append to the listbox field."""
        self.list.insert(tk.END, item)

    def clear_list(self):
        """Clear the listbox field."""
        self.list.delete(0, tk.END)

    def start_main_loop(self):
        """Start the loop of the application."""
        self.root.mainloop()


class Controller:

    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

    def start(self):
        """Start the application."""
        self.view.setup(self)
        self.view.start_main_loop()

    def handle_click_generate_uuid(self):
        """Generate a uuid and add it to the list."""
        self.model.uuid.append(uuid.uuid4())
        self.view.append_to_list(self.model.uuid[-1])

    def handle_click_clear_list(self):
        """Clear the uuid list and delete it from the list."""
        self.model.uuid = []
        self.view.clear_list()


if __name__ == '__main__':
    m = Model()
    v = TkView()
    c = Controller(model=m, view=v)

    c.start()


