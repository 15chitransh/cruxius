#palindrome
class Palindrome:

    @staticmethod
    def is_palindrome(word):
        s=list(word) 
        print(s)
        m=s[::-1]
        print(s)
        print(m)
        s = [element.upper() for element in s] ; s
        m = [element.upper() for element in m] ; m

        if s==m:
            return True
        else:
            print("False")

print(Palindrome.is_palindrome('Deleveled'))