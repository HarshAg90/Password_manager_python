from tkinter import *
from csv import writer
import csv
import os
import sys
from tkinter import messagebox
 
f= open(os.path.join(sys.path[0], "csv file.csv"),'r')
record=csv.reader(f)
data=[]

for rec in record:
    data.append(rec)
f.close()

def adding_info(row):                                   #same as name
    data.append(row)
    updatedata()
    summit_confirm["text"]="summited!"
    
def updatedata():                                                       #updating csv with data 2D list
    sw=csv.writer(open(os.path.join(sys.path[0], "csv file.csv"), "wt",newline=""), delimiter=",")#,newline=""
    sw.writerows(data)#.encode()
    
def password(x):                                                        #to login
    if int(x)==2002:
        raise_frame(mainf)

def modify(c,rCont):                                                    #changing specific data
    data[c]=rCont
    updatedata()
    modifyconf["text"]="modified! please go back"
        
def Delete(s):                                                          #deleting data
    dele=messagebox.askyesno(title='Confirmation',message='do u want to delete this?')
    if dele==True:
        data.pop(s)
        updatedata()
    else:
        raise_frame(showinf)

flag=0
def search(dname):                                                      #searching data
    global flag
    for i in range(len(data)):
        if dname == data[i][0]:
            searchid['text']=data[i][1]
            searchpa['text']=data[i][2]
            flag=1
    if flag==0:
        SF['text']='not found!! please recheck'
        
rownum =  None
def modifyFrameRaise(a):                                                #raising frame and storing input as variable
    global rownum
    rownum=a
    raise_frame(modifyf)
    
a=0
def proceed(d):                                                         #changing data in show data frame
    l=len(data)
    global a
    if d == 'f':
        if a<l-1:
            a+=1
            plab['text']  = data[a][0]
            idlab['text'] = data[a][1]
            palab['text'] = data[a][2]
        elif a==l-1:
            a=0
            plab['text']  = data[a][0]
            idlab['text'] = data[a][1]
            palab['text'] = data[a][2]
        
    elif d=='b':
        if a>=0:
            a-=1
            plab['text']  = data[a][0]
            idlab['text'] = data[a][1]
            palab['text'] = data[a][2]
        elif a<0:
            a=l-2
            plab['text']  = data[a][0]
            idlab['text'] = data[a][1]
            palab['text'] = data[a][2]

def raise_frame(frame):                                                 #transition b/w windows
    frame.tkraise()

root=Tk()
root.title('ID/Password Manager')
root.geometry('400x300')
root.configure(bg='#272727')

passf=Frame(root)
passf.config(bg="#272727")
mainf = Frame(root)
mainf.config(bg="#272727")
askinf = Frame(root)
askinf.config(bg="#272727")
showinf = Frame(root)
showinf.config(bg="#272727")
searchf=Frame(root)
searchf.config(bg="#272727")
modifyf=Frame(root)
modifyf.config(bg="#272727")

for frame in (passf,mainf, askinf, showinf, searchf, modifyf):
    frame.grid(row=0, column=0, sticky='news')
    
#_________PASS_2002____________________________________________________________

Label(passf,text='PLEASE ENTER',font=('Franklin Gothic Heavy','22'),fg='#F5F5F5',bg='#272727',borderwidth=0).grid(row=0,column=0,padx=80,pady=10)
Label(passf,text='PASSWORD',font=('Franklin Gothic Heavy','22'),fg='#F5F5F5',bg='#272727',borderwidth=0).grid(row=1,column=0,padx=100,pady=10)

pasw=Entry(passf,borderwidth=0,bg='#000000',fg='#F5F5F5',width=25,show="*")
pasw.grid(row=2,column=0,padx=110,pady=8)

Button(passf,text='submit',width=15,font=('Arial Rounded MT Bold','12'),fg='#FF652F',bg='#000000',borderwidth=0,command = lambda:password(pasw.get())).grid(row=3,column=0,padx=110,pady=8)

    
#___________MAIN_______________________________________________________________
    
Label(mainf,text='HELLO USER!!',font=('Franklin Gothic Heavy','22'),fg='#F5F5F5',bg='#272727',borderwidth=0).grid(row=0,column=0,columnspan=4,pady=15,padx=95)
Label(mainf,text='here you can manage your IDs and password',font=('Agency FB','15'),fg='#747474',bg='#272727',borderwidth=0).grid(row=1,column=0,columnspan=4)
Label(mainf,text='in organised manner',font=('Agency FB','15'),fg='#747474',bg='#272727',borderwidth=0).grid(row=2,column=0,columnspan=4)
Button(mainf,text='ENTER NEW STUFF',width=35,font=('Arial Rounded MT Bold','12'),fg='#FFE400',bg='#000000',borderwidth=0,command = lambda:raise_frame(askinf)).grid(row=3,column=1,columnspan=2,pady=10)
Button(mainf,text='SHOW ALL',width=15,font=('Arial Rounded MT Bold','12'),fg='#FF652F',bg='#000000',borderwidth=0,command = lambda:raise_frame(showinf)).grid(row=4,column=0,columnspan=2,pady=10)
Button(mainf,text='SEARCH',width=15,font=('Arial Rounded MT Bold','12'),fg='#FF652F',bg='#000000',borderwidth=0,command = lambda:raise_frame(searchf)).grid(row=4,column=2,columnspan=2,pady=10)


#____________asking_info_______________________________________________________

Label(askinf,text='ENTER YOUR DETAILS',font=('Franklin Gothic Heavy','18'),fg='#F5F5F5',bg='#272727',borderwidth=0).grid(row=0,column=0,columnspan=4,pady=15,padx=90)
Label(askinf,text='why are u reading this, aint u smart enough',font=('Agency FB','15'),fg='#747474',bg='#272727',borderwidth=0).grid(row=1,column=0,columnspan=4,pady=10)

Label(askinf,text='enter field:',font=('Arial Rounded MT Bold','12'),fg='#FFE400',bg='#272727').grid(row=2,column=0,pady=8)

field=Entry(askinf,borderwidth=0,bg='#000000',fg='#F5F5F5',width=25)
field.grid(row=2,column=1,columnspan=3,padx=30,pady=8)


Label(askinf,text='enter email:',font=('Arial Rounded MT Bold','12'),fg='#FF652F',bg='#272727').grid(row=3,column=0,pady=8)

email=Entry(askinf,borderwidth=0,bg='#000000',fg='#F5F5F5',width=25)
email.grid(row=3,column=1,columnspan=3,padx=30,pady=8)

Label(askinf,text='enter password:',font=('Arial Rounded MT Bold','12'),fg='#14A76C',bg='#272727').grid(row=4,column=0,pady=8)

passw=Entry(askinf,borderwidth=0,bg='#000000',fg='#F5F5F5',width=25 )
passw.grid(row=4,column=1,columnspan=3,padx=30,pady=8)
   
Button(askinf,text='SUBMIT',width=10,font=('Arial Rounded MT Bold','12'),fg='#FF652F',bg='#000000',borderwidth=0,command=lambda:adding_info([field.get(),email.get(),passw.get()])).grid(row=5,column=0,pady=10)

Button(askinf,text='GO BACK',width=10,font=('Arial Rounded MT Bold','12'),fg='#14A76C',bg='#000000',borderwidth=0, command=lambda:raise_frame(mainf)).grid(row=5,column=2,pady=10)

summit_confirm=Label(askinf,text='',font=('Agency FB','15'),fg='#747474',bg='#272727',borderwidth=0)
summit_confirm.grid(row=6,column=0,columnspan=4)
#_____________Show_Details_____________________________________________________

Label(showinf, text='YOUR DETAILS', font = ('Franklin Gothic Heavy', '18'), fg='#F5F5F5', bg='#272727').grid(row=0, column=0, columnspan=4, pady=15, padx=120)

Label(showinf, text='the field:', font=('Arial Rounded MT Bold', '12'),fg='#747474',bg='#272727').grid(row=1,column=0,columnspan=2,pady=5)
plab = Label( showinf,text=data[0][0],font = ('Arial Rounded MT Bold','12'),fg='#FFE400',bg='#272727')
plab.grid(row = 1, column = 2, columnspan = 2, padx = 40,pady=5)

Label(showinf, text='email:', font=('Arial Rounded MT Bold', '12'), fg='#747474', bg='#272727').grid(row=2, column=0, columnspan=2, pady=5)
idlab=Label(showinf,text= data[0][1],font=('Arial Rounded MT Bold', '12'), fg='#FF652F', bg='#272727')
idlab.grid(row=2, column=2, columnspan=2, pady=5, padx=40)

Label(showinf, text='password:', font=('Arial Rounded MT Bold', '12'), fg='#747474',bg='#272727').grid(row=3, column=0, columnspan=2, pady=5)
palab=Label(showinf, text = data[0][2],font=('Arial Rounded MT Bold', '12'), fg='#14A76C', bg='#272727')
palab.grid(row=3,column=2,columnspan=2,pady=5,padx=40)

Button(showinf,text='<--',width=15,font=('Arial Rounded MT Bold','12'),fg='#FFE400',bg='#000000',borderwidth=0,command = lambda:proceed('b')).grid(row=5,column=0,columnspan=2,pady=10)
Button(showinf,text='-->',width=15,font=('Arial Rounded MT Bold','12'),fg='#14A76C',bg='#000000',borderwidth=0,command = lambda:proceed('f')).grid(row=5,column=2,columnspan=2,pady=10)
Button(showinf,text='Modify',width=10,font=('Arial Rounded MT Bold','12'),fg='#FFE400',bg='#000000',borderwidth=0,command = lambda:modifyFrameRaise(a)).grid(row=6,column=0,pady=10)
Button(showinf,text='Delete',width=10,font=('Arial Rounded MT Bold','12'),fg='#14A76C',bg='#000000',borderwidth=0,command = lambda:Delete(a)).grid(row=6,column=3,pady=10)
Button(showinf,text='Back',width=15,font=('Arial Rounded MT Bold','12'),fg='#FF652F',bg='#000000',borderwidth=0,command = lambda:raise_frame(mainf)).grid(row=6,column=1,columnspan=2,pady=10)
#___________________________MODIFY_____________________________________________

Label(modifyf,text='EDITING DATA',font=('Franklin Gothic Heavy','18'),fg='#F5F5F5',bg='#272727',borderwidth=0).grid(row=0,column=0,columnspan=4,pady=15,padx=90)
Label(modifyf,text='edit data, click summit when done',font=('Agency FB','15'),fg='#747474',bg='#272727',borderwidth=0).grid(row=1,column=0,columnspan=4,pady=10)
Label(modifyf,text='enter field:',font=('Arial Rounded MT Bold','12'),fg='#FFE400',bg='#272727').grid(row=2,column=0,pady=8)
for_ask=Entry(modifyf,borderwidth=0,bg='#000000',fg='#F5F5F5',width=25)
for_ask.grid(row=2,column=1,columnspan=3,padx=30,pady=8)
Label(modifyf,text='enter email:',font=('Arial Rounded MT Bold','12'),fg='#FF652F',bg='#272727').grid(row=3,column=0,pady=8)
ask_email=Entry(modifyf,borderwidth=0,bg='#000000',fg='#F5F5F5',width=25)
ask_email.grid(row=3,column=1,columnspan=3,padx=30,pady=8)
Label(modifyf,text='enter password:',font=('Arial Rounded MT Bold','12'),fg='#14A76C',bg='#272727').grid(row=4,column=0,pady=8)
ask_pass=Entry(modifyf,borderwidth=0,bg='#000000',fg='#F5F5F5',width=25 )
ask_pass.grid(row=4,column=1,columnspan=3,padx=30,pady=8)
Button(modifyf,text='SUBMIT',width=10,font=('Arial Rounded MT Bold','12'),fg='#FF652F',bg='#000000',borderwidth=0,command=lambda:modify(rownum,[for_ask.get(),ask_email.get(),ask_pass.get()])).grid(row=5,column=0,pady=10)
Button(modifyf,text='GO BACK',width=10,font=('Arial Rounded MT Bold','12'),fg='#14A76C',bg='#000000',borderwidth=0, command=lambda:raise_frame(mainf)).grid(row=5,column=2,pady=10)

modifyconf=Label(modifyf,text='',font=('Agency FB','15'),fg='#747474',bg='#272727',borderwidth=0)
modifyconf.grid(row=6,column=0,columnspan=4)
#___________________________search_____________________________________________


Label(searchf,text='ENTER SEARCHABLE DOMAIN',font=('Franklin Gothic Heavy','18'),fg='#F5F5F5',bg='#272727',borderwidth=0).grid(row=0,column=0,columnspan=4,pady=15,padx=40)
Label(searchf,text='enter the domain name that you wish to search',font=('Agency FB','15'),fg='#747474',bg='#272727',borderwidth=0).grid(row=1,column=0,columnspan=4,pady=10)

Label(searchf,text='domain name',font=('Arial Rounded MT Bold','12'),fg='#FFE400',bg='#272727').grid(row=2,column=0,pady=8,padx=40)

domainS=Entry(searchf,borderwidth=0,bg='#000000',fg='#F5F5F5',width=25)
domainS.grid(row=2,column=1,pady=8)

Button(searchf,text='SEARCH',width=10,font=('Arial Rounded MT Bold','12'),fg='#FF652F',bg='#000000',borderwidth=0, command=lambda:search(domainS.get())).grid(row=3,column=0,pady=5)

Button(searchf,text='GO BACK',width=10,font=('Arial Rounded MT Bold','12'),fg='#14A76C',bg='#000000',borderwidth=0, command=lambda:raise_frame(mainf)).grid(row=3,column=1,pady=5)

Label(searchf,text='email:',font=('Arial Rounded MT Bold','12'),fg='#747474',bg='#272727').grid(row=4,column=0,pady=8)
searchid=Label(searchf,text="your emai",font=('Arial Rounded MT Bold','12'),fg='#FF652F',bg='#272727')
searchid.grid(row=4,column=1,columnspan=1,pady=5,padx=20)

Label(searchf,text='password:',font=('Arial Rounded MT Bold','12'),fg='#747474',bg='#272727').grid(row=5,column=0,pady=8)
searchpa=Label(searchf,text="your pass.",font=('Arial Rounded MT Bold','12'),fg='#14A76C',bg='#272727')
searchpa.grid(row=5,column=1,columnspan=1,pady=5,padx=20)

SF=Label(searchf,text='',font=('Agency FB','15'),fg='#747474',bg='#272727',borderwidth=0)
SF.grid(row=6,column=0,columnspan=4)

#____________X________________X_________________X______________________________




  
    
raise_frame(passf)

root.mainloop()