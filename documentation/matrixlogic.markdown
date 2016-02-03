# How nodes are currently implemented

Currently the matrix is just a 1D list, rather than 2D. So this means that for a
 3x3 array the storage isn't as -

```python
node_matrix = [
              [1,2,3],
              [4,5,6],
              [7,8,9]] 
```

but rather 

```python
node_matrix = [1,2,3,4,5,6,7,8,9]
```

This is so that the coordinates for cells can be indexed as follows. 


Using 3x3 again - 

```
0, 1, 2
3, 4, 5
6, 7, 8
```

To calculate a position for a node is as follows - 

```
Matrix size = 3x3 = 9
Matrix width = 3

node position = (i, j)

i = floor(matrix_size / width)
j = matrix_size mod(width)
```

To give an example of this, say one wants to know the position of `7` (which can
be seen to be `(1, 2)`, remember zero indexed...) one would use;

```
1 = 7 % 3 which = 1
i = floor(7 / 3) which = 2
```

So that shows how one can find the `(i,j)` position of a node.

## Calculating neighbours

Hopefully this method will make it a bit easier to implement some of the
algorithms, as given the value of and node (lets say `4`) one can work out those
around it. Using up down left and right the neighbours of 4 would be `1, 3, 5,
7`. which can be worked out a few ways (will have to decide which is best). 

For example - 

```
node = 4
width = 3

neighbours;
up    = n - w = 4 - 3 = 1
left  = n - 1 = 4 - 1 = 3
right = n + 1 = 4 + 1 = 5
down  = n + 3 = 4 + 3 = 7
```

Seems as though it might lend itself to any type of algorithmic methods.
