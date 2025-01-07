
# Create an empty dictionary to store contact information 

contacts = {}

a = True

while a == True:

    step_1 = input("If you would like to add a contact write 'add', if you would like to view a contact write 'view',if you would like to delete a contact write 'delete' if you would like to leave the contact book write 'done'")

    if step_1 == 'add':

        new_name = input('Write the name of the contact you would like to add ')
        new_number = input('Write the name of the new number you would like to add ')

        contacts[new_name] = new_number

    elif step_1 == 'view':

        view_name = input("Write the name of the contact you would like to view ")
        try:
            print(view_name, contacts[view_name])
        except:
            print("This following name is not in the contact book ", view_name)

    elif step_1 == 'delete':

        delete_name = input("Write the name of the contact you would like to delete ")
        try:
            contacts.pop(delete_name)
            print("The following contact has been deleted ",delete_name)
        except:
             print("This following name is not in the contact book ", view_name)


    elif step_1 == 'done':
        a = False
        print("You have left the contact book")    

    else:
        print("Error! Try again.")
