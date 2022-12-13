lines = [];
sum = 0;

# Calculate common item between three arrays
def common_member(a, b, c):
    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(c)):
                if (a[i] == b[j] == c[k]):
                    return a[i];

# Calculare Priority of letter
def calc_priority(x):
    priority = 0;
    itemCode = ord(x);
    if itemCode >= 65 and itemCode <= 90:
        priority += (itemCode - 38);
    elif itemCode >= 97 and itemCode <= 122:
        priority += (itemCode - 96);
    return priority;

# Save input file to a list
with open('day3-input.txt', 'r') as f:
    for line in f.readlines():
        lines.append(line.strip());
    f.close();

# Itterate through every three lines
count = 0;
for i in range(int(len(lines) / 3)):
    line1 = lines[count];
    line2 = lines[count + 1];
    line3 = lines[count + 2];
    sum+= calc_priority(common_member(line1, line2, line3));
    count += 3;

print(sum);

