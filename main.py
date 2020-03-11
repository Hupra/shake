import re
import numpy as np
import numba as nb
import math
import time
from random import *


def get_text():
    with open("shakespeare-complete-works.txt", "r+", encoding="utf-8-sig") as f:
        return re.findall(r"[a-z][a-z-']*", f.read().lower())


def selection_sort(arr):
    a = arr[:]
    n = len(a)

    # loop through all elements except the last one
    for i in range(n - 1):
        min_index = i

        # loop from current index +1 to end of array
        for j in range(i + 1, n):

            # if we find a lower val then our current min_index,
            # we change it to the index of the new value
            if a[min_index] > a[j]:
                min_index = j

        # swap elements #pylife
        a[i], a[min_index] = a[min_index], a[i]

    return a


def insertion_sort(arr):
    a = arr[:]
    n = len(a)

    # skip the first since that is gonna be our subarray,
    # and is already sorted as it's only one value
    for i in range(1, n):
        # the value i wanna relocate
        val = a[i]
        # the position of the value at this moment
        pos = i

        # is the value left of our value bigger?
        # then we keep going further left
        while pos > 0 and a[pos - 1] > val:
            # we moved the left value onto our current position
            # and declares our new position, that we will then
            # test to see if we have to move further left in our while()
            a[pos] = a[pos - 1]
            pos = pos - 1

        # sets the new position of our value
        a[pos] = val

    return a


def heapify(a, n, i):
    # i could also be called "top", so think of i as
    # the top element of the small heap (3 elements)
    # largest, right, left are all indexes
    # setting largest to root
    largest = i
    left = 2 * i + 1  # i = 5 l = 11
    right = 2 * i + 2  # i = 5 r = 12

    # left < n checks if left is out of range
    if left < n and a[left] > a[largest]:
        largest = left

    if right < n and a[right] > a[largest]:
        largest = right

    if i != largest:
        # swap values
        a[i], a[largest] = a[largest], a[i]

        # we call heapify again to make sure our change
        # didnt ruin something further down the tree, we do
        # this recursivly all the way to the root of the tree (the top)
        heapify(a, n, largest)

####

# insert 1  O(log N)
# sort      O(n log N)
# swim      O(log n)


###
def heap_sort(arr):
    a = arr[:]
    n = len(a)

    # starts our maxheap
    # we go backwards because we wanna,
    # start at the bottom of the tree.
    # loop from n to/including 0 -> 5,4,3,2,1,0
    for i in range(n, -1, -1):
        heapify(a, n, i)

    # extract the numbers
    # we loop backwards because we put the largest number at the end
    # and then dont look at them again
    for i in range(n - 1, 0, -1):
        # swap the numbers because we want the largest number last
        # and then because of our loop we dont look at it again
        a[i], a[0] = a[0], a[i]

        # we want the next largest value at the top so we have to run heapify again
        # we use "i" as the second value because we dont wanna look at values after that
        # because that part is already sorted
        heapify(a, i, 0)

    return a


def merge_sort(arr):

    a = arr[:]

    def merge_sort(arr):
        if(len(arr) > 1):

            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            merge_sort(left)
            merge_sort(right)

            left_cursor = right_cursor = x = 0

            # hvis left_cursor er mindre end længden på left & right_cursor er mindre end længden på
            # bliver ved med at kigge hvilke array har den laveste værdi og sætter den til venstre!!!(altså på vores x)
            while left_cursor < len(left) and right_cursor < len(right):
                # Hvis venstre er mindre end højre
                if left[left_cursor] < right[right_cursor]:
                    # sætter vi arr[x] til den venstre value
                    arr[x] = left[left_cursor]
                    # og vi tilføjer en til vores left cursor
                    left_cursor += 1
                else:
                    arr[x] = right[right_cursor]
                    right_cursor += 1

                # tilføjer en til x da det er den næste værdi vi skal sætte
                x += 1

            # Tilføjer resterende værdier....
            while left_cursor < len(left):
                arr[x] = left[left_cursor]
                left_cursor += 1
                x += 1

            while right_cursor < len(right):
                arr[x] = right[right_cursor]
                right_cursor += 1
                x += 1

    merge_sort(a)
    return a


def trie_sort(arr):

    class Node:
        def __init__(self, char):
            self.char = char
            self.children = [None for _ in range(28)] #np.empty(28, dtype="object")
            self.counter = 0

    def char_to_int(char):
        val = ord(char) - 95
        if char == "'": val = 0
        if char == "-": val = 1
        return val

    def add_to_trie(node, word):

        # loop every char in word
        for char in word:

            # convert our char to a number
            val = char_to_int(char)

            # if the node doesn't contain our char
            # we make a new node with that char
            if(node.children[val] is None):
                node.children[val] = Node(char)

            node = node.children[val]

        node.counter += 1

    # sets a root node to get started
    root = Node("")

    # adds every word from the array to our Trie
    for word in arr:
        add_to_trie(root, word)

    # converts our Trie to a sorted array
    res = []

    def add_to_res(node, prefix=""):

        # Constructs the word from the chars that have come
        # before and the current char
        word = prefix + node.char

        # if counter > 0 it means we are at a real word
        # and we add x of that word to our array
        for _ in range(node.counter):
            res.append(word)

        # loop through every node
        # and call this function
        # on the node to see if its a word
        # and go to its children
        for child in node.children:
            if child is not None:
                add_to_res(child, word)

    def add_to_res_reversed(node, prefix=""):

        # Constructs the word from the chars that have come
        # before and the current char
        word = prefix + node.char

        # loop through every node
        # and call this function
        # on the node to see if its a word
        # and go to its children
        for idx in range(28):
            child = node.children[27 - idx]
            if child is not None:
                add_to_res_reversed(child, word)

        # if counter > 0 it means we are at a real word
        # and we add x of that word to our array
        for _ in range(node.counter):
            res.append(word)

    add_to_res(root)

    return res


def quick_sort(arr):
    a = arr[:]

    def quick_sort(arr):

        n = len(arr)

        if n < 2:
            return arr

        last = n - 1
        rand = randint(0, last)
        arr[last], arr[rand] = arr[rand], arr[last]

        pivot = arr.pop()
        lower = []
        greater = []

        for x in arr:
            if x > pivot:
                greater.append(x)
            else:
                lower.append(x)

        return quick_sort(lower) + [pivot] + quick_sort(greater)

    return quick_sort(a)


def quick_sort2(arr):

    def quick_sort(arr):

        n = len(arr)
        if n < 2:
            return arr

        pivot = choice(arr)
        same = []
        lower = []
        greater = []

        for x in arr:
            if x > pivot:
                greater.append(x)
            elif x < pivot:
                lower.append(x)
            else:
                same.append(x)

        return quick_sort(lower) + same + quick_sort(greater)

    return quick_sort(arr[:])


def merge_sort2(arr):

    a = arr[:]
    new_a = arr[:]

    def merge(left, mid, right):

        left_cursor = left       # deres   i
        right_cursor = mid + 1   # deres   j

        # right + 1 to include the value
        for x in range(left, right + 1):
            new_a[x] = a[x]

        for x in range(left, right + 1):
            # Hvis vesntre pointer er større end mid vil der ikke være flere "venstre" værdier tilbage og vi tager derfor fra højre
            if left_cursor > mid:
                a[x] = new_a[right_cursor]
                right_cursor += 1

            # Hvis højre pointer er kommet helt forbi right, tager vi fra venstre
            elif right_cursor > right:
                a[x] = new_a[left_cursor]
                left_cursor += 1

            # Kigger om den højre værdi er mindre end den venstre værdi
            # og ligger den ind som næste element
            elif new_a[right_cursor] < new_a[left_cursor]:
                a[x] = new_a[right_cursor]
                right_cursor += 1

            # Ellers må værdien enten være det samme eller større og så ligger vi den ind som det næste
            else:
                a[x] = new_a[left_cursor]
                left_cursor += 1

    def sort(left, right):

        # [7,5,2,9,1,4]
        elements = right - left + 1  # index - index + 1
        if(elements > 1):
            mid = (right + left) // 2      # left = 0 right = 5 ----> mid = 2

                                  # [7,5,2,9,1,4]
            sort(left, mid)       # [7, 5, 2] -> [7, 5] -> [7]
            sort(mid + 1, right)  # [9, 1, 4] -> [4]
            merge(left, mid, right)

    n = len(a)
    left = 0
    right = n - 1

    sort(left, right)
    return a


@nb.njit
def merge_sort3(a):

    a = a.copy()
    temp = a.copy()
    n = a.size

    def merge(left_start, left_end, right_start, right_end):

        left_cursor = left_start
        right_cursor = right_start

        # Adds our values to our temp array
        for x in range(left_start, right_end + 1):
            temp[x] = a[x]

        for x in range(left_start, right_end + 1):

            # Hvis vesntre pointer er større end mid vil der ikke være flere "venstre" værdier tilbage og vi tager derfor fra højre
            if left_cursor > left_end:
                a[x] = temp[right_cursor]
                right_cursor += 1

            # if rc > re -> no more data in right array -> start emptying left array
            elif right_cursor > right_end:
                a[x] = temp[left_cursor]
                left_cursor += 1

            # Kigger om den højre værdi er mindre end den venstre værdi
            # og ligger den ind som næste element
            elif temp[right_cursor] < temp[left_cursor]:
                a[x] = temp[right_cursor]
                right_cursor += 1

            # Ellers må værdien enten være det samme eller større og så ligger vi den ind som det næste
            else:
                a[x] = temp[left_cursor]
                left_cursor += 1

    # 2,4,8,16,32,64...
    for i in range(1, math.ceil(np.log2(n)) + 1):
        interval = 2**i
        print(i, interval)

        # sub loop for eah interval
        # interval = 4 | x=0->3   x=4-7   x=8-11   x=12-15
        for x in range(0, n, interval):
            left_start = x
            left_end = x + (interval // 2) - 1
            right_start = x + (interval // 2)
            right_end = min(x + interval - 1, n - 1)  # min condition, to insure right_end doesnt go over the length of the array

            merge(left_start, left_end, right_start, right_end)

    return a


def merge_runs(arr):
    def merge(left, right):

        arr = []
        left_cursor = right_cursor = 0

        # hvis left_cursor er mindre end længden på left & right_cursor er mindre end længden på
        # bliver ved med at kigge hvilke array har den laveste værdi og sætter den til venstre!!!(altså på vores x)
        while left_cursor < len(left) and right_cursor < len(right):
            if left[left_cursor] < right[right_cursor]:
                arr.append(left[left_cursor])
                left_cursor += 1
            else:
                arr.append(right[right_cursor])
                right_cursor += 1

        # Tilføjer resterende værdier....
        while right_cursor < len(right):
            arr.append(right[right_cursor])
            right_cursor += 1

        while left_cursor < len(left):
            arr.append(left[left_cursor])
            left_cursor += 1

        return arr

    def find_runs(a):
        runs = []
        runn = []
        for i in range(len(a)):

            n_runn = len(runn)
            if n_runn == 0:
                runn.append(a[i])
            elif a[i] > runn[n_runn - 1]:
                runn.append(a[i])
            else:
                runs.append(runn)
                runn = [a[i]]

        if len(runn) > 0:
            runs.append(runn)

        return runs

    def magic(arr):

        n = len(arr)
        a = []

        for i in range(n - 2, -1, -2):

            i = i
            j = i + 1

            if j >= 0:
                a.append(merge(arr[i], arr[j]))
            else:
                a.append(arr[i])

        return a

    runs = arr[:]
    runs = find_runs(runs)

    while len(runs) > 1:
        runs = magic(runs)

    return runs[0]


def dict_sort(arr):
    text = arr[:]
    dict = {}

    for word in text:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

    keys = quick_sort2(list(dict.keys()))

    a = []
    for key in keys:
        for i in range(dict[key]):
            a.append(key)

    return a

def time_sort(func):
    text=get_text()
    start=time.time()
    func(text)
    end=time.time()
    return end - start


def time_sort_n2(func):
    text=get_text()
    start=time.time()
    func(text[:40000])
    end=time.time()


    n1=40000
    n2=len(text)
    t1=(end - start)

    return (n2**2 / n1**2) * t1
