from tkinter import *
from PIL import Image, ImageTk
from string import ascii_uppercase
import random
from tkinter import messagebox
#Let's create our project window as below
run=True
while run:
        root=Tk()#creating object to tkinter class (creating a window)
        root.geometry("1050x550")
        root.title('Hangman')
       # root.configure(bg='#ffffff')
        bg=ImageTk.PhotoImage(Image.open('dream.png'))
        a=Label(root,image=bg)
        a.place(x=0,y=0)
        la=Label(root)
        la.place(x=820,y=90)
        l=['apple','banana','orange','watermelon','cherry','strawberry','hangman','invert','python','tkinter','java','krishna','murari','rajkumar']
        himg=['1.png','2.png','3.png','4.png','5.png','6.png','7.png']
        l1=[]
        count=0
        i=0
        def close():
                global run
                yes=messagebox.askyesno("Hangman","Do you want to continue")
                if yes:
                    run=True
                    root.destroy()
                else:
                    run=False
                    root.destroy()
        exited=ImageTk.PhotoImage(Image.open('exit.png'))
        exitbtn=Button(root,image=exited,command=close,bg='#55CFFE')
        exitbtn.place(x=870,y=0)
    
        def checkwin(s):
                global run
                global la
                if s==len(word):
                        wonimg=ImageTk.PhotoImage(Image.open('WIN.png'))
                        la.configure(image=wonimg)
                        la.image=wonimg
                        messagebox.showinfo("Hangman","YOU WON")
                        print(s)
                        yes=messagebox.askyesno("Hangman","Do you want to play again???")
                        print(yes)
                        if yes:
                            run=True
                            count=0
                            root.destroy()
                        else:
                                run=False
                                root.destroy()
        def Hangman():
            global i
            global img
            global la
            if i==0:
                        img=ImageTk.PhotoImage(Image.open(himg[0]))
                        la=Label(root,image=img)
                        la.place(x=820,y=90)
                        i+=1
            elif i!=0 and i<7:
                
                img=ImageTk.PhotoImage(Image.open(himg[i]))
                la.configure(image=img)
                la.image=img
                i+=1
                                

                            
        def play(letter):
            global chances
            global run
            global count
            if chances>0:
                l2.config(text="Remaining chances :"+str(chances))
                chances-=1
                if letter in word:
                        for i in range(0,len(word)):
                            if word[i]==letter:
                                l1[i].config(text=letter)
                                count+=1
                                checkwin(count)
                else:
                        Hangman()
            elif chances==0:
                loseimg=ImageTk.PhotoImage(Image.open('LOSE.png'))
                la.configure(image=loseimg)
                la.image=loseimg
                messagebox.showinfo("Hangman","Chances over")
                res=messagebox.askyesno("Hangman","Do you want to play again???")
                if res:
                    print(res)
                    for i in range(0,len(word)):
                        l1[i].config(text=" _ ")
                    run=True
                    root.destroy()
                else:
                        run=False
                        root.destroy()
        l2=Label(root,text=" ",bg="#7EAE26",fg='#ffffff',font=("arial",30))
        l2.place(x=0,y=500)
        def game():
            global word
            global chances
            global run
            word=random.choice(l)
            chances=len(word)
            print(word)
            x=60
            for i in range(0,len(word)):
                x+=60
                l1.append(Label(root,text=" _ ",bg='#55CFFE',fg='#ffffff',font=("arial",30)))
                l1[i].place(x=x,y='150')



        btn1=Button(root,text='A',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('a'))
        btn1.place(x=50,y=300)
        btn2=Button(root,text='B',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('b'))
        btn2.place(x=110,y=300)
        btn3=Button(root,text='C',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('c'))
        btn3.place(x=170,y=300)
        btn4=Button(root,text='D',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('d'))
        btn4.place(x=230,y=300)
        btn5=Button(root,text='E',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('e'))
        btn5.place(x=290,y=300)
        btn6=Button(root,text='F',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('f'))
        btn6.place(x=350,y=300)
        btn7=Button(root,text='G',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('g'))
        btn7.place(x=410,y=300)
        btn8=Button(root,text='H',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('h'))
        btn8.place(x=470,y=300)
        btn9=Button(root,text='I',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('i'))
        btn9.place(x=530,y=300)
        btn10=Button(root,text='J',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('j'))
        btn10.place(x=590,y=300)
        btn11=Button(root,text='K',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('k'))
        btn11.place(x=650,y=300)
        btn12=Button(root,text='L',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('l'))
        btn12.place(x=710,y=300)
        btn13=Button(root,text='M',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('m'))
        btn13.place(x=770,y=300)
        btn14=Button(root,text='N',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('n'))
        btn14.place(x=830,y=300)
        btn15=Button(root,text='O',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('o'))
        btn15.place(x=120,y=360)
        btn16=Button(root,text='P',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('p'))
        btn16.place(x=180,y=360)
        btn17=Button(root,text='Q',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('q'))
        btn17.place(x=240,y=360)
        btn18=Button(root,text='R',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('r'))
        btn18.place(x=300,y=360)
        btn19=Button(root,text='S',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('s'))
        btn19.place(x=360,y=360)
        btn20=Button(root,text='T',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('t'))
        btn20.place(x=420,y=360)
        btn21=Button(root,text='U',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('u'))
        btn21.place(x=480,y=360)
        btn22=Button(root,text='V',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('v'))
        btn22.place(x=540,y=360)
        btn23=Button(root,text='W',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('w'))
        btn23.place(x=600,y=360)
        btn24=Button(root,text='X',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('x'))
        btn24.place(x=660,y=360)
        btn25=Button(root,text='Y',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('y'))
        btn25.place(x=720,y=360)
        btn26=Button(root,text='Z',bg="#010221",font=("24"),fg="#faeded",height='2',width='5',bd=0,command=lambda:play('z'))
        btn26.place(x=780,y=360)


        game()
        root.mainloop()


