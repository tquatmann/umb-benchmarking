# Log files for prism_from-umb_check_norewards on model [cluster.64-2000-20](../../models/cluster.64-2000-20)

Parsed values: `[32.827, 27.211, 27.098, 26.27, 26.986]`



### Log file: prism_from-umb_check_norewards_cluster.64-2000-20_rep1.log

```
Command(s):
../bin/prism  -importmodel models/cluster.64-2000-20/prism.model.umb models/cluster.64-2000-20/property.props
Wallclock time: 184.567 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 08:03:08 GMT+01:00 2026
Hostname: r23m0141.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/cluster.64-2000-20/prism.model.umb models/cluster.64-2000-20/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   x
Labels:      "minimum"

Parsing properties file "models/cluster.64-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:symbolic)...
Importing transitions... [ 10% 22% 32% 42% 50% 60% 68% 78% 86% 94% 100% ]

Computing reachable states...

Reachability (BFS): 133 iterations in 0.31 seconds (average 0.002331, setup 0.00)

Time for model construction: 32.827 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 25495 nodes (71 terminal), 733216 minterms, vars: 18r/18c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 36133 of 151060 (23.9%)

Building hybrid MTBDD matrix... [levels=18, nodes=51088] [2.3 MB]
Adding explicit sparse matrices... [levels=6, num=5507, compact] [839.4 KB]
Creating vector for diagonals... [dist=1448, compact] [306.4 KB]
Allocating iteration vectors... [3 x 1.2 MB]
TOTAL: [6.9 MB]

Uniformisation: q.t = 41.057295 x 2000.000000 = 82114.590000
Fox-Glynn: left = 80105, right = 84548

Starting iterations...
Iteration 2839 (of 84548): max relative diff=0.000427, 5.01 sec so far
Iteration 5695 (of 84548): max relative diff=0.000181, 10.02 sec so far
Iteration 8544 (of 84548): max relative diff=0.000119, 15.03 sec so far
Iteration 11290 (of 84548): max relative diff=0.000090, 20.04 sec so far
Iteration 14120 (of 84548): max relative diff=0.000072, 25.05 sec so far
Iteration 16946 (of 84548): max relative diff=0.000060, 30.06 sec so far
Iteration 19794 (of 84548): max relative diff=0.000051, 35.07 sec so far
Iteration 22647 (of 84548): max relative diff=0.000044, 40.08 sec so far
Iteration 25489 (of 84548): max relative diff=0.000039, 45.09 sec so far
Iteration 28336 (of 84548): max relative diff=0.000035, 50.10 sec so far
Iteration 31192 (of 84548): max relative diff=0.000032, 55.11 sec so far
Iteration 34047 (of 84548): max relative diff=0.000030, 60.12 sec so far
Iteration 36890 (of 84548): max relative diff=0.000027, 65.13 sec so far
Iteration 39732 (of 84548): max relative diff=0.000025, 70.14 sec so far
Iteration 42587 (of 84548): max relative diff=0.000024, 75.15 sec so far
Iteration 45345 (of 84548): max relative diff=0.000022, 80.16 sec so far
Iteration 48165 (of 84548): max relative diff=0.000021, 85.17 sec so far
Iteration 50994 (of 84548): max relative diff=0.000020, 90.18 sec so far
Iteration 53831 (of 84548): max relative diff=0.000019, 95.19 sec so far
Iteration 56679 (of 84548): max relative diff=0.000018, 100.20 sec so far
Iteration 59526 (of 84548): max relative diff=0.000017, 105.21 sec so far
Iteration 62361 (of 84548): max relative diff=0.000016, 110.22 sec so far
Iteration 65211 (of 84548): max relative diff=0.000015, 115.23 sec so far
Iteration 68059 (of 84548): max relative diff=0.000015, 120.24 sec so far
Iteration 70897 (of 84548): max relative diff=0.000014, 125.25 sec so far
Iteration 73735 (of 84548): max relative diff=0.000014, 130.26 sec so far
Iteration 76587 (of 84548): max relative diff=0.000013, 135.27 sec so far
Iteration 79339 (of 84548): max relative diff=0.000013, 140.28 sec so far
Iteration 82068 (of 84548): max relative diff=0.000012, 145.29 sec so far

Iterative method: 84548 iterations in 150.64 seconds (average 0.001772, setup 0.78)

Value in the initial state: 0.0010445396729789396

Time for model checking: 151.078 seconds.

Result: 0.0010445396729789396


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_cluster.64-2000-20_rep2.log

```
Command(s):
../bin/prism  -importmodel models/cluster.64-2000-20/prism.model.umb models/cluster.64-2000-20/property.props
Wallclock time: 187.636 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:04:04 GMT+01:00 2026
Hostname: n23m0341.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/cluster.64-2000-20/prism.model.umb models/cluster.64-2000-20/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   x
Labels:      "minimum"

Parsing properties file "models/cluster.64-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:symbolic)...
Importing transitions... [ 12% 22% 34% 46% 56% 68% 78% 90% 100% ]

Computing reachable states...

Reachability (BFS): 133 iterations in 0.21 seconds (average 0.001579, setup 0.00)

Time for model construction: 27.211 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 25495 nodes (71 terminal), 733216 minterms, vars: 18r/18c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 36133 of 151060 (23.9%)

Building hybrid MTBDD matrix... [levels=18, nodes=51088] [2.3 MB]
Adding explicit sparse matrices... [levels=6, num=5507, compact] [839.4 KB]
Creating vector for diagonals... [dist=1448, compact] [306.4 KB]
Allocating iteration vectors... [3 x 1.2 MB]
TOTAL: [6.9 MB]

Uniformisation: q.t = 41.057295 x 2000.000000 = 82114.590000
Fox-Glynn: left = 80105, right = 84548

Starting iterations...
Iteration 2554 (of 84548): max relative diff=0.000588, 5.01 sec so far
Iteration 5118 (of 84548): max relative diff=0.000202, 10.02 sec so far
Iteration 7673 (of 84548): max relative diff=0.000133, 15.03 sec so far
Iteration 10232 (of 84548): max relative diff=0.000099, 20.04 sec so far
Iteration 12794 (of 84548): max relative diff=0.000079, 25.05 sec so far
Iteration 15345 (of 84548): max relative diff=0.000066, 30.06 sec so far
Iteration 18058 (of 84548): max relative diff=0.000056, 35.07 sec so far
Iteration 20825 (of 84548): max relative diff=0.000048, 40.08 sec so far
Iteration 23609 (of 84548): max relative diff=0.000043, 45.09 sec so far
Iteration 26319 (of 84548): max relative diff=0.000038, 50.10 sec so far
Iteration 29063 (of 84548): max relative diff=0.000035, 55.11 sec so far
Iteration 31775 (of 84548): max relative diff=0.000032, 60.12 sec so far
Iteration 34481 (of 84548): max relative diff=0.000029, 65.13 sec so far
Iteration 37156 (of 84548): max relative diff=0.000027, 70.14 sec so far
Iteration 39859 (of 84548): max relative diff=0.000025, 75.15 sec so far
Iteration 42540 (of 84548): max relative diff=0.000024, 80.16 sec so far
Iteration 45239 (of 84548): max relative diff=0.000022, 85.17 sec so far
Iteration 47903 (of 84548): max relative diff=0.000021, 90.18 sec so far
Iteration 50596 (of 84548): max relative diff=0.000020, 95.19 sec so far
Iteration 53292 (of 84548): max relative diff=0.000019, 100.20 sec so far
Iteration 55996 (of 84548): max relative diff=0.000018, 105.21 sec so far
Iteration 58702 (of 84548): max relative diff=0.000017, 110.22 sec so far
Iteration 61415 (of 84548): max relative diff=0.000016, 115.23 sec so far
Iteration 64121 (of 84548): max relative diff=0.000016, 120.24 sec so far
Iteration 66827 (of 84548): max relative diff=0.000015, 125.25 sec so far
Iteration 69536 (of 84548): max relative diff=0.000014, 130.26 sec so far
Iteration 72244 (of 84548): max relative diff=0.000014, 135.27 sec so far
Iteration 74943 (of 84548): max relative diff=0.000013, 140.28 sec so far
Iteration 77650 (of 84548): max relative diff=0.000013, 145.29 sec so far
Iteration 80312 (of 84548): max relative diff=0.000012, 150.30 sec so far
Iteration 82923 (of 84548): max relative diff=0.000012, 155.31 sec so far

Iterative method: 84548 iterations in 159.26 seconds (average 0.001874, setup 0.84)

Value in the initial state: 0.0010445396729789396

Time for model checking: 159.753 seconds.

Result: 0.0010445396729789396


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_cluster.64-2000-20_rep3.log

```
Command(s):
../bin/prism  -importmodel models/cluster.64-2000-20/prism.model.umb models/cluster.64-2000-20/property.props
Wallclock time: 172.313 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:14:19 GMT+01:00 2026
Hostname: n23m0399.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/cluster.64-2000-20/prism.model.umb models/cluster.64-2000-20/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   x
Labels:      "minimum"

Parsing properties file "models/cluster.64-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:symbolic)...
Importing transitions... [ 12% 24% 34% 42% 54% 66% 78% 90% 100% ]

Computing reachable states...

Reachability (BFS): 133 iterations in 0.23 seconds (average 0.001729, setup 0.00)

Time for model construction: 27.098 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 25495 nodes (71 terminal), 733216 minterms, vars: 18r/18c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 36133 of 151060 (23.9%)

Building hybrid MTBDD matrix... [levels=18, nodes=51088] [2.3 MB]
Adding explicit sparse matrices... [levels=6, num=5507, compact] [839.4 KB]
Creating vector for diagonals... [dist=1448, compact] [306.4 KB]
Allocating iteration vectors... [3 x 1.2 MB]
TOTAL: [6.9 MB]

Uniformisation: q.t = 41.057295 x 2000.000000 = 82114.590000
Fox-Glynn: left = 80105, right = 84548

Starting iterations...
Iteration 2812 (of 84548): max relative diff=0.000441, 5.01 sec so far
Iteration 5694 (of 84548): max relative diff=0.000181, 10.02 sec so far
Iteration 8653 (of 84548): max relative diff=0.000118, 15.03 sec so far
Iteration 11662 (of 84548): max relative diff=0.000087, 20.04 sec so far
Iteration 14678 (of 84548): max relative diff=0.000069, 25.05 sec so far
Iteration 17562 (of 84548): max relative diff=0.000057, 30.06 sec so far
Iteration 20512 (of 84548): max relative diff=0.000049, 35.07 sec so far
Iteration 23547 (of 84548): max relative diff=0.000043, 40.08 sec so far
Iteration 26584 (of 84548): max relative diff=0.000038, 45.09 sec so far
Iteration 29584 (of 84548): max relative diff=0.000034, 50.10 sec so far
Iteration 32481 (of 84548): max relative diff=0.000031, 55.11 sec so far
Iteration 35523 (of 84548): max relative diff=0.000028, 60.12 sec so far
Iteration 38512 (of 84548): max relative diff=0.000026, 65.13 sec so far
Iteration 41550 (of 84548): max relative diff=0.000024, 70.14 sec so far
Iteration 44325 (of 84548): max relative diff=0.000023, 75.15 sec so far
Iteration 47296 (of 84548): max relative diff=0.000021, 80.16 sec so far
Iteration 50324 (of 84548): max relative diff=0.000020, 85.17 sec so far
Iteration 53367 (of 84548): max relative diff=0.000019, 90.18 sec so far
Iteration 56239 (of 84548): max relative diff=0.000018, 95.19 sec so far
Iteration 59126 (of 84548): max relative diff=0.000017, 100.20 sec so far
Iteration 62170 (of 84548): max relative diff=0.000016, 105.21 sec so far
Iteration 65211 (of 84548): max relative diff=0.000015, 110.22 sec so far
Iteration 68185 (of 84548): max relative diff=0.000015, 115.23 sec so far
Iteration 71076 (of 84548): max relative diff=0.000014, 120.24 sec so far
Iteration 74064 (of 84548): max relative diff=0.000014, 125.25 sec so far
Iteration 77106 (of 84548): max relative diff=0.000013, 130.26 sec so far
Iteration 80048 (of 84548): max relative diff=0.000013, 135.27 sec so far
Iteration 82691 (of 84548): max relative diff=0.000012, 140.28 sec so far

Iterative method: 84548 iterations in 144.34 seconds (average 0.001697, setup 0.87)

Value in the initial state: 0.0010445396729789396

Time for model checking: 144.586 seconds.

Result: 0.0010445396729789396


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_cluster.64-2000-20_rep4.log

```
Command(s):
../bin/prism  -importmodel models/cluster.64-2000-20/prism.model.umb models/cluster.64-2000-20/property.props
Wallclock time: 177.819 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:38:12 GMT+01:00 2026
Hostname: n23m0176.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/cluster.64-2000-20/prism.model.umb models/cluster.64-2000-20/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   x
Labels:      "minimum"

Parsing properties file "models/cluster.64-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:symbolic)...
Importing transitions... [ 12% 24% 34% 46% 58% 70% 82% 92% 100% ]

Computing reachable states...

Reachability (BFS): 133 iterations in 0.24 seconds (average 0.001805, setup 0.00)

Time for model construction: 26.27 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 25495 nodes (71 terminal), 733216 minterms, vars: 18r/18c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 36133 of 151060 (23.9%)

Building hybrid MTBDD matrix... [levels=18, nodes=51088] [2.3 MB]
Adding explicit sparse matrices... [levels=6, num=5507, compact] [839.4 KB]
Creating vector for diagonals... [dist=1448, compact] [306.4 KB]
Allocating iteration vectors... [3 x 1.2 MB]
TOTAL: [6.9 MB]

Uniformisation: q.t = 41.057295 x 2000.000000 = 82114.590000
Fox-Glynn: left = 80105, right = 84548

Starting iterations...
Iteration 2887 (of 84548): max relative diff=0.000404, 5.01 sec so far
Iteration 5750 (of 84548): max relative diff=0.000179, 10.02 sec so far
Iteration 8616 (of 84548): max relative diff=0.000118, 15.03 sec so far
Iteration 11470 (of 84548): max relative diff=0.000088, 20.04 sec so far
Iteration 14217 (of 84548): max relative diff=0.000071, 25.05 sec so far
Iteration 17107 (of 84548): max relative diff=0.000059, 30.06 sec so far
Iteration 19981 (of 84548): max relative diff=0.000050, 35.07 sec so far
Iteration 22816 (of 84548): max relative diff=0.000044, 40.08 sec so far
Iteration 25720 (of 84548): max relative diff=0.000039, 45.09 sec so far
Iteration 28557 (of 84548): max relative diff=0.000035, 50.10 sec so far
Iteration 31397 (of 84548): max relative diff=0.000032, 55.11 sec so far
Iteration 34198 (of 84548): max relative diff=0.000029, 60.12 sec so far
Iteration 37100 (of 84548): max relative diff=0.000027, 65.13 sec so far
Iteration 39960 (of 84548): max relative diff=0.000025, 70.14 sec so far
Iteration 42817 (of 84548): max relative diff=0.000023, 75.15 sec so far
Iteration 45625 (of 84548): max relative diff=0.000022, 80.16 sec so far
Iteration 48452 (of 84548): max relative diff=0.000021, 85.17 sec so far
Iteration 51270 (of 84548): max relative diff=0.000020, 90.18 sec so far
Iteration 54127 (of 84548): max relative diff=0.000019, 95.19 sec so far
Iteration 57014 (of 84548): max relative diff=0.000018, 100.20 sec so far
Iteration 59929 (of 84548): max relative diff=0.000017, 105.21 sec so far
Iteration 62806 (of 84548): max relative diff=0.000016, 110.22 sec so far
Iteration 65613 (of 84548): max relative diff=0.000015, 115.23 sec so far
Iteration 68414 (of 84548): max relative diff=0.000015, 120.24 sec so far
Iteration 71287 (of 84548): max relative diff=0.000014, 125.25 sec so far
Iteration 74089 (of 84548): max relative diff=0.000014, 130.26 sec so far
Iteration 76916 (of 84548): max relative diff=0.000013, 135.27 sec so far
Iteration 79720 (of 84548): max relative diff=0.000013, 140.28 sec so far
Iteration 82474 (of 84548): max relative diff=0.000012, 145.29 sec so far

Iterative method: 84548 iterations in 149.83 seconds (average 0.001762, setup 0.83)

Value in the initial state: 0.0010445396729789396

Time for model checking: 150.442 seconds.

Result: 0.0010445396729789396


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_cluster.64-2000-20_rep5.log

```
Command(s):
../bin/prism  -importmodel models/cluster.64-2000-20/prism.model.umb models/cluster.64-2000-20/property.props
Wallclock time: 176.417 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:28:13 GMT+01:00 2026
Hostname: n23m0249.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/cluster.64-2000-20/prism.model.umb models/cluster.64-2000-20/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [startLeft] [repairLeft] [startRight] [repairRight] [startToLeft] [startToRight] [startLine] [repairToLeft] [repairToRight] [repairLine]
Variables:   x
Labels:      "minimum"

Parsing properties file "models/cluster.64-2000-20/property.props"...

1 property:
(1) "qos1": P=? [ F<=2000 !"minimum" ]

---------------------------------------------------------------------

Model checking: "qos1": P=? [ F<=2000 !"minimum" ]

Building model (engine:symbolic)...
Importing transitions... [ 12% 24% 36% 46% 56% 68% 80% 90% 100% ]

Computing reachable states...

Reachability (BFS): 133 iterations in 0.23 seconds (average 0.001729, setup 0.00)

Time for model construction: 26.986 seconds.

Type:        CTMC
States:      151060 (1 initial)
Transitions: 733216

Rate matrix: 25495 nodes (71 terminal), 733216 minterms, vars: 18r/18c

Computing probabilities...
Engine: Hybrid

Number of non-absorbing states: 36133 of 151060 (23.9%)

Building hybrid MTBDD matrix... [levels=18, nodes=51088] [2.3 MB]
Adding explicit sparse matrices... [levels=6, num=5507, compact] [839.4 KB]
Creating vector for diagonals... [dist=1448, compact] [306.4 KB]
Allocating iteration vectors... [3 x 1.2 MB]
TOTAL: [6.9 MB]

Uniformisation: q.t = 41.057295 x 2000.000000 = 82114.590000
Fox-Glynn: left = 80105, right = 84548

Starting iterations...
Iteration 2824 (of 84548): max relative diff=0.000435, 5.01 sec so far
Iteration 5629 (of 84548): max relative diff=0.000183, 10.02 sec so far
Iteration 8469 (of 84548): max relative diff=0.000120, 15.03 sec so far
Iteration 11276 (of 84548): max relative diff=0.000090, 20.04 sec so far
Iteration 14169 (of 84548): max relative diff=0.000071, 25.05 sec so far
Iteration 17040 (of 84548): max relative diff=0.000059, 30.06 sec so far
Iteration 19907 (of 84548): max relative diff=0.000051, 35.07 sec so far
Iteration 22807 (of 84548): max relative diff=0.000044, 40.08 sec so far
Iteration 25704 (of 84548): max relative diff=0.000039, 45.09 sec so far
Iteration 28610 (of 84548): max relative diff=0.000035, 50.10 sec so far
Iteration 31522 (of 84548): max relative diff=0.000032, 55.11 sec so far
Iteration 34434 (of 84548): max relative diff=0.000029, 60.12 sec so far
Iteration 37332 (of 84548): max relative diff=0.000027, 65.13 sec so far
Iteration 40241 (of 84548): max relative diff=0.000025, 70.14 sec so far
Iteration 43123 (of 84548): max relative diff=0.000023, 75.15 sec so far
Iteration 45947 (of 84548): max relative diff=0.000022, 80.16 sec so far
Iteration 48841 (of 84548): max relative diff=0.000021, 85.17 sec so far
Iteration 51734 (of 84548): max relative diff=0.000019, 90.18 sec so far
Iteration 54642 (of 84548): max relative diff=0.000018, 95.19 sec so far
Iteration 57543 (of 84548): max relative diff=0.000017, 100.20 sec so far
Iteration 60446 (of 84548): max relative diff=0.000017, 105.21 sec so far
Iteration 63347 (of 84548): max relative diff=0.000016, 110.22 sec so far
Iteration 66256 (of 84548): max relative diff=0.000015, 115.23 sec so far
Iteration 69162 (of 84548): max relative diff=0.000014, 120.24 sec so far
Iteration 72073 (of 84548): max relative diff=0.000014, 125.25 sec so far
Iteration 74970 (of 84548): max relative diff=0.000013, 130.26 sec so far
Iteration 77879 (of 84548): max relative diff=0.000013, 135.27 sec so far
Iteration 80692 (of 84548): max relative diff=0.000012, 140.28 sec so far
Iteration 83478 (of 84548): max relative diff=0.000012, 145.29 sec so far

Iterative method: 84548 iterations in 148.01 seconds (average 0.001741, setup 0.81)

Value in the initial state: 0.0010445396729789396

Time for model checking: 148.51 seconds.

Result: 0.0010445396729789396


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

