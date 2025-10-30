from brain_games.engine import game_engine
from brain_games.games.brain_progression import DESCRIPTION, question_generator


def main():
    game_engine(DESCRIPTION, question_generator)


if __name__ == '__main__':
    main()
