from brain_games.engine import game_engine
from brain_games.games.brain_calc import DESCRIPTION, generate_question


def main():
    game_engine(DESCRIPTION, generate_question)
    
    
if __name__ == '__main__':
    main()
