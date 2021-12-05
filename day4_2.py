import numpy
inputLines = [x for x in open("Data/day4.txt", "r").readlines()]

winning_numbers = [int(x) for x in inputLines[0].split(',')]
boards_lines = [[int(x) for x in numbers.split()] for numbers in [line for line in inputLines[1:] if line.strip()]]
boards = [boards_lines[board_index: board_index + 5] for board_index in range(0, len(boards_lines), 5)]

def isBoardWinning(board, numbers):
    horizontalRowsWinning = any([set(row).issubset(numbers) for row in board])
    verticallRowsWinning = any([all([(row[index] in set(numbers)) for row in board]) for index in range(0, 5)])
    return horizontalRowsWinning or verticallRowsWinning

def getRoundResult(boards, winning_numbers):
    winning_boards_indexes = set()
    for index, board in enumerate(boards):
        if isBoardWinning(board, winning_numbers):
            winning_boards_indexes.add(index)
    return winning_boards_indexes

last_board_index = 0
for round in range(0, len(winning_numbers)):
    print(f"ROUND {round + 1}")
    winning_boards_indexes = set()
    round_results = getRoundResult(boards, winning_numbers[:round + 1])
    winning_boards_indexes = winning_boards_indexes | round_results
    print(round_results)
    if len(winning_boards_indexes) == len(boards) - 1:
        last_board_index = set(range(0, len(boards))).difference(winning_boards_indexes).pop()
    if len(winning_boards_indexes) == len(boards):
        print("WINNING BOARD: ", boards[last_board_index])
        flat_board = {item for sublist in boards[last_board_index] for item in sublist}
        unmarked_numbers = flat_board.difference(set(winning_numbers[:round + 1]))
        print(unmarked_numbers)
        print(sum(unmarked_numbers) * winning_numbers[round])
        break
