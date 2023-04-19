import random

a = str(input("Want to roll a die? (Y/N): "))
b = random.randint(1, 6)
while a == "Y":
    if b == 1:
        print('''You rolled a    
        ┌─────────┐
        │         │
        │    ●    │
        │         │
        └─────────┘
        ''')
        a = str(input("Want to roll again? (Y/N): "))
        b = random.randint(1, 6)
    elif b == 2:
        print('''You rolled a
        ┌─────────┐
        │  ●      │
        │         │
        │      ●  │
        └─────────┘
    ''')
        a = str(input("Want to roll again? (Y/N): "))
        b = random.randint(1, 6)
    elif b == 3:
        print('''You rolled a
        ┌─────────┐
        │  ●      │
        │    ●    │
        │      ●  │
        └─────────┘
    ''' )
        a = str(input("Want to roll again? (Y/N): "))
        b = random.randint(1, 6)
    elif b == 4:
        print('''You rolled a
        ┌─────────┐
        │  ●   ●  │
        │         │
        │  ●   ●  │
        └─────────┘
    ''' )
        a = str(input("Want to roll again? (Y/N): "))
        b = random.randint(1, 6)
    elif b == 5:
        print('''You rolled a
        ┌─────────┐
        │  ●   ●  │
        │    ●    │
        │  ●   ●  │
        └─────────┘
    ''')
        a = str(input("Want to roll again? (Y/N): "))
        b = random.randint(1, 6)
    elif b == 6:
        print('''You rolled a
        ┌─────────┐
        │  ●   ●  │
        │  ●   ●  │
        │  ●   ●  │
        └─────────┘
    ''')
        a = str(input("Want to roll again? (Y/N): "))
        b = random.randint(1, 6)
print("cool, hope you enjoyed your game")