#This approach is another great representation of the abilities that Python has and the advantage it gives you as opposed to other languages.
#We tackle this problem by storing the length of the list and using a modulo operator for taking a remainder of k/n. This is important..
#..in case the value of k is greater than the length of the array. For example, if a list has 5 elements, a rotation of 1 and a rotation 6 would..
#..yield the same result because rotating 5 times sets the list back into it's original position. This check prevents unnecessary loops.
#The final line works by adding all values from index -3 -> end of list ([-k:]) & all values from the start -> -3 ([:-k]). The colon represents the splice point.
#Once you splice the list and re-add it after splicing, you'll get the correct number of rotations. The addition order DOES matter, so you..
#..have to add the values with [-k:] first and then put the [:-k] second.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # Handle cases where k is greater than the array length.
        nums[:] = nums[-k:] + nums[:-k]

#EX: [1,2,3,4,5], k = 3

#Step 1: n = length of the list, so n is 5.
#Step 2: k = k & n, k = 3 % 5, k = 3. Remember for modulo if the first number is smaller, then that number is the result of the operation.
#Step 3: We now separate the list by the two different splices we set. The first slice would be from -3:-1 (end of the list)..
#..so the first splice is: [3,4,5]. Keep in mind that -3 is the third number from the end of the list. -1 represents the last item in a list.
#The other fragment of nums would be from index 0 to -3 (which is 3). So, the second splice is [1,2]. Remember that we never include..
#..the final index element in the list. For example, if a list is [1,2,3,4], and we iterate from [0,3], we only get 1,2,3, since we don't include item 4 at index 3.
#So, to wrap up, we add [3,4,5] and [1,2], so our final result is [3,4,5,1,2], which is a rotation of 3, matching our k value.
        