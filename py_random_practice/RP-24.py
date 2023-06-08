# Drawing a game board

p = int(input("enter column and row number= "))

# defining function for making matrices


def game_board(sqr_matrix):
    a = " - - - "
    b = "|      "
    for s in range(sqr_matrix):
        print(a*sqr_matrix)
        print(b*(sqr_matrix+1))
    return print(a*p)


# result = game_board(p)
print(game_board(p))
