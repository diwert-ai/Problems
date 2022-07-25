data = [1,1,1,3]

data.sort()
all_sum = sum(data)
print(sum(data))

half_sum = 0

for i in range(len(data)):
    half_sum += data[i]
    if half_sum > all_sum:
        break
    i += 1

print(i)
print(min(all_sum - half_sum, half_sum - data[i-1]))



