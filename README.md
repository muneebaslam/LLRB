# Left Leaning Red Black Trees
This is an implementation of LLRB trees in python. LLRB are self-balancing binary search trees that offer worst-case guarantees for insertion, deletion and search operations.

| **Operation** | **Worst Case** |
|--|--|
| Insert | O(log N) |
| Delete | O(log N) |
| Search | O(log N) |

## Usage
Import the class from the LLRB module

    from LLRB import LLRB
Instantiate the class to use the API

    tree = LLRB()
## API

 - `tree.insert(item)` -  Insert item into the tree
 - `tree.search(item)` - Verify the presence of item in tree
 - `tree.delete(item)` - Delete item from the tree
 ## Resources
 To learn more about LLRB trees, you can see my poster [here](www.github.com/muneebaslam/LLRB/blob/poster.pdf).
 ## Reference
 [https://www.cs.princeton.edu/~rs/talks/LLRB/RedBlack.pdf](https://www.cs.princeton.edu/~rs/talks/LLRB/RedBlack.pdf)
 ## License
 This project is available under the MIT license.
