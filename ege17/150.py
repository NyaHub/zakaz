c = 0
nums = [0,0,0]
mins = 999999

with open("17-1.txt") as file:
    it = 0
    for line in file:
        nums[0], nums[1], nums[2] = nums[1], nums[2], int(line)
        it+=1

        if it<3:
            continue

        if nums[1]%7==0:
            if nums[0]%17!=0:
                c+=1
                mins = min(mins, nums[1] + nums[0])
            if nums[2]%17!=0:
                c+=1
                mins = min(mins, nums[1] + nums[2])

print(c, mins)
