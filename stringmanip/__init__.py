def reverse(str):
    l = list(str)

    r = []
    for ch in l:
        r.insert(0, ch)
    return r


print reverse("abcdefgh")


