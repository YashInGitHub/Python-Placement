# Write a python program representing shopping cart, include methods for adding and removing item and calculating the total price
import sys
class shoppingCart:
    total_Price = int(0)
    itemID = ""
    itemName = ""
    itemPrice = 0

    def __init__(self):
        self.itemList = dict({}) 

    
    def printTotalPrice(self):
        totalPrice = 0
        for item in self.itemList:
            totalPrice += self.itemList[item]["Item Price"]

        print("\n\nTotal Price: ", totalPrice)

    def addItem(self, itemID, itemName, itemRate, quantity = 1):

        if itemID in self.itemList:
            self.itemList[itemID]["Quantity"] += quantity
            self.itemList[itemID]["Item Price"] += itemRate * quantity
        else:
            self.itemList[itemID] = {"Item name" : itemName, "Item Rate" : itemRate, "Quantity" : quantity, "Item Price" : itemRate * quantity}
        print("\nItem Added: ")
        print(self.itemList[itemID], "\n")


    def removeItem(self, itemID, quantity = 1):
        if itemID in self.itemList:
            if self.itemList[itemID]["Quantity"] <= quantity:
                print(self.itemList[itemID]["Quantity"], quantity)
                print("Entire Item Removed")
                del self.itemList[itemID]
            else:
                self.itemList[itemID]["Quantity"] -= quantity 
                self.itemList[itemID]["Item Price"] -= self.itemList[itemID]["Item Rate"] * quantity
                print("\nItem Removed")
                print("Item Status: ")
                print(self.itemList[itemID])

        else:
            print("Item ", itemID, "not available !!!")


print("WELCOME TO THE STORE !!!\n")
cart = shoppingCart()

while(True):
    print("\n1. ADD ITEM  2. REMOVE ITEM  3. DISPLAY CART  4. DISPLAY TOTAL PRICE")
    n = int(input("Choose option: "))

    match(n):
        case 1:
            print("\n1. APPLE : 10\n2. MANGO : 9\n3. ORANGE : 8\n4. AVOCADO : 11\n5. DRAGON FRUIT : 15")
            ch = int(input("Choose option: "))

            match(ch):
                case 1:
                    quant = int(input("Enter quantity: "))
                    cart.addItem("001", "APPLE", 10, quant)
                    
                case 2:
                    quant = int(input("Enter quantity: "))
                    cart.addItem("002", "MANGO", 9, quant)
                    
                case 3:
                    quant = int(input("Enter quantity: "))
                    cart.addItem("003", "ORANGE", 8, quant)
                    
                case 4:
                    quant = int(input("Enter quantity: "))
                    cart.addItem("004", "AVOCADO", 11, quant)
                    
                case 5:
                    quant = int(input("Enter quantity: "))
                    cart.addItem("005", "DRAGON FRUIT", 15, quant)

        case 2:
            itemid = input("Enter item ID: ")
            quan = int(input("Enter quantity: "))
            cart.removeItem(itemid, quan)
            
        case 3:
            print("ITEMS IN YOUR CART")
            for item in cart.itemList:
                print(cart.itemList[item])
            
        case 4:
            cart.printTotalPrice() 

        case _:
            print("Exiting.....")
            sys.exit()







    
        