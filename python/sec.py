PF=65
ICT =60
EH=40
AP=90
FA=89
PS=70
print("..........................MARKSHEET..........................")
print("NAME          = SALMAN AKBAR AKHUND")
print("S/O           = GHULAM AKBAR AKHUND")
print("D.O.B         = 22-08-2001")
print("INSTITUTE     = SINDH UNIVERSITY")
print("ROLL NO       = 2K22/CSEE/61")
print("************************************************************")
print("************************ACADEMIC RECORDS********************")
print("PROGRAMMING FUNDAMENTALS                           =",PF)
print("INTRODUCTION TO INFO. & COMMUNICATION TECHNOLOGIES =",ICT)
print("ENGLISH COMPOSITION AND COMPREHENSION              =",EH)
print("APPLIED PHYSICS                                    =",AP)
print("FINANCIAL ACCOUNTING                               =",FA)
print("PAKISTAN STUDIES                                   =",PS)

PF=55
ICT =77
EH=60
AP=82
FA=66
PS=50

tot = PF+ICT+EH+AP+FA+PS
avg = tot/5

if avg>=91 and avg<=100:
    print("Your Grade is A1")
elif avg>=81 and avg<91:
    print("Your Grade is A2")
elif avg>=71 and avg<81:
    print("Your Grade is B1")
elif avg>=61 and avg<71:
    print("Your Grade is B2")
elif avg>=51 and avg<61:
    print("Your Grade is C1")
elif avg>=41 and avg<51:
    print("Your Grade is C2")
elif avg>=33 and avg<41:
    print("Your Grade is D")
elif avg>=21 and avg<33:
    print("Your Grade is E1")
elif avg>=0 and avg<21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")
