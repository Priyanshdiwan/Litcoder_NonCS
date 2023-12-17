def is_possible(tasks, n, k, mid):
    workers = 0
    current_time = 0
    for i in range(n):
        current_time += tasks[i]

        if current_time > mid:
            workers += 1
            current_time = tasks[i]
    workers += 1  
    return workers <= k
def min_time_to_complete_tasks(tasks, k):
    n = len(tasks)
    low, high = max(tasks), sum(tasks)

    while low < high:
        mid = (low + high) // 2

        if is_possible(tasks, n, k, mid):
            high = mid
        else:
            low = mid + 1
    return low
if __name__ == "__main__":
    n = int(input())
    tasks = list(map(int, input().split()))
    k = int(input())
    result = min_time_to_complete_tasks(tasks, k)
    print(result)