input_ = open("Day 1/input.txt", "r")

elfs: list[list] = [[]]
elf_index = 0



for line, content in enumerate(input_, 1):

    content = content.removesuffix("\n")

    if content.isnumeric():
        elfs[elf_index].append(int(content))

    else:
        elfs.append([])
        elf_index += 1

sums = []

for elf in elfs:
    sums.append(sum(elf))

maximum_cals = max(sums)
elf = sums.index(maximum_cals)

print(f"Elf carrying the most calories is elf {elf} with a total of {maximum_cals} calories")

sums.sort(reverse=True)

print(f"The top 3 elfs are carrying a total of {sums[0] + sums[1] + sums[2]} calories")