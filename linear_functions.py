from matplotlib import pyplot as plt
import numpy as np
import customtkinter
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkFrame



def linearFunctionAlgorithm(user_firstInput, user_2ndInput):
    x_str, y_str = user_firstInput.split(',')
    x_value = float(x_str)
    y_value = float(y_str)
    x_str2, y_str2 = user_2ndInput.split(',')
    x_value2 = float(x_str2)
    y_value2 = float(y_str2)
    
    slopeFormula = (y_value2 - y_value) / (x_value2 - x_value)
    b = y_value - slopeFormula * x_value
    
    if b >= 0:
        equation = f'y = {slopeFormula:.3f}x + {b:.3f}'
    else:
        equation = f'y = {slopeFormula:.3f}x - {abs(b):.3f}'
    

    
    x_values = np.linspace(-50, 50, 1000)
    y_values = slopeFormula * x_values + b
    fig, ax = plt.subplots(figsize=(8, 6))       
    plt.plot(x_values, y_values, label=equation, color='g')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of the Linear Equation')
    plt.grid(True)
    plt.legend()   
    plt.show()
    return equation


    
class App(customtkinter.CTk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1000x600")
        customtkinter.set_appearance_mode("Dark")

        self.frame = customtkinter.CTkFrame(master=self, fg_color='#787276', border_color='#3E454B', border_width=4, width=450, height=250, corner_radius=32)
        self.frame.pack(expand=True)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        self.button = customtkinter.CTkButton(master=self.frame, text='Click Here', corner_radius=32, fg_color="#333333",
                                 hover_color='#555555', 
                                 border_color="#252525", border_width=4, command=self.on_button_click)
        self.button.place(relx=0.5, rely=0.65, anchor='center')
        
        self.direction1 = customtkinter.CTkLabel(master=self.frame, text="The Set of points should be like this: 2,4.",
                                     font=('Times New Roman', 20), text_color='white')
        self.direction1.place(relx=0.5, rely=0.3, anchor='center')
        
        self.entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Start typing...", width=350, text_color='grey')
        self.entry1.place(relx=0.5, rely=0.5, anchor='center')
        
        self.label = customtkinter.CTkLabel(master=self, text="Linear Function Problem Solver",
                               font=('Times New Roman', 30), text_color='white')
        self.label.place(relx=0.5, rely=0.1, anchor='center') 
        
        self.label2 = customtkinter.CTkLabel(master=self,
                                text='In order to create a linear equation, first, we need to find the slope. Provide the first set of points spaced by a comma.',
                                font=('Arial', 17), text_color='white')
        self.label2.place(relx=0.5, rely=0.2, anchor='center')
        
        self.toplevel_window = None

    def on_button_click(self):
        self.user_firstInput = self.entry1.get()
        print('1st Input:', self.user_firstInput)
        self.entry1.destroy()
        self.entry2 = customtkinter.CTkEntry(master=self, placeholder_text="Start typing...", width=350, text_color='grey')
        self.entry2.place(relx=0.5, rely=0.5, anchor='center')
        self.button.configure(text='Continue', corner_radius=32, command=self.on_second_button_click)

    def on_second_button_click(self):
        self.user_2ndInput = self.entry2.get()
        print('2nd', self.user_2ndInput)

        self.entry2.destroy()
        self.toplevel_window = None
        self.direction1.destroy()
        self.label5 = customtkinter.CTkLabel(master=self.frame, text="Click Continue to see the results",
                                     font=('Times new roman', 17), text_color='white', bg_color='#787276')
        self.label5.place(relx=0.5, rely=0.3, anchor='center')
        self.button.place(relx=0.5, rely=0.5)
        self.button.configure(command=self.open_toplevel)

    def open_toplevel(self):   
        equation_result = linearFunctionAlgorithm(self.user_firstInput, self.user_2ndInput)
        # Now you can use equation_result as needed
        print("Equation Result:", equation_result)
if __name__ == "__main__":
    app = App()
    app.mainloop()


