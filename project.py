### ..............owner data..................
import json
import random

try:
    with open("smart_grocery.json","r") as file:
        grocery=json.load(file)

except Exception as e:
    grocery={}


try:
    with open("kart.json","r") as file:
        kart=json.load(file)

except Exception as e:
    kart={}

try:
    with open("bill.json","r") as file:
        bill=json.load(file)

except Exception as e:
    bill={}

def file_save_json():
    try:
        with open("smart_grocery.json", "w") as file:
            json.dump(grocery, file, indent=4)

    except Exception as e:
        print("file not found error")

def file_save_json1():
    try:
        with open("kart.json", "w") as file:
            json.dump(kart, file, indent=4)

    except Exception as e:
        print("file not found error")

def file_save_json2():
    try:
        with open("bill.json", "w") as file:
            json.dump(bill, file, indent=4)

    except Exception as e:
        print("file not found error")

### ..............owner data..................

def add_product():
    product= input("enter a product name: ")
    if product not in grocery:
        quantity=int(input("enter a quantity: "))
        price=int(input("enter a price: "))

        grocery[product]={
            "quantity": quantity,
            "price": price
        }

    else:
        print("product is already present")

        abc=int(input("if you want to update price and quantity type 1: "))

        if abc==1:
            print("do you want to add quantity: press 1")
            print("want to add new price: press 2 ")
            print(" if you want to add both: type 3")

            chio=int(input("enter a choice: "))

            if chio==1:
                new_quantity=int(input("enter a new quantity: "))
                grocery[product]["quantity"] += new_quantity

            elif chio==2:
                new_price= int(input("enter a new quantity: "))
                grocery[product]["price"] = new_price

            elif chio==3:
                new_quantity = int(input("enter a new quantity: "))
                new_price= int(input("enter a new quantity: "))

                grocery[product]["quantity"] += new_quantity
                grocery[product]["price"] = new_price
            else:
                print("enter a proper choice")
    file_save_json()



def low_stock():
    print("out of stock products are: ")
    m=1
    for i, j in grocery.items():

        if (j['quantity'])< 10:
            print(f"{m} {i} and quantity is {j['quantity']}")
            m+=1

def show_QR():
    pass
def generate_bill():
    name=input("name of customer: ")
    total = 0
    for i, j in kart.items():
        price = grocery[i]['price']
        print(f"{i} and quantity {j} sub_total is {j * price}")
        total += j * price

    print(f"total_price is {total}")
    return {
        "name of customer: ": name,
        "total": total
    }

def show_bill():
    k=generate_bill()

    ch=int(input("want to pay online(1) or cash(2) "))

    if ch==1:
        show_QR()
    else:
        print("pay in cash")
    while True:
        is_pay=int(input("is bill pay(1): "))
        if is_pay==1:
            print("bill payed")
            break
        else:
            print("error occur")


def save_bill():
    invoice_no=random.randint(1000,9999)
    bill[invoice_no]=generate_bill()
    file_save_json2()

def load_last_bill():
    save_bill()

###.................customer data...................

def view_product():
    for i, j in grocery.items():
            print(f"items {i} and price is {j['price']} and quantity {j['quantity']}")

def place_order():
    n=int(input("how many items you want to buy"))
    for i in range(n):
        name=input("enter a name of product: ")
        if name in grocery:
            quant=int(input("enter a quantity: "))
            if quant<= grocery[name]['quantity']:
                kart[name]=quant
                grocery[name]['quantity']-=quant
            else:
                print("less quantity available")

    file_save_json1()
    file_save_json()

def see_bill():
    show_bill()
    save_bill()

a=True
while a:
    print("1: owner")
    print("2: customer")
    print("3: exit")
    ch=int(input("enter a choice: "))

    if ch==1:
        owner_user="sai_kirana_store"
        owner_pass="sai@123"

        user=input("enter your username")
        pass1=input("enter your password: ")
        if (user==owner_user) and (pass1==owner_pass):
            z=True
            while z:
                print("1: add products")
                print("2: view low stock items: ")
                print("3: generate bill")
                print("4: show bill")
                print("5: save bill")
                print("6: load last bill")

                choice=int(input("enter a choice: "))

                if choice==1:
                    add_product()
                elif choice==2:
                    low_stock()
                elif choice==3:
                    generate_bill()
                elif choice==4:
                    show_bill()
                elif choice==5:
                    save_bill()
                elif choice==6:
                    load_last_bill()
                elif choice==7:
                    print("thanks for visiting!!!")
                    z=False
                else:
                    print("enter a valid choice")

    elif ch==2:
        z=True
        while z:
            print("1: view product")
            print("2: place order")
            print("3: see bill")
            print("4: back to main menu")

            choice=int(input("enter a choice"))

            if choice==1:
                view_product()
            elif choice==2:
                place_order()
            elif choice==3:
                see_bill()
            elif choice==4:
                print("thank you for visiting!!!")
                z=False
            else:
                print("enter a valid choice!!!")
    elif ch==3:
        print("thank you for visiting!!!")
        a=False
    else:
        print("enter a valid choice!!")

