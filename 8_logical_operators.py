# in this case all the conditions has to be true to print the final result
is_hungry = True
has_money = True
restaurant_open = True
meeting_friends = False

# AND means that both conditions has to be true to print the final result
# OR means if any of the conditions are true it will print the final result
# AND always goes first then comes OR
# if you put OR first it will read it for both conditions even if the second condition has AND
if is_hungry and restaurant_open and has_money or meeting_friends:
    print("I am starving, I need some food ")