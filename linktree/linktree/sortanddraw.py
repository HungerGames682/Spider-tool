import turtle
t = turtle.Turtle()


t.forward(99)

with open('results.txt', 'r') as f:
    bob = f.readlines()
    if bob[0] == bob[1]:
        print("Matching...")



with open('uncut.txt', 'r') as s:
    bob1 = s.readlines()
    
    print(bob1)
    # for i in range(len(bob1)):
