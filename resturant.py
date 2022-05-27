#classes:
class meals:
 class meal :
     def __init__(meal,name,size):
       meal.name=name
       meal.size=size
 class meal2 :
    name=[]
    L_size=[]
    M_size=[]
    S_size=[]
    offer=[]

#mode choice
def mode():
    print("welcome to our restaurant")
    choice=input("admin or user")
    if choice=="admin":
        admin_mode()
    elif choice=="user":
       print("user") #user
    elif choice=="employee":
        print("employee")#employee
    else:
        print("that is not an allowed choice")
        return mode()
#admin mode
def admin_mode():
    print("welcome admin!!")
    password="12345"
    password_input=input("type ur password:")
    if password==password_input:
        admin_interferance()
    elif len(password_input)!=len(str(password)):
        print("password has ",len(str(password))," characters")
        return admin_mode()
    else:
        print("invalid password")
        return admin_mode()

#admin interference
def admin_interferance():
    print("welcome to our admin varieties")
    print("u can\n1-add meal\n2-change prices\n3-change password\n4-employees monitoring")
    admin_choice=input("what u want")
    if admin_choice=="1":
        new_meal_enter()
    elif admin_choice == 2:
      print("change price")# change price
    elif admin_choice == 3:
      print("change pass")# change password
    elif admin_choice == 4:
      print("employee monior")# employee monitor

def new_meal_enter():
    x=meals.meal.__name__=input("ur meal")
    meals.meal.__sizeof__=(input("size"))
    print(meals.meal.__name__)
    retry=input("try again") 
    if retry=="y":
            meals.meal={
                meals.meal.__name__:
                meals.meal.__sizeof__ }

           print(meals.meal)

    if retry=="n":
        print(meals.meal.__name__)









mode()
