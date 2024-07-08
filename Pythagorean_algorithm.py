import math
import customtkinter

class PythagorasApp(customtkinter.CTk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1000x600")
        customtkinter.set_appearance_mode("Dark")
        
        self.frame = customtkinter.CTkFrame(master=self, fg_color='#001861', border_color='#3E454B', border_width=4, width=500, height=300, corner_radius=32)
        self.frame.pack(expand=True)
        self.frame.place(relx=0.5, rely=0.6, anchor='center')

        self.button = customtkinter.CTkButton(master=self.frame, text='Click Here', corner_radius=32, fg_color="#333333",
                                 hover_color='#555555', 
                                 border_color="#252525", border_width=4, command=self.on_button_click)
        self.button.place(relx=0.5, rely=0.9, anchor='center')
        
        self.entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Value or Type 'None'", width= 200, text_color='grey')
        self.entry1.place(relx=0.55, rely=0.2, anchor='center')
        self.label_angle_a = customtkinter.CTkLabel(master=self.frame,  text = 'Angle A value: ', font=('Times New Roman', 20))        
        self.label_angle_a.place(relx=0.2,rely=0.2, anchor='center')
        
        self.label_angle_b = customtkinter.CTkLabel(master=self.frame,  text = 'Angle B value: ', font=('Times New Roman', 20))        
        self.label_angle_b.place(relx=0.2,rely=0.4, anchor='center')
        self.entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Value or Type 'None'", width= 200, text_color='grey')
        self.entry2.place(relx=0.55, rely=0.4, anchor='center')
        
        self.label_hypotenuse = customtkinter.CTkLabel(master=self.frame,  text = 'Value of Hypotenuse: ', font=('Times New Roman', 20))        
        self.label_hypotenuse.place(relx=0.2,rely=0.6, anchor='center')
        self.entry3 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Value or Type 'None' ", width= 200, text_color='grey')
        self.entry3.place(relx=0.59, rely=0.6, anchor='center')
        
        self.label = customtkinter.CTkLabel(master=self, text="Pythagoras Problem Solver",
                               font=('Times New Roman', 30), text_color='white')
        self.label.place(relx=0.5, rely=0.1, anchor='center') 
        
        self.label_description = customtkinter.CTkLabel(master=self,text='What is the Pythagoras Theorem in Math?\n   The Pythagoras theorem states that in a right-angled triangle, the square of the hypotenuse\n is equal to the sum of the squares of the other two sides. Meaning that the hypotenuse will be the largest angle.',
                                font=('Arial', 17), text_color='white')
        self.label_description.place(relx=0.5, rely=0.2, anchor='center')
        
        self.toplevel_window = None
        
    def on_button_click(self):
        # Get user inputs from entry fields
        user_AngleAInput = self.entry1.get()
        user_AngleBInput = self.entry2.get()
        user_HypotenuseInput = self.entry3.get()

        # Check conditions and perform calculations
        try:
            if user_AngleAInput != '' and user_AngleAInput != 'None':
                user_AngleAInput = float(user_AngleAInput)
            if user_AngleBInput != '' and user_AngleBInput != 'None':
                user_AngleBInput = float(user_AngleBInput)
            if user_HypotenuseInput != '' and user_HypotenuseInput != 'None':
                user_HypotenuseInput = float(user_HypotenuseInput)

            if user_AngleAInput == 'None':
                user_AngleBInput = float(user_AngleBInput)
                user_HypotenuseInput = float(user_HypotenuseInput)
                user_AngleAInput = math.degrees(math.acos(user_AngleBInput / user_HypotenuseInput))
            elif user_AngleBInput == 'None':
                user_AngleAInput = float(user_AngleAInput)
                user_HypotenuseInput = float(user_HypotenuseInput)
                user_AngleBInput = math.degrees(math.acos(user_AngleAInput / user_HypotenuseInput))
            elif user_HypotenuseInput == 'None':
                user_AngleAInput = float(user_AngleAInput)
                user_AngleBInput = float(user_AngleBInput)
                user_HypotenuseInput = math.sqrt(user_AngleAInput**2 + user_AngleBInput**2)
        
        except ValueError:
            print("Error: Please enter valid numeric values.")
    
        print('Angle A:', user_AngleAInput)
        print('Angle B:', user_AngleBInput)
        print('Hypotenuse:', user_HypotenuseInput)
    
        # Create a new frame to display results
        self.frame_result = customtkinter.CTkFrame(master=self, fg_color='#8D6F3A', border_color='#FFCC70', width=1300, height=450)
        self.frame_result.pack(expand=True)
        self.frame_result.place(relx=0.89, rely=0.6, anchor='center')
    
        # Display the results
        label_angle_a_result = customtkinter.CTkLabel(master=self.frame_result, text=f"Angle A: {user_AngleAInput:.1f}", font=('Arial', 14))
        label_angle_a_result.pack()
        label_angle_b_result = customtkinter.CTkLabel(master=self.frame_result, text=f"Angle B: {user_AngleBInput:.1f}", font=('Arial', 14))
        label_angle_b_result.pack()
        label_hypotenuse_result = customtkinter.CTkLabel(master=self.frame_result, text=f"Hypotenuse: {user_HypotenuseInput:.2f}", font=('Arial', 14))
        label_hypotenuse_result.pack()
        
if __name__ == "__main__":
    app = PythagorasApp()
    app.mainloop()
