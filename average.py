name=input("Enter your First Name:")
family=input("Enter your Last Name:")

score1=float(input("Enter your 1st score:"))
score2=float(input("Enter your 2nd score:"))
score3=float(input("Enter your 3th score:"))

average=(score1+score2+score3)/3

if average>=17:
    print("dear",name,family,"your average is:",average,"it is GREAT:D")

elif average<17 and average>=12:
    print("dear",name,family,"your average is",average,"it is NORMAL")

elif average<12:
    print("dear",name,family,"your average is",average,"it is a FAIL!")