"""
Description: Implementing an algorithm to a linked list of countries by their populations in descending order.
This code does not use the built-in sorting functions nor changes the linked list to a normal list to work on it.

"""


# The linked list class implementation.
class LinkedList:
    def __init__(self, data):
        self.label = data[0][0]
        self.value = data[0][1]
        # The tail of each node recursively points to another instance of the Linkedlist with data from the next
        # element onward, until there is only one element.
        self.tail = None if (len(data) == 1) else LinkedList(data[1:])
        # Assigning a head of the list to it, i.e. first node.
        self.head = self

    # Method to get the size of the linked list.
    def size(self):
        # Starting at the head, iterate through the list by assigning the tail of the current node to the node itself
        # and incrementing a counter at each iteration.
        count = 0
        current_node = self.head
        while current_node:
            current_node = current_node.tail
            count += 1
        # Return the final counter, which represents the size of the linked list.
        return count

    # Method to get the middle node of the Linkedlist, this will be used later to divide it into sub-linked lists.
    def get_mid_node(self):
        # Starting at the head, iterate half-way through the list by assigning the tail of the current node to the
        # node itself each time; at the end, the middle node will be the current node.
        count = 0
        current_node = self.head
        length = self.size()
        while count < (length // 2) - 1:
            current_node = current_node.tail
            count += 1
        # Return the current node at the end of the iteration (middle node).
        return current_node

    # Method to print the labels and the values of the Linkedlist.
    def print_nodes(self):
        # Starting at the head, iterate through the list printing the label and the value of each
        # node, moving through list by assigning the tail of the current node to itself.
        current_node = self.head
        while current_node:
            # The if else statement is only for the good formatting of the output.
            if current_node.tail:
                print(f"(\"{current_node.label}\", {current_node.value})", end=", ")
            else:
                print(f"(\"{current_node.label}\", {current_node.value})")
            current_node = current_node.tail

    # Method to add a specific node at the end of the Linkedlist.
    def append_list(self, new_node):
        # Iterate through list starting at the head and as long as the current node has a tail (not None). The
        # iteration will stop when the current node is the last node.
        current_node = self.head
        while current_node.tail:
            current_node = current_node.tail
        # Assign the tail of the last node to the node that needs to be added.
        current_node.tail = new_node


"""The sorting algorithm: 

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


"""


# The merge sort function.
def merge_sort_lnk_lst(linked_list: LinkedList):
    # If the list has one node, return it (base case).
    if linked_list.head is None or linked_list.size() == 1:
        return linked_list

    # If the list has more than one node, divide it into two sub-lists.
    if linked_list.size() > 1:
        mid_node = linked_list.get_mid_node()
        # Assign the nodes at the tail (right) of the middle node to right_list
        right_list = mid_node.tail
        # Cut out the nodes at the tail of the middle node and assign the rest to left_list
        mid_node.tail = None
        left_list = linked_list

        # Recursively call the function on the two sub-lists to divide them further until they reach the base case.
        left_list = merge_sort_lnk_lst(left_list)
        right_list = merge_sort_lnk_lst(right_list)

        # Sort and merge the two sub-lists by calling the merge function on them.
        return merge(left_list, right_list)


# The merge function (This could have been included in the merge_sort_lnkd_lst function but was separated for easier
# management of the code).
def merge(left_list, right_list):
    # Create a new list with no nodes to store the sorted elements.
    sorted_list = None
    node = None

    # While there are nodes in both lists, i.e. not None, iterate through them.
    while left_list and right_list:
        # Compare the values of the first nodes of the two lists and add the larger value node to the sorted list. if
        # the sorted list still has no nodes (first iteration), assign the larger value node to it; otherwise,
        # append that node to it.
        if left_list.value >= right_list.value:
            node = left_list
            # left_list without its first node
            left_list = left_list.tail
            # the first node of the left list isolated
            node.tail = None

        elif right_list.value > left_list.value:
            node = right_list
            # right_list without its first node
            right_list = right_list.tail
            # the first node of the right list isolated
            node.tail = None

        if sorted_list is None:
            sorted_list = node
        else:
            sorted_list.append_list(node)

    # If one of the sub-lists has no nodes left (None), append the other one (which is already sorted) to the sorted
    # list as nothing is left to compare with.
    if left_list is None:
        sorted_list.append_list(right_list)

    if right_list is None:
        sorted_list.append_list(left_list)

    return sorted_list


"""The List goes here"""

countries = LinkedList(
    [("Ukraine", 41879904), ("Brunei", 442400), ("Christmas Island (Australia)", 1928), ("Mauritius", 1265985),
     ("Lesotho", 2007201), ("Guatemala", 16604026), ("British Virgin Islands (UK)", 30030), ("Malta", 493559),
     ("Greenland (Denmark)", 56081), ("Guernsey (UK)", 62792), ("Ethiopia", 98665000), ("Suriname", 581372),
     ("Turkmenistan", 6031187), ("American Samoa (US)", 56700), ("French Polynesia (France)", 275918),
     ("Equatorial Guinea", 1358276), ("Solomon Islands", 680806), ("Burundi", 10953317), ("Abkhazia", 244832),
     ("Rwanda", 12374397), ("Iceland", 364260), ("Monaco", 38300), ("Namibia", 2458936), ("United States", 329532925),
     ("Brazil", 211402908), ("Finland", 5527573), ("Armenia", 2957500), ("Wallis and Futuna (France)", 11700),
     ("Cuba", 11209628), ("Guyana", 782766), ("Oman", 4664790), ("Aruba (Netherlands)", 112309), ("Nauru", 11000),
     ("Sri Lanka", 21803000), ("Myanmar", 54339766), ("United Arab Emirates", 9890400), ("Hungary", 9772756),
     ("Norfolk Island (Australia)", 1756), ("Cambodia", 15288489), ("Fiji", 884887), ("Benin", 11733059),
     ("Egypt", 100264508), ("Northern Cyprus", 351965), ("Angola", 31127674), ("Barbados", 287025),
     ("Trinidad and Tobago", 1363985), ("Colombia", 49395678), ("Turks and Caicos Islands (UK)", 41369),
     ("Norway", 5367580), ("Kiribati", 120100), ("Kosovo", 1795666), ("Azerbaijan", 10067108), ("Romania", 19405156),
     ("Kyrgyzstan", 6533500), ("Peru", 32131400), ("Australia", 25680766), ("Faroe Islands (Denmark)", 52124),
     ("Turkey", 83154997), ("Georgia", 3723464), ("Singapore", 5703600), ("Eswatini", 1093238),
     ("Saint Vincent and the Grenadines", 110608), ("East Timor", 1387149), ("Tuvalu", 10200), ("Pakistan", 219313520),
     ("Bahrain", 1543300), ("Paraguay", 7152703), ("Jersey (UK)", 106800), ("Slovakia", 5456362), ("Mongolia", 3313049),
     ("Argentina", 44938712), ("Jordan", 10660256), ("Saint Barthélemy (France)", 9793), ("Andorra", 77543),
     ("Bangladesh", 168456310), ("Saint Martin (France)", 35746), ("FS Micronesia", 104468), ("South Sudan", 12778250),
     ("Artsakh", 148000), ("Slovenia", 2094060), ("Senegal", 16209125), ("Ivory Coast", 25823071), ("Syria", 17500657),
     ("Montserrat (UK)", 4989), ("Philippines", 108505959), ("Laos", 7123205), ("Gibraltar (UK)", 33701),
     ("Iran", 83371987), ("Bahamas", 385340), ("Mauritania", 4077347), ("Portugal", 10276617), ("Madagascar", 26251309),
     ("Malawi", 19129952), ("Central African Republic", 5496011), ("Saint Kitts and Nevis", 52823), ("Ghana", 30280811),
     ("Honduras", 9158345), ("Belarus", 9408400), ("India", 1361140893), ("Estonia", 1328360), ("Nicaragua", 6460411),
     ("Mali", 20250833), ("Zambia", 17885422), ("S\u00e3o Tom\u00e9 and Pr\u00edncipe", 201784),
     ("Cura\u00e7ao (Netherlands)", 158665), ("Jamaica", 2726667), ("Northern Mariana Islands (US)", 56200),
     ("Vanuatu", 304500), ("Kuwait", 4420110), ("Cameroon", 26545864), ("Netherlands", 17456281),
     ("Saudi Arabia", 34218169), ("Dominican Republic", 10358320), ("Japan", 125950000), ("Djibouti", 1078373),
     ("Antigua and Barbuda", 96453), ("Morocco", 35871167), ("Nigeria", 206139587), ("Iraq", 39127900),
     ("South Korea", 51780579), ("Pitcairn Islands (UK)", 50), ("US Virgin Islands (US)", 104578), ("Ireland", 4921500),
     ("Sierra Leone", 7901454), ("Cyprus", 875900), ("Palestine", 4976684), ("Luxembourg", 626108),
     ("Falkland Islands (UK)", 3198), ("France", 67076000), ("Bolivia", 11469896), ("Panama", 4218808),
     ("Seychelles", 97625), ("Guinea-Bissau", 1604528), ("Puerto Rico (US)", 3193694), ("Anguilla (UK)", 14869),
     ("Macau (China)", 679600), ("North Macedonia", 2077132), ("Saint Helena, Ascension", 5633), ("Sweden", 10338368),
     ("Kazakhstan", 18683712), ("China", 1402247960), ("Italy", 60238522), ("Israel", 9186750),
     ("Uzbekistan", 34131625), ("Guam (US)", 172400), ("Dominica", 71808), ("Malaysia", 32752760),
     ("New Zealand", 4978784), ("Cape Verde", 550483), ("Uruguay", 3518552), ("Belgium", 11524454), ("Kenya", 47564296),
     ("Saint Pierre and Miquelon (France)", 6008), ("Uganda", 40299300), ("Yemen", 29825968), ("Nepal", 29996478),
     ("Switzerland", 8603899), ("Sint Maarten (Netherlands)", 40614), ("Tonga", 100651), ("Algeria", 43000000),
     ("Haiti", 11577779), ("Zimbabwe", 15159624), ("North Korea", 25450000), ("Congo", 5518092), ("Belize", 408487),
     ("Czech Republic", 10693939), ("Poland", 38379000), ("San Marino", 33574), ("Tanzania", 55890747),
     ("Tokelau (NZ)", 1400), ("Saint Lucia", 178696), ("Cook Islands (NZ)", 15200), ("Mozambique", 30066648),
     ("Indonesia", 266911900), ("Grenada", 112003), ("Burkina Faso", 20870060), ("Western Sahara", 582463),
     ("New Caledonia (France)", 282200), ("Albania", 2845955), ("Greece", 10724599),
     ("Bosnia and Herzegovina", 3301000), ("Montenegro", 622359), ("Russia", 146745098), ("Samoa", 200874),
     ("Comoros", 873724), ("United Kingdom", 66435550), ("Taiwan", 23604265), ("Vatican City", 799),
     ("Austria", 8902600), ("Lebanon", 6825442), ("Latvia", 1906800), ("Mexico", 126577691), ("Venezuela", 32219521),
     ("Papua New Guinea", 8935000), ("Chad", 16244513), ("Canada", 37996639), ("Maldives", 374775),
     ("Denmark", 5822763), ("Tajikistan", 9127000), ("Isle of Man (UK)", 83314), ("Afghanistan", 32225560),
     ("Germany", 83149300), ("Vietnam", 96208984), ("Eritrea", 3497117), ("Spain", 47100396), ("Costa Rica", 5058007),
     ("Cayman Islands (UK)", 65813), ("Niger", 22314743), ("Liechtenstein", 38749), ("Gambia", 2347706),
     ("Hong Kong (China)", 7500700), ("Sudan", 42432665), ("Tunisia", 11722038),
     ("\u00c5land Islands (Finland)", 29885), ("DR Congo", 89561404), ("Bulgaria", 6951482), ("Liberia", 4475353),
     ("Botswana", 2338851), ("Palau", 17900), ("Niue (NZ)", 1520), ("Thailand", 66494417), ("South Africa", 58775022),
     ("Lithuania", 2793471), ("Gabon", 2172579), ("Libya", 6871287), ("Transnistria", 469000), ("Moldova", 2681735),
     ("South Ossetia", 53532), ("Guinea", 12218357), ("El Salvador", 6486201), ("Croatia", 4076246), ("Qatar", 2747282),
     ("Serbia", 6963764), ("Togo", 7538000), ("Ecuador", 17466864), ("Cocos (Keeling) Islands (Australia)", 538),
     ("Chile", 19107216), ("Bermuda (UK)", 64027), ("Somalia", 15893219), ("Bhutan", 741672),
     ("Marshall Islands", 55500)])

"""The Result"""

# Printing the original unsorted Linkedlist nodes.
print("The unsorted list of countries by population is: ")
countries.print_nodes()

# Applying the merge sort method and printing the result.
countries_sorted = merge_sort_lnk_lst(countries)
print("\n\033[4mThe sorted list of countries by population in decreasing order is:\033[0m ")
countries_sorted.print_nodes()
