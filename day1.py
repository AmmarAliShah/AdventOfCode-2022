sum = 0;
max = 0;

with open('day1-input.txt', 'r') as f:
    for line in f.readlines():
        if (line != '\n'):
            sum += int(line.strip());
            #print(type(int(line)));
        else:
            if (max < sum):
                max = sum;
            sum = 0;
    f.close();

print(max);