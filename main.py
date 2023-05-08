import tkinter as tk

from nvwec import nftcon


class ImageValidator:

    def __init__(self, master):
        self.master = master
        self.result = None
        self.master.title("Testing Software")
        self.master.geometry("300x200")

        # set the window attributes
        self.master.attributes('-toolwindow', True)

        self.master.resizable(False, False)  # disable resizing

        # center the window on the screen
        self.master.eval('tk::PlaceWindow %s center' % self.master.winfo_toplevel())

        self.sw_label = tk.Label(self.master, text="Please click Validate Me button for validation",
                                 font=("Times New Roman", 12))
        self.sw_label.pack(anchor='nw', padx=10, pady=10)

        self.sw_button = tk.Button(self.master, text="Validate Me...", font=("Times New Roman", 12),
                                   command=self.validate_image)
        self.sw_button.pack(side='bottom', anchor='se', padx=10, pady=10)

    def validate_image(self):
        self.result = nftcon.nvwec(self)

        if self.result == '1':
            self.show_success()
        else:
            self.show_error()

    def show_success(self):
        # create a new window to show the success message
        success_window = tk.Toplevel(self.master)
        success_window.title("Success")

        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width // 2) - (400 // 2)
        y = (screen_height // 2) - (200 // 2)

        success_window.geometry(f"400x200+{x}+{y}")

        success_label = tk.Label(success_window, text="Your NFT License validation is Successful! You can use our "
                                                      "software now on...!", font=("Times New Roman", 12),
                                 wraplength=380)
        success_label.pack()

    def show_error(self):
        # create a new window to show the error message
        error_window = tk.Toplevel(self.master)
        error_window.title("Error")

        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width // 2) - (400 // 2)
        y = (screen_height // 2) - (200 // 2)

        # set the size and location of the error window
        error_window.geometry(f"400x200+{x}+{y}")

        error_label = tk.Label(error_window, text="Sorry! You owned wrong NFT", font=("Times New Roman", 12))
        error_label.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageValidator(root)
    root.mainloop()
