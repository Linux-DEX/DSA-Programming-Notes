class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0


class SnakeLadder:
    """
    Players start off the board at 0. A roll that would pass the last
    square is ignored. Landing on a snake or a ladder moves once;
    the destination is not checked for another snake or ladder.

    play(roll, max_turns) asks roll() for each turn and returns the
    winner, or None when max_turns is used up.
    """

    def __init__(self, board_size, snakes, ladders, players):
        if board_size <= 0:
            raise ValueError("board_size must be positive")
        self.board_size = board_size
        self.snakes = dict(snakes)
        self.ladders = dict(ladders)
        self.players = list(players)

    def play(self, roll, max_turns):
        if max_turns <= 0:
            raise ValueError("max_turns must be positive")
        turns = 0
        while turns < max_turns:
            for player in self.players:
                player.position = self._move(player.position, roll())
                turns += 1
                if player.position == self.board_size:
                    return player
                if turns >= max_turns:
                    return None
        return None

    def _move(self, position, rolled):
        if rolled <= 0:
            raise ValueError("roll must be positive")
        target = position + rolled
        if target > self.board_size:
            return position
        if target in self.snakes:
            return self.snakes[target]
        if target in self.ladders:
            return self.ladders[target]
        return target
