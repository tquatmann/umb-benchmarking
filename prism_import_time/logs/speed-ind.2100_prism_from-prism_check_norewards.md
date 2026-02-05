# Log files for prism_from-prism_check_norewards on model [speed-ind.2100](../../models/speed-ind.2100)

Parsed values: `[21.253, 21.683, 20.463, 22.181, 20.527]`



### Log file: prism_from-prism_check_norewards_speed-ind.2100_rep1.log

```
Command(s):
../bin/prism  models/speed-ind.2100/model.prism models/speed-ind.2100/property.props
Wallclock time: 129.252 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:33:21 GMT+01:00 2026
Hostname: n23m0176.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/speed-ind.2100/model.prism models/speed-ind.2100/property.props

Parsing PRISM model file "models/speed-ind.2100/model.prism"...

Type:        CTMC
Modules:     S1_def S2_def S3_def S4_def Y_def Z_def CC_def XX_def
Actions:     []
Variables:   S1 S2 S3 S4 Y Z CC XX
Labels:      "target"

Parsing properties file "models/speed-ind.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.64 seconds (average 0.016842, setup 0.00)

Time for model construction: 21.253 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 33024 nodes (187 terminal), 9518080 minterms, vars: 58r/58c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 718848 of 743424 (96.7%)

Building hybrid MTBDD matrix... [levels=58, nodes=33162] [1.5 MB]
Adding explicit sparse matrices... [levels=33, num=428, compact] [756.5 KB]
Creating vector for diagonals... [5.7 MB]
Allocating iteration vectors... [3 x 5.7 MB]
TOTAL: [24.9 MB]

Uniformisation: q.t = 2.797911 x 2100.000000 = 5875.612619
Fox-Glynn: left = 5336, right = 6527

Starting iterations...
Iteration 313 (of 6527): max relative diff=0.032723, 5.01 sec so far
Iteration 620 (of 6527): max relative diff=0.011062, 10.03 sec so far
Iteration 935 (of 6527): max relative diff=0.004625, 15.05 sec so far
Iteration 1239 (of 6527): max relative diff=0.002761, 20.06 sec so far
Iteration 1551 (of 6527): max relative diff=0.001825, 25.07 sec so far
Iteration 1865 (of 6527): max relative diff=0.001292, 30.09 sec so far
Iteration 2179 (of 6527): max relative diff=0.000967, 35.10 sec so far
Iteration 2494 (of 6527): max relative diff=0.000759, 40.11 sec so far
Iteration 2808 (of 6527): max relative diff=0.000618, 45.12 sec so far
Iteration 3123 (of 6527): max relative diff=0.000519, 50.13 sec so far
Iteration 3437 (of 6527): max relative diff=0.000446, 55.14 sec so far
Iteration 3750 (of 6527): max relative diff=0.000391, 60.15 sec so far
Iteration 4065 (of 6527): max relative diff=0.000347, 65.17 sec so far
Iteration 4380 (of 6527): max relative diff=0.000312, 70.18 sec so far
Iteration 4695 (of 6527): max relative diff=0.000283, 75.19 sec so far
Iteration 4999 (of 6527): max relative diff=0.000260, 80.20 sec so far
Iteration 5312 (of 6527): max relative diff=0.000240, 85.21 sec so far
Iteration 5616 (of 6527): max relative diff=0.000223, 90.22 sec so far
Iteration 5921 (of 6527): max relative diff=0.000208, 95.24 sec so far
Iteration 6226 (of 6527): max relative diff=0.000195, 100.25 sec so far

Iterative method: 6527 iterations in 106.70 seconds (average 0.016118, setup 1.50)

Value in the initial state: 0.042294497978464705

Time for model checking: 107.003 seconds.

Result: 0.042294497978464705


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_speed-ind.2100_rep2.log

```
Command(s):
../bin/prism  models/speed-ind.2100/model.prism models/speed-ind.2100/property.props
Wallclock time: 133.014 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:05:04 GMT+01:00 2026
Hostname: n23m0134.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/speed-ind.2100/model.prism models/speed-ind.2100/property.props

Parsing PRISM model file "models/speed-ind.2100/model.prism"...

Type:        CTMC
Modules:     S1_def S2_def S3_def S4_def Y_def Z_def CC_def XX_def
Actions:     []
Variables:   S1 S2 S3 S4 Y Z CC XX
Labels:      "target"

Parsing properties file "models/speed-ind.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.68 seconds (average 0.017895, setup 0.00)

Time for model construction: 21.683 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 33024 nodes (187 terminal), 9518080 minterms, vars: 58r/58c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 718848 of 743424 (96.7%)

Building hybrid MTBDD matrix... [levels=58, nodes=33162] [1.5 MB]
Adding explicit sparse matrices... [levels=33, num=428, compact] [756.5 KB]
Creating vector for diagonals... [5.7 MB]
Allocating iteration vectors... [3 x 5.7 MB]
TOTAL: [24.9 MB]

Uniformisation: q.t = 2.797911 x 2100.000000 = 5875.612619
Fox-Glynn: left = 5336, right = 6527

Starting iterations...
Iteration 304 (of 6527): max relative diff=0.034053, 5.02 sec so far
Iteration 607 (of 6527): max relative diff=0.011509, 10.03 sec so far
Iteration 912 (of 6527): max relative diff=0.004905, 15.05 sec so far
Iteration 1215 (of 6527): max relative diff=0.002861, 20.06 sec so far
Iteration 1519 (of 6527): max relative diff=0.001897, 25.08 sec so far
Iteration 1824 (of 6527): max relative diff=0.001347, 30.09 sec so far
Iteration 2123 (of 6527): max relative diff=0.001015, 35.10 sec so far
Iteration 2428 (of 6527): max relative diff=0.000796, 40.11 sec so far
Iteration 2733 (of 6527): max relative diff=0.000647, 45.13 sec so far
Iteration 3040 (of 6527): max relative diff=0.000542, 50.14 sec so far
Iteration 3349 (of 6527): max relative diff=0.000464, 55.16 sec so far
Iteration 3654 (of 6527): max relative diff=0.000406, 60.17 sec so far
Iteration 3960 (of 6527): max relative diff=0.000361, 65.19 sec so far
Iteration 4262 (of 6527): max relative diff=0.000324, 70.20 sec so far
Iteration 4567 (of 6527): max relative diff=0.000294, 75.21 sec so far
Iteration 4871 (of 6527): max relative diff=0.000270, 80.22 sec so far
Iteration 5176 (of 6527): max relative diff=0.000248, 85.24 sec so far
Iteration 5474 (of 6527): max relative diff=0.000231, 90.26 sec so far
Iteration 5757 (of 6527): max relative diff=0.000216, 95.28 sec so far
Iteration 6053 (of 6527): max relative diff=0.000202, 100.30 sec so far
Iteration 6344 (of 6527): max relative diff=0.000191, 105.32 sec so far

Iterative method: 6527 iterations in 109.93 seconds (average 0.016611, setup 1.51)

Value in the initial state: 0.042294497978464705

Time for model checking: 110.247 seconds.

Result: 0.042294497978464705


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_speed-ind.2100_rep3.log

```
Command(s):
../bin/prism  models/speed-ind.2100/model.prism models/speed-ind.2100/property.props
Wallclock time: 143.302 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:09:44 GMT+01:00 2026
Hostname: r23m0016.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/speed-ind.2100/model.prism models/speed-ind.2100/property.props

Parsing PRISM model file "models/speed-ind.2100/model.prism"...

Type:        CTMC
Modules:     S1_def S2_def S3_def S4_def Y_def Z_def CC_def XX_def
Actions:     []
Variables:   S1 S2 S3 S4 Y Z CC XX
Labels:      "target"

Parsing properties file "models/speed-ind.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.67 seconds (average 0.017632, setup 0.00)

Time for model construction: 20.463 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 33024 nodes (187 terminal), 9518080 minterms, vars: 58r/58c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 718848 of 743424 (96.7%)

Building hybrid MTBDD matrix... [levels=58, nodes=33162] [1.5 MB]
Adding explicit sparse matrices... [levels=33, num=428, compact] [756.5 KB]
Creating vector for diagonals... [5.7 MB]
Allocating iteration vectors... [3 x 5.7 MB]
TOTAL: [24.9 MB]

Uniformisation: q.t = 2.797911 x 2100.000000 = 5875.612619
Fox-Glynn: left = 5336, right = 6527

Starting iterations...
Iteration 270 (of 6527): max relative diff=0.039909, 5.02 sec so far
Iteration 542 (of 6527): max relative diff=0.014111, 10.03 sec so far
Iteration 818 (of 6527): max relative diff=0.006283, 15.05 sec so far
Iteration 1091 (of 6527): max relative diff=0.003471, 20.07 sec so far
Iteration 1362 (of 6527): max relative diff=0.002322, 25.08 sec so far
Iteration 1638 (of 6527): max relative diff=0.001648, 30.09 sec so far
Iteration 1912 (of 6527): max relative diff=0.001233, 35.10 sec so far
Iteration 2184 (of 6527): max relative diff=0.000963, 40.11 sec so far
Iteration 2457 (of 6527): max relative diff=0.000779, 45.12 sec so far
Iteration 2733 (of 6527): max relative diff=0.000647, 50.14 sec so far
Iteration 3006 (of 6527): max relative diff=0.000552, 55.16 sec so far
Iteration 3281 (of 6527): max relative diff=0.000480, 60.18 sec so far
Iteration 3556 (of 6527): max relative diff=0.000423, 65.19 sec so far
Iteration 3833 (of 6527): max relative diff=0.000378, 70.20 sec so far
Iteration 4109 (of 6527): max relative diff=0.000342, 75.21 sec so far
Iteration 4386 (of 6527): max relative diff=0.000312, 80.23 sec so far
Iteration 4660 (of 6527): max relative diff=0.000286, 85.24 sec so far
Iteration 4936 (of 6527): max relative diff=0.000265, 90.26 sec so far
Iteration 5211 (of 6527): max relative diff=0.000246, 95.27 sec so far
Iteration 5481 (of 6527): max relative diff=0.000230, 100.29 sec so far
Iteration 5753 (of 6527): max relative diff=0.000216, 105.31 sec so far
Iteration 6023 (of 6527): max relative diff=0.000204, 110.32 sec so far
Iteration 6288 (of 6527): max relative diff=0.000193, 115.34 sec so far

Iterative method: 6527 iterations in 121.52 seconds (average 0.018351, setup 1.74)

Value in the initial state: 0.042294497978464705

Time for model checking: 121.995 seconds.

Result: 0.042294497978464705


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_speed-ind.2100_rep4.log

```
Command(s):
../bin/prism  models/speed-ind.2100/model.prism models/speed-ind.2100/property.props
Wallclock time: 136.724 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:07:22 GMT+01:00 2026
Hostname: n23m0061.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/speed-ind.2100/model.prism models/speed-ind.2100/property.props

Parsing PRISM model file "models/speed-ind.2100/model.prism"...

Type:        CTMC
Modules:     S1_def S2_def S3_def S4_def Y_def Z_def CC_def XX_def
Actions:     []
Variables:   S1 S2 S3 S4 Y Z CC XX
Labels:      "target"

Parsing properties file "models/speed-ind.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.71 seconds (average 0.018684, setup 0.00)

Time for model construction: 22.181 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 33024 nodes (187 terminal), 9518080 minterms, vars: 58r/58c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 718848 of 743424 (96.7%)

Building hybrid MTBDD matrix... [levels=58, nodes=33162] [1.5 MB]
Adding explicit sparse matrices... [levels=33, num=428, compact] [756.5 KB]
Creating vector for diagonals... [5.7 MB]
Allocating iteration vectors... [3 x 5.7 MB]
TOTAL: [24.9 MB]

Uniformisation: q.t = 2.797911 x 2100.000000 = 5875.612619
Fox-Glynn: left = 5336, right = 6527

Starting iterations...
Iteration 296 (of 6527): max relative diff=0.035305, 5.02 sec so far
Iteration 590 (of 6527): max relative diff=0.012128, 10.04 sec so far
Iteration 876 (of 6527): max relative diff=0.005385, 15.06 sec so far
Iteration 1168 (of 6527): max relative diff=0.003072, 20.07 sec so far
Iteration 1460 (of 6527): max relative diff=0.002042, 25.08 sec so far
Iteration 1756 (of 6527): max relative diff=0.001446, 30.09 sec so far
Iteration 2052 (of 6527): max relative diff=0.001081, 35.10 sec so far
Iteration 2350 (of 6527): max relative diff=0.000843, 40.12 sec so far
Iteration 2648 (of 6527): max relative diff=0.000683, 45.13 sec so far
Iteration 2944 (of 6527): max relative diff=0.000571, 50.14 sec so far
Iteration 3242 (of 6527): max relative diff=0.000489, 55.16 sec so far
Iteration 3539 (of 6527): max relative diff=0.000426, 60.18 sec so far
Iteration 3838 (of 6527): max relative diff=0.000378, 65.20 sec so far
Iteration 4136 (of 6527): max relative diff=0.000339, 70.21 sec so far
Iteration 4428 (of 6527): max relative diff=0.000307, 75.22 sec so far
Iteration 4725 (of 6527): max relative diff=0.000281, 80.23 sec so far
Iteration 5020 (of 6527): max relative diff=0.000259, 85.24 sec so far
Iteration 5317 (of 6527): max relative diff=0.000240, 90.25 sec so far
Iteration 5603 (of 6527): max relative diff=0.000224, 95.27 sec so far
Iteration 5888 (of 6527): max relative diff=0.000210, 100.28 sec so far
Iteration 6172 (of 6527): max relative diff=0.000197, 105.29 sec so far
Iteration 6457 (of 6527): max relative diff=0.000186, 110.30 sec so far

Iterative method: 6527 iterations in 113.06 seconds (average 0.017087, setup 1.53)

Value in the initial state: 0.042294497978464705

Time for model checking: 113.386 seconds.

Result: 0.042294497978464705


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_speed-ind.2100_rep5.log

```
Command(s):
../bin/prism  models/speed-ind.2100/model.prism models/speed-ind.2100/property.props
Wallclock time: 131.465 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:23 GMT+01:00 2026
Hostname: n23m0252.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/speed-ind.2100/model.prism models/speed-ind.2100/property.props

Parsing PRISM model file "models/speed-ind.2100/model.prism"...

Type:        CTMC
Modules:     S1_def S2_def S3_def S4_def Y_def Z_def CC_def XX_def
Actions:     []
Variables:   S1 S2 S3 S4 Y Z CC XX
Labels:      "target"

Parsing properties file "models/speed-ind.2100/property.props"...

1 property:
(1) "change_state": P=? [ F<=2100 "target" ]

---------------------------------------------------------------------

Model checking: "change_state": P=? [ F<=2100 "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 38 iterations in 0.66 seconds (average 0.017368, setup 0.00)

Time for model construction: 20.527 seconds.

Type:        CTMC
States:      743424 (1 initial)
Transitions: 9518080

Rate matrix: 33024 nodes (187 terminal), 9518080 minterms, vars: 58r/58c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 718848 of 743424 (96.7%)

Building hybrid MTBDD matrix... [levels=58, nodes=33162] [1.5 MB]
Adding explicit sparse matrices... [levels=33, num=428, compact] [756.5 KB]
Creating vector for diagonals... [5.7 MB]
Allocating iteration vectors... [3 x 5.7 MB]
TOTAL: [24.9 MB]

Uniformisation: q.t = 2.797911 x 2100.000000 = 5875.612619
Fox-Glynn: left = 5336, right = 6527

Starting iterations...
Iteration 310 (of 6527): max relative diff=0.033157, 5.02 sec so far
Iteration 622 (of 6527): max relative diff=0.010995, 10.04 sec so far
Iteration 930 (of 6527): max relative diff=0.004684, 15.05 sec so far
Iteration 1234 (of 6527): max relative diff=0.002782, 20.06 sec so far
Iteration 1542 (of 6527): max relative diff=0.001845, 25.07 sec so far
Iteration 1853 (of 6527): max relative diff=0.001307, 30.08 sec so far
Iteration 2164 (of 6527): max relative diff=0.000980, 35.09 sec so far
Iteration 2475 (of 6527): max relative diff=0.000769, 40.10 sec so far
Iteration 2788 (of 6527): max relative diff=0.000626, 45.12 sec so far
Iteration 3099 (of 6527): max relative diff=0.000525, 50.13 sec so far
Iteration 3410 (of 6527): max relative diff=0.000452, 55.15 sec so far
Iteration 3721 (of 6527): max relative diff=0.000395, 60.17 sec so far
Iteration 4032 (of 6527): max relative diff=0.000351, 65.18 sec so far
Iteration 4343 (of 6527): max relative diff=0.000316, 70.19 sec so far
Iteration 4646 (of 6527): max relative diff=0.000288, 75.20 sec so far
Iteration 4954 (of 6527): max relative diff=0.000263, 80.22 sec so far
Iteration 5263 (of 6527): max relative diff=0.000243, 85.23 sec so far
Iteration 5565 (of 6527): max relative diff=0.000226, 90.25 sec so far
Iteration 5864 (of 6527): max relative diff=0.000211, 95.26 sec so far
Iteration 6163 (of 6527): max relative diff=0.000198, 100.27 sec so far
Iteration 6462 (of 6527): max relative diff=0.000186, 105.28 sec so far

Iterative method: 6527 iterations in 107.87 seconds (average 0.016297, setup 1.50)

Value in the initial state: 0.042294497978464705

Time for model checking: 108.219 seconds.

Result: 0.042294497978464705


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

