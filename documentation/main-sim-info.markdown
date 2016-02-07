# Main-sim

I've just created this to explain in a bit more detail (to myself as well as
others) what's going on currently with `main-sim.py`.

# Classes

* Node
* AllGraph

# Searching 

Currently the searching is growing extremely quickly. AFAICT it's 2^n, which is
obviouly along

![exp](http://mathinsight.org/media/image/image/exponential_function_two_to_x.png)

## 2D arrays?

Seems that the indexing is still done via 1D arrays here?

Information about what's currently in place needs to be properly understood so
as to build from it.

## test_graph.matrix

This is a 2D array, which will be a square the size of the nodes specified.
Currently that's `40x40`.

## What should be going where at the moment





