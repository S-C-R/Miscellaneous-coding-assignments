from board import Board

import random, time

def main():
    game = Board()
    start = time.time()
    playx = 1
    playy = 1
    while not game.game_over():
        game.add_move(playx,playy)
        playx = random.randint(0,2)
        playy = random.randint(0,2)
        print(game)
    print(game.winner)
    end = time.time()
    print(end - start)
    
if __name__ == "__main__":
	main()