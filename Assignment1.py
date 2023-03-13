import sys
import math


##
def preRecieptS(amount, price, discount, student):
    print("Items; \n\n Lasagna: 16.29$ \n Pizza Pockets: 4.69 \n\nQuantity:\n "+ str(amount) + "\nDiscount: \n " + str(discount) + "\nStudent: \n " + str(student) + "\nPrice: \n " + str(price))
    
def preReciept(amount, price, discount):
    print("Items: \n\n Lasagna: 16.29$ \n Pizza Pockets: 4.69 \n\nQuantity:\n "+ str(amount) + "\nDiscount: \n " + str(discount) + "\nPrice: \n " + str(price))
    
def receiptS(first, last, email, adress, city, province, postal, instruct, phone, dinner, amount, price, student, discount, tax, total):
    print("\n\nFirst and Last Name: " + str(first) + str(last) + "\nEmail: " + str(email) + "\nCity: " + str(city) + "\nAdresss: " + str(adress) + "\nProvince: " + str(province) + "\nPostal: " + str(postal) + "\nInstructions: " + str(instruct) + "\nPhone Number: " + str(phone) + "\n")
    print("Order: "+str(dinner)+"\nAmount: "+str(amount)+"\nPrice:"+str(price)+ "$" "\nStudent: "+str(student)+ "$" "\nDiscount: "+str(discount)+ "$" "\nTax (HST 13%): "+str(tax)+ "$" "\nTotal: "+ str(total) + "$")

def reciept(first, last, email, adress, city, province, postal, instruct, phone, dinner, amount, price, discount, tax, total):
    print("First and Last Name: " + str(first) + " " + str(last) + "\nEmail: " + str(email) + "\nCity: " + str(city) + "\nAdresss: " + str(adress) + "\nProvince: " + str(province) + "\nPostal: " + str(postal) + "\nInstructions: " + str(instruct) + "\nPhone Number: " + str(phone) + "\n")
    print("\nOrder: "+str(dinner)+"\nAmount: "+str(amount)+"\nPrice:"+str(price)+ "$" "\nDiscount: "+str(discount)+ "$" "\nTax (HST 13%): "+str(tax)+ "$" "\nTotal: "+str(total) + "$")
    
def tax(tax13):
    sum = float((tax13 / 100) * 13)
    round(sum,2)
    return sum

def studenDiscount10(disc10):
    sum = float((disc10 / 100) * 10)
    round(sum,2)
    return sum

def discount15(disc15):
    sum = float((disc15 / 100) * 15)
    round(sum,2)
    return sum

def discount20(disc20):
    sum = float((disc20 / 100) * 20)
    round(sum,2)
    return sum

def discount25(disc25):
    sum = float((disc25 / 100) * 25)
    round(sum,2)
    return sum

def total1(Amo1):
    amount1 = Amo1
    sum = float(Amo1 * 16.29)
    round(sum,2)
    return sum

def total2(Amo2):
    amount2 = Amo2
    sum = float(Amo2 * 4.69)
    round(sum,2)
    return sum

def startmenu():
    start = True
    
    while start == True:
        
        uStart = input("Welcome to Amazing Eats II! We are a local food service and delivery buisness here in Waterloo!\nWe take orders over the phone and text\n\nWould you like to order? (Y/N): ")
        
        if uStart == "Y" or uStart == "y":  
        
            uFirst = input("\nWhat is your First Name?: ")
            uLast = input ("what is your Last Name?: ")
            uEmail = input("What is your Email?: ")
            uAdress = input("What is your Delivery Adress?: ")
            uCity = input("What is your City?: ")
            uProvince = input("What is your Province?: ")
            uPostal = input("What is your Postal Code?: ")
            uInstruct = input("Instruction for delivery: ")
            uPhone = input("What is your Phone Number?: ")
            print("\nGreat! We currently only have two menu options which are:\n1. Lasagna (Serves 2) - 16.29$\n2. Pizza Pockets (Serves 1) - 4.69$")
            
            while start == True:
                
                uSelection = input("\nWhich one would you like (1 or 2): ")
            
                while start == True:
                    
                    if uSelection == "1":
                        uAmount1 = int(input("How many Lasagnas would you like?: "))
                        uConfirm1 = input("Is " + str(uAmount1) + " the correct amount? (Y/N): ")
                        
                        if uConfirm1 == "Y" or uConfirm1 == "y":
                            uTotal1 = total1(uAmount1)
                            uStudent1 = input("Are you a Student? (Y/N): ")
                            
                            if uTotal1 < 100:
                                uDiscount15 = discount15(uTotal1)
                                
                                if uStudent1 == "Y" or uStudent1 == "y":
                                    uDiscount10 = studenDiscount10(uTotal1)
                                    afterDiscountSTop = (uTotal1 - uDiscount15) - uDiscount10
                                    taxSTop = tax(afterDiscountSTop)
                                    totalSTop = taxSTop
                                    finalSTop = preRecieptS(uAmount1, uTotal1, uDiscount15, uDiscount10)
                                    finalRecieptSTop = receiptS(uFirst, uLast, uEmail, uAdress, uCity, uProvince, uPostal, uInstruct, uPhone, "Lasagna", uAmount1, uTotal1, uDiscount10, afterDiscountSTop, taxSTop, finalSTop)
                                
                                elif uStudent1 == "N" or uStudent1 == "n":
                                    afterDiscountTop = (uTotal1 - uDiscount15) 
                                    taxTop = tax(afterDiscountTop)
                                    totalTop = taxTop
                                    finalTop = preReciept(uAmount1, uTotal1, uDiscount15)
                                    finalRecieptTop = reciept(uFirst, uLast, uEmail, uAdress, uCity, uProvince, uPostal, uInstruct, uPhone, "Lasagna", uAmount1, uTotal1, afterDiscountTop, taxTop, finalTop)
                                    
                                else:
                                    print("Invalid Input")
                                
                                break
                                    
                            elif uTotal1 > 100 and uTotal1 < 500:
                                uDiscount20 = discount20(uTotal1)
                                afterDiscountS1 = uTotal1 - uDiscount20
                                
                                if uStudent1 == "Y" or uStudent1 == "y":
                                    uDiscount10 = studenDiscount10(uTotal1)
                                    afterDiscountSMiddle = (uTotal1 - uDiscount20) - uDiscount10
                                    taxSMiddle = tax(afterDiscountSMiddle)
                                    totalSMiddle = taxSMiddle
                                    finalSMiddle = preRecieptS(uAmount1, uTotal1, uDiscount20, uDiscount10)
                                    finalRecieptSMiddle = receiptS(uFirst, uLast, uEmail, uAdress, uCity, uProvince, uPostal, uInstruct, uPhone, "Lasagna", uAmount1, uTotal1, uDiscount10, afterDiscountSMiddle, taxSMiddle, finalSMiddle)
                                    
                                elif uStudent1 == "N" or uStudent1 == "n":
                                    afterDiscountMiddle = (uTotal1 - uDiscount20) 
                                    taxMiddle = tax(afterDiscountMiddle)
                                    totalMiddle = taxMiddle
                                    finalMiddle = preReciept(uAmount1, uTotal1, uDiscount20)
                                    finalRecieptMiddle = reciept(uFirst, uLast, uEmail, uAdress, uCity, uProvince, uPostal, uInstruct, uPhone, "Lasagna", uAmount1, uTotal1, afterDiscountMiddle, taxMiddle, finalMiddle)
                                    
                                else:
                                    print("Invalid Input")
                                
                                break
                                    
                            elif uTotal1 > 500:
                                uDiscount25 = discount25(uTotal1)
                                
                                if uStudent1 == "Y" or uStudent1 == "y":
                                    uDiscount10 = studenDiscount10(uTotal1)
                                    afterDiscountSBottom = (uTotal1 - uDiscount25) - uDiscount10
                                    taxSBottom = tax(afterDiscountSBottom)
                                    totalSBottom = taxSBottom
                                    finalSBottom = preRecieptS(uAmount1, uTotal1, uDiscount25, uDiscount10)
                                    finalRecieptSBottom = receiptS(uFirst, uLast, uEmail, uAdress, uCity, uProvince, uPostal, uInstruct, uPhone, "Lasagna", uAmount1, uTotal1, uDiscount10, afterDiscountSBottom, taxSBottom, finalSBottom)
                                    
                                elif uStudent1 == "N" or uStudent1 == "n":
                                    afterDiscountBottom = (uTotal1 - uDiscount25) 
                                    taxBottom = tax(afterDiscountBottom)
                                    totalBottom = taxBottom
                                    finalBottom = preReciept(uAmount1, uTotal1, uDiscount25)
                                    finalRecieptBottom = reciept(uFirst, uLast, uEmail, uAdress, uCity, uProvince, uPostal, uInstruct, uPhone, "Lasagna", uAmount1, uTotal1, afterDiscountBottom, taxBottom, finalBottom)
                                else:
                                    print("Invalid Input")
                                
                                break
                        
                        elif uConfirm1 == "N" or uConfirm1 == "n":
                            print("You can re-do your order now!")
                            break
                        
                        else:
                            print("Invalid Input")
                    
                    elif uSelection == "2":
                        uAmount2 = int(input("How many Pizza Pockets would you like?: "))
                        uConfirm2 = input("Is " + str(uAmount2) + " the correct amount? (Y/N): ")
                        
                        if uConfirm2 == "Y" or uConfirm2 == "y":
                            uTotal2 = total2(uAmount2)
                            uStudent2 = input("Are you a Student? (Y/N): ")
                            
                            if uTotal2 < 100:
                                uDiscount15 = discount15(uTotal2)

                                if uStudent2 == "Y" or uStudent2 == "y":
                                    uDiscount10 = studenDiscount10(uTotal2)
                                    afterDiscountSTop2 = (uTotal2 - uDiscount15) - uDiscount10
                                    taxSTop2 = tax(afterDiscountSTop2)
                                    totalSTop2 = taxSTop2
                                    finalSTop2 = preRecieptS(uAmount2, uTotal2, uDiscount15, uDiscount10)
                                    finalRecieptSTop2 = receiptS(uFirst, uLast, uEmail, uAdress, uCity, uProvince, uPostal, uInstruct, uPhone, "Pizza Pockets", uAmount2, uTotal2, uDiscount10, afterDiscountSTop2, taxSTop2, finalSTop2)
                                
                                elif uStudent2 == "N" or uStudent2 == "n":
                                    afterDiscountTop2 = (uTotal2 - uDiscount15) 
                                    taxTop2 = tax(afterDiscountTop2)
                                    totalTop2 = taxTop2
                                    finalTop2 = preReciept(uAmount2, uTotal2, uDiscount15)
                                    finalRecieptTop2 = reciept(uFirst, uLast, uEmail, uAdress, uCity, uProvince, uPostal, uInstruct, uPhone, "Pizza Pockets", uAmount2, uTotal2, afterDiscountTop, taxTop2, finalTop2)
                                    
                                else:
                                    print("Invalid Input")
                                
                                break
                                    
                            elif uTotal2 > 100 and uTotal2 < 500:
                                uDiscount20 = discount20(uTotal2)

                                if uStudent2 == "Y" or uStudent2 == "y":
                                    uDiscount10 = studenDiscount10(uTotal2)
                                    afterDiscountSMiddle2 = (uTotal2 - uDiscount20) - uDiscount10
                                    taxSMiddle2 = tax(afterDiscountSMiddle2)
                                    totalSMiddle2 = taxSMiddle2
                                    finalSMiddle2 = preRecieptS(uAmount2, uTotal2, uDiscount20, uDiscount10)
                                    finalRecieptSMiddle2 = receiptS(uFirst, uLast, uEmail, uAdress, uCity, uProvince, uPostal, uInstruct, uPhone, "Pizza Pockets", uAmount2, uTotal2, uDiscount10, afterDiscountSMiddle2, taxSMiddle2, finalSMiddle2)
                                
                                elif uStudent2 == "N" or uStudent2 == "n":
                                    afterDiscountMiddle2 = (uTotal2 - uDiscount20) 
                                    taxMiddle2 = tax(afterDiscountMiddle2)
                                    totalMiddle2 = taxMiddle2
                                    finalMiddle2 = preReciept(uAmount2, uTotal2, uDiscount20)
                                    finalRecieptMiddle2 = reciept(uFirst, uLast, uEmail, uAdress, uCity, uProvince, uPostal, uInstruct, uPhone, "Pizza Pockets", uAmount2, uTotal2, afterDiscountMiddle2, taxMiddle2, finalMiddle2)
                                    
                                else:
                                    print("Invalid Input")
                                
                                break
                                    
                            elif uTotal2 > 500:
                                uDiscount25 = discount25(uTotal2)
                                
                                if uStudent2 == "Y" or uStudent2 == "y":
                                    uDiscount10 = studenDiscount10(uTotal2)
                                    afterDiscountSBottom2 = (uTotal2 - uDiscount25) - uDiscount10
                                    taxSBottom2 = tax(afterDiscountSBottom2)
                                    totalSBottom2 = taxSBottom2
                                    finalSBottom2 = preRecieptS(uAmount2, uTotal2, uDiscount20, uDiscount10)
                                    finalRecieptSBottom2 = receiptS(uFirst, uLast, uEmail, uAdress, uCity, uProvince, uPostal, uInstruct, uPhone, "Pizza Pockets", uAmount2, uTotal2, uDiscount10, afterDiscountSBottom2, taxSBottom2, finalSBottom2)
                                
                                elif uStudent2 == "N" or uStudent2 == "n":
                                    afterDiscountBottom2 = (uTotal2 - uDiscount25) 
                                    taxBottom2 = tax(afterDiscountBottom2)
                                    totalBottom2 = taxMiddle2
                                    finalBottom2 = preReciept(uAmount2, uTotal2, uDiscount25)
                                    finalRecieptBottom2 = reciept(uFirst, uLast, uEmail, uAdress, uCity, uProvince, uPostal, uInstruct, uPhone, "Pizza Pockets", uAmount2, uTotal2, afterDiscountBottom2, taxBottom2, finalBottom2)
                                    
                                else:
                                    print("Invalid Input")
                                
                                break
                        
                        elif uConfirm2 == "N" or uConfirm2 == "n":
                            print("You can re-do your order now!")
                            break
                        
                        else:
                            print("Invalid Input")
                        
                        break
                            
                    else:
                        print("Invalid Input")
                    
                    break
                 
            break
        
        elif uStart == "N" or uStart == "n":
             print("Have a Great Day!!")
             break
        
        else:
            ("Invalid Input")
        
        break
        
startmenu()