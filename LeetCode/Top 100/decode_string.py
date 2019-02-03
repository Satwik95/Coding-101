class Solution(object):
    def decodeString(self, s):
            """
            :type s: str
            :rtype: str
            """


            word = ""
            num = 0
            stack = []

            for ch in s:

                if ch.isdigit(): 

                    num = num*10 + int(ch) 

                if ch == "[":

                    stack.append(word)
                    stack.append(num)

                    num = 0
                    word =""


                if ch.isalpha():

                    word += ch

                if ch == "]":

                    count = stack.pop()

                    prev_word = stack.pop()

                    word = prev_word+ word*count


            return word