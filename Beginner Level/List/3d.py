justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
# Find indexes
flash_index = justice_league.index("Flash")
aquaman_index = justice_league.index("Aquaman")

# Remove Green Lantern temporarily if it exists elsewhere
justice_league.remove("Green Lantern")

# Insert Green Lantern in between
min_index = min(flash_index, aquaman_index)
max_index = max(flash_index, aquaman_index)

# Insert after the first of the two (so between them)
justice_league.insert(min_index + 1, "Green Lantern")

print(f"\nStep 4: Separated Aquaman and Flash with Green Lantern: {justice_league}")
