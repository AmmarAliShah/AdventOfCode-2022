sum = 0;
priority = 0;

with open('day3-input.txt', 'r') as f:
    for line in f.readlines():
        items = list(line.strip());
        comp1 = items[:len(items)//2]
        comp2 = items[len(items)//2:]
        
        for i in range(len(comp1)):
            if comp1[i] == comp2[i]:
                itemCode = ord(comp1[i]);
                if itemCode >= 65 and itemCode <= 90:
                    priority += (itemCode - 38);
                elif itemCode >= 97 and itemCode <= 122:
                    priority += (itemCode - 96);
        print(comp1[i]);
        #print("Compartment1: " + str(comp1) + "\nCompartment2: " + str(comp2));
    
f.close();
#print(priority);