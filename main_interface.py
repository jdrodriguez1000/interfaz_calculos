from tkinter import *



class interface():
    
    def __init__(self):
        
        root = Tk()
        
        frm_information = Frame(root, padx=10, pady=10)
        frm_information.pack()
        
        lbl_first_number = Label(frm_information, text='Enter first number: ', pady=10)
        lbl_first_number.grid(row=0, column=0, sticky='e')
        lbl_first_number.config(font=('verdana',10))
        
        txt_entry_1 = StringVar()
        ent_first_number = Entry(frm_information, textvariable=txt_entry_1)
        ent_first_number.grid(row=0, column=1)
        ent_first_number.config(font=('verdana',12), justify='center')
        
        lbl_second_number = Label(frm_information, text='Enter second number: ', pady=10)
        lbl_second_number.grid(row=1, column=0, sticky='e')
        lbl_second_number.config(font=('verdana',10))
        
        txt_entry_2 = StringVar()
        ent_second_number = Entry(frm_information, textvariable=txt_entry_2)
        ent_second_number.grid(row=1, column=1)
        ent_second_number.config(font=('verdana',12), justify='center')
        
        lbl_result = Label(frm_information, text='The result is: ')
        lbl_result.grid(row=2, column=0, sticky='e')
        lbl_result.config(font=('verdana',10))
        
        txt_result = StringVar()
        ent_result = Entry(frm_information, textvariable=txt_result, state='disabled')
        ent_result.grid(row=2, column=1)
        ent_result.config(font=('verdana',12), justify='center')
        
        frm_button_add = Frame(root, padx=10, pady=10)
        frm_button_add.pack()
        
        btn_add = Button(frm_button_add, text="Addition", command=lambda:self.add_operation(txt_entry_1.get(), txt_entry_2.get(), txt_result))
        btn_add.grid(row=4, column=0)
        btn_add.config(font=('verdana', 12), justify='center', width= 15)
        
        btn_subt = Button(frm_button_add, text="Subtraction", command=lambda:self.subt_operation(txt_entry_1.get(), txt_entry_2.get(), txt_result))
        btn_subt.grid(row=4, column=2)
        btn_subt.config(font=('verdana', 12), justify='center', width= 15)
                
        root.mainloop()
        

    
    def add_operation(self, num_1, num_2, entry_1):
        try:
            number_1 = float(num_1)
            number_2 = float(num_2)
            result_add = number_1 + number_2
            return entry_1.set(result_add)
        except:
            return entry_1.set('Function not valid.')
        
    def subt_operation(self, num_1, num_2, entry_1):
        try:
            number_1 = float(num_1)
            number_2 = float(num_2)
            result_subt = number_1 - number_2
            return entry_1.set(result_subt)
        except:
            return entry_1.set('Function not valid.')

        
        
        