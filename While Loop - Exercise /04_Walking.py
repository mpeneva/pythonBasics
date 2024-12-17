goal_steps = 10000
sum_steps = 0

while sum_steps < goal_steps:
    command = input()

    if command == 'Going home':
        steps_to_home = int(input())
        sum_steps += steps_to_home
        break

    sum_steps += int(command)

if sum_steps >= goal_steps:
    print(f"Goal reached! Good job!\n{sum_steps - goal_steps} steps over the goal!")
else:
    print(f"{goal_steps-sum_steps} more steps to reach goal.")