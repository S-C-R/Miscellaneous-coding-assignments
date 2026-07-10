from board import Board
from minimax import Minimax

import time

def main():
    game = Board()
    start = time.time()
    solution = Minimax(game)
    end = time.time()
    print(end - start)

if __name__ == "__main__":
    main()