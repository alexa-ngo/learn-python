# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens:
for alien_number in range(3):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow', }
    aliens.append(new_alien)
print(aliens)

for alien in aliens[:2]:
    print(alien)

# Show how many aliens have been created
print(f"Total number of alients: {len(aliens)}")