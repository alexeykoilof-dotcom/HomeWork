def min_index(lst):
    min_val = lst[0]
    min_idx = 0
    for i in range(1, len(lst)):
        if lst[i] < min_val:
            min_val = lst[i]
            min_idx = i
    return min_idx

def sort_numbers(text):
    nums = text.split()
    for i in range(len(nums)):
        nums[i] = int(nums[i])

    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    result = ""
    for num in nums:
        result += str(num) + " "
    return result.strip()


print(min_index([5, 2, 8, 1, 9]))
print(sort_numbers("8 3 11 1 5"))