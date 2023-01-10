# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#part1
goalScorer1 = "Ruud Gullit"
goalScorer2 = "Marco van Basten"

goal_1 = 32
goal_2 = 54

scorers = goalScorer1 + " " + str(goal_1) + ", " + goalScorer2 + " " + str(goal_2)

report = f"{goalScorer1} scored in the {goal_1}nd minute\n{goalScorer2} scored in the {goal_2}th minute"
## print (report)

#part2

player = "Ronald Koeman";
first_name = player[:player.find(' ')]

last_name_len = len(player[player.find(' '):])-1

name_short = player[0] + '.' + player[player.find(' '):]

chant = ((first_name + '! ') * len(first_name)).rstrip()
good_chant =  chant[-1] != ' '

## print(chant)
## print(good_chant)