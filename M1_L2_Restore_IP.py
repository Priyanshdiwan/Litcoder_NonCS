def restore_ip_addresses(s):
    def backtrack(start, path):
        if start == len(s) and len(path) == 4:
            result.append(".".join(path))
            return

        for end in range(start + 1, min(start + 4, len(s) + 1)):
            segment = s[start:end]

            if 0 <= int(segment) <= 255 and (len(segment) == 1 or segment[0] != "0"):
                backtrack(end, path + [segment])
    result = []
    backtrack(0, [])
    return "\n".join(result)
ip_list=input()
print(restore_ip_addresses(ip_list))