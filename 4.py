from collections import Counter

def solve():
    T = int(input()) 
    for _ in range(T):
        N = int(input())  
        faces = list(map(int, input().split()))  

        freq = Counter(faces)
        
        total_sum = sum(faces)
        
        min_expected_payment = float('inf')
        best_x = -1
        
        for x in freq:
            new_sum = total_sum - (x * freq[x])
            expected_payment = new_sum / N
            
            if expected_payment < min_expected_payment:
                min_expected_payment = expected_payment
                best_x = x
        
        print(best_x)

solve()
