BasicPay1=0
SpecialPay1=0
StagnationPay1=0
QualtifcationPay1=0
FixedPersonalPay1=0
OtherPay1=0
YearsOfService1=0
AgeAtNextbirthday1=0
CommutationPercent1=0


CommutationFactor=0


print('***********************************************************************************')
print('***********************************************************************************')
print('               **PENSION AND COMMUTATION CALCULATOR-PSU BANKS** ')
print('-----------------WELCOME TO PENSION AND COMMUTATION CALCULATOR-----------------------')
BasicPay=float(input('Enter Basic Pay :'))   
print('___________________________________________________________________________________')
SpecialPay=float(input('Enter special Pay :'))
print('___________________________________________________________________________________')
StagnationPay=float(input('Enter Stagnation Pay :'))
print('___________________________________________________________________________________')
QualificationPay=float(input('Enter Qualification Pay :'))
print('___________________________________________________________________________________')
FixedPersonalPay=float(input('Enter Fixed Personal Pay (Portion Eligibe for PF Deduction ) :'))
print('___________________________________________________________________________________')
OtherPay=float(input('Enter Other Pay (portion Eligible For PF Deduction) :'))
print('___________________________________________________________________________________')
YearsOfService=float(input('Enter Years of Service (Maximum 33 Years) :'))
print('___________________________________________________________________________________')
AgeAtNextbirthday=float(input('Enter Age At Next Birthday :'))
print('___________________________________________________________________________________')
CommutationPercent=float(input('Enter Commutation Percentage (MAX= 33.3333%) :'))
print('___________________________________________________________________________________')



if(BasicPay>0):
    BasicPay1=BasicPay
else:
    BasicPay1=0

if(SpecialPay>0):
    SpecialPay1=SpecialPay
else:
    SpecialPay1=0

if(StagnationPay>0):
    StagnationPay1=StagnationPay
else:
    StagnationPay1=0

if(QualificationPay>0):
    QualifationPay1=QualificationPay
else:
    QualificationPay=0

if(FixedPersonalPay>0):
    FixedPersonalPay1=FixedPersonalPay
else:
    FixedPersonalPay1=0

if(OtherPay>0):
    OtherPay1=OtherPay
else:
    OtherPay1=0

if(YearsOfService>=33):
    YearsOfService1=33
elif (YearsOfService>=10):
    YearsOfService1=YearsOfService
else:
    YearsOfService1=0

if(CommutationPercent>=33.33):
    CommutationPercent1=33.3333
elif(CommutationPercent>0):
    CommutationPercent1=CommutationPercent
else:
    CommutationPercent1=0

if(AgeAtNextbirthday>0):
    AgeAtNextbirthday1=AgeAtNextbirthday
else:
    AgeAtNextbirthday1=0





if (AgeAtNextbirthday == 28):
    CommutationFactor = 18.07
    
elif(AgeAtNextbirthday == 29):
    CommutationFactor = 17.93
    
elif(AgeAtNextbirthday == 30):
    CommutationFactor = 17.78


elif(AgeAtNextbirthday == 31):
    CommutationFactor = 17.62


elif(AgeAtNextbirthday == 32):
    CommutationFactor = 17.46
elif(AgeAtNextbirthday == 33):
    CommutationFactor = 17.29

elif(AgeAtNextbirthday == 34):
    CommutationFactor = 17.11


elif(AgeAtNextbirthday == 35):
    CommutationFactor = 16.92


elif(AgeAtNextbirthday == 36):
    CommutationFactor = 16.72


elif(AgeAtNextbirthday == 37):
    CommutationFactor = 16.52


elif (AgeAtNextbirthday == 38):
    CommutationFactor = 16.31


elif (AgeAtNextbirthday == 39):
    CommutationFactor = 16.09


elif (AgeAtNextbirthday == 40):
    CommutationFactor = 15.87


elif (AgeAtNextbirthday == 41):
    CommutationFactor = 15.64


elif (AgeAtNextbirthday == 42):
    CommutationFactor = 15.40


elif (AgeAtNextbirthday == 43):
    CommutationFactor = 15.15


elif (AgeAtNextbirthday == 44):
    CommutationFactor = 14.90


elif (AgeAtNextbirthday == 45):
    CommutationFactor = 14.64


elif (AgeAtNextbirthday == 46):
    CommutationFactor = 14.37
    
    
elif (AgeAtNextbirthday == 47):
    CommutationFactor = 14.10
    
elif (AgeAtNextbirthday == 48):
    CommutationFactor = 13.82
    
elif (AgeAtNextbirthday == 49):
    CommutationFactor = 13.54
    
elif (AgeAtNextbirthday == 50):
    CommutationFactor = 13.25
    
elif (AgeAtNextbirthday == 51):
    CommutationFactor = 12.95
    
elif (AgeAtNextbirthday == 52):
    CommutationFactor = 12.66
    
elif (AgeAtNextbirthday == 53):
    CommutationFactor = 12.35
    
elif (AgeAtNextbirthday == 54):
    CommutationFactor = 12.05
    
elif (AgeAtNextbirthday == 55):
    CommutationFactor = 11.73
    
elif (AgeAtNextbirthday == 56):
    CommutationFactor = 11.42
    
elif (AgeAtNextbirthday == 57):
    CommutationFactor = 11.10
    
elif (AgeAtNextbirthday == 58):
    CommutationFactor = 10.78
    
elif (AgeAtNextbirthday == 59):
    CommutationFactor = 10.46
    
elif (AgeAtNextbirthday == 60):
    CommutationFactor = 10.13
    
elif (AgeAtNextbirthday == 61):
    CommutationFactor = 9.81
    
elif (AgeAtNextbirthday == 62):
    CommutationFactor = 9.48
    
elif (AgeAtNextbirthday == 63):
    CommutationFactor = 9.15
    
elif (AgeAtNextbirthday == 64):
    CommutationFactor = 8.82
    
elif (AgeAtNextbirthday == 65):
    CommutationFactor = 8.50
else:
    print('invalid')




basicPension=.5*(float(BasicPay1) + float(SpecialPay1) +float(StagnationPay1)+ float(QualifationPay1) +float(FixedPersonalPay1)+ float(OtherPay1))*float(YearsOfService1)/33
basicpension1=round(basicPension)


CommutationAmount=basicPension*CommutationPercent1/100
CommutationAmount1=round(CommutationAmount)
CommutationValue=CommutationAmount*CommutationFactor*12
CommutationValue1=round(CommutationValue)
ReducedBasicPension=(basicpension1-CommutationAmount1)    
print('\n')
print('\n')
print('\n')
print('----------------------CALCULATED PENSION AND COMMUTATION IS------------------------- ')

print('\n')
print('\n')

print('BASIC PENSION :',basicpension1)
print('___________________________________________________________________________________')
print('COMMUTATION AMOUNT :',CommutationAmount1)
print('___________________________________________________________________________________')
print('REDUCED BASIC PENSION :',ReducedBasicPension)
print('___________________________________________________________________________________')
print('COMMUTATION FACTOR :',CommutationFactor)
print('___________________________________________________________________________________')
print('COMMUTATION VALUE :',CommutationValue1)
print('\n')
print('***********************************************************************************')
print('***********************************************************************************')








