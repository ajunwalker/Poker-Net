from game import Game

##### TOP ROW #####

# Check for double queen 7 points top row
game = Game()
game.play(player=0, row=0, suit=0, number=11)
game.play(player=0, row=0, suit=1, number=11)
assert game.calculate_royalty(player=0) == 7

# Check for triple queen 7 points top row
game = Game()
game.play(player=0, row=0, suit=0, number=11)
game.play(player=0, row=0, suit=1, number=11)
game.play(player=0, row=0, suit=2, number=11)
assert game.calculate_royalty(player=0) == 20

##### MIDDLE ROW #####

# Check if double is not counted in middle row
game = Game()
game.play(player=0, row=1, suit=0, number=0)
game.play(player=0, row=1, suit=1, number=0)
assert game.calculate_royalty(player=0) == 0

# Check for triple queen 2 points middle row
game = Game()
game.play(player=0, row=1, suit=0, number=11)
game.play(player=0, row=1, suit=1, number=11)
game.play(player=0, row=1, suit=2, number=11)
assert game.calculate_royalty(player=0) == 2

# Check for straight 4 points in middle row
game = Game()
game.play(player=0, row=1, suit=0, number=0)
game.play(player=0, row=1, suit=1, number=1)
game.play(player=0, row=1, suit=2, number=2)
game.play(player=0, row=1, suit=1, number=3)
game.play(player=0, row=1, suit=2, number=4)
assert game.calculate_royalty(player=0) == 4

# Check for flush 8 points in middle row
game = Game()
game.play(player=0, row=1, suit=0, number=0)
game.play(player=0, row=1, suit=0, number=4)
game.play(player=0, row=1, suit=0, number=1)
game.play(player=0, row=1, suit=0, number=7)
game.play(player=0, row=1, suit=0, number=8)
assert game.calculate_royalty(player=0) == 8

# Check for full house 12 points in middle row
game = Game()
game.play(player=0, row=1, suit=0, number=0)
game.play(player=0, row=1, suit=1, number=0)
game.play(player=0, row=1, suit=0, number=1)
game.play(player=0, row=1, suit=1, number=1)
game.play(player=0, row=1, suit=2, number=1)
assert game.calculate_royalty(player=0) == 12

# Check for quad 20 points in middle row
game = Game()
game.play(player=0, row=1, suit=0, number=0)
game.play(player=0, row=1, suit=1, number=0)
game.play(player=0, row=1, suit=2, number=0)
game.play(player=0, row=1, suit=3, number=0)
assert game.calculate_royalty(player=0) == 20

# Check for straight flush 30 points in middle row
game = Game()
game.play(player=0, row=1, suit=0, number=0)
game.play(player=0, row=1, suit=0, number=1)
game.play(player=0, row=1, suit=0, number=2)
game.play(player=0, row=1, suit=0, number=3)
game.play(player=0, row=1, suit=0, number=4)
assert game.calculate_royalty(player=0) == 30

# Check for royal flush 50 points in middle row
game = Game()
game.play(player=0, row=1, suit=0, number=9)
game.play(player=0, row=1, suit=0, number=10)
game.play(player=0, row=1, suit=0, number=11)
game.play(player=0, row=1, suit=0, number=12)
game.play(player=0, row=1, suit=0, number=0)
assert game.calculate_royalty(player=0) == 50

##### BOTTOM ROW #####

# Check if double is not counted in bottom row
game = Game()
game.play(player=0, row=2, suit=0, number=0)
game.play(player=0, row=2, suit=1, number=0)
assert game.calculate_royalty(player=0) == 0

# Check if triple is not counted in bottom row
game = Game()
game.play(player=0, row=2, suit=0, number=11)
game.play(player=0, row=2, suit=1, number=11)
game.play(player=0, row=2, suit=2, number=11)
assert game.calculate_royalty(player=0) == 0

# Check for straight 2 points in bottom row
game = Game()
game.play(player=0, row=2, suit=0, number=0)
game.play(player=0, row=2, suit=1, number=1)
game.play(player=0, row=2, suit=2, number=2)
game.play(player=0, row=2, suit=1, number=3)
game.play(player=0, row=2, suit=2, number=4)
assert game.calculate_royalty(player=0) == 2

# Check for flush 4 points in bottom row
game = Game()
game.play(player=0, row=2, suit=0, number=0)
game.play(player=0, row=2, suit=0, number=2)
game.play(player=0, row=2, suit=0, number=4)
game.play(player=0, row=2, suit=0, number=6)
game.play(player=0, row=2, suit=0, number=8)
assert game.calculate_royalty(player=0) == 4

# Check for full house 6 points in bottom row
game = Game()
game.play(player=0, row=2, suit=0, number=0)
game.play(player=0, row=2, suit=1, number=0)
game.play(player=0, row=2, suit=0, number=1)
game.play(player=0, row=2, suit=1, number=1)
game.play(player=0, row=2, suit=2, number=1)
assert game.calculate_royalty(player=0) == 6

# Check for quad 10 points in bottom row
game = Game()
game.play(player=0, row=2, suit=0, number=0)
game.play(player=0, row=2, suit=1, number=0)
game.play(player=0, row=2, suit=2, number=0)
game.play(player=0, row=2, suit=3, number=0)
assert game.calculate_royalty(player=0) == 10

# Check for straight fush 15 points in bottom row
game = Game()
game.play(player=0, row=2, suit=0, number=0)
game.play(player=0, row=2, suit=0, number=1)
game.play(player=0, row=2, suit=0, number=2)
game.play(player=0, row=2, suit=0, number=3)
game.play(player=0, row=2, suit=0, number=4)
assert game.calculate_royalty(player=0) == 15

# Check for full house 25 points in bottom row
game = Game()
game.play(player=0, row=2, suit=0, number=9)
game.play(player=0, row=2, suit=0, number=10)
game.play(player=0, row=2, suit=0, number=11)
game.play(player=0, row=2, suit=0, number=12)
game.play(player=0, row=2, suit=0, number=0)
assert game.calculate_royalty(player=0) == 25
