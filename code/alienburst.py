alien_0 = {'color': 'green', 'points': 5, 'speed': 'slow'}

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# defying the alien speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# moving the alien space ship
alien_0['x_position'] = alien_0['x_position'] + x_increment






