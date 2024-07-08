import math
import customtkinter
from customtkinter import CTkButton

def quadraticFunctionSolver(equation):
    index_of_xsquared = equation.find("x^2")
    if index_of_xsquared != -1:
        partA = equation[:index_of_xsquared].strip()
        if partA == '':
            partA = '1'
    else:
        partA = '1'

    equation = equation[index_of_xsquared + len("x^2"):]

    index_of_x = equation.find("x")
    partB_str = equation[:index_of_x]

    equation = equation[index_of_x + len("x"):]
    partC = equation.strip()

    partA = int(partA)
    partC = int(partC)

    if partB_str.startswith('-'):
        partB = -int(partB_str.strip('-'))
    else:
        partB = int(partB_str.strip())

    discriminant = partB**2 - 4 * partA * partC

    if discriminant > 0:
        root1 = (-partB + math.sqrt(discriminant)) / (2 * partA)
        root2 = (-partB - math.sqrt(discriminant)) / (2 * partA)
        return f"Root 1: {root1}\n\nRoot 2: {root2}"
    elif discriminant == 0:
        root = -partB / (2 * partA)
        return f"Root: {root}"
    else:
        real_part = -partB / (2 * partA)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * partA)
        return f"Roots: {real_part} + {imaginary_part}i, {real_part} - {imaginary_part}i"


class quadraticAlgorithmApp(customtkinter.CTk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1000x600")
        customtkinter.set_appearance_mode("Dark")
        self.label = customtkinter.CTkLabel(master=self, text="Quadratic Equation Solver",
                               font=('Times New Roman', 30), text_color='white')
        self.label.place(relx=0.5, rely=0.1, anchor='center')
        self.label2 = customtkinter.CTkLabel(master=self, text="A quadratic equation is a polynomial equation of degree 2, typically in the form ax^2 + bx + c = 0."
                                             , font=('Times New Roman', 23), text_color='white')
        self.label2.place(relx=0.5,rely=0.25, anchor='center')
        
        self.frame = customtkinter.CTkFrame(master=self, fg_color='#787276', border_color='#3E454B', border_width=5, width=500, height=290, corner_radius=32)
        self.frame.pack(expand=True)
        self.frame.place(relx=0.5, rely=0.6, anchor='center')
        
        self.frameLabel1 = customtkinter.CTkLabel(master=self.frame, text="Provide the quadratic equation", font=('Times New Roman', 20), text_color='white')
        self.frameLabel1.place(relx=0.5,rely=0.2, anchor='center')
        self.entry = customtkinter.CTkEntry(master=self.frame, placeholder_text='Type here',width=250, text_color='grey', border_width=4)
        self.entry.place(relx=0.5, rely=0.45, anchor='center')        
        
        self.button = CTkButton(master=self.frame, text='Continue', corner_radius=32, fg_color="#333333",
                                 hover_color='#555555', 
                                 border_color="#252525", border_width=4, command=self.on_button_click)
        self.button.place(relx=0.5, rely=0.7, anchor='center')  

    def on_button_click(self):
        equation = self.entry.get()
        result = quadraticFunctionSolver(equation)
        self.button.destroy()
        self.frameLabel1.configure(text="Result:", font= ('Arial', 20))
        self.frameLabel1.place(relx=0.5,rely=0.2)
        self.entry.destroy()
        self.resultLabel = customtkinter.CTkLabel(master=self.frame, text=f'{result}', font=('Arial', 20))
        self.resultLabel.place(rely=0.5,relx=0.5, anchor='center')
        print(result)
        


if __name__ == "__main__":
    app = quadraticAlgorithmApp()
    app.mainloop()
