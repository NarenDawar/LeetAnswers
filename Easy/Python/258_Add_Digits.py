#Leetcode 258. Add Digits: https://leetcode.com/problems/add-digits/
# So this problem is very tricky and honestly I find it hard to believe that people come up with 
#    the O(1) solution by themsevles
# However, the recursive/iterative solution is pretty simple and could be important as well
#    but typically if you get this question, they are likely asking for the constant time solution

#The trick to this problem is that for every number when you continuously add its digits until it is a 
#  single digit, you can shortcut to the end by doing num%9, except in the scenario if the num is 0 or divisble by 9
# If the number is 0 then you should just return 0 and if it is divisble by 9 then you just return 9 because
#   the digits always add up to 9.
# Because of some complex math formula, this problem is essentially finding a numbers closest distance to a 
#   multiple of 9, which the exception of 9 and 0

#If you want to understand why this solution works, its based on a proof using the binomial expansion for the sum of the digits. So the sum of the digits for 57 represented as 5*10^1 + 7 *10^0. 
# The generalized formula splits 10^k, (k is the digits place) into (9+1)^k. The binomial expansion explains all of this.

#Here is a video to explain it: https://www.youtube.com/watch?v=tIjdI-ioXh0

def addDigits(self, num: int) -> int:
	if (num==0):
		return 0
	if (num%9==0):
		return 9
	return num%9

# Example if you take the number 541 you do (5) + (4) + (1), you get 10 then (1) + (0) you get 1
#		But you can notice that the closest number divisble by 9 is 540 which is 1 number away

