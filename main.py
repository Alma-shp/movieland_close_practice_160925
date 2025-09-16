# imports:
import theatre


# code:

def main():
    print("Welcome to MovieLand!")

    # initializing the theatres dict:
    theatres_dict = {}

    # getting the number of theatres:
    theatres_number = input("How many theatres are there:")
    # input validation:
    while not theatres_number.isdigit():
        print("theatres number should be a number.\nTry again.")
        theatres_number = input("Enter the number of theatres:")

    for i in range(int(theatres_number)):
        movie_name = input(f"Enter the movie name in theatre number {i + 1}: ")

        # initializing the theatre matrix:
        matrix_theatre = theatre.new_theatre()

        # creating a dict key of num-of-theatre : [movie_name, matrix]
        theatres_dict[i + 1] = [movie_name, matrix_theatre]

        # # adding the dict to the whole theatres list:
        # theatres_list.append(theatres_dict)

    print("Ready for invitations!")

    # while loop for each customer:
    num_of_tickets = int(input("How many tickets would you like? enter 0 to exit: "))
    name = input("Enter the invitor name: ")
    while num_of_tickets != 0:

        # printing movie options to the user:
        print("Here is a list of movies in each theatre: ")
        for each in theatres_dict:
            print(f"Theatre number {each}: {theatres_dict[each][0]}")

        # getting the number of theatre from the user:
        number_of_theatre = int(input("Enter the theatre number: "))

        # saving the current matrix_theatre to work with:
        matrix_theatre = theatres_dict[number_of_theatre][1]

        # printing the theatre matrix for the costumer:
        print("Here are the places in the theatre: ")
        theatre.print_matrix(matrix_theatre)

        # initializing the tickets list:
        tickets_list = []

        # getting the tickets from the user:
        for i in range(num_of_tickets):
            print("Where would you like to seat?")
            row = int(input("Enter the row number: "))
            column = int(input("Enter the column number: "))
            ticket_tuple = (row - 1, column - 1)
            tickets_list.append(ticket_tuple)

        # checking validation of 'tickets_list':
        while not theatre.tickets_validation(matrix_theatre, tickets_list, name):
            flag = True
            break

        if flag:
            flag = False
            continue

        # placing the tickets order in the matrix:
        theatre.ticket_placing(matrix_theatre, tickets_list, name)

        # printing the matrix for the user:
        theatre.print_matrix(matrix_theatre)

        # next customer :
        num_of_tickets = int(input("Next customer. How many tickets would you like? enter 0 to exit: "))
        name = input("Enter the invitor name: ")


main()
