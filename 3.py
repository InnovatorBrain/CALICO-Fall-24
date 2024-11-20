import collections
import heapq


# Helper function for Queue behavior (FIFO)
def is_queue(operations):
    queue = collections.deque()
    for op, num in operations:
        if op == "feed":
            queue.append(num)
        elif op == "poop":
            if not queue or queue.popleft() != num:
                return False
    return True


# Helper function for Stack behavior (LIFO)
def is_stack(operations):
    stack = []
    for op, num in operations:
        if op == "feed":
            stack.append(num)
        elif op == "poop":
            if not stack or stack.pop() != num:
                return False
    return True


# Helper function for Heap behavior (Max-Heap)
def is_heap(operations):
    heap = []
    for op, num in operations:
        if op == "feed":
            heapq.heappush(heap, -num)
        elif op == "poop":
            if not heap or -heapq.heappop(heap) != num:
                return False
    return True


def identify_datamon():
    T = int(input().strip())
    all_correct = True

    for _ in range(T):
        operations = []
        while True:
            query = input().strip()
            if query.startswith("feed"):
                _, num = query.split()
                num = int(num)
                operations.append(("feed", num))
            elif query == "poop":
                pooped_number = int(input().strip())
                operations.append(("poop", pooped_number))
            elif query.startswith("guess"):
                species_guess = query.split()[1]
                if species_guess == "queueon" and is_queue(operations):
                    pass
                elif species_guess == "stackeon" and is_stack(operations):
                    pass
                elif species_guess == "heapeon" and is_heap(operations):
                    pass
                else:
                    all_correct = False
                break

    if all_correct:
        print("AC", end="")
    else:
        print("WA", end="")


identify_datamon()
