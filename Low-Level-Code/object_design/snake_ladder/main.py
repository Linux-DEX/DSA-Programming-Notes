from snake_ladder import Player, SnakeLadder


def main():
    players = [Player("Ada"), Player("Lin")]
    game = SnakeLadder(
        board_size=10,
        snakes={9: 3},
        ladders={2: 8},
        players=players,
    )
    rolls = iter([2, 1, 2])
    winner = game.play(lambda: next(rolls), max_turns=10)
    print(winner.name, [(player.name, player.position) for player in players])
    assert winner.name == "Ada"
    assert players[0].position == 10
    assert players[1].position == 1

    overshoot = SnakeLadder(10, {}, {}, [Player("Ken")])
    rolls = iter([6, 6])
    assert overshoot.play(lambda: next(rolls), max_turns=2) is None
    assert overshoot.players[0].position == 6


if __name__ == "__main__":
    main()
