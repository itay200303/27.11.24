
# 1.
def sogrim(s: str) -> bool:

    stack = []

    for char in s:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        elif char == ')' or char == '}' or char == ']':
            if not stack:
                return False
            top = stack.pop()
            if char == ')' and top != '(':
                return False
            if char == '}' and top != '{':
                return False
            if char == ']' and top != '[':
                return False

    return len(stack) == 0

print(sogrim("()"))  # True
print(sogrim("()[]{}"))  # True
print(sogrim("(]"))

# 2.
def remove_dup(sorted_list):
    result = []

    for item in sorted_list:
        if not result or result[-1] != item:
            result.append(item)

    return result

print(remove_dup([1, 1, 2, 3, 3, 3, 4, 5]))

# 3.
def merge_sorted_lists(list1, list2):
    x, y = 0, 0
    merged_list = []
    while x < len(list1) and y < len(list2):
        if list1[x] <= list2[y]:
            merged_list.append(list1[x])
            x += 1
        else:
            merged_list.append(list2[y])
            y += 1
    while x < len(list1):
        merged_list.append(list1[x])
        x += 1
    while y < len(list2):
        merged_list.append(list2[y])
        y += 1

    return merged_list

print(merge_sorted_lists([1, 3, 5, 7], [2, 4, 6, 8]))
