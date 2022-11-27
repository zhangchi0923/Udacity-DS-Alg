# Task0
Getting the first and the last element from a given list both indicate $O(1)$ time complexity and need no other space.
So this program is of $O(1)$ time and space complexity.

# Task1
To get the number of *phone*, we must wholly traverse given lists --- `texts` and `calls`. Let them be the inputs.
The program runs two loops to traverse them. So time complexity should be $O(n)$. Additionally, we built a set to store
the results whose size depends linearly on the size of the input lists. So the space complexity should also be $O(n)$

# Task2
It runs a `for` loop of a list, inside it there are two `.set() `operations of a dict each of which needs $O(n)$ time
complexity. In general, this will lead n x 2n operations. In the end, the builtin max() needs $O(n)$, another two
consecutive `.get()` operations of `list(keys & values)` need $O(n)$. They sum up as $3n$. So the whole time consuming would be
$O(2n^2 + 3n)$ --> $O(n^2)$. Size of `res_dict` has linear relation with the input size, so space complexity would be $O(n)$.

***UPDATED*** Addressing *defaultdict* as data structure will eliminate *in* operation which takes $O(n)$ and bring time complexity
down to only $O(n)$ of *for* loops.

# Task3
According to the information about the phone# and timestamp, let's suppose the size of each element of list inside
calls will not change along with the input size. On that basis, `.get()` of those elements will take $O(1)$ complexity.
`for` loop --> $O(n)$. Inside it, the worst case for `.get()` and `.set()` operations need $O(n)$. So the overall time complexity
of the for loop is $O(n^2)$. In the end, .sorted() function takes $O(nlogn)$ complexity. To traverse the sorted list need
$O(n)$. This part takes $O(n + nlogn)$. $O(n^2 + n + nlogn)$ --> $O(n^2)$.
As for space complexity, res_dict takes the same size with input in the worst case. So $O(n)$ space complexity.

# Task4
Each 'for' loop takes $O(n)$. `.get()`, `.set()` and `in` operation takes $O(n)$. So three loops takes $O(2n^2 + n^3)$ in the
worst case. To print the results, it takes $O(n)$ after the $O(nlogn)$ of `.sorted()` function, $O(n + nlogn)$.
So time complexity $O(2n^2 + n^3 + n + nlogn)$ --> $O(n^3)$.
Space complexity: $O(2n) --> O(n)$.