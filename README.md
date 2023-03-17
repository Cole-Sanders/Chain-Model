# Chain-Model
Approximates the position of a chain hanging between two points.

How it works:
The two fixed points of the chain are set in the (x, y) plane with the variables x0, and y0 referring to the first point
and x1, y1 referring to the second point. This program plots a graph displaying how the chain would realistically hang if it was
fixed between those two points. An initial guess of the chain's location is entered; in this case, it was a simple straight
line between the two points. From there the program applies a derived force equation on each segment along the chain and nudges them
ever so slightly in the direction in which they would be pulled. It then repeats this process over and over in successive "sweeps"
across the chain until each segment "relaxes" into its equilibrium position. There is a system set up to minimize runtime throughout
this process by terminating the program when more sweeps fail to significantly impact the position of the segments. 

How to run it:
It can by run as a simple .py file. Be sure the check the plots view to see the graph.
