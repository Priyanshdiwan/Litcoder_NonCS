def combination_sum(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path.copy())
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                continue
            path.append(candidates[i])
            backtrack(i, target - candidates[i], path)
            path.pop()

    result = []
    candidates.sort()
    backtrack(0, target, [])
    return result

in_candidates = input().split(" ")
processed_input=[int(ch) for ch in in_candidates]
target = int(input())
output=combination_sum(processed_input, target)
for lst in output:
    print(" ".join(map(str, lst)))