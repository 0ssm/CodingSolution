"""class Solution(object):
    def isPalindrome(self,n):
        st = str(n)
        rev = st[::-1]
        if rev == st:
            return rev
        if rev == n:
            print("palindrome")
        else:
            print("not palindrome")
print(Solution().isPalindrome(n = 121))"""

# TODO Test cases with multiple lines of input

"""t = int(input())
for i in range(t):
    A, B = map(int,input().split())
    C, D, E = map(int,input().split())
    print(A, B, C, D, E)"""



"""t = int(input("input do "))
for i in range(t):
    n = int(input("number batawa"))
    print(n+1)"""


# class Solution(object):
#     def countPrimes(self, n):
#         is_prime = True
#         count = 0
#         for number in range(2, n):
#             if number%n == 0:
#                 is_prime = False
#             if is_prime:
#                 count+=1
#             else:
#                 pass
#         return count
#
#
# print(Solution().countPrimes(n = 1))

"""n = int(input("enter a number: "))
is_prime = True
if n == 1 or n == 0:
    print("prime number start from 2")
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False

    if is_prime:
        print("its a prime number: ")
    else:
        print("its not a prime number")"""


"""class Solution(object):
    def countPrimes(self, n):
        count = 0
        for number in range(2, n):
            is_prime = True
            for i in range(2, int(number**0.5) + 1):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                count += 1
        return count

print(Solution().countPrimes(n=10))"""



"""You have been given a random integer array/list(ARR) and a number X. Find and return the number of triplets in the array/list which sum to X.
Note :
Given array/list can contain duplicate elements.
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the first array/list.

Second line contains 'N' single space separated integers representing the elements in the array/list.

Third line contains an integer 'X'.
Output format :
For each test case, print the total number of triplets present in the array/list.

Output for every test case will be printed in a separate line.
Constraints :
1 <= t <= 50
0 <= N <= 10^2
0 <= X <= 10^9
Time Limit: 1 sec
Sample Input 1:
1
7
1 2 3 4 5 6 7 
12
Sample Output 1:
5
Sample Input 2:
2
7
1 2 3 4 5 6 7 
19
9
2 -5 8 -6 0 5 10 11 -3
10
Sample Output 2:
0
5


 Explanation for Input 2:
Since there doesn't exist any triplet with sum equal to 19 for the first query, we print 0.

For the second query, we have 5 triplets in total that sum up to 10. They are, (2, 8, 0), (2, 11, -3), (-5, 5, 10), (8, 5, -3) and (-6, 5, 11)"""




"""You have been given an integer array/list(ARR) of size N that contains only integers, 0 and 1. Write a function to sort this array/list. Think of a solution which scans the array/list only once and don't require use of an extra array/list.
Note:
You need to change in the given array/list itself. Hence, no need to return or print anything. 
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains an integer 'N' representing the size of the array/list.

Second line contains 'N' single space separated integers(all 0s and 1s) representing the elements in the array/list.
Output format :
For each test case, print the sorted array/list elements in a row separated by a single space.

Output for every test case will be printed in a separate line.
Constraints :
1 <= t <= 10^2
0 <= N <= 10^5
Time Limit: 1 sec
Sample Input 1:
1
7
0 1 1 0 1 0 1
Sample Output 1:
0 0 0 1 1 1 1
Sample Input 2:
2
8
1 0 1 1 0 1 0 1
5
0 1 0 1 0
Sample Output 2:
0 0 0 1 1 1 1 1
0 0 0 1 1"""





















































