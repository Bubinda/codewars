# The Wumpus world is a simple world example to illustrate the worth of a knowledge-based agent and to represent knowledge representation.

# Wumpus world rules

# The Wumpus world is a cave consisting of 16 rooms (in a 4x4 layout) with passageways between each pair of neighboring rooms. This cave contains:

# 1 agent - always starts from room (0, 0)
# 1 wumpus, a monster who eats anybody entering his room - inside random empty room
# 1 treasure - inside random empty room
# 1-3 bottomless pits - each inside a random empty room
# (The original rules for valid cave layouts are slightly different, but they were changed for the sake of this kata.)

# Initially the agent doesn't know the contents of each room. He navigates the cave blindly having only 2 sources of information:

# a smell sensor which signals about the presence of Wumpus in any of the neighboring rooms
# a wind sensor which signals about the presence of a bottomless pit in any of the neighboring rooms
# The agent's goal is to find the hidden treasure while avoiding the bottomless pits and avoiding or killing the Wumpus - if the Wumpus's exact location can be determined, the agent can throw a spear in his direction, across a horizontal/vertical row of rooms, and kill the monster (original rules don't require knowing Wumpus's exact location: instead you can take a guess when throwing the spear and an additional sound sensor will tell you whether it hit the monster, but this was also changed for the sake of this kata).

# Task

# Implement a function which receives a cave representing a configuration of the Wumpus world and returns a boolean value signifying whether it's possible to find the treasure safely.

# Note: the cave is provided to you for simplicity, so that there would be no need in an oracle-function/oracle-object which would have to be queried for the smell and wind sensors' states in the given room; although, you can print the cave and see where everything is located for yourself, the agent doesn't know the cave layout, and all his actions must be based on the information that he has gathered, i.e. "I can move here because I know that there will be no bottomless pit in this room" and "I can throw the spear in this direction because I know that Wumpus is located across this row/column". At the same time, your agent does know how many bottomless pits there are - this is the only piece of information that both you and your agent share, and it will not be provided as a separate function argument since the input cave already encodes this information.

# Input cave format

# The input will always be a 4x4 cave filled with following characters:

# 'W' - Wumpus
# 'G' - treasure (gold)
# 'P' - bottomless pit
# '_' - empty space
# Visual example

# Additional legend:

# Agent - agent's initial location
# s - smell from Wumpus
# w - wind from bottomless pits
# |------------|------------|------------|------------|
# |            |            |            |            |
# |            |            |            |            |
# |    Agent                                          |
# |            |            |            |  wwwwwwww  |
# |            |            |            |  wwwwwwww  |
# |-----  -----|-----  -----|-----  -----|-----  -----|
# |            |            |            |            |
# |            |            |         ww |            |
# |                                   ww       Pit    |
# |  ssssssss  |            |  wwwwwwwww |            |
# |  ssssssss  |            |  wwwwwwww  |            |
# |-----  -----|-----  -----|-----  -----|-----  -----|
# |            |            |            |  wwwwwwww  |
# |            | ss      ww |            | wwwwwwwww  |
# |   Wumpus     ss Gold ww       Pit      ww         |
# |            | ss      ww |            | ww         |
# |            |            |            |            |
# |-----  -----|-----  -----|-----  -----|-----  -----|
# |  ssssssss  |            |  wwwwwwww  |            |
# |  ssssssss  |            |  wwwwwwww  |            |
# |                                                   |
# |            |            |            |            |
# |            |            |            |            |
# |------------|------------|------------|------------|




def wumpus_world(cave):
    visited = [[False] * 4 for _ in range(4)]
    return dfs(0, 0, cave, visited)

def dfs(row, col, cave, visited):
    if row < 0 or row >= 4 or col < 0 or col >= 4:
        return False
    
    if visited[row][col]:
        return False
    
    visited[row][col] = True
    
    if cave[row][col] == 'G':
        return True
    
    if cave[row][col] == 'P' or cave[row][col] == 'W':
        return False
    
    neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    
    for neighbor in neighbors:
        n_row, n_col = neighbor
        if n_row >= 0 and n_row < 4 and n_col >= 0 and n_col < 4:
            if cave[n_row][n_col] != 'P' and cave[n_row][n_col] != 'W':
                if dfs(n_row, n_col, cave, visited):
                    return True
    
    return False



cave = [
            [*"__WP"],
            [*"____"],
            [*"__P_"],
            [*"P_G_"]
]



# cave = [
#             [*"__PG"],
#             [*"___W"],
#             [*"__PP"],
#             [*"____"]
#         ]

result = wumpus_world(cave)
print(result)  # True


