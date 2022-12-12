# A = Rock | B = Paper | C = Scissors
# X = Rock | Y = Paper | Z = Scissors
# X = 1; | Y = 2; | Z = 3;
# lost = 0; | draw = 3; | win = 6;

totalScore = 0;

with open('day2-input.txt', 'r') as f:
    for line in f.readlines():
        moves = line.split();
        opponentMove = moves[0];
        yourMove = moves[1];
        if opponentMove == "A" and yourMove == "X":
            totalScore += 4;
        elif opponentMove == "A" and yourMove == "Y":
            totalScore += 8;
        elif opponentMove == "A" and yourMove == "Z":
            totalScore += 3;
        elif opponentMove == "B" and yourMove == "X":
            totalScore += 1;
        elif opponentMove == "B" and yourMove == "Y":
            totalScore += 5;
        elif opponentMove == "B" and yourMove == "Z":
            totalScore += 9;
        elif opponentMove == "C" and yourMove == "X":
            totalScore += 7;
        elif opponentMove == "C" and yourMove == "Y":
            totalScore += 2;
        elif opponentMove == "C" and yourMove == "Z":
            totalScore += 6;
        #print("Opponent: " + moves[0] + " | You: " + moves[1]);
        #print(line);
    f.close();

print(totalScore);