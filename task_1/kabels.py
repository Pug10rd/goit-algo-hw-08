import heapq

def minimize_cost(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
    
        combined_length = first + second
        total_cost += combined_length
        
        heapq.heappush(cables, combined_length)

    return total_cost


cables = [4, 3, 2, 6]
result = minimize_cost(cables)
print(f"Загальні витрати на злиття: {result}")  # Очікувано: 29
