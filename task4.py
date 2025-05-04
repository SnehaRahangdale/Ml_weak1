# Task 4
football_players = {"Alice", "Bob", "David"}
cricket_players = {"Bob", "Charlie", "Eve"}

both = football_players & cricket_players
only_one = football_players ^ cricket_players
none = {"Alice", "Bob", "Charlie", "David", "Eve", "Frank"} - (football_players | cricket_players)

print("Both:", both)
print("Only one:", only_one)
print("None:", none)