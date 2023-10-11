import math

calls_to_merge = 0
calls_to_merge_sort = 0

def merge_sort(A):
    global calls_to_merge_sort
    calls_to_merge_sort += 1
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])
    return merge(left, right)

def merge(left, right):
    global calls_to_merge
    calls_to_merge += 1
    result = []
    i, j = 0, 0
    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

if __name__ == "__main__":
    A = [3, 2, 1, 4, 5, 6, 7, 8, 9]
    print(merge_sort(A))
    print("calls to merge:", calls_to_merge)
    print("calls to merge_sort:", calls_to_merge_sort)
    print("upper bound:", len(A) * math.log2(len(A)))