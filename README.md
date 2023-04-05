# Creating classes and objects

### Description:

There is a **"Warrior"** class. Two units are created from it. Each unit has a health of 100 points. They hit each other in a random order. The one who hits does not lose health. The one who gets hit loses 20 points of health from each attack. After each attack, a message should be displayed indicating which unit attacked and how much health the other unit has left. Once one of them runs out of health, the program should end with a message indicating who won.

### Example:

```python
# Input
unit_1 = Warrior()
unit_2 = Warrior()

unit_1.set_name('Nikita')
unit_2.set_name('Tolik')

b = Battle()

b.battle(unit_1, unit_2)

b.who_won()

# Output, something like
Tolik was attacked, his health is 80
Nikita was attacked, his health is 80
Nikita was attacked, his health is 60
Nikita was attacked, his health is 40
Nikita was attacked, his health is 20
Nikita was attacked, his health is 0

Tolik has won!
```

---

Task 2 from course: <https://younglinux.info/oopython/course>
