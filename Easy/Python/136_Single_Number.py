#Bitwise operators can be a handy python tool in certain scenarios, including this one. The way this answer works is that it goes through..
#..the values in the loop with a variable named result and it applies the ^= bitwise operator. The way this operator works is that it has..
#..a few properties to be aware of.
#Property 1: 5 ^ 5 = 0 , any number with itself yields 0.
#Property 2: 2 ^ 0 = 2, any number with 0 yields the number.
#Property 3: 5 ^ 1 = 6, but if you do 6 ^ 1 in the same sequence it'll yield 5. When the same number appears again it will switch between..
#..addition and subtraction. This is exactly how we find our single values. Since every value but one is cloned, the result variable will go up by..
#..some amount but then go down by that same amount assuming a clone exists.

#WARNING: ^ does not mean exponentiation. ** is used for exponents, so don't confuse it with ^. ^ represents XOR, otherwise known as exclusive or.

#Time complexity: O(n)

 Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        
        for num in nums:
            result ^= num  # XOR each number
        
        return result  # The remaining value is the single number

#EX: [1,2,1,2,4]

#Step 1: result = 0, 0 ^ 1 = 1, so result is now 1.
#Step 2: result = 1, 1 ^ 2 = 3, so result is now 3.
#Step 4: result = 3, 3 ^ 1 = 2, so result is now 2.
#Step 5: result = 2, 2 ^ 2 = 0, so result is now 0.
#Step 6: result = 0, 0 ^ 4 = 4, so result is 4.

#Result is 4, and that value is returned, which is true!


