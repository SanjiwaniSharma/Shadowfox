total_jacks = 100
done_jacks = 0

for _ in range(total_jacks // 10):
    done_jacks += 10
    tired = input(f"You have done {done_jacks} jumping jacks. Are you tired? (yes/no): ").strip().lower()
    
    if tired in ["yes", "y"]:
        print(f"You completed a total of {done_jacks} jumping jacks.")
        break
    else:
        remaining = total_jacks - done_jacks
        if remaining == 0:
            print("Congratulations! You completed the workout.")
        else:
            print(f"{remaining} jumping jacks remaining.")
