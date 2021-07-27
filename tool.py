########################################BACKUP################################
from tkinter import * 
import os
import time
import shutil
from PIL import ImageTk,Image  
imglist=[0]
global label1,i
current_actions={'gender':'','age':'','emp': ''}
previous_actions={'gender':'','age':'','emp': ''}
i=0
source_path='images/'
for i in os.listdir(source_path):
    imglist.append(i)
    
    
if('data' not in os.listdir()):
        os.mkdir('data')
        
        os.mkdir('data/gender')
        os.mkdir('data/gender/male')
        os.mkdir('data/gender/female')
        os.mkdir('data/gender/notsure')
        
        os.mkdir('data/emp_or_not')
        os.mkdir('data/emp_or_not/employee')
        os.mkdir('data/emp_or_not/not_employee')
        os.mkdir('data/emp_or_not/notsure')
        
        os.mkdir('data/age')
        os.mkdir('data/age/youth(0-20)')
        os.mkdir('data/age/young_adult(20-35)')
        os.mkdir('data/age/adult(35-55)')
        os.mkdir('data/age/old(56-above)')
        os.mkdir('data/age/notsure')
        
        

def male():
    current_actions['gender']='male'
    shutil.copy(source_path+imglist[0],'data/gender/male/') 
    m=Label(top,text='Moved to Male',font=("Arial", 15)).place(x=550,y=200)
    femaleb["state"] =DISABLED
    maleb["state"] =DISABLED
    notsure_genderb['state']=DISABLED

def female():
    current_actions['gender']='female'
    shutil.copy(source_path+imglist[0],'data/gender/female/') 
    f=Label(top,text='Moved to female',font=("Arial", 15)).place(x=550,y=200) 
    maleb["state"] =DISABLED
    femaleb["state"] =DISABLED
    notsure_genderb['state']=DISABLED
    
def emp():
    current_actions['emp']='employee'
    shutil.copy(source_path+imglist[0],'data/emp_or_not/employee/') 
    e=Label(top,text='Moved to Employee',font=("Arial", 15)).place(x=550,y=250)
    notempb["state"] =DISABLED
    empb["state"] =DISABLED
    notsure_empb['state']=DISABLED
def nootemp():
    current_actions['emp']='not_employee'
    shutil.copy(source_path+imglist[0],'data/emp_or_not/not_employee/') 
    n=Label(top,text='Moved to NotEmployee',font=("Arial", 15)).place(x=550,y=250)
    empb["state"] =DISABLED
    notempb["state"] =DISABLED
    notsure_empb['state']=DISABLED

def youth():
    current_actions['age']='youth(0-20)'
    shutil.copy(source_path+imglist[0],'data/age/youth(0-20)/')
    t=Label(top,text='Moved to teen',font=("Arial", 15)).place(x=550,y=300)
   
    youthb["state"] =DISABLED
    adultb["state"] =DISABLED
    young_adultb["state"] =DISABLED
    oldb["state"] =DISABLED
    notsure_ageb['state']=DISABLED    
def young_adult():
    current_actions['age']='young_adult(20-35)'
    shutil.copy(source_path+imglist[0],'data/age/young_adult(20-35)/') 
    a=Label(top,text='Moved to adult',font=("Arial", 15)).place(x=550,y=300)
    youthb["state"] =DISABLED
    adultb["state"] =DISABLED
    young_adultb["state"] =DISABLED
    oldb["state"] =DISABLED
    notsure_ageb['state']=DISABLED  
def adult():
    current_actions['age']='adult(35-55)'
    shutil.copy(source_path+imglist[0],'data/age/adult(35-55)/') 
    a=Label(top,text='Moved to adult',font=("Arial", 15)).place(x=550,y=300)
    youthb["state"] =DISABLED
    adultb["state"] =DISABLED
    young_adultb["state"] =DISABLED
    oldb["state"] =DISABLED
    notsure_ageb['state']=DISABLED  
def old():
    current_actions['age']='old(56-above)'
    shutil.copy(source_path+imglist[0],'data/age/old(56-above)')
    o=Label(top,text='Moved to Old',font=("Arial", 15)).place(x=550,y=300)    
    youthb["state"] =DISABLED
    adultb["state"] =DISABLED
    young_adultb["state"] =DISABLED
    oldb["state"] =DISABLED
    notsure_ageb['state']=DISABLED  
def discard():
    print("Discard pressed")
   # Label(top,text='Image discarded').place(x=1250,y=350)
    youthb["state"] =DISABLED
    adultb["state"] =DISABLED
    young_adultb["state"] =DISABLED
    oldb["state"] =DISABLED
    empb["state"] =DISABLED
    notempb["state"] =DISABLED
    femaleb["state"] =DISABLED
    maleb["state"] =DISABLED




def prevaction():
    
    movedornot=Label(top,text="Previous action Performed",font=("Comic Sans MS", 13,'bold'))
    movedornot.place(x=890,y=50)
    
    shutil.copy(source_path+imglist[0],'data/gender/'+current_actions['gender'])
    shutil.copy(source_path+imglist[0],'data/age/'+current_actions['age'])
    shutil.copy(source_path+imglist[0],'data/emp_or_not/'+current_actions['emp'])
    nextfunbut()
    

def notsure_age():
    current_actions['age']='notsure'
    o=Label(top,text='NotSure Age',font=("Arial", 15)).place(x=550,y=300)  
def notsure_gender():
    current_actions['gender']='notsure'
    m=Label(top,text='NotSure Gender',font=("Arial", 15)).place(x=550,y=200)
def notsure_emp():
    current_actions['emp']='notsure'
    n=Label(top,text='NotSure Employee',font=("Arial", 15)).place(x=550,y=250)



        
def nextfunbut():
    
        gen=Label(top,text='                                                                              ',font=("Arial", 25))
        gen.place(x=890,y=50)
        
        try:
            try:
            
                os.remove(source_path+imglist[0])
                
            except:
                pass
            imgname_label1=Label(top,text='                                                                              ',font=("Arial", 25))
            imgname_label1.place(x=50,y=10)

            pactions=Label(top,text='Previous Actions: ',font=("Comic Sans MS", 15,'bold'))
            pactions.place(x=1080,y=100)

            gen1=Label(top,text='                                                                              ',font=("Arial", 25))
            gen1.place(x=1180,y=150)
            
            pgender=Label(top,text=current_actions['gender'],font=("Comic Sans MS", 13))
            pgender.place(x=1180,y=150)

            
            gen1=Label(top,text='                                                                              ',font=("Arial", 25))
            gen1.place(x=1180,y=200)
            pemp=Label(top,text=current_actions['emp'],font=("Comic Sans MS", 13))
            pemp.place(x=1180,y=200)
            
            gen1=Label(top,text='                                                                              ',font=("Arial", 25))
            gen1.place(x=1180,y=250)
            page=Label(top,text=current_actions['age'],font=("Comic Sans MS", 13))
            page.place(x=1180,y=250)


            black = Image.open("ba.jpg")
            black = black.resize((850, 450), Image.ANTIALIAS)
            testb = ImageTk.PhotoImage(black)

            label1b = Label(image=testb,)
            label1b.image = testb
            label1b.place(x=0, y=40)


            imgname_label=Label(top,text='ImageName:'+imglist[1],font=("Arial", 15))
            imgname_label.place(x=50,y=0)
            print("Now showing: ",imglist[1])
            image1 = Image.open(source_path+imglist[1])
            test = ImageTk.PhotoImage(image1)

            label1 = Label(image=test)
            label1.image = test
            label1.place(x=50, y=100)

            imglist.pop(0)
            imremaining2=Label(top,text='                                                                               ',font=("Arial", 25))
            imremaining2.place(x=950,y=10)
            remaining=len(imglist)
            imremaining=Label(top,text='Remaing:'+str(len(imglist)),font=("Arial", 15))
            imremaining.place(x=950,y=10)

            if(remaining==0):
                top.destroy()

            # Label(top,text='                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ',font=5).place(x=10,y=600)

            youthb["state"] =NORMAL
            adultb["state"] =NORMAL
            young_adultb["state"] =NORMAL
            oldb["state"] =NORMAL
            empb["state"] =NORMAL
            notempb["state"] =NORMAL
            femaleb["state"] =NORMAL
            maleb["state"] =NORMAL
            notsure_genderb['state']=NORMAL  
            notsure_empb['state']=NORMAL  
            notsure_ageb['state']=NORMAL  
        except:
            popupmsg()
           # top.destroy()

def popupmsg():
    popup = Tk()
    popup.title('Its Over')
    popup.geometry('300x300')
    
    label = Label(popup, text='Your Done!!!!!!!!!',font=("Comic Sans MS", 25,"bold"))
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command = lambda:[popup.destroy(),top.destroy()],font=("Comic Sans MS", 20))
    B1.pack()
    popup.mainloop()    
top =Tk()


top.geometry("1920x800")  
top.title("Tool")


h=2
w=10
maleb=Button(top,text='Male',command=male,font=("Comic Sans MS", 13,"bold"),borderwidth= 5)
maleb.config(height = h, width = w)
maleb.place(x=10,y=500)


femaleb=Button(top,width=10,text='Female',command=female,font=("Comic Sans MS", 13,"bold"),borderwidth= 5)
femaleb.config(height = h, width = w)
femaleb.place(x=200,y=500)

notsure_genderb=Button(top,width=10,text='NotSure Gender',command=notsure_gender,font=("Comic Sans MS", 13,"bold"),borderwidth= 5)
notsure_genderb.config(height = h, width = w+3)
notsure_genderb.place(x=100,y=600)

empb=Button(top,width=10,text='Employee',command=emp,font=("Comic Sans MS", 13,"bold"),borderwidth= 5)
empb.config(height = h, width = w)
empb.place(x=550,y=500)

notempb=Button(top,width=10,text='Not-Employee',command=nootemp,font=("Comic Sans MS", 13,"bold"),borderwidth= 5)
notempb.config(height = h, width = w+5)
notempb.place(x=750,y=500)

notsure_empb=Button(top,width=10,text='NotSure Emp',command=notsure_emp,font=("Comic Sans MS", 13,"bold"),borderwidth= 5)
notsure_empb.config(height = h, width = w+1)
notsure_empb.place(x=600,y=600)

youthb=Button(top,width=10,text='Youth\n(0-20)',command=youth,font=("Comic Sans MS", 13,"bold"),borderwidth= 5)
youthb.config(height = h, width = w)
youthb.place(x=1020,y=500)

adultb=Button(top,width=10,text='Adult\n(35-55)',command=adult,font=("Comic Sans MS", 13,"bold"),borderwidth= 5)
adultb.config(height = h, width = w)
adultb.place(x=1210,y=500)

young_adultb=Button(top,width=10,text='Young_Adult\n(20-35)',command=young_adult,font=("Comic Sans MS", 13,"bold"),borderwidth= 5)
young_adultb.config(height = h, width = w)
young_adultb.place(x=1220,y=400)


oldb=Button(top,width=10,text='Old\n(56-above)',command=old,font=("Comic Sans MS", 13,"bold"),borderwidth= 5)
oldb.config(height = h, width = w)
oldb.place(x=1020,y=400)
notsure_ageb=Button(top,width=10,text='NotSure Age',command=notsure_age,font=("Comic Sans MS", 13,"bold"),borderwidth= 5)
notsure_ageb.config(height = h, width = w)
notsure_ageb.place(x=1150,y=600)

discardb=Button(top,width=10,text='Discard',command=nextfunbut,font=("Comic Sans MS", 13,"bold"),borderwidth= 5)
discardb.config(height = h, width = w)
discardb.place(x=900,y=330)
performprev=Button(top,width=10,text='Previous action',command=prevaction,font=("Comic Sans MS", 13,"bold"),borderwidth= 5)
performprev.config(height = h, width = w+5)
performprev.place(x=900,y=200)

nextb=Button(top,width=10,text='Next',command=nextfunbut,font=("Comic Sans MS", 13,"bold"),borderwidth= 5)
nextb.config(height = h, width = w)
nextb.place(x=900,y=85)




top.mainloop()