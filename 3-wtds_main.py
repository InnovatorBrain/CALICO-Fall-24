import heapq


def interact():
    t = int(input().strip())

    for _ in range(t):
        queue = []
        stack = []
        heap = []
        is_queueon = True
        is_stackeon = True
        is_heapeon = True

        # Track feed and poop queries
        feed_count = 0

        while True:
            num = int(input().strip().split()[1])
            feed_count += 1

            if is_queueon:
                queue.append(num)
            if is_stackeon:
                stack.append(num)
            if is_heapeon:
                heapq.heappush(heap, -num)

            poop = int(input().strip())

            if is_queueon:
                if poop != queue.pop(0):
                    is_queueon = False
            if is_stackeon:
                if poop != stack.pop():
                    is_stackeon = False
            if is_heapeon:
                if poop != -heapq.heappop(heap):
                    is_heapeon = False

            if feed_count >= 3:
                if is_queueon:
                    print("guess queueon")
                elif is_stackeon:
                    print("guess stackeon")
                elif is_heapeon:
                    print("guess heapeon")
                break

            response = input().strip()
            if response == "CORRECT":
                break
            elif response == "WRONG_ANSWER":
                return
