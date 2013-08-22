import string


class PalindromeWrapperIterator:
    def __init__(self, obj):
        self.obj = obj
        self.cnt = 0

    def __iter__(self):
        return self

    def next(self):
        try:
            result = self.obj.get(self.cnt)
            self.cnt += 1
            return result
        except IndexError:
            raise StopIteration


class Palindrome(object):
    def clean(self, str):
        blacklist = string.join([string.whitespace, string.punctuation])

        cleaned = string.translate(str, None, blacklist).lower()
        return cleaned


    def isA(self, str):
        cleaned = self.clean(str)

        start = 0
        end = len(cleaned)
        match = True
        while start <= end and match:
            startch = cleaned[start]
            endch = cleaned[end - 1]

            match = startch == endch
            if start == end or start + 1 == end:
                return match
            else:
                start += 1
                end -= 1
        return match


class PalindromeWrapper(object):
    def __init__(self, base, dupe ):
        self.base = base
        self.dupe = dupe

    def __str__(self):
        if self.dupe:
            return self.base + self.base[::-1]
        else:
            s = self.base[1::-1]

            return self.base + s

    def __iter__(self):
        return PalindromeWrapperIterator(self)

    def get(self, index):
        if index < len(self.base):
            return self.base[index]
        else:
            if self.dupe:

                if index == len(self.base):
                    pos = len(self.base) - 1
                else:
                    pos = len(self.base) - index - 1

                return self.base[pos]
            else:
                pos = -index + 1

                return self.base[pos]





