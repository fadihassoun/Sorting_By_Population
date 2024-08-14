# Sorting_By_Population

Description: Implementing an algorithm to a linked list of countries by their populations in descending order.
This code does not use the built-in sorting functions nor changes the linked list to a normal list to work on it.

The sorting algorithm: 

The merge sort algorithm was chosen to sort the linked list above for the following reasons:

The linked list is a data structure where the elements need to be accessed linearly and orderly from one node to 
another, in other words, it cannot be accessed randomly in an efficient manner. Therefore, an algorithm that does not 
rely on random access is required. 

Also, swapping elements in a linked list is not efficient as it would involve changing the links between the nodes, 
and the pointers may be spread out in the memory. Hence, algorithms that rely heavily on swapping elements such as 
the bubble sort, selection sort, insertion sort, and shell sort are not suitable for this data structure.

In terms of time complexity, the bubble sort, selection sort, insertion sort, and shell sort algorithms have a time 
complexity of O(n^2) which can have poor performance for large lists. On the other hand, two divide-and-conquer 
sorting algorithms that do not rely on swapping and random access are the merge sort and the quick sort. Both of 
these divide the list recursively into sub-lists until they are small enough to work on efficiently. The split into 
sub-lists operation is done in (log n) times (n = length of the list) and the merge operation to combine the two 
sub-list is done in a linear time O(n). The time complexity for the average case is therefore O(n log n). However, 
as the quick sort depends on the choice of the pivot which can lead to very uneven sub-lists, it can have a worst 
case time complexity of O(n^2). The merge sort is a safer choice as its time complexity does not change (always 
divides the list in the middle).

It is worth mentioning that the merge sort algorithm is also a stable sorting algorithm. However, this can only be 
useful if, for example, the order of countries with the same population needs to be preserved in the alphabetical order 
they are given with. Also, it is an out-of-place sorting algorithm i.e. it creates a new list for the sorted 
elements. This can be inefficient in terms of memory for large lists; nevertheless, is safe in terms of preserving the 
original list unchanged.

The merge and sort algorithm divides the list into sub-lists, sorts them and then merges them recursively as follows:

-   If the list has only one element, return the list. 
-   If the list has more than one element, divide the list into two halves (sub-lists). 
-   Keep Splitting the two sub-lists recursively until there is only one element.
-   Sort the sub-lists by comparing the first nodes by value and adding the node with the bigger value to the beginning 
    of a new list.
-   Merge the two lists: When one sub-list is exhausted, add the other (which will be already sorted) to the end of the 
    new list.

    
