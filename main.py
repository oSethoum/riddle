import random


def main():
    boxes = list(range(0, 100))
    safes = 0
    print("opening boxes randomly")
    for i in range(100):
        random.shuffle(boxes)
        if rand(boxes) == 100:
            safes += 1
    print("safes", safes)

    print("opening boxes with loop method")
    boxes = list(range(0, 100))
    safes = 0
    for i in range(100):
        random.shuffle(boxes)
        if loop(boxes) == 100:
            safes += 1
    print("safes", safes)


def rand(boxes):
    safe = 0
    for i in range(len(boxes)):
        opened = []
        while True:
            box = random.randint(0, len(boxes) - 1)
            if not (box in opened):
                opened.append(boxes[box])
            if len(opened) == (len(boxes) / 2):
                break
        if i in opened:
            safe += 1
    return safe


def loop(boxes):
    safe = 0
    for i in range(len(boxes)):
        opened = []
        box = i
        while True:
            content = boxes[box]
            opened.append(content)
            box = content
            if len(opened) == len(boxes) / 2:
                break
        if i in opened:
            safe += 1
    return safe


main()
