from tabulate import tabulate #imports the tabulate method 

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):#initialises the following objects 
        self.country = country 
        self.code = code 
        self.product = product 
        self.cost = cost 
        self.quantity = quantity 
    

    def get_cost(self):#can be used to get the costs of the object 
        cost = self.cost 
        return cost 


    def get_quantity(self):#can be used to get the quantity of the object 
        quantity = self.quantity
        return quantity


    def __str__(self):#returns the string 
        return f"""the country is {self.country}
the code is {self.code} 
the product is {self.product} 
the cost is {self.cost} 
the quantity is {self.quantity}"""



#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    message = "The list of objects has been created"
    try:
        with open ('inventory.txt', 'r', encoding='utf-8-sig') as text_read: 
            data = text_read.readlines()
            
            for idx, line in enumerate(data): 
                if idx > 0: 
                    new_line = line.strip('\n')
                    new_line = line.split(",")
                    country = new_line[0]
                    code = new_line[1] 
                    product = new_line[2]
                    cost = new_line[3] 
                    quantity = int(new_line[4])  
                    shoe = Shoe(country, code, product, cost, quantity) #creates an object from the line
                    shoe_list.append(shoe)
    except: 
        FileNotFoundError#accounts for the file not found error 
    return message

def capture_shoes():
    message = "Shoe has been appended as object and added to inventory"
    country = input("Please input a country: ")
    code = input("Please input a code: ")
    product = input("Please input a product: ") 
    cost = input("Please input a cost: ")
    while True:
        try:
            quantity = int(input("Please input the quantity: "))
            break 
        except:
            if ValueError: #accounts for a potential value error
                continue 
            else: 
                break  
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe) 
    with open ('inventory.txt', 'a+') as text_write: 
        text_write.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")#appends the new object to the list

    return message 
    

def view_all():
    new_list = [["Country", "Code", "Product", "Cost", "Quantity"]]
    for object in shoe_list: 
        new_list.append([object.country, object.code, object.product, object.cost, int(object.quantity)])
    
    table = (tabulate(new_list))#uses the tabulate function to create an aesthetic output of the data 
    print(table)
    return table


def re_stock():
    message = "New stock has been ordered"
    shoe_quantity = []
    for shoe in shoe_list:
        shoe_quantity.append(shoe.quantity) 
    min_shoe = min(shoe_quantity)
    with open ('inventory.txt', 'r', encoding='utf-8-sig') as text_read: 
        data = text_read.readlines()
        print(data)
        for idx, shoe in enumerate(shoe_quantity): 
            if shoe == min_shoe: 
                update = input("Would you like to update the shoes value: ")
                if update == "yes" or "Yes":
                    new_object = int(input("Please input the restock amount: "))
                    edit_object = shoe_list[idx] 
                    shoe_list[idx] = Shoe(edit_object.country, edit_object.code, edit_object.product, edit_object.cost, new_object)
                    data[idx + 1] = f"{edit_object.country},{edit_object.code},{edit_object.product},{edit_object.cost},{new_object}\n"
                    break 
                else: 
                    break #again accounts for another logical error  
    with open ('inventory.txt', 'w') as text_write: 
        for shoe in data: 
            text_write.write(shoe)

              
    
    return message 

def search_shoe():
    message = ""
    for shoe in shoe_list: 
        if shoe.code == code: 
            print(shoe.__str__()) #gets the shoe code 
    return message

def value_per_item():
    message = ""
    for shoe in shoe_list: 
        shoe = Shoe(shoe.country,shoe.code,shoe.product,shoe.cost,shoe.quantity) #instantiates the object
        total_value = int(shoe.get_quantity()) * int(shoe.get_cost()) #means the method can be accessed   
        message += f"the total value of {shoe.product} is £{str(total_value)}\n"    
    return message

def highest_qty():
    
    quantity = []
    for shoe in shoe_list: 
        
        quantity.append(int(shoe.quantity)) 
    maximum = max(quantity)  
    for_sale = ""
    for shoe in shoe_list:
        if shoe.quantity == maximum: 
            for_sale = f"{shoe.product} is for sale" 
    
    return for_sale


   

#==========Main Menu=============
read_shoes_data()
while True: 
    
    menu = input("""Please select one of the following: 
add a shoe - a 
view shoes - vs 
re-stock a shoe - rs 
search for a shoe - s 
get the value of the shoe - gv 
put a shoe on the market - om 
exit - e
""")

    if menu == 'a': 
        
        capture_shoes() 
    elif menu == 'vs': 
        
        view_all()
    elif menu == 'rs': 
        
        re_stock()
    elif menu == 's': 
        
        code = input("Please input the code of the shoe you would like to obtain: ")
        print(search_shoe()) 
    elif menu == 'gv': 
        
        print(value_per_item())  
    elif menu == 'om': 
        
        print(highest_qty())
    elif menu == 'e': 
        exit()
    else: 
        print("Please select one of the options")#error handling taking into account a potential logical error 
