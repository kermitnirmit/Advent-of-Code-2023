import re
from collections import deque
import numpy as np
f = [x for x in open("input.txt").read().strip().split("\n\n")]


def parse(everything):
    ret = []
    for paragraph in everything:
        lines = np.array([list(x) for x in paragraph.split("\n")])
        transpose = lines.transpose()
        ret.append((turn_to_numbers(lines), turn_to_numbers(transpose)))
    return ret


def findMirror(arr):
    # Function to check if an array is a palindrome and return its center index
    def is_palindrome_and_center(subarr):
        # Using np.array_equal for comparison if it's a numpy array
        if isinstance(subarr, np.ndarray):
            if np.array_equal(subarr, subarr[::-1]) and len(subarr) >= 2 and len(subarr) % 2 == 0:
                return len(subarr) // 2
        return -1

    # Convert to numpy array if it's not already
    if not isinstance(arr, np.ndarray):
        arr = np.array(arr)

    # Check for a palindrome starting from the beginning
    for i in range(arr.size, 0, -1):
        center = is_palindrome_and_center(arr[:i])
        if center != -1:
            return center

    # Check for a palindrome ending at the end
    for i in range(0, arr.size):
        center = is_palindrome_and_center(arr[i:])
        if center != -1:
            return arr.size - len(arr[i:]) + center

    return 0

def turn_to_numbers(lines):
    return [row_to_binary(x) for x in lines]

def row_to_binary(row):
    # Replace '#' with '1' and '.' with '0'
    binary_string = ''.join('1' if char == '#' else '0' for char in row)
    return int(binary_string, 2)

c = 0
for horz, vert in parse(f):
    hmirror, vmirror = findMirror(horz), findMirror(vert)
    c += (100 * hmirror + vmirror)
print(c)


# part 2
def hamming_distance(a: int, b: int) -> int:
    x = a ^ b
    set_bits = 0

    while (x > 0) :
        set_bits += x & 1
        x >>= 1

    return set_bits


def findMirror_2(arr):
    def is_palindrome_and_center(subarr):
        totalHamming = 0
        if len(subarr) % 2 == 0 and len(subarr) >= 2:
            for a, b in zip(subarr, subarr[::-1]):
                totalHamming += hamming_distance(a,b)
            if totalHamming == 2: #because i look at each element twice... oops
                return len(subarr) // 2
        return -1

    # Convert to numpy array if it's not already
    if not isinstance(arr, np.ndarray):
        arr = np.array(arr)

    # Check for a palindrome starting from the beginning
    for i in range(arr.size, 0, -1):
        center = is_palindrome_and_center(arr[:i])
        if center != -1:
            return center

    # Check for a palindrome ending at the end
    for i in range(0, arr.size):
        center = is_palindrome_and_center(arr[i:])
        if center != -1:
            return arr.size - len(arr[i:]) + center

    return 0

c = 0
for horz, vert in parse(f):
    hmirror, vmirror = findMirror_2(horz), findMirror_2(vert)
    c += (100 * hmirror + vmirror)
print(c)