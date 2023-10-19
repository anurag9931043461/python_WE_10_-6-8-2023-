import database as db

customer=input("""which class would you  like to travel
               1. 1st
               2. 2nd 
               3. 3rd
               """)
start_point=input("Enter you boarding location :")
end_point=input("Enter you destination :")
amount=eval(input("give me money:"))
if 
amount_1st_class=3500.43
amount_2nd_class=2500.43
amount_3rd_class=1500.43

if customer=="1" and amount_1st_class<=amount:
    returning_amount=amount-amount_1st_class
    db.car.execute(f"insert into ticket_booking(class,amount) values('1st',{amount_1st_class})")
    print("kindly collect your cash", returning_amount)
    print("ticket confirmed")
elif customer=="2" and amount_2nd_class<=amount:
    returning_amount=amount-amount_2nd_class
    db.car.execute(f"insert into ticket_booking(class,amount) values('2nd',{amount_2nd_class})")
    print("kindly collect your cash", returning_amount)
    print("ticket confirmed")
elif customer=="3" and amount_3rd_class<=amount:
    returning_amount=amount-amount_3rd_class
    db.car.execute(f"insert into ticket_booking(class,amount) values('3rd',{amount_3rd_class})")
    print("kindly collect your cash", returning_amount)
    print("ticket confirmed")
else:
    print("booking not confirmed, kindly try again")
db.krishna.commit()