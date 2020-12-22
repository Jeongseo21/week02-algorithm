import sys
'''
5
-101 -3 -1 5 93 (통과)

4
-1000000000 -999999999 333333333 333333334
'''
sol_num = int(input())
solutions = sorted(map(int, input().split()))

def find_value(solution, origin, target):
  pl = 0
  pr = len(solution)-1
  while True:
    pc = (pl + pr) // 2
    if solution[pc] == target:
      return (origin, solution[pc])
    elif target < solution[pc]:
      pr = pc -1
    else:
      pl = pc + 1
    if pr < pl:
      if pr >= 0 and pl < len(solution):
        if solution[pl] - target < target - solution[pr]:
          return (origin, solution[pl])
        else:
          return (origin, solution[pr])
      elif pr < 0:
        return (origin, solution[pl])
      else:
        return (origin, solution[pr])

temp_list = list()
if solutions[0] >= 0:
  print(f"{solutions[0]} {solutions[1]}")
elif solutions[-1] <= 0:
  print(f"{solutions[-2]} {solutions[-1]}")
else:
  for solution in solutions:
    find = find_value(solutions, solution, -solution)
    temp_list.append(find)
  answer = list(map(lambda x : abs(x[0]+x[1]), temp_list))

  new_temp_list = []
  for temp in temp_list:
      if temp[0] - temp[1] != 0:
        new_temp_list.append([abs(sum(temp)), temp])
  print(*sorted(new_temp_list)[0][1])