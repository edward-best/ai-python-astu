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
