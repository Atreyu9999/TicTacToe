from turtle import *

center_grids_positions = {
    1: (1/6, 1/6),
    2: (1/2, 1/6),
    3: (5/6, 1/6),
    4: (1/6, 1/2),
    5: (1/2, 1/2),
    6: (5/6, 1/2),
    7: (1/6, 5/6),
    8: (1/2, 5/6),
    9: (5/6, 5/6)
}
def create_initial_grid():
    screen = Screen()
    screen.setworldcoordinates(-50, -50, screen.window_width() - 1, screen.window_height() - 1)
    forward(screen.window_width() - 50)
    left(90)
    forward(screen.window_height() - 50)
    left(90)
    forward(screen.window_width() - 50)
    left(90)
    forward(screen.window_height() - 50)
    left(90)
    forward((screen.window_width() - 50)/3)
    left(90)
    forward(screen.window_height() - 50)
    right(90)
    forward((screen.window_width() - 50) / 3)
    right(90)
    forward(screen.window_height() - 50)
    left(90)
    forward((screen.window_width() - 50) / 3)
    left(90)
    forward((screen.window_height() - 50)/3)
    left(90)
    forward(screen.window_width() - 50)
    right(90)
    forward((screen.window_height() - 50) / 3)
    right(90)
    forward(screen.window_width() - 50)
    left(90)
    forward((screen.window_height() - 50) / 3)
def create_grid_numbers():
    screen = Screen()
    screen.setworldcoordinates(-50, -50, screen.window_width() - 1, screen.window_height() - 1)
    penup()
    home()
    setposition((screen.window_width() - 50)/6, (screen.window_height() - 50)/6)
    write("1", align="right", font=('Arial', 20, 'normal'))
    forward((screen.window_width() - 50)/3)
    write("2", align="right", font=('Arial', 20, 'normal'))
    forward((screen.window_width() - 50) / 3)
    write("3", align="right", font=('Arial', 20, 'normal'))
    setposition((screen.window_width() - 50) * center_grids_positions[4][0], (screen.window_height() - 50) *center_grids_positions[4][1])
    write("4", align="right", font=('Arial', 20, 'normal'))
    forward((screen.window_width() - 50) / 3)
    write("5", align="right", font=('Arial', 20, 'normal'))
    forward((screen.window_width() - 50) / 3)
    write("6", align="right", font=('Arial', 20, 'normal'))
    setposition((screen.window_width() - 50) * center_grids_positions[7][0], (screen.window_height() - 50) * center_grids_positions[7][1])
    write("7", align="right", font=('Arial', 20, 'normal'))
    forward((screen.window_width() - 50) / 3)
    write("8", align="right", font=('Arial', 20, 'normal'))
    forward((screen.window_width() - 50) / 3)
    write("9", align="right", font=('Arial', 20, 'normal'))
    setposition((screen.window_width() - 50), (screen.window_height() - 50))


def draw_cross(player):
    penup()
    initial_pos = pos()
    setposition(pos()[0] - 50, pos()[1] - 50)
    pendown()
    color(player.player_color)
    setposition(pos()[0] + 100, pos()[1] + 100)
    penup()
    setposition(initial_pos[0] - 50, initial_pos[1] + 50)
    pendown()
    setposition(pos()[0] + 100, pos()[1] - 100)
    penup()
    setposition(initial_pos)  # Spostati al centro
    color('black')

def draw_circle(player):
    color(player.player_color)
    penup()
    initial_pose = pos()
    setposition(initial_pose[0], initial_pose[1] - 50)
    pendown()
    circle(50)
    penup()

def check_win_condition(player, position):
    current_position = position
    horizontal_line = [x for x in player.position_visited if x[1] == current_position[1]]
    vertical_line = [x for x in player.position_visited if x[0] == current_position[0]]
    secondary_diagonal_list = [x for x in player.position_visited if x[0] == x[1]]
    principal_diagonal_list = [x for x in player.position_visited if (1 - x[1] == x[0])]

    if len(horizontal_line) == 3 or len(vertical_line) == 3 or len(secondary_diagonal_list) == 3 or len(principal_diagonal_list) == 3:
        return True
    else:
        return False
class Player:
    screen = Screen()
    def __init__(self, player_name, player_color, player_number):
        self.player_name = player_name
        self.player_color = player_color
        self.player_number = player_number
        self.position_visited = []

    def make_turn(self, position):
        print(center_grids_positions[position][0], center_grids_positions[position][1])
        setposition((self.screen.window_width() - 50) * center_grids_positions[position][0], (self.screen.window_height() - 50) * center_grids_positions[position][1])
        self.position_visited.append(center_grids_positions[position])
        if self.player_number == 1:
            draw_cross(self)
        elif self.player_number == 2:
            draw_circle(self)

def get_players_info():
    colors = ['red', 'blue', 'green']
    first_player_name = input("Name of the first player: ")
    first_player_color_letter = input("Color of the first player, choose from: r = red, b = blue, g = green")

    first_player_color = list(filter(lambda x: x.startswith(first_player_color_letter), colors))[0]

    second_player_name = input("Name of the second player: ")
    second_player_color_letter = input("Color of the second player, choose from: r = red, b = blue, g = green")
    second_player_color = list(filter(lambda x: x.startswith(second_player_color_letter), colors))[0]

    player1 = Player(first_player_name, first_player_color, 1)

    player2 = Player(second_player_name, second_player_color, 2)

    return player1, player2

def change_turn(current_player, player1, player2):
    if current_player.player_number == player1.player_number:
        current_player = player2
    else:
        current_player = player1
    return current_player
if __name__ == '__main__':
    end_game = False
    available_cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player1, player2 = get_players_info()
    screen = Screen()
    current_player = player1
    t = Turtle()
    t.screen.title('Tic Tac Toe')

    create_initial_grid()
    write(f"Player {current_player.player_name} 's turn", align="right", font=('Arial', 10, 'normal'))

    create_grid_numbers()

    while(not end_game and len(available_cells) != 0):

        current_player_choise = input(f"Player: {current_player.player_name}, Choose a cell from : {available_cells}")
        if not int(current_player_choise) or int(current_player_choise) not in available_cells:
            print("Error, try again")
            continue
        available_cells.remove(int(current_player_choise))
        current_player.make_turn(int(current_player_choise))
        end_game = check_win_condition(current_player, center_grids_positions[int(current_player_choise)])
        if end_game or len(available_cells) == 0:
            break
        current_player = change_turn(current_player, player1, player2)

    if end_game:
        bgcolor(current_player.player_color)
        setposition(screen.window_width() / 2, screen.window_height() / 2)
        color('white')
        write(f"{current_player.player_name} won!", align="right", font=('Arial', 30, 'normal'))
    elif len(available_cells) == 0:
        bgcolor('black')
        setposition(screen.window_width() /2, screen.window_height() /2)
        color('white')
        write(f"Draw!", align="right", font=('Arial', 30, 'normal'))

    mainloop()