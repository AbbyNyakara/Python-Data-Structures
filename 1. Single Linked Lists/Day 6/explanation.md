    def binary_to_decimal(self):
        num = 0
        current = self.head
        while current:
            num = num * 2 + current.value
            current = current.next
        return num






Given the linked list: 1 → 0 → 1 → 0

This represents the binary number 1010, where the head of the list is the most significant bit (MSB) and the tail is the least significant bit (LSB).

Method Walkthrough:

def binary_to_decimal(self):


Initialize the decimal number:

num = 0
Here, num will store our resulting decimal number. We initialize it to 0.



Start at the head of the linked list:

current = self.head
This current pointer will help us traverse the linked list from the start (MSB) to the end (LSB).



Traverse the linked list:

while current:
This loop runs as long as we have nodes left in the linked list.



Convert the binary number to decimal:

    num = num * 2 + current.value


For every node we encounter, we:

Multiply the current num by 2. This shifts our binary number left, preparing it for the next bit. It's analogous to multiplying by 10 in decimal arithmetic.

Add the value of the current node (0 or 1) to num.



Illustrative Steps for 1010:

Starting with num as 0.

First node (MSB) is 1. So, num = 0 * 2 + 1 which makes num equal to 1.

Move to the next node, which is 0. Now, num = 1 * 2 + 0 which makes num equal to 2.

The next node is 1. So, num = 2 * 2 + 1 which results in num becoming 5.

The last node (LSB) is 0. Thus, num = 5 * 2 + 0 which makes num equal to 10.

Consequently, the binary number 1010 converts to the decimal number 10.



Proceed to the next node:

    current = current.next
This line shifts our attention to the next node in the linked list.



Return the decimal number:

return num
After processing all the bits in our binary number (i.e., all the nodes in our linked list), we can return our decimal result stored in num.


Conclusion:

The process for converting binary to decimal using a linked list reflects standard binary conversion rules. We work from the MSB (head of the linked list) to the LSB (tail), doubling our current result and adding the next bit at every step. This method ensures that each binary bit contributes the correct power of 2 to our final decimal result. In our example, 1010 rightly converts to 10.





Code with inline comments:



def binary_to_decimal(self):
    # 1. Initialize a variable 'num' to 0. This will be used to accumulate the 
    # decimal value as we traverse the linked list.
    num = 0
    
    # 2. Start at the head of the linked list.
    current = self.head
 
    # 3. Traverse through the linked list.
    while current:
        # 3.1. For each node, left shift the accumulated value by 1 position. 
        # This is the same as multiplying by 2. This step ensures that we are 
        # moving to the next binary position.
        # 
        # Example: If num is '10' (binary for 2) and next node value is '1', 
        # left shifting '10' results in '100' (binary for 4). 
        # Now, adding the next node value gives '101' (binary for 5).
        num = num * 2
        
        # 3.2. Add the current node's value (which should be either 0 or 1) 
        # to the accumulated value 'num'.
        num = num + current.value
        
        # OR both the above steps can be combined as:
        # num = num * 2 + current.value
        
        # 3.3. Move to the next node in the list.
        current = current.next
 
    # 4. Return the accumulated decimal value.
    return num





All changes saved
|
Line 39, Column 35
Test Cases
Failed: 0, Passed: 5 of 5 tests
test_binary_0_returns_0
test_binary_1000_returns_8
test_binary_1101_returns_13
test_binary_110_returns_6
test_binary_1_returns_1
Your code passed this test
Coding Exercise

