#This problem is a bit harder than the other beginner problems.The general idea behind this problem is setting the two strings to equal length...
#..using the zfill() function (this just adds zeros since its binary.). After that, we add the two values together after converting them to integers, then..
#..getting the remainder from the bit_sum and updating the carry. The remainder (%) is how we get our zeros and ones, and floor dividing by 2 follows the ...
#..rules of binary, since a number like 0101 in binary represents 8(0) + 4(1) + 2(0) + 1(1) = 5. Lastly, after you add your carry value, reverse the result sincr the..
#..bits were added in reverse order.

def add_binary(a, b):
    result = []
    carry = 0

    # Make both strings of equal length by using '0'.
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    # Iterate from the last bit (rightmost) to the first bit (leftmost).
    for i in range(max_len - 1, -1, -1):
        bit_sum = carry
        bit_sum += int(a[i])  # Convert binary string to int and add them up.
        bit_sum += int(b[i])

        # Append the result bit (bit_sum % 2) to the result list. This obtains 0s and 1s.
        result.append(str(bit_sum % 2))

        # Update the carry (bit_sum // 2).
        carry = bit_sum // 2

    # Append the carry if one exists.
    if carry:
        result.append(str(carry))

    # Reverse the result and join it into a string.
    return ''.join(reversed(result))

#Time complexity: O(n)

#EX: 
#a = "1010" & b = "1101"
#Step 1: a[3] = 0, b[3] = 1, carry = 0 → bit_sum = 0 + 1 + 0 = 1 → result bit = 1, carry = 0.
#Step 2: a[2] = 1, b[2] = 0, carry = 0 → bit_sum = 1 + 0 + 0 = 1 → result bit = 1, carry = 0.
#Step 3: a[1] = 0, b[1] = 1, carry = 0 → bit_sum = 0 + 1 + 0 = 1 → result bit = 1, carry = 0.
#Step 4: a[0] = 1, b[0] = 1, carry = 0 → bit_sum = 1 + 1 + 0 = 2 → result bit = 0, carry = 1.