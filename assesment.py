
#Q.no:1
x=open('mynew.txt','w+')
x.write('Karthik code\n my self karthi')            
x.write('python writing')
x.close()

y=open('mynew.txt','r+')
print(y.read())
y.close()

#Q.no:2
import random
for i in range(0,4):
    print(random.randint(0,50))
    
#3.Use Time Module:
import time
print(help(time.strftime))
current_date=time.strftime("%d")
current_month=time.strftime("%m")
current_year=time.strftime("%Y")

print("current date:",current_date)
print("current Month:",current_month)
print("current year:",current_year)

name=input("Enter Your Name:").upper()
birth_date=int(input("Enter Your Birth date ex: 01   :"))
birth_month=int(input("Enter Your Birth month ex 01  :"))
birth_year=int(input("Enter Your Birth Year ex 1990  :")) 

val_1=int(current_date)-birth_date
val_2=int(current_month)-birth_month
val_3=int(current_year)-birth_year

print("YOUR NAME   :",name)
print('Total Days  :',abs(val_1))
print('Total Months:',abs(val_2))
print('Total Years :',abs(val_3))


#Q.No:4    
import time

current_date=time.strftime("%d")
current_month=time.strftime("%m")
current_year=time.strftime("%Y")

print("current date:",current_date)
print("current Month:",current_month)
print("current year:",current_year)

val_1=int(current_date)-1
val_2=int(current_month)-1
val_3=int(current_year)-1

print('Previous Days  :',abs(val_1))
print('Previous Month:',abs(val_2))
print('Previous Year :',abs(val_3))


