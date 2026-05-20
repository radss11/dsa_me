class Solution(object):

    def findComplement(self, num):

        temp = num
        binary = ""

        # decimal to binary manually
        while temp > 0:

            rem = temp % 2
            binary = str(rem) + binary

            temp = temp // 2

        toggled = ""

        # toggle bits
        for bit in binary:

            if bit == '0':
                toggled += '1'

            else:
                toggled += '0'

        # binary to decimal manually
        power = 0
        decimal = 0

        for i in range(len(toggled)-1, -1, -1):

            if toggled[i] == '1':
                decimal += 2 ** power

            power += 1

        return decimal