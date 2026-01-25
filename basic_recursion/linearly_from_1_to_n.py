# def f(i , n):
#     if i > n :
#         return
#     print(i)
#     f(i + 1 , n)
# def main():
#     n = int(input("enter number : "))
#     f(1 , n)
# main()

class Solution:
     # Recursive function to print numbers from current to n
    
    def printNumbers(self, current, n):
        # Base case: if current exceeds n, stop recursion
        if current > n:
            return

        # Print current number
        print(current, end=' ')

        # Recursive call with next number
        self.printNumbers(current + 1, n)


if __name__ == "__main__":
    sol = Solution()
    n = 10

    sol.printNumbers(1, n)
    print()
    