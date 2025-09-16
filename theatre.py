from typing import List, Any


def print_matrix(matrix: list):
    """
    (function 1)
    this function receives a matrix and prints it to the user:
    :param matrix: list
    :return: None
    """
    row_index = 1
    for row in matrix:
        print(row_index, end=" ")
        for col in row:
            print(col, end=" ")
        print()
        row_index += 1


def tickets_validation(matrix: list, tickets_list: list, customer: str):
    """
    this function receives a matrix(theatre) and a tickets_list, and checks if the seats are valid.
    (function 2)
    :param customer: str name
    :param matrix: list
    :param tickets_list:tuples list
    :return: boolean
    """

    # checking if seat exist in the theatre:
    for ticket in tickets_list:
        if not is_seat_exist(matrix, ticket):
            return False

    # copy matrix and implementation:
    matrix_copy = copy_matrix(matrix)
    ticket_placing(matrix_copy, tickets_list, customer)
    num_of_tickets = len(tickets_list)
    ticket_count = 0

    this_row = tickets_list[0][0]

    for ticket in tickets_list:

        # saving the num of rows:
        last_row = this_row
        this_row = ticket[0]

        # checking if the chair is not empty:
        if matrix[ticket[0]][ticket[1]] != "_":
            print("some of the seats are taken.\nTry again.")
            return False

        # checking if the tickets are not in the same row:
        if this_row != last_row:
            print("not all tickets are in the same row. \nTry again.")
            return False

    first = True
    for row in matrix_copy:

        for col in row:
            if first:
                col_index = 1
                this_col = col
                first = False

            last_col = this_col
            this_col = col

            if this_col == customer:
                ticket_count += 1

            # checking if there are spaces between the tickets:
            if last_col == customer and this_col == "_" and ticket_count != num_of_tickets:
                print("Not all tickets are linked. \nTry again.")
                return False

            # checking that the tickets are not next to another customer:
            if last_col != customer and last_col != "_" and this_col == customer:
                print("Tickets dont have space around them. \nTry again.")
                return False
            elif this_col != customer and this_col != "_" and last_col == customer:
                print("Tickets dont have space around them. \nTry again.")
                return False

            col_index += 1

    return True


def new_theatre():
    """
    (function 3)
    this function build a new matrix - theatre according to user input
    :return: matrix - theatre
    """
    matrix_theatre = []
    rows_number = int(input("Enter the number of rows in the theatre: "))
    for row in range(rows_number):
        matrix_theatre.append([])
        columns_number = int(input(f"Enter the number of columns in row number {row + 1}: "))
        for col in range(columns_number):
            matrix_theatre[row].append("_")

    return matrix_theatre


def ticket_placing(matrix: list, tickets_list: list, name: str):
    """
    (function 4)
    this function places the tickets ordered inside the matrix.
    :param matrix: list of lists
    :param tickets_list:  list of tuples
    :param name: str
    :return: None
    """
    for ticket in tickets_list:
        matrix[ticket[0]][ticket[1]] = name


def copy_matrix(matrix: list):
    """
    (function 5)
    this function receives a matrix and returns a copy of it
    :param matrix: list of lists
    :return: list of lists
    """
    matrix_copy = []
    row_index = 0
    for row in matrix:
        matrix_copy.append([])
        for col in row:
            matrix_copy[row_index].append(col)

        row_index += 1

    return matrix_copy


def is_seat_exist(matrix: list, seat: tuple):
    """
    (function 6)
    this function checks id a seat number exists in a theatre.
    :param matrix: list
    :param seat: tuple
    :return: boolean
    """

    # if row number doesn't exist:
    rows_len = len(matrix)
    if seat[0] > rows_len or seat[0] < 0:
        print("Invalid row number.\nTry again.")
        return False

    # if seat number doesn't exist:
    seat_len = len(matrix[seat[0]])
    if seat[1] > seat_len or seat[1] < 0:
        print("Invalid seat number.\nTry again.")
        return False

    return True


