"""
#@aithor Arnab Maiti Pulastya™ ® Inc 
from tkinter import*
r=Tk()
r.geometry('720x720')
r.config(bg='light blue')
r.title('Pulastya:Brain BOOSter')
def start():
    b1.config(text='PRESS HERE TO CONTINUE',state='disabled')
    def f1():
        m3=Label(r,text='The first question is',font=('verdana',10))
        m3.pack()
        m2=Label(r,text='Question.1: Something divided by 0 is?',bg='light yellow',font=('verdana',10))
        b2.config(state='disabled')
        m2.pack()
        def op1():
            b3.config(state='disabled')
            def cans():
                ml=Label(r,text='OK you gave the correct answer,the next question is',font=('verdana',10))
                ml.pack()
                ml2=Label(r,text="Question 2: You saw a smartphone and a smartwatch lying in middle of the road,what will you do?",bg='light yellow',font=('verdana',10))
                ml2.pack()
                m4=Label(r,text="Your options for question number two")
                m4.pack()
                
                def q2():
#editting in the style by Arnab maiti
                    def cans1():
                        m5=Label(r,text="OK don't start flying we are getting started,the next question is",font=('verdana',10))
                        m5.pack()
                        m6=Label(r,text="Question 3: ")
                        b7.config(state='disabled',bg='light green',font=('elephant',10))
                        b6.config(state='disabled',bg='pink',font=('elephant',10))
                        b5.config(state='disabled',bg='pink',font=('elephant',10))
                        b4.config(state='disabled',bg='pink',font=('elephant',10))
                    def wans1():
                        b7.config(state='disabled',bg='light green',font=('elephant',10))
                        b6.config(state='disabled',bg='pink',font=('elephant',10))
                        b5.config(state='disabled',bg='pink',font=('elephant',10))
                        b4.config(state='disabled',bg='pink',font=('elephant',10))
                    b4=Button(r,text='1.You will leave them and go',pady=10,padx=42,command=wans1,font=('elephant',10))
                    b5=Button(r,text='2.You will take the phone',pady=10,padx=41,command=wans1,font=('elephant',10))
                    b6=Button(r,text='3.You will take the watch',pady=10,padx=50,command=wans1,font=('elephant',10))
                    b7=Button(r,text='4.You will take the both',pady=10,padx=55,command=cans1,font=('elephant',10))
                    b4.pack()
                    b5.pack()
                    b6.pack()
                    b7.pack()
                q2()        
                a1.config(state='disabled',bg='light green')
                a2.config(state='disabled',bg=' pink')
                a3.config(state='disabled',bg=' pink')
                a4.config(state='disabled',bg=' pink')
                
            def wans():
                m8=Label(r,text="Sorry you gave wrong answer , you can restart the app and try again",fg='red')
                m8.pack()
                a2.config(state='disabled',bg='pink')
                a3.config(state='disabled',bg='pink')
                a4.config(state='disabled',bg='pink')
                a1.config(state='disabled',bg='light green')
            a1=Button(r,text='1.Undefined',pady=10,padx=56,command=cans,font=('elephant',10))
            a2=Button(r,text='2.Zero',pady=10,padx=72,command=wans,font=('elephant',10))
            a3=Button(r,text='3.One',pady=10,padx=73,command=wans,font=('elephant',10))
            a4=Button(r,text='4.None of the above',pady=10,padx=35,command=wans,font=('elephant',10))
            a1.pack()
            a2.pack()
            a3.pack()
            a4.pack()
        b3=Button(r,text='Lets see the options for question 1',relief='ridge',command=op1,font=(4))
        b3.pack()
    b2=Button(r,text='Press here to know the first question',relief='ridge',command=f1,font=('georgia',14),bg='light grey')
    b2.pack()
b1=Button(r,text='PRESS HERE TO CONTINUE',command=start,font=('georgia',10),bg='light grey')
b1.pack()
mainloop()
"""
