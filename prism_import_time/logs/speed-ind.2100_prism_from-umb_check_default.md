# Log files for prism_from-umb_check_default on model [speed-ind.2100](../../models/speed-ind.2100)

Parsed values: `[1282.446, 312.691, 277.285, 277.156, 337.567]`



### Log file: prism_from-umb_check_default_speed-ind.2100_rep1.log

```
Command(s):
../bin/prism  -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props
Wallclock time: 1777.167 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:45:55 GMT+01:00 2026
Hostname: r23m0210.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/speed-ind.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 38 iterations in 0.06 seconds (average 0.001579, setup 0.00)

Time for model construction: 1282.446 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 9389 nodes (187 terminal), 9518080 minterms, vars: 20r/20c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 718848 of 743424 (96.7%)

Building hybrid MTBDD matrix... [levels=20, nodes=9533] [446.9 KB]
Adding explicit sparse matrices... [levels=8, num=171, compact] [430.2 KB]
Creating vector for diagonals... [5.7 MB]
Allocating iteration vectors... [3 x 5.7 MB]
TOTAL: [23.5 MB]

Uniformisation: q.t = 2.797911 x 2100.000000 = 5875.612619
Fox-Glynn: left = 5336, right = 6527

Starting iterations...
Iteration 68 (of 6527): max relative diff=0.277469, 5.01 sec so far
Iteration 137 (of 6527): max relative diff=0.093648, 10.09 sec so far
Iteration 206 (of 6527): max relative diff=0.056490, 15.16 sec so far
Iteration 275 (of 6527): max relative diff=0.038953, 20.23 sec so far
Iteration 344 (of 6527): max relative diff=0.028691, 25.30 sec so far
Iteration 413 (of 6527): max relative diff=0.021950, 30.37 sec so far
Iteration 481 (of 6527): max relative diff=0.017262, 35.38 sec so far
Iteration 550 (of 6527): max relative diff=0.013754, 40.46 sec so far
Iteration 619 (of 6527): max relative diff=0.011096, 45.53 sec so far
Iteration 688 (of 6527): max relative diff=0.009041, 50.60 sec so far
Iteration 757 (of 6527): max relative diff=0.007428, 55.67 sec so far
Iteration 826 (of 6527): max relative diff=0.006149, 60.75 sec so far
Iteration 895 (of 6527): max relative diff=0.005125, 65.82 sec so far
Iteration 964 (of 6527): max relative diff=0.004314, 70.88 sec so far
Iteration 1032 (of 6527): max relative diff=0.003830, 75.89 sec so far
Iteration 1101 (of 6527): max relative diff=0.003415, 80.96 sec so far
Iteration 1170 (of 6527): max relative diff=0.003063, 86.03 sec so far
Iteration 1239 (of 6527): max relative diff=0.002761, 91.10 sec so far
Iteration 1308 (of 6527): max relative diff=0.002501, 96.17 sec so far
Iteration 1377 (of 6527): max relative diff=0.002276, 101.25 sec so far
Iteration 1446 (of 6527): max relative diff=0.002079, 106.32 sec so far
Iteration 1515 (of 6527): max relative diff=0.001906, 111.40 sec so far
Iteration 1584 (of 6527): max relative diff=0.001754, 116.47 sec so far
Iteration 1653 (of 6527): max relative diff=0.001620, 121.54 sec so far
Iteration 1722 (of 6527): max relative diff=0.001500, 126.61 sec so far
Iteration 1791 (of 6527): max relative diff=0.001393, 131.68 sec so far
Iteration 1860 (of 6527): max relative diff=0.001298, 136.75 sec so far
Iteration 1928 (of 6527): max relative diff=0.001214, 141.76 sec so far
Iteration 1997 (of 6527): max relative diff=0.001137, 146.83 sec so far
Iteration 2066 (of 6527): max relative diff=0.001067, 151.90 sec so far
Iteration 2135 (of 6527): max relative diff=0.001004, 156.97 sec so far
Iteration 2204 (of 6527): max relative diff=0.000947, 162.04 sec so far
Iteration 2273 (of 6527): max relative diff=0.000896, 167.11 sec so far
Iteration 2342 (of 6527): max relative diff=0.000849, 172.18 sec so far
Iteration 2410 (of 6527): max relative diff=0.000806, 177.19 sec so far
Iteration 2479 (of 6527): max relative diff=0.000767, 182.26 sec so far
Iteration 2548 (of 6527): max relative diff=0.000731, 187.33 sec so far
Iteration 2617 (of 6527): max relative diff=0.000697, 192.41 sec so far
Iteration 2686 (of 6527): max relative diff=0.000667, 197.48 sec so far
Iteration 2755 (of 6527): max relative diff=0.000639, 202.55 sec so far
Iteration 2824 (of 6527): max relative diff=0.000612, 207.62 sec so far
Iteration 2893 (of 6527): max relative diff=0.000588, 212.69 sec so far
Iteration 2962 (of 6527): max relative diff=0.000566, 217.76 sec so far
Iteration 3030 (of 6527): max relative diff=0.000545, 222.77 sec so far
Iteration 3099 (of 6527): max relative diff=0.000525, 227.84 sec so far
Iteration 3168 (of 6527): max relative diff=0.000507, 232.91 sec so far
Iteration 3237 (of 6527): max relative diff=0.000490, 237.98 sec so far
Iteration 3306 (of 6527): max relative diff=0.000474, 243.05 sec so far
Iteration 3375 (of 6527): max relative diff=0.000459, 248.13 sec so far
Iteration 3444 (of 6527): max relative diff=0.000445, 253.20 sec so far
Iteration 3513 (of 6527): max relative diff=0.000431, 258.28 sec so far
Iteration 3582 (of 6527): max relative diff=0.000419, 263.35 sec so far
Iteration 3651 (of 6527): max relative diff=0.000407, 268.42 sec so far
Iteration 3720 (of 6527): max relative diff=0.000396, 273.49 sec so far
Iteration 3789 (of 6527): max relative diff=0.000385, 278.56 sec so far
Iteration 3858 (of 6527): max relative diff=0.000375, 283.63 sec so far
Iteration 3926 (of 6527): max relative diff=0.000365, 288.64 sec so far
Iteration 3995 (of 6527): max relative diff=0.000356, 293.71 sec so far
Iteration 4064 (of 6527): max relative diff=0.000347, 298.78 sec so far
Iteration 4133 (of 6527): max relative diff=0.000339, 303.85 sec so far
Iteration 4202 (of 6527): max relative diff=0.000331, 308.92 sec so far
Iteration 4271 (of 6527): max relative diff=0.000323, 313.99 sec so far
Iteration 4340 (of 6527): max relative diff=0.000316, 319.06 sec so far
Iteration 4408 (of 6527): max relative diff=0.000309, 324.07 sec so far
Iteration 4477 (of 6527): max relative diff=0.000303, 329.14 sec so far
Iteration 4546 (of 6527): max relative diff=0.000296, 334.21 sec so far
Iteration 4615 (of 6527): max relative diff=0.000290, 339.28 sec so far
Iteration 4684 (of 6527): max relative diff=0.000284, 344.35 sec so far
Iteration 4752 (of 6527): max relative diff=0.000279, 349.36 sec so far
Iteration 4821 (of 6527): max relative diff=0.000273, 354.43 sec so far
Iteration 4890 (of 6527): max relative diff=0.000268, 359.50 sec so far
Iteration 4959 (of 6527): max relative diff=0.000263, 364.57 sec so far
Iteration 5028 (of 6527): max relative diff=0.000258, 369.64 sec so far
Iteration 5097 (of 6527): max relative diff=0.000254, 374.71 sec so far
Iteration 5166 (of 6527): max relative diff=0.000249, 379.78 sec so far
Iteration 5234 (of 6527): max relative diff=0.000245, 384.79 sec so far
Iteration 5303 (of 6527): max relative diff=0.000241, 389.86 sec so far
Iteration 5371 (of 6527): max relative diff=0.000237, 394.91 sec so far
Iteration 5438 (of 6527): max relative diff=0.000233, 399.93 sec so far
Iteration 5505 (of 6527): max relative diff=0.000229, 404.96 sec so far
Iteration 5572 (of 6527): max relative diff=0.000225, 409.99 sec so far
Iteration 5639 (of 6527): max relative diff=0.000222, 415.02 sec so far
Iteration 5706 (of 6527): max relative diff=0.000219, 420.04 sec so far
Iteration 5773 (of 6527): max relative diff=0.000215, 425.06 sec so far
Iteration 5840 (of 6527): max relative diff=0.000212, 430.09 sec so far
Iteration 5907 (of 6527): max relative diff=0.000209, 435.11 sec so far
Iteration 5974 (of 6527): max relative diff=0.000206, 440.15 sec so far
Iteration 6041 (of 6527): max relative diff=0.000203, 445.17 sec so far
Iteration 6108 (of 6527): max relative diff=0.000200, 450.20 sec so far
Iteration 6175 (of 6527): max relative diff=0.000197, 455.22 sec so far
Iteration 6242 (of 6527): max relative diff=0.000195, 460.25 sec so far
Iteration 6309 (of 6527): max relative diff=0.000192, 465.28 sec so far
Iteration 6376 (of 6527): max relative diff=0.000189, 470.31 sec so far
Iteration 6443 (of 6527): max relative diff=0.000187, 475.33 sec so far
Iteration 6510 (of 6527): max relative diff=0.000185, 480.36 sec so far

Iterative method: 6527 iterations in 488.46 seconds (average 0.073792, setup 6.82)

Value in the initial state: 0.04229449797846605

Time for model checking: 492.379 seconds.

Result: 0.04229449797846605


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_speed-ind.2100_rep2.log

```
Command(s):
../bin/prism  -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props
Wallclock time: 418.641 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:12:15 GMT+01:00 2026
Hostname: n23m0392.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/speed-ind.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 38 iterations in 0.01 seconds (average 0.000263, setup 0.00)

Time for model construction: 312.691 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 9389 nodes (187 terminal), 9518080 minterms, vars: 20r/20c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 718848 of 743424 (96.7%)

Building hybrid MTBDD matrix... [levels=20, nodes=9533] [446.9 KB]
Adding explicit sparse matrices... [levels=8, num=171, compact] [430.2 KB]
Creating vector for diagonals... [5.7 MB]
Allocating iteration vectors... [3 x 5.7 MB]
TOTAL: [23.5 MB]

Uniformisation: q.t = 2.797911 x 2100.000000 = 5875.612619
Fox-Glynn: left = 5336, right = 6527

Starting iterations...
Iteration 319 (of 6527): max relative diff=0.031879, 5.01 sec so far
Iteration 637 (of 6527): max relative diff=0.010509, 10.02 sec so far
Iteration 956 (of 6527): max relative diff=0.004386, 15.03 sec so far
Iteration 1275 (of 6527): max relative diff=0.002621, 20.04 sec so far
Iteration 1595 (of 6527): max relative diff=0.001732, 25.06 sec so far
Iteration 1913 (of 6527): max relative diff=0.001232, 30.07 sec so far
Iteration 2225 (of 6527): max relative diff=0.000931, 35.09 sec so far
Iteration 2541 (of 6527): max relative diff=0.000734, 40.10 sec so far
Iteration 2859 (of 6527): max relative diff=0.000600, 45.11 sec so far
Iteration 3178 (of 6527): max relative diff=0.000505, 50.12 sec so far
Iteration 3497 (of 6527): max relative diff=0.000434, 55.13 sec so far
Iteration 3816 (of 6527): max relative diff=0.000381, 60.14 sec so far
Iteration 4136 (of 6527): max relative diff=0.000339, 65.16 sec so far
Iteration 4456 (of 6527): max relative diff=0.000305, 70.17 sec so far
Iteration 4775 (of 6527): max relative diff=0.000277, 75.18 sec so far
Iteration 5095 (of 6527): max relative diff=0.000254, 80.20 sec so far
Iteration 5413 (of 6527): max relative diff=0.000234, 85.21 sec so far
Iteration 5721 (of 6527): max relative diff=0.000218, 90.23 sec so far
Iteration 6026 (of 6527): max relative diff=0.000204, 95.24 sec so far
Iteration 6334 (of 6527): max relative diff=0.000191, 100.25 sec so far

Iterative method: 6527 iterations in 104.81 seconds (average 0.015836, setup 1.45)

Value in the initial state: 0.04229449797846605

Time for model checking: 105.193 seconds.

Result: 0.04229449797846605


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_speed-ind.2100_rep3.log

```
Command(s):
../bin/prism  -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props
Wallclock time: 382.921 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:28:57 GMT+01:00 2026
Hostname: n23m0114.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/speed-ind.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 38 iterations in 0.01 seconds (average 0.000263, setup 0.00)

Time for model construction: 277.285 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 9389 nodes (187 terminal), 9518080 minterms, vars: 20r/20c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 718848 of 743424 (96.7%)

Building hybrid MTBDD matrix... [levels=20, nodes=9533] [446.9 KB]
Adding explicit sparse matrices... [levels=8, num=171, compact] [430.2 KB]
Creating vector for diagonals... [5.7 MB]
Allocating iteration vectors... [3 x 5.7 MB]
TOTAL: [23.5 MB]

Uniformisation: q.t = 2.797911 x 2100.000000 = 5875.612619
Fox-Glynn: left = 5336, right = 6527

Starting iterations...
Iteration 321 (of 6527): max relative diff=0.031605, 5.01 sec so far
Iteration 643 (of 6527): max relative diff=0.010322, 10.03 sec so far
Iteration 964 (of 6527): max relative diff=0.004314, 15.04 sec so far
Iteration 1285 (of 6527): max relative diff=0.002584, 20.05 sec so far
Iteration 1604 (of 6527): max relative diff=0.001714, 25.06 sec so far
Iteration 1924 (of 6527): max relative diff=0.001218, 30.07 sec so far
Iteration 2239 (of 6527): max relative diff=0.000921, 35.09 sec so far
Iteration 2555 (of 6527): max relative diff=0.000727, 40.10 sec so far
Iteration 2872 (of 6527): max relative diff=0.000595, 45.12 sec so far
Iteration 3190 (of 6527): max relative diff=0.000502, 50.14 sec so far
Iteration 3509 (of 6527): max relative diff=0.000432, 55.15 sec so far
Iteration 3828 (of 6527): max relative diff=0.000379, 60.16 sec so far
Iteration 4147 (of 6527): max relative diff=0.000337, 65.17 sec so far
Iteration 4467 (of 6527): max relative diff=0.000304, 70.18 sec so far
Iteration 4787 (of 6527): max relative diff=0.000276, 75.19 sec so far
Iteration 5107 (of 6527): max relative diff=0.000253, 80.21 sec so far
Iteration 5424 (of 6527): max relative diff=0.000233, 85.22 sec so far
Iteration 5736 (of 6527): max relative diff=0.000217, 90.23 sec so far
Iteration 6048 (of 6527): max relative diff=0.000203, 95.24 sec so far
Iteration 6362 (of 6527): max relative diff=0.000190, 100.26 sec so far

Iterative method: 6527 iterations in 104.33 seconds (average 0.015764, setup 1.44)

Value in the initial state: 0.04229449797846605

Time for model checking: 104.501 seconds.

Result: 0.04229449797846605


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_speed-ind.2100_rep4.log

```
Command(s):
../bin/prism  -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props
Wallclock time: 381.663 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:02 GMT+01:00 2026
Hostname: r23m0143.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/speed-ind.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 38 iterations in 0.01 seconds (average 0.000263, setup 0.00)

Time for model construction: 277.156 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 9389 nodes (187 terminal), 9518080 minterms, vars: 20r/20c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 718848 of 743424 (96.7%)

Building hybrid MTBDD matrix... [levels=20, nodes=9533] [446.9 KB]
Adding explicit sparse matrices... [levels=8, num=171, compact] [430.2 KB]
Creating vector for diagonals... [5.7 MB]
Allocating iteration vectors... [3 x 5.7 MB]
TOTAL: [23.5 MB]

Uniformisation: q.t = 2.797911 x 2100.000000 = 5875.612619
Fox-Glynn: left = 5336, right = 6527

Starting iterations...
Iteration 322 (of 6527): max relative diff=0.031470, 5.02 sec so far
Iteration 644 (of 6527): max relative diff=0.010291, 10.04 sec so far
Iteration 965 (of 6527): max relative diff=0.004307, 15.05 sec so far
Iteration 1286 (of 6527): max relative diff=0.002580, 20.06 sec so far
Iteration 1606 (of 6527): max relative diff=0.001710, 25.07 sec so far
Iteration 1926 (of 6527): max relative diff=0.001216, 30.08 sec so far
Iteration 2248 (of 6527): max relative diff=0.000914, 35.10 sec so far
Iteration 2570 (of 6527): max relative diff=0.000720, 40.11 sec so far
Iteration 2891 (of 6527): max relative diff=0.000589, 45.12 sec so far
Iteration 3212 (of 6527): max relative diff=0.000496, 50.13 sec so far
Iteration 3534 (of 6527): max relative diff=0.000427, 55.14 sec so far
Iteration 3855 (of 6527): max relative diff=0.000375, 60.15 sec so far
Iteration 4177 (of 6527): max relative diff=0.000334, 65.16 sec so far
Iteration 4499 (of 6527): max relative diff=0.000301, 70.18 sec so far
Iteration 4821 (of 6527): max relative diff=0.000273, 75.19 sec so far
Iteration 5142 (of 6527): max relative diff=0.000251, 80.21 sec so far
Iteration 5459 (of 6527): max relative diff=0.000232, 85.22 sec so far
Iteration 5771 (of 6527): max relative diff=0.000215, 90.23 sec so far
Iteration 6085 (of 6527): max relative diff=0.000201, 95.25 sec so far
Iteration 6399 (of 6527): max relative diff=0.000189, 100.26 sec so far

Iterative method: 6527 iterations in 103.74 seconds (average 0.015675, setup 1.43)

Value in the initial state: 0.04229449797846605

Time for model checking: 103.957 seconds.

Result: 0.04229449797846605


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_speed-ind.2100_rep5.log

```
Command(s):
../bin/prism  -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props
Wallclock time: 466.020 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:24:18 GMT+01:00 2026
Hostname: r23m0206.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/speed-ind.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 38 iterations in 0.01 seconds (average 0.000263, setup 0.00)

Time for model construction: 337.567 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 9389 nodes (187 terminal), 9518080 minterms, vars: 20r/20c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 718848 of 743424 (96.7%)

Building hybrid MTBDD matrix... [levels=20, nodes=9533] [446.9 KB]
Adding explicit sparse matrices... [levels=8, num=171, compact] [430.2 KB]
Creating vector for diagonals... [5.7 MB]
Allocating iteration vectors... [3 x 5.7 MB]
TOTAL: [23.5 MB]

Uniformisation: q.t = 2.797911 x 2100.000000 = 5875.612619
Fox-Glynn: left = 5336, right = 6527

Starting iterations...
Iteration 265 (of 6527): max relative diff=0.040903, 5.01 sec so far
Iteration 530 (of 6527): max relative diff=0.014669, 10.03 sec so far
Iteration 796 (of 6527): max relative diff=0.006670, 15.05 sec so far
Iteration 1061 (of 6527): max relative diff=0.003647, 20.07 sec so far
Iteration 1326 (of 6527): max relative diff=0.002439, 25.09 sec so far
Iteration 1592 (of 6527): max relative diff=0.001738, 30.10 sec so far
Iteration 1859 (of 6527): max relative diff=0.001299, 35.11 sec so far
Iteration 2123 (of 6527): max relative diff=0.001015, 40.12 sec so far
Iteration 2388 (of 6527): max relative diff=0.000820, 45.13 sec so far
Iteration 2653 (of 6527): max relative diff=0.000681, 50.14 sec so far
Iteration 2921 (of 6527): max relative diff=0.000579, 55.15 sec so far
Iteration 3186 (of 6527): max relative diff=0.000503, 60.17 sec so far
Iteration 3450 (of 6527): max relative diff=0.000443, 65.18 sec so far
Iteration 3714 (of 6527): max relative diff=0.000396, 70.19 sec so far
Iteration 3979 (of 6527): max relative diff=0.000358, 75.20 sec so far
Iteration 4243 (of 6527): max relative diff=0.000326, 80.22 sec so far
Iteration 4509 (of 6527): max relative diff=0.000300, 85.24 sec so far
Iteration 4780 (of 6527): max relative diff=0.000277, 90.26 sec so far
Iteration 5044 (of 6527): max relative diff=0.000257, 95.27 sec so far
Iteration 5308 (of 6527): max relative diff=0.000240, 100.29 sec so far
Iteration 5565 (of 6527): max relative diff=0.000226, 105.30 sec so far
Iteration 5825 (of 6527): max relative diff=0.000213, 110.32 sec so far
Iteration 6083 (of 6527): max relative diff=0.000201, 115.33 sec so far
Iteration 6341 (of 6527): max relative diff=0.000191, 120.35 sec so far

Iterative method: 6527 iterations in 125.71 seconds (average 0.018993, setup 1.74)

Value in the initial state: 0.04229449797846605

Time for model checking: 126.307 seconds.

Result: 0.04229449797846605


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

