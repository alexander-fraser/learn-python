# Tower of Hanoi Solver
# Alexander Fraser
# 5 March 2020

# Solves a Tower of Hanoi puzzle using a recursive algorithm.

"""

Notes
- There are three sticks: A, B, and C.
- The disks all start on stick A. The goal is to get them to C.
- Disks can only stack in the order they start (i.e. small to large).
- For each disk, you need to get the disks above onto B, so that you 
can move that disk to C.
- There is a recursive element then. The process is the same for 3 or 100 disks.

"""


def print_move(move_from, move_to):
    print("Move disk from {} to {}.".format(move_from, move_to))


def hanoi_move(disks, move_from, move_via, move_to):
    if disks == 0:
        pass
    else:
        hanoi_move(disks-1, move_from, move_to, move_via)
        print_move(move_from, move_to)
        hanoi_move(disks-1, move_via, move_from, move_to)


def main():
    disks_number = 3
    hanoi_move(disks_number, "A", "B", "C")


if __name__ == "__main__":
    main()