from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #enter name label r0 c0 [1]
        Label(self,
              text="Enter a name:",
              ).grid(row=0, column=0, sticky="w")

        #student entry r0 c1 [2]
        self.student_entry = Entry(self, width=14)
        self.student_entry.grid(row=0, column=1, sticky="w")

        #add button r1 c0-2(centered) [3]
        self.add_button = Button(self, text="Add", command=self.add)
        self.add_button.grid(row=1, column=0, columnspan = 2)

        #horizontal separator r0 c0-2 [4]
        ttk.Separator(self,
                      orient='horizontal'
                      ).grid(row=2, column=0, columnspan=3, sticky="ew", pady=7)

        #list of students label r3 c0 [5]
        Label(self,
              text="List of students:"
              ).grid(row=3, column=0, sticky="w")

        #listbox? r4-5 c0-1 [6]
        #separator r4 c2 [7]
        self.student_box = Listbox(self)
        self.scrollbar = Scrollbar(self.student_box, orient=VERTICAL)
        self.student_box.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.student_box.yview)

        self.student_box.grid(row=4, rowspan=2,
                              column=0, columnspan=2, sticky=N+E+S+W)
        self.student_box.columnconfigure(0, weight=1)
        self.scrollbar.grid(row=4, column=2, sticky=N+S)

        self.student_box.bind("<<ListboxSelect>>", self.sel_student)

        #student selected label r6 c0 [8]
        Label(self,
              text="Student selected:"
              ).grid(row=6, column=0, sticky="w")

        #student actually selected r6 c1 [9]
        self.student_selected = Label(self, text="<no one>")
        self.student_selected.grid(row=6, column=1, sticky="w")

        #remove button r7 c0-2(centered) [10]
        self.remove_button = Button(self, text="Remove", command=self.remove)
        self.remove_button.grid(row=7, column=0, columnspan=2)

        #horizontal separator r8 c0-2 [11]
        ttk.Separator(self,
                      orient='horizontal'
                      ).grid(row=8, column=0, columnspan=3, sticky="ew", pady=7)

        #random student label r9 c0 [12]
        Label(self,
              text="Random student:"
              ).grid(row=9, column=0, sticky="w")

        #generated student r9 c1 [13]
        self.gen_student = Label(self, text="<no one>")
        self.gen_student.grid(row=9, column=1, sticky="w")

        #generate button r10 c0-2 [14]
        self.gen_button = Button(self, text="Generate!", command=self.generate)
        self.gen_button.grid(row=10, column=0, columnspan=2)

        #total of 14 widgets.

    def add(self):
        contents = self.student_entry.get()
        if contents.strip():
            self.student_box.insert(END, contents)
            self.student_entry.delete(0, END)
        else:
            messagebox.showerror(
                "Error!",
                "Cannot enter a blank student."
                )
            return

    def remove(self):
        try:
            selection = self.student_box.curselection()
            self.student_box.delete(selection[0])
            self.student_selected["text"] = "<no one>"
        except IndexError:
            if self.student_box.size() == 0:        
                messagebox.showerror(
                    "Error!",
                    "There is nothing else to delete!"
                )
            else:
                messagebox.showerror(
                    "Error!",
                    "You have not selected anything to delete."
                )
            

    def generate(self):
        temp_list = list(self.student_box.get(0, END))

        if len(temp_list) not in (0, 1):
            choice = random.choice(temp_list)
            self.gen_student["text"] = choice
        else:
            if len(temp_list) == 0:
                messagebox.showerror(
                    "Error!",
                    "There are no students to pick from!"
                )
            elif len(temp_list) == 1:
                messagebox.showerror(
                    "Error!",
                    "You have only one student to pick from!"
                )

    def sel_student(self, event):
        try:
            widget = event.widget
            selection = widget.curselection()
            value = widget.get(selection[0])
            self.student_selected["text"] = value
        except:
            self.student_selected["text"] = "<no one>"

root = Tk()

w = 192 # width for the Tk root
h = 250 # height for the Tk root

ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2) - 100

root.title("RSG")
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(width=False, height=False)

app = Application(root)

root.mainloop()
