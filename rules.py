from color import Color

def board_diff(old: list[list[Color]], current: list[list[Color]]) -> int:
    total = 0
    for i in range(8):
        for j in range(8):
            if not old[i][j] is current[i][j]:
                total += 1
    return total

def check_turn_validness(turn_made: tuple[int, int], allowed: list[tuple[int, int]]) -> bool:
    for expected_turn in allowed:
        if turn_made == expected_turn:
            return True
    return False

def color_fields(board: list[list[Color]], current_color) -> list[tuple[int, int]]:
    return [[(i, j) for j in range(8) if board[i][j] is current_color] for i in range(8)]

def check_field_validness(field: tuple[int, int]) -> bool:
    return (field[0] >= 0 and field[0] < 8) and (field[1] >= 0 and field[1] < 8)

def available_fields(board: list[list[Color]], current_color) -> list[tuple[int, int]]:
    result = []
    player_fields = color_fields(board, current_color)
    enemy_color = Color.BLACK if current_color is Color.WHITE else Color.WHITE
    for field in player_fields:
        for direction in [(-1, -1), (-1, 0), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 0), (1, 1)]:
            current_field = (field[0] + direction[0], field[1] + direction[1])
            while check_field_validness(current_field) and board[current_field[0], current_field[1]] is enemy_color:
                current_field = (current_field[0] + direction[0], current_field[1] + direction[1])
                if check_field_validness(current_field) and board[current_field[0], current_field[1]] is Color.EMPTY:
                    result.append(current_field)
    return result