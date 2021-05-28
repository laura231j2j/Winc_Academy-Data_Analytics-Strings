# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Part 1
player_0 = 'Ruud Gullit'
player_1 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = player_0 + ' ' + str(goal_0) + ', ' + player_1 + ' ' + str(goal_1)
print(scorers)

report = (f'{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute')
print(report)

# Part 2
player = 'Wim Kieft'
print(player)

first_name = player[:player.find(' ')]
print(first_name)

last_name_len = len(player[player.find(' ')+1:])
print(last_name_len)

name_short = player[0] + '. ' + player[player.find(' ')+1:]
print(name_short)

chant = ((first_name + '! ') * (len(first_name) - 1)) + (first_name + '!')
print(chant) # chant blijft ook na deze aanpassingen en het gebruik van de naam van een andere speler zorgen voor een foutmelding .

good_chant = (chant[-1] != ' ')
print(good_chant)
