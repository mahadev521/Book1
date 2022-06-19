def towersOfHanoi(numdisks,start=1,end=3):
    if numdisks:
        towersOfHanoi(numdisks-1,start,6-start-end)
        print(f'move disk {numdisks} from peg {start} to peg {end}')
        towersOfHanoi(numdisks-1,6-start-end,end)

towersOfHanoi(20)