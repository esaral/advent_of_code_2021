#!/usr/bin/python

with open("$FILE", 'r') as f:
    data = [a.strip() for a in f.readlines()]

numbers = [int(n) for n in data[0].split(',')]
rows = [list(map(int, r)) for r in  [l.split() for l in data[2:] if l]]
boards = [rows[i:i+5] for i in range(0, len(rows), 5)]

draws = []

def main():
    board_wins = [0] * len(boards)
    last_board = False

    for n in numbers:
        draws.append(n)

        if len(draws) < len(boards[0][0]):
            continue
        for i, board in enumerate(boards):
            if board_wins[i] != 1:
                winning_numbers = check_board(board, draws)
                if winning_numbers:
                    board_wins[i] = 1
            if sum(board_wins) == len(boards):
                last_board = True
                break
        if last_board:
            unmarked = sum([v for row in board for v in row if v not in draws])
            print(unmarked * n)
            break


def check_board(board, nums):
    # Check rows
    for row in board:
        if all(v in draws for v in row):
            return row
    
    # Check columns
    for i in range(len(board[0])):
        column = [row[i] for row in board]
        if all(v in draws for v in column):
            return column

main()
