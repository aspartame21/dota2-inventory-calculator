from tkinter import *
from steamapi import Inventory
from threading import Thread
from time import time

def submit():
        global start_time, counter, check, nontradable, amount

        counter = float()
        check = 0
        nontradable = 0
        amount = 0

        start_time = time()

        submit_button.configure(state='disabled')

        logbox_text.configure(state='normal')

        logbox_text.insert(END, 'In prosess...\n')
        inp = nickname_input.get()
        inp = nickname_input.get()

        a = Inventory(str(inp), 570)
        logbox_text.insert(END, 'Fetching inventory items for ' + str(inp).upper() + ' - ')
        logbox_text.configure(state='disabled')
        buffer = a.get_inventory_descriptions()
        if len(buffer) != 0:
                amount = len(buffer)
                logbox_text.configure(state='normal')
                logbox_text.insert(END, 'OK\nFetching item prices. It will take some time...\n'+20*'-'+'\n')
                logbox_text.configure(state='disabled')
                counter = float()
                for x in buffer:
                        t = Thread(target=bg_proc, args=(a, x))
                        t.deamon = True
                        t.start()
        
        else:
                submit_button.configure(state='normal')
                logbox_text.configure(state='normal')
                logbox_text.insert(END,  ' Failed\n')
                logbox_text.configure(state='disabled')

def bg_proc(a, i):
        global start_time, amount, check, nontradable, counter

        price_buffer = a.get_item_price(i)
        logbox_text.configure(state='normal')
        logbox_text.insert(END, i + ' - $' + price_buffer + '\n')
        logbox_text.configure(state='disabled')
        counter += float(price_buffer)
        if float(price_buffer) == 0.00:
                nontradable += 1
        check += 1
        if check == amount:
                logbox_text.configure(state='normal')
                logbox_text.insert(END, 20 * '-' + '\n')
                logbox_text.insert(END, 'Total items: ' + str(amount) + '\n')
                logbox_text.insert(END,'Total sum: $' + str(counter) + '\n')
                logbox_text.insert(END,'Amount of non-tradable: ' + str(nontradable) + '\n')
                logbox_text.insert(END,'Entire job took: ' + str(int(time() - start_time)) + 's\n\n')
                logbox_text.configure(state='disabled')
                submit_button.configure(state='normal')

root = Tk()
root.title('Dota 2 inventory calculator')
root['padx'] = 20
root['pady'] = 10
root['bg'] = '#1e1e1e'
root.resizable(0, 0)

nickname = str()

input_frame = Frame(root)
input_frame.config(bg='#1e1e1e')
input_frame.grid(row=0, column=0)
nickname_label = Label(input_frame, text='Enter your nickname: ', bg='#1e1e1e', fg='#ccc')
nickname_label.grid(row=0, column=0)
nickname_input = Entry(input_frame, textvariable=nickname, bg='#111', fg='#ccc')
nickname_input.insert(0, 'mypsycho')
nickname_input.grid(row=0, column=1)
submit_button = Button(input_frame, text='submit', command=submit, bg='#1e1e1e', fg='#ccc')
submit_button.grid(row=0,column=2)
logbox_text = Text(root, bg='#111', fg='#ccc')
logbox_text.grid()

root.mainloop()
