def valid_moves(start):
    x_start = start % 8
    y_start = start // 8
    possible_moves = []
    for step in ((1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)):
        x = x_start + step[0]
        y = y_start + step[1]
        if (x < 0) or (x > 7) or (y < 0) or (y > 7):
            continue
        else:
            possible_moves.append(y*8+x)
    return possible_moves


def answer(src,dest):
    if src == dest:
        return 0
    all_squares = list(range(64))
    all_squares.remove(src)
    current_positions = [src]
    total_moves = 1
    while 1:
        next_moves = []
        for i in current_positions:
            new_moves = valid_moves(i)
            for j in new_moves[:]:
                if j in all_squares:
                    all_squares.remove(j)
                else:
                    new_moves.remove(j)
            next_moves.extend(new_moves)
        if dest in next_moves:
            return total_moves
        else:
            total_moves += 1
            current_positions = next_moves
