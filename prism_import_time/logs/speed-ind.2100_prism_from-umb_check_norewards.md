# Log files for prism_from-umb_check_norewards on model [speed-ind.2100](../../models/speed-ind.2100)

Parsed values: `[309.077, 350.514, 279.739, 322.141, 277.266]`



### Log file: prism_from-umb_check_norewards_speed-ind.2100_rep1.log

```
Command(s):
../bin/prism  -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props
Wallclock time: 419.966 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:29:42 GMT+01:00 2026
Hostname: r23m0203.hpc.itc.rwth-aachen.de
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

Time for model construction: 309.077 seconds.

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
Iteration 306 (of 6527): max relative diff=0.033750, 5.02 sec so far
Iteration 611 (of 6527): max relative diff=0.011369, 10.03 sec so far
Iteration 920 (of 6527): max relative diff=0.004806, 15.05 sec so far
Iteration 1228 (of 6527): max relative diff=0.002806, 20.07 sec so far
Iteration 1534 (of 6527): max relative diff=0.001863, 25.09 sec so far
Iteration 1840 (of 6527): max relative diff=0.001325, 30.10 sec so far
Iteration 2146 (of 6527): max relative diff=0.000995, 35.12 sec so far
Iteration 2451 (of 6527): max relative diff=0.000782, 40.13 sec so far
Iteration 2757 (of 6527): max relative diff=0.000638, 45.14 sec so far
Iteration 3060 (of 6527): max relative diff=0.000536, 50.15 sec so far
Iteration 3362 (of 6527): max relative diff=0.000462, 55.16 sec so far
Iteration 3665 (of 6527): max relative diff=0.000404, 60.18 sec so far
Iteration 3968 (of 6527): max relative diff=0.000360, 65.19 sec so far
Iteration 4273 (of 6527): max relative diff=0.000323, 70.21 sec so far
Iteration 4578 (of 6527): max relative diff=0.000293, 75.22 sec so far
Iteration 4882 (of 6527): max relative diff=0.000269, 80.23 sec so far
Iteration 5185 (of 6527): max relative diff=0.000248, 85.25 sec so far
Iteration 5484 (of 6527): max relative diff=0.000230, 90.27 sec so far
Iteration 5775 (of 6527): max relative diff=0.000215, 95.29 sec so far
Iteration 6067 (of 6527): max relative diff=0.000202, 100.30 sec so far
Iteration 6358 (of 6527): max relative diff=0.000190, 105.32 sec so far

Iterative method: 6527 iterations in 109.68 seconds (average 0.016583, setup 1.44)

Value in the initial state: 0.04229449797846605

Time for model checking: 110.022 seconds.

Result: 0.04229449797846605


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_speed-ind.2100_rep2.log

```
Command(s):
../bin/prism  -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props
Wallclock time: 475.684 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:22:07 GMT+01:00 2026
Hostname: n23m0033.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 38 iterations in 0.02 seconds (average 0.000526, setup 0.00)

Time for model construction: 350.514 seconds.

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
Iteration 277 (of 6527): max relative diff=0.038581, 5.02 sec so far
Iteration 555 (of 6527): max relative diff=0.013536, 10.04 sec so far
Iteration 833 (of 6527): max relative diff=0.006035, 15.05 sec so far
Iteration 1107 (of 6527): max relative diff=0.003382, 20.07 sec so far
Iteration 1382 (of 6527): max relative diff=0.002261, 25.08 sec so far
Iteration 1656 (of 6527): max relative diff=0.001614, 30.09 sec so far
Iteration 1928 (of 6527): max relative diff=0.001214, 35.11 sec so far
Iteration 2202 (of 6527): max relative diff=0.000949, 40.13 sec so far
Iteration 2478 (of 6527): max relative diff=0.000767, 45.15 sec so far
Iteration 2750 (of 6527): max relative diff=0.000641, 50.17 sec so far
Iteration 3023 (of 6527): max relative diff=0.000547, 55.18 sec so far
Iteration 3296 (of 6527): max relative diff=0.000476, 60.20 sec so far
Iteration 3564 (of 6527): max relative diff=0.000422, 65.21 sec so far
Iteration 3838 (of 6527): max relative diff=0.000378, 70.23 sec so far
Iteration 4111 (of 6527): max relative diff=0.000342, 75.25 sec so far
Iteration 4385 (of 6527): max relative diff=0.000312, 80.26 sec so far
Iteration 4654 (of 6527): max relative diff=0.000287, 85.27 sec so far
Iteration 4923 (of 6527): max relative diff=0.000266, 90.28 sec so far
Iteration 5191 (of 6527): max relative diff=0.000247, 95.29 sec so far
Iteration 5459 (of 6527): max relative diff=0.000232, 100.31 sec so far
Iteration 5720 (of 6527): max relative diff=0.000218, 105.33 sec so far
Iteration 5979 (of 6527): max relative diff=0.000206, 110.35 sec so far
Iteration 6239 (of 6527): max relative diff=0.000195, 115.36 sec so far
Iteration 6500 (of 6527): max relative diff=0.000185, 120.38 sec so far

Iterative method: 6527 iterations in 122.59 seconds (average 0.018526, setup 1.67)

Value in the initial state: 0.04229449797846605

Time for model checking: 123.178 seconds.

Result: 0.04229449797846605


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_speed-ind.2100_rep3.log

```
Command(s):
../bin/prism  -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props
Wallclock time: 388.487 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:01 GMT+01:00 2026
Hostname: r23m0152.hpc.itc.rwth-aachen.de
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

Time for model construction: 279.739 seconds.

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
Iteration 315 (of 6527): max relative diff=0.032438, 5.01 sec so far
Iteration 630 (of 6527): max relative diff=0.010733, 10.02 sec so far
Iteration 946 (of 6527): max relative diff=0.004498, 15.04 sec so far
Iteration 1260 (of 6527): max relative diff=0.002678, 20.06 sec so far
Iteration 1574 (of 6527): max relative diff=0.001775, 25.08 sec so far
Iteration 1889 (of 6527): max relative diff=0.001261, 30.10 sec so far
Iteration 2205 (of 6527): max relative diff=0.000947, 35.11 sec so far
Iteration 2520 (of 6527): max relative diff=0.000745, 40.12 sec so far
Iteration 2836 (of 6527): max relative diff=0.000608, 45.14 sec so far
Iteration 3152 (of 6527): max relative diff=0.000511, 50.16 sec so far
Iteration 3468 (of 6527): max relative diff=0.000440, 55.17 sec so far
Iteration 3784 (of 6527): max relative diff=0.000386, 60.18 sec so far
Iteration 4100 (of 6527): max relative diff=0.000343, 65.20 sec so far
Iteration 4416 (of 6527): max relative diff=0.000309, 70.21 sec so far
Iteration 4732 (of 6527): max relative diff=0.000280, 75.22 sec so far
Iteration 5046 (of 6527): max relative diff=0.000257, 80.24 sec so far
Iteration 5358 (of 6527): max relative diff=0.000237, 85.25 sec so far
Iteration 5661 (of 6527): max relative diff=0.000221, 90.26 sec so far
Iteration 5965 (of 6527): max relative diff=0.000206, 95.27 sec so far
Iteration 6269 (of 6527): max relative diff=0.000194, 100.28 sec so far

Iterative method: 6527 iterations in 105.90 seconds (average 0.016006, setup 1.43)

Value in the initial state: 0.04229449797846605

Time for model checking: 106.197 seconds.

Result: 0.04229449797846605


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_speed-ind.2100_rep4.log

```
Command(s):
../bin/prism  -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props
Wallclock time: 435.506 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:00:27 GMT+01:00 2026
Hostname: n23m0105.hpc.itc.rwth-aachen.de
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

Time for model construction: 322.141 seconds.

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
Iteration 302 (of 6527): max relative diff=0.034359, 5.02 sec so far
Iteration 595 (of 6527): max relative diff=0.011942, 10.04 sec so far
Iteration 895 (of 6527): max relative diff=0.005125, 15.06 sec so far
Iteration 1194 (of 6527): max relative diff=0.002953, 20.07 sec so far
Iteration 1495 (of 6527): max relative diff=0.001954, 25.08 sec so far
Iteration 1797 (of 6527): max relative diff=0.001385, 30.10 sec so far
Iteration 2099 (of 6527): max relative diff=0.001036, 35.12 sec so far
Iteration 2400 (of 6527): max relative diff=0.000812, 40.13 sec so far
Iteration 2701 (of 6527): max relative diff=0.000661, 45.14 sec so far
Iteration 3003 (of 6527): max relative diff=0.000553, 50.15 sec so far
Iteration 3304 (of 6527): max relative diff=0.000474, 55.16 sec so far
Iteration 3603 (of 6527): max relative diff=0.000415, 60.17 sec so far
Iteration 3903 (of 6527): max relative diff=0.000368, 65.18 sec so far
Iteration 4195 (of 6527): max relative diff=0.000332, 70.19 sec so far
Iteration 4495 (of 6527): max relative diff=0.000301, 75.20 sec so far
Iteration 4794 (of 6527): max relative diff=0.000275, 80.22 sec so far
Iteration 5095 (of 6527): max relative diff=0.000254, 85.23 sec so far
Iteration 5393 (of 6527): max relative diff=0.000235, 90.25 sec so far
Iteration 5681 (of 6527): max relative diff=0.000220, 95.26 sec so far
Iteration 5970 (of 6527): max relative diff=0.000206, 100.28 sec so far
Iteration 6258 (of 6527): max relative diff=0.000194, 105.29 sec so far

Iterative method: 6527 iterations in 111.43 seconds (average 0.016850, setup 1.45)

Value in the initial state: 0.04229449797846605

Time for model checking: 111.716 seconds.

Result: 0.04229449797846605


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_speed-ind.2100_rep5.log

```
Command(s):
../bin/prism  -importmodel models/speed-ind.2100/prism.model.umb models/speed-ind.2100/property.props
Wallclock time: 385.212 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:01 GMT+01:00 2026
Hostname: r23m0152.hpc.itc.rwth-aachen.de
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

Time for model construction: 277.266 seconds.

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
Iteration 318 (of 6527): max relative diff=0.032018, 5.02 sec so far
Iteration 634 (of 6527): max relative diff=0.010604, 10.04 sec so far
Iteration 949 (of 6527): max relative diff=0.004464, 15.05 sec so far
Iteration 1263 (of 6527): max relative diff=0.002667, 20.06 sec so far
Iteration 1578 (of 6527): max relative diff=0.001767, 25.08 sec so far
Iteration 1891 (of 6527): max relative diff=0.001259, 30.09 sec so far
Iteration 2207 (of 6527): max relative diff=0.000945, 35.10 sec so far
Iteration 2522 (of 6527): max relative diff=0.000744, 40.11 sec so far
Iteration 2838 (of 6527): max relative diff=0.000607, 45.13 sec so far
Iteration 3154 (of 6527): max relative diff=0.000511, 50.15 sec so far
Iteration 3469 (of 6527): max relative diff=0.000440, 55.16 sec so far
Iteration 3785 (of 6527): max relative diff=0.000385, 60.17 sec so far
Iteration 4101 (of 6527): max relative diff=0.000343, 65.19 sec so far
Iteration 4417 (of 6527): max relative diff=0.000308, 70.20 sec so far
Iteration 4733 (of 6527): max relative diff=0.000280, 75.21 sec so far
Iteration 5047 (of 6527): max relative diff=0.000257, 80.23 sec so far
Iteration 5361 (of 6527): max relative diff=0.000237, 85.24 sec so far
Iteration 5664 (of 6527): max relative diff=0.000221, 90.26 sec so far
Iteration 5968 (of 6527): max relative diff=0.000206, 95.27 sec so far
Iteration 6272 (of 6527): max relative diff=0.000193, 100.28 sec so far

Iterative method: 6527 iterations in 105.94 seconds (average 0.016009, setup 1.45)

Value in the initial state: 0.04229449797846605

Time for model checking: 106.191 seconds.

Result: 0.04229449797846605


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

