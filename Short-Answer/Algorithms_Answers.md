#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  O(n): as the size of the input increases (n), the number of operations N will increase at a linear rate


b)  O(n log n): Because of the outer for loop and the nested inner while loop (each with a value of n), they are multiplied together.
    outer loop will increase at n O(n); inner loop will increase at O(log n)

c)  O(n): There is no loop, but n is still called recursively so the operation still has to go through each value(bunnies) and performe the single operation.

## Exercise II

    O(logn)

    find the mid point of the number of floors
        (n // 2) - needs the // to ensure that an integer is returned (floor division)
    Drop an egg at the mid-point
    If the egg breaks, eliminate the floors above, assign mid-point - 1 to the new highest value
    If the egg does not break eliminate the floors below, assign the new floor to current floor +1
    Calculate the new mid-point
    Drop the egg and continue
