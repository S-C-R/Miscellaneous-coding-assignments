from board import Board
from mccfr import MCCFR
import time

def main():
    game = Board()
    start = time.time()
    solution = MCCFR(game)
    end = time.time()
    print(end - start)

if __name__ == "__main__":
    main()