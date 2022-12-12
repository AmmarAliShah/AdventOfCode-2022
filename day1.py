sum = 0;
max = 0;
totals = [];


# Itterate through file input and save sums to a array
with open('day1-input.txt', 'r') as f:
    for line in f.readlines():
        if (line != '\n'):
            sum += int(line.strip());
        else:
            totals.append(sum);
            #if (max < sum):
            #    max = sum;
            sum = 0;
    f.close();

# Sort the array
totals.sort(reverse=True);

# Add top 3 and print
total = totals[0] + totals[1] + totals[2]
print(total);