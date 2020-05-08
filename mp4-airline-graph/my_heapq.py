def hif(a, i):
    # i could also be called "top", so think of i as
    # the top element of the small heap (3 elements)
    # largest, right, left are all indexes
    # setting largest to root
    smalest = i
    left = 2 * i + 1  # i = 5 l = 11
    right = 2 * i + 2  # i = 5 r = 12

    # right < len(a) checks if right is out of range
    if right < len(a) and a[right] < a[smalest]:
        smalest = right

    if left < len(a) and a[left] < a[smalest]:
        smalest = left

    if i != smalest:
        # swap values
        a[i], a[smalest] = a[smalest], a[i]

        # we call heapify again to make sure our change
        # didnt ruin something further down the tree, we do
        # this recursivly all the way to the root of the tree (the top)
        hif(a, smalest)

def heapify(a):

    n = len(a)

    # starts our maxheap
    # we go backwards because we wanna,
    # start at the bottom of the tree.
    # loop from n to/including 0 -> 5,4,3,2,1,0
    for i in range(n, -1, -1):
        hif(a, i)


def heappop(a):

    a[0], a[-1] = a[-1], a[0]

    val = a.pop()
    hif(a, 0)

    return val
