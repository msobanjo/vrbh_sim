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


The use of the `new_seeker_list` and `new_seeker_list` currently have values -

```python
# first iteration
new_seeker_list = [620]
newer_seeker_list = [621, 619, 660, 580]

# next iteration

new_seeker_list = [621, 619, 660, 580]
newer_seeker_list = [622, 620, 661, 581, 620, 618, 659, 579, 661, 659, 700, 620, 581, 579, 620, 540]
```

So each iteration, for each node values in `new_seeker_list` there are 4 nodes
created in `newer_seeker_list`.


## test_graph.matrix

This is a 2D array, which will be a square the size of the nodes specified.
Currently that's `40x40`.


## SCREEN_REFRESH

Currently setting this pretty high so that the comp isn't blasted really quickly
(crashed a few times on me!)




