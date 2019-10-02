'''
print('1)Create a new file\n2)Display the file\n3)Add a new item to the file')
user=input('Make a selection to 1,2 or 3: ')
if int(user) == 1:
    fname=open('Subject.txt','w')
    user=input('Enter a subject name:')
    fname.write(user+'\n')
    fname.close()
elif int(user) == 2:
    fname=open('Subject.txt','r')
    lines=fname.read()
    print(lines)
    fname.close()
elif int(user) == 3:
    fname=open('Subject.txt','a')
    new=input('Enter a new one: ')
    fname.write(new+'\n')   
    fname.close()
    fname=open('Subject.txt','r')
    print(fname.read())
    fname.close()
else:
    print('Invalid input')
'''
'''
import random
quiz=open('Mathquiz.csv','a')
name=input('Enter your name: ')
quiz.write(name+'\n')
grade=0
for i in range(0,2):
    num1=random.randint(0,100)
    num2=random.randint(0,100)
    ans=num1+num2
    print(num1,'+',num2,'=')
    yans=int(input('Enter your answer: '))
    quiz.write(str(num1)+'+'+str(num2)+'='+'\n')
    if ans==yans:
        grade=grade+1
    quiz.write('Your answer:'+str(yans)+'\n')
quiz.write('Your score:'+str(grade)+'\n')
quiz.close()
'''

file=open('Salaries.csv','w')
n=input('Your name: ')
s=input('Your salary: ')
file.write(n+'\n'+str(s)+'\n')
file.close()
print('1)Add to file\n2)View all records\n3)Delete a record\n4)Quit programme')
c=0
while c!='4':
    c=input('Select: ')
    if int(c):
        if c=='1':
            file=open('Salaries.csv','a')
            n=input('Your name: ')
            s=input('Your salary: ')
            file.write(n+'\n'+str(s)+'\n')
            file.close()
        elif c=='2':
            file=open('Salaries.csv','r')
            print(file.read())
            file.close()
        elif c=='3':
            file=open('Salaries.csv','r')
            content=file.read()
            li=list()
            rows=content.split('\n')
            for row in rows:
                li.append(row.split(','))
            file.close()
            n1=[]
            n=input('Enter name:')
            n1.append(n)
            li.remove(n1)
            file=open('Salaries.csv','w')
            file.write(str(li))
            print(li)
            file.close()
        elif c=='4':
            print('Programme stop')
        else:
            print('Error')

'''
from tkinter import*
import random
def roll():
    a=random.randint(1,6)
    msg=Label(window, text=a)
    msg.place(x=30,y=50)
window = Tk()
window.geometry('200x110')
button=Button(text="Let's roll", command=roll)
button.place(x=30,y=20,width=120,height=25)
window.mainloop()
'''
'''
from tkinter import*
def add():
    num=textbox1.get()
    message=str()

'''