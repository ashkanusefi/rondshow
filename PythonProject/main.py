from functions.project_funcs import *

contacts = {}

fake_data(contacts)

show_menu()

while True:
    try:
        item = int(input('choose an item:'))
    except:
        print('invalid text')
        continue

    if item == 1:
        add_new_contact(contacts)


    elif item == 2:
        show_all_contacts(contacts)

        if contacts == {}:
            print('contacts list is empty')


    elif item == 3:
        name = input('who are you looking for?')
        result = search_contacts(contacts, name)

        if not result:
            print('there is no contact with name', name)


    elif item == 4:
        name = input('who do you want to update?')
        search_result = search_contacts(contacts, name)

        if search_result:
            update_result = update_contact(contacts, name)

            if update_result:
                print('contact', name, 'update successfully')
        else:
            print('cannot find the contact with name', name)


    elif item == 5:
        name = input('who do you want to delete?')
        delete_result = delete_contact(contacts, name)

        if delete_result:
            print('contact', name, 'deleted successfully')
        else:
            print('cannot find the contact with name', name)


    elif item == 0:
        response = input('are u sure?y/n')

        if response == 'y':
            exit()


    else:
        print('invalid item')
        show_menu()
