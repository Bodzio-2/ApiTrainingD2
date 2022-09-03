from tkinter import *
from tkinter import ttk
import tkinter.font as font
from PIL import ImageTk, Image
import d2Api as dest

db = r"world_sql_content_eab836f0f0bd68f7ac09055c2e38fe14.sqlite3"

class App(Tk):
    
    
    def __init__(self):
        super().__init__()

        self.title('Simple Destiny Item Manager')

        window_width = 480
        window_height = 200

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)

        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.resizable(False, False)

        #configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        #membershipType

        username_label = ttk.Label(self, text="Membership Type:")
        username_label.grid(column=0, row=0, sticky=W, padx=20, pady=20)
        username_label.config(font=('Arial', 15, font.BOLD))

        username_entry = ttk.Entry(self)
        username_entry.grid(column=1, row=0, sticky=E, padx=20, pady=20)
        username_entry.config(font=('Arial', 15, font.BOLD))

        #membershipID

        password_label = ttk.Label(self, text="Membership ID:")
        password_label.grid(column=0, row=1, sticky=W, padx=20, pady=20)
        password_label.config(font=('Arial', 15, font.BOLD))

        password_entry = ttk.Entry(self)
        password_entry.grid(column=1, row=1, sticky=E, padx=20, pady=20)
        password_entry.config(font=('Arial', 15, font.BOLD))

        #login button

        login_button = Button(self, text="Load")
        login_button.grid(column=1, row=3, sticky=E, padx=20, pady=5)
        login_button['font'] = font.Font(family='Arial', size=15, weight='bold')
        login_button['command'] = lambda: showEquipment(str(username_entry.get()), str(password_entry.get()), self)

def showEquipment(memberType, memberId, app):
        equipmentImgs = dest.printEquippedItems(memberType, memberId, db)
        result = eqInfo(equipmentImgs)
        result.mainloop()


class eqInfo(Toplevel):
    def __init__(self, imgPaths):
        super().__init__()

        self.title('Simple Destiny Item Manager')

        window_width = 480
        window_height = 500

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)

        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.resizable(False, False)

        gridPositionsX =[0, 0, 0, 3, 3, 3, 3, 3, 0, 1, 2, 0]
        gridPositionsY = [0, 1, 2, 0, 1, 2, 3, 4, 3, 4, 4, 4]

        imgs = []
        labels = [Label]

        for x in range(12):
            imgs.append(ImageTk.PhotoImage(Image.open(imgPaths[x])))
            label = Label(master=self, image=imgs[-1])
            label.grid(row=gridPositionsY[x], column=gridPositionsX[x])
            label.image = imgs[-1]
            labels.append(label)
            
            
            
            
            
        



if __name__ == "__main__":
    app=App()
    app.mainloop()



