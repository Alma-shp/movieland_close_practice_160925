# imports:
import theatre


# code:

def main():
    print("Welcome to MovieLand!")

    # initializing the theatre matrix:
    matrix_theatre = theatre.new_theatre()
    print("Ready for invitations!")

    # while loop for each customer:
    num_of_tickets = int(input("How many tickets would you like? enter 0 to exit: "))
    while num_of_tickets != 0:
        name = input("Enter the invitor name: ")

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
            ticket_tuple = (row-1, column-1)
            tickets_list.append(ticket_tuple)

        # checking validation of 'tickets_list':
        while not theatre.tickets_validation(matrix_theatre, tickets_list, name):

            # initializing the tickets list:
            tickets_list = []

            # printing the theatre matrix for the costumer:
            print("Here are the places in the theatre: ")
            theatre.print_matrix(matrix_theatre)

            # getting the tickets from the user:
            for i in range(num_of_tickets):
                print("Where would you like to seat?")
                row = int(input("Enter the row number: "))
                column = int(input("Enter the column number: "))
                ticket_tuple = (row - 1, column - 1)
                tickets_list.append(ticket_tuple)

        # placing the tickets order in the matrix:
        theatre.ticket_placing(matrix_theatre, tickets_list, name)

        # printing the matrix for the user:
        theatre.print_matrix(matrix_theatre)

        # next customer :
        num_of_tickets = int(input("Next customer. How many tickets would you like? enter 0 to exit: "))


main()
