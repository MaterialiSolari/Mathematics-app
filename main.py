from tkinter import *
import customtkinter
from customtkinter import CTk, CTkLabel, CTkEntry, CTkCheckBox, CTkFont
import linear_functions
import Pythagorean_algorithm 
import quadraticAlgorithm

class MainApp(customtkinter.CTk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1000x600")
        customtkinter.set_appearance_mode("Dark")
        self.my_font = CTkFont(family="Times new Roman", slant="italic", size=36)
        self.entry = CTkEntry(master=self, placeholder_text="Start typing...", width=350, text_color='white')
        self.entry.place(relx=0.5, rely=0.5, anchor='center')
        self.label = customtkinter.CTkLabel(master=self, text="Mathematics\nby JG", font=self.my_font)
        self.label.pack(pady=40)
        self.label.place(rely=0.2, relx=0.5, anchor='center')
        self.frame = customtkinter.CTkFrame(master=self, fg_color='#001a33', border_color='#03396c', width=350, height=190, border_width=4, corner_radius=20)
        self.frame.pack(expand=True)
        self.frame.place(relx=0.5, rely=0.7, anchor='center')
        self.checkbox = CTkCheckBox(master=self.frame, text="Linear Functions", fg_color="#000000", command=self.checkBox_click)
        self.checkbox.place(relx=0.25, rely=0.2, anchor="center")
        self.checkBox2 = CTkCheckBox(master=self.frame, text='Pythagoras(A^2 + B^2=C^2)', fg_color="#000000", command=self.checkBox_click)
        self.checkBox2.place(relx=0.335, rely=0.4, anchor="center")
        self.button = customtkinter.CTkButton(master=self, text='Continue', corner_radius=32, fg_color="#333333",
                                 hover_color='#555555', 
                                 border_color="#252525", border_width=4, command= self.on_button_click)
        self.button.place(relx=0.5, rely=0.8, anchor='center')

        self.checkbox_names = ["Linear Functions", 'Pythagoras(A^2 + B^2=C^2)']
        self.checkBox3 = CTkCheckBox(master=self.frame, text='Quadratic Equation Solver', fg_color="#000000", command=self.checkBox_click)
        self.checkBox3.place(relx=0.325, rely=0.59, anchor="center")

    def checkBox_click(self):
        selected_checkboxes = []

        if self.checkbox.get():
            selected_checkboxes.append("Linear Functions")

        if self.checkBox2.get():
            selected_checkboxes.append('Pythagoras(A^2 + B^2=C^2)')

        if self.checkBox3.get():
            selected_checkboxes.append('Quadratic Equation Solver')

        if "Linear Functions" in selected_checkboxes:
            label_text = 'Linear Function'
            self.entry.delete(0, END)
            self.entry.insert(0, label_text)
        
        elif "Pythagoras(A^2 + B^2=C^2)" in selected_checkboxes:
            label_text = 'Pythagoras'
            self.entry.delete(0, END)
            self.entry.insert(0, label_text)
            self.entry.configure(foreground='white')
        
        elif "Quadratic Equation Solver" in selected_checkboxes:
            label_text = "Quadratic Equation Solver"
            self.entry.delete(0, END)
            self.entry.insert(0, label_text)     

            
    def on_button_click(self):
        entry_box = self.entry.get()
        if entry_box == "Linear Function":
            linear_functions()
        elif entry_box == "Pythagoras":
            Pythagorean_algorithm()
    
    def on_button_click(self):
        entry_box = self.entry.get()
        if entry_box == "Linear Function":
            linear_functions_app = linear_functions.App()
            linear_functions_app.mainloop()
        elif entry_box == "Pythagoras":
            pythagoras_app = Pythagorean_algorithm.PythagorasApp()
            pythagoras_app.mainloop()
        elif entry_box == "Quadratic Equation Solver":
            quadratic_app = quadraticAlgorithm.quadraticAlgorithmApp()
            quadratic_app.mainloop()

                
if __name__ == "__main__":
    main_app = MainApp()
    main_app.mainloop()
    
    # This block will only execute after main_app is closed
    if main_app.toplevel_window:  # If PythagorasApp was created
        main_app.toplevel_window.destroy()
        

