#!/usr/bin/env python3
from brain_games.game_engine import play_game
from brain_games.games import is_prime


def main():
    play_game(is_prime)


if __name__ == '__main__':
    main()
