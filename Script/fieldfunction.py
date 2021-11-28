import var
import fielddata as fd

def field_load(place):
    var.Field.place = place
    var.Field.size = [fd.size[place][0], fd.size[place][1]]
    var.Field.wall = []
    var.Field.interaction = []
    var.Field.connection = []
    var.Field.enemy = []
    temp = []
    
    for i in range(len(fd.wall[place])):
        temp = []
        
        for j in range(len(fd.wall[place][i])):
            temp.append(fd.wall[place][i][j])

        var.Field.wall.append(temp)

    for i in range(len(fd.connection[place])):
        var.Field.connection.append([[fd.connection[place][i][0][0], fd.connection[place][i][0][1], fd.connection[place][i][0][2], fd.connection[place][i][0][3]], fd.connection[place][i][1], fd.connection[place][i][2], [fd.connection[place][i][3][0], fd.connection[place][i][3][1]]])

    for i in range(len(fd.interaction[place])):
        var.Field.interaction.append([[fd.interaction[place][i][0][0], fd.interaction[place][i][0][1]], fd.interaction[place][i][1], fd.interaction[place][i][2]])

    for i in range(len(fd.enemy[place])):
        var.Field.enemy.append([[fd.enemy[place][i][0][0], fd.enemy[place][i][0][1]], fd.enemy[place][i][1]])


def collision_check():
    player_row = var.Player_Field.position[1] // 80
    player_column = var.Player_Field.position[0] // 80

    direction = {'left' : [0, -1], 'right' : [0, 1], 'up' : [-1, 0], 'down' : [1, 0]}

    target_position = [player_row + direction[var.Player_Field.face][0], player_column + direction[var.Player_Field.face][1]]

    if target_position[0] < 0 or target_position[0] >= len(var.Field.wall) or target_position[1] < 0 or target_position[1] >= len(var.Field.wall[0]):
        return True

    if var.Field.wall[target_position[0]][target_position[1]] == 0:
        return False

    return True

def field_move():
    for i in range(len(var.Field.connection)):
        if var.Player_Field.position[0] >= var.Field.connection[i][0][0] and var.Player_Field.position[0] <= var.Field.connection[i][0][2] and var.Player_Field.position[1] >= var.Field.connection[i][0][1] and var.Player_Field.position[1] <= var.Field.connection[i][0][3]:
            if var.Player_Field.face == var.Field.connection[i][1]:
                if var.Field.connection[i][3][0] == -1:
                    var.Player_Field.position[0] += 0

                elif var.Field.connection[i][3][0] == -2:
                    var.Player_Field.position[0] -= 1280

                elif var.Field.connection[i][3][0] == -3:
                    var.Player_Field.position[0] += 1280

                else:
                    var.Player_Field.position[0] = var.Field.connection[i][3][0]

                if var.Field.connection[i][3][1] == -1:
                    var.Player_Field.position[1] += 0

                elif var.Field.connection[i][3][1] == -2:
                    var.Player_Field.position[1] -= 1280

                elif var.Field.connection[i][3][1] == -3:
                    var.Player_Field.position[1] += 1280

                else:
                    var.Player_Field.position[1] = var.Field.connection[i][3][1]

                var.Field.place = var.Field.connection[i][2]
                field_load(var.Field.place)

                break
