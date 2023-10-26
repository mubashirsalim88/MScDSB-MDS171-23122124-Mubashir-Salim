# class MSCDSB:

#     def __init__(self):
#         # Data members / Properties / Attributes
#         self.name = "MSC DS B"
#         self.students = ['A','B','C','D']

#     def printstudents(self): # Member function
#         for student in self.students:
#             print(student)
    

# obj = MSCDSB()
# print(obj.name)
# print(obj.students)

# -----------------------------------------------------------

# class car:

#     def __init__(self,mfg,mdl,yer):
#         self.Manufacturer = mfg
#         self.Model = mdl
#         self.Year = yer
# carname=input("enter name")

# bmw = car(carname,'F Series',2020)
# print(bmw.Manufacturer)

# ----------------------------------------------------------

# Create a class rstaurant, that accepts
# itemname and qty as input 
# inside your class you are having the item
# and its cost [unit price] as a dictionary
# create a function calculate total cost
# that prints the itemname, qty & total cost

class restaurant:

    def __init__(self,itemname,qty):
        self.itemname = itemname
        self.qty = qty
        self.menuitems = {
            'RICE' : 30,
            'CHICKEN' : 100,
            'DAL' : 30,
            'CHAPATI' : 15,
        }

    def total_cost(self):
        print("Total cost of order : ")
        print('Item\t:',self.itemname)
        print('Quantity\t:',self.qty)
        total = self.qty * self.menuitems[self.itemname]
        print('Total\t:',total)

order = restaurant('RICE',4)
order.total_cost()