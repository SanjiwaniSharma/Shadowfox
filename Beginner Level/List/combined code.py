# Initial list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print(f"Step 1: Initial members: {justice_league}")
print(f"Number of members: {len(justice_league)}")

# Add Batgirl and Nightwing
justice_league += ["Batgirl", "Nightwing"]
print(f"\nStep 2: After adding Batgirl and Nightwing: {justice_league}")

# Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print(f"\nStep 3: Wonder Woman becomes the leader: {justice_league}")

# Separate Aquaman and Flash by inserting Green Lantern between them
flash_index = justice_league.index("Flash")
aquaman_index = justice_league.index("Aquaman")
justice_league.remove("Green Lantern")
min_index = min(flash_index, aquaman_index)
justice_league.insert(min_index + 1, "Green Lantern")
print(f"\nStep 4: Separated Aquaman and Flash with Green Lantern: {justice_league}")

# Replace with new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(f"\nStep 5: New team assembled: {justice_league}")

# Sort alphabetically
justice_league.sort()
print(f"\nStep 6: Alphabetically sorted team: {justice_league}")
print(f"New leader is: {justice_league[0]}")
