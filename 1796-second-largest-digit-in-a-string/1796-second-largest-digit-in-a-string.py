
class Solution(object):
    def secondHighest(self, s):
        largest = -1
        second = -1

        for ch in s:
            if ch.isdigit():
                digit = int(ch)

                if digit > largest:
                    second = largest
                    largest = digit
                elif digit < largest and digit > second:
                    second = digit

        return second
