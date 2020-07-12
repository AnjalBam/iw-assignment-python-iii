"""
A. Make pythonic solutions for each of the following data structure
and algorithm problems.
i) Tower of Hanoi for n no. of disks

Tower of Hanoi is a mathematical puzzle where we have three rods and n disks.
 The objective of the puzzle is to move the entire stack to another rod,
  obeying the following simple rules:
1) Only one disk can be moved at a time.
2) Each move consists of taking the upper disk from one of the stacks and
placing it on top of another stack i.e. a disk can only be moved if it is the
uppermost disk on a stack.
3) No disk may be placed on top of a smaller disk.
"""
# tower of hanoi


def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height-1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height-1, with_pole, to_pole, from_pole)


def move_disk(fp,tp):
    print("moving disk from", fp, "to", tp)


move_tower(3,"A","B","C")

