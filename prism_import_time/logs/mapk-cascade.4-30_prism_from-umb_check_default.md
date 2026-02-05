# Log files for prism_from-umb_check_default on model [mapk-cascade.4-30](../../models/mapk-cascade.4-30)

Parsed values: `[171.87, 53.512, 57.812, 39.899, 39.867]`



### Log file: prism_from-umb_check_default_mapk-cascade.4-30_rep1.log

```
Command(s):
../bin/prism  -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props
Wallclock time: 3724.454 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:32:57 GMT+01:00 2026
Hostname: r23m0216.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   x
Labels:      "target"
Rewards:     "time"

Parsing properties file "models/mapk-cascade.4-30/property.props"...

1 property:
(1) "activated_time": R{"time"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "activated_time": R{"time"}=? [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 44 iterations in 8.36 seconds (average 0.190000, setup 0.00)

Time for model construction: 171.87 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 189663 nodes (15 terminal), 910872 minterms, vars: 17r/17c

Diagonals vector: 22061 nodes (128 terminal), 99535 minterms
Embedded Markov chain: 662070 nodes (681 terminal), 910872 minterms

Prob0: 23 iterations in 1.75 seconds (average 0.076087, setup 0.00)

Prob1: 1 iterations in 0.01 seconds (average 0.010000, setup 0.00)

goal = 1461, inf = 0, maybe = 98074

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=17, nodes=655007] [30.0 MB]
Adding explicit sparse matrices... [levels=2, num=47802, compact] [729.0 KB]
Creating vector for diagonals... [dist=1, compact] [194.4 KB]
Creating vector for RHS... [dist=128, compact] [195.4 KB]
Allocating iteration vectors... [2 x 777.6 KB]
TOTAL: [32.6 MB]

Starting iterations...
Iteration 44: max relative diff=0.055526, 5.09 sec so far
Iteration 88: max relative diff=0.024059, 10.15 sec so far
Iteration 132: max relative diff=0.013994, 15.19 sec so far
Iteration 176: max relative diff=0.008929, 20.23 sec so far
Iteration 220: max relative diff=0.006102, 25.26 sec so far
Iteration 264: max relative diff=0.004366, 30.29 sec so far
Iteration 308: max relative diff=0.003221, 35.32 sec so far
Iteration 355: max relative diff=0.002380, 40.33 sec so far
Iteration 399: max relative diff=0.001824, 45.35 sec so far
Iteration 444: max relative diff=0.001408, 50.44 sec so far
Iteration 488: max relative diff=0.001100, 55.51 sec so far
Iteration 532: max relative diff=0.000864, 60.58 sec so far
Iteration 576: max relative diff=0.000682, 65.64 sec so far
Iteration 620: max relative diff=0.000541, 70.65 sec so far
Iteration 664: max relative diff=0.000430, 75.70 sec so far
Iteration 708: max relative diff=0.000342, 80.74 sec so far
Iteration 752: max relative diff=0.000273, 85.79 sec so far
Iteration 796: max relative diff=0.000218, 90.82 sec so far
Iteration 840: max relative diff=0.000175, 95.83 sec so far
Iteration 887: max relative diff=0.000137, 100.88 sec so far
Iteration 932: max relative diff=0.000110, 105.94 sec so far
Iteration 976: max relative diff=0.000088, 110.96 sec so far
Iteration 1020: max relative diff=0.000071, 115.99 sec so far
Iteration 1064: max relative diff=0.000057, 121.04 sec so far
Iteration 1108: max relative diff=0.000045, 126.09 sec so far
Iteration 1152: max relative diff=0.000036, 131.13 sec so far
Iteration 1196: max relative diff=0.000029, 136.18 sec so far
Iteration 1240: max relative diff=0.000024, 141.22 sec so far
Iteration 1284: max relative diff=0.000019, 146.26 sec so far
Iteration 1328: max relative diff=0.000015, 151.30 sec so far
Iteration 1373: max relative diff=0.000012, 156.35 sec so far
Iteration 1420: max relative diff=0.000010, 161.45 sec so far
Iteration 1465: max relative diff=0.000008, 166.51 sec so far
Iteration 1509: max relative diff=0.000006, 171.57 sec so far
Iteration 1553: max relative diff=0.000005, 176.62 sec so far
Iteration 1597: max relative diff=0.000004, 181.66 sec so far
Iteration 1641: max relative diff=0.000003, 186.71 sec so far
Iteration 1685: max relative diff=0.000003, 191.76 sec so far
Iteration 1729: max relative diff=0.000002, 196.80 sec so far
Iteration 1773: max relative diff=0.000002, 201.81 sec so far
Iteration 1817: max relative diff=0.000001, 206.85 sec so far
Iteration 1861: max relative diff=0.000001, 211.89 sec so far

Jacobi: 1875 iterations in 3518.60 seconds (average 0.113840, setup 3305.15)

Value in the initial state: 40.67270371188303

Time for model checking: 3548.748 seconds.

Result: 40.67270371188303 (+/- 4.0451335066928187E-4 estimated; rel err 9.945573167074662E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_mapk-cascade.4-30_rep2.log

```
Command(s):
../bin/prism  -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props
Wallclock time: 1955.197 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:16:52 GMT+01:00 2026
Hostname: n23m0053.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   x
Labels:      "target"
Rewards:     "time"

Parsing properties file "models/mapk-cascade.4-30/property.props"...

1 property:
(1) "activated_time": R{"time"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "activated_time": R{"time"}=? [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 8% 16% 22% 28% 36% 42% 48% 54% 58% 64% 70% 76% 80% 86% 90% 96% 100% ]

Computing reachable states...

Reachability (BFS): 44 iterations in 3.01 seconds (average 0.068409, setup 0.00)

Time for model construction: 53.512 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 189663 nodes (15 terminal), 910872 minterms, vars: 17r/17c

Diagonals vector: 22061 nodes (128 terminal), 99535 minterms
Embedded Markov chain: 662070 nodes (681 terminal), 910872 minterms

Prob0: 23 iterations in 0.61 seconds (average 0.026522, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 1461, inf = 0, maybe = 98074

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=17, nodes=655007] [30.0 MB]
Adding explicit sparse matrices... [levels=2, num=47802, compact] [729.0 KB]
Creating vector for diagonals... [dist=1, compact] [194.4 KB]
Creating vector for RHS... [dist=128, compact] [195.4 KB]
Allocating iteration vectors... [2 x 777.6 KB]
TOTAL: [32.6 MB]

Starting iterations...
Iteration 131: max relative diff=0.014203, 5.02 sec so far
Iteration 263: max relative diff=0.004387, 10.06 sec so far
Iteration 395: max relative diff=0.001868, 15.09 sec so far
Iteration 526: max relative diff=0.000893, 20.10 sec so far
Iteration 657: max relative diff=0.000445, 25.11 sec so far
Iteration 789: max relative diff=0.000226, 30.15 sec so far
Iteration 921: max relative diff=0.000116, 35.19 sec so far
Iteration 1053: max relative diff=0.000060, 40.22 sec so far
Iteration 1184: max relative diff=0.000031, 45.26 sec so far
Iteration 1315: max relative diff=0.000016, 50.28 sec so far
Iteration 1446: max relative diff=0.000008, 55.29 sec so far
Iteration 1577: max relative diff=0.000004, 60.32 sec so far
Iteration 1707: max relative diff=0.000002, 65.33 sec so far
Iteration 1837: max relative diff=0.000001, 70.34 sec so far

Jacobi: 1875 iterations in 1893.87 seconds (average 0.038288, setup 1822.08)

Value in the initial state: 40.67270371188303

Time for model checking: 1900.82 seconds.

Result: 40.67270371188303 (+/- 4.0451335066928187E-4 estimated; rel err 9.945573167074662E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_mapk-cascade.4-30_rep3.log

```
Command(s):
../bin/prism  -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props
Wallclock time: 1415.276 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:10 GMT+01:00 2026
Hostname: r23m0030.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   x
Labels:      "target"
Rewards:     "time"

Parsing properties file "models/mapk-cascade.4-30/property.props"...

1 property:
(1) "activated_time": R{"time"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "activated_time": R{"time"}=? [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 8% 16% 22% 28% 34% 40% 44% 50% 56% 60% 66% 72% 76% 80% 86% 90% 94% 100% ]

Computing reachable states...

Reachability (BFS): 44 iterations in 3.34 seconds (average 0.075909, setup 0.00)

Time for model construction: 57.812 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 189663 nodes (15 terminal), 910872 minterms, vars: 17r/17c

Diagonals vector: 22061 nodes (128 terminal), 99535 minterms
Embedded Markov chain: 662070 nodes (681 terminal), 910872 minterms

Prob0: 23 iterations in 0.65 seconds (average 0.028261, setup 0.00)

Prob1: 1 iterations in 0.01 seconds (average 0.010000, setup 0.00)

goal = 1461, inf = 0, maybe = 98074

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=17, nodes=655007] [30.0 MB]
Adding explicit sparse matrices... [levels=2, num=47802, compact] [729.0 KB]
Creating vector for diagonals... [dist=1, compact] [194.4 KB]
Creating vector for RHS... [dist=128, compact] [195.4 KB]
Allocating iteration vectors... [2 x 777.6 KB]
TOTAL: [32.6 MB]

Starting iterations...
Iteration 127: max relative diff=0.014870, 5.01 sec so far
Iteration 254: max relative diff=0.004696, 10.02 sec so far
Iteration 381: max relative diff=0.002030, 15.03 sec so far
Iteration 509: max relative diff=0.000978, 20.07 sec so far
Iteration 637: max relative diff=0.000494, 25.11 sec so far
Iteration 764: max relative diff=0.000257, 30.13 sec so far
Iteration 891: max relative diff=0.000135, 35.15 sec so far
Iteration 1019: max relative diff=0.000071, 40.19 sec so far
Iteration 1146: max relative diff=0.000038, 45.21 sec so far
Iteration 1273: max relative diff=0.000020, 50.22 sec so far
Iteration 1400: max relative diff=0.000011, 55.23 sec so far
Iteration 1535: max relative diff=0.000005, 60.25 sec so far
Iteration 1684: max relative diff=0.000003, 65.27 sec so far
Iteration 1834: max relative diff=0.000001, 70.31 sec so far

Jacobi: 1875 iterations in 1347.62 seconds (average 0.038235, setup 1275.93)

Value in the initial state: 40.67270371188303

Time for model checking: 1352.371 seconds.

Result: 40.67270371188303 (+/- 4.0451335066928187E-4 estimated; rel err 9.945573167074662E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_mapk-cascade.4-30_rep4.log

```
Command(s):
../bin/prism  -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props
Wallclock time: 810.889 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:52:59 GMT+01:00 2026
Hostname: n23m0277.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   x
Labels:      "target"
Rewards:     "time"

Parsing properties file "models/mapk-cascade.4-30/property.props"...

1 property:
(1) "activated_time": R{"time"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "activated_time": R{"time"}=? [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 10% 20% 28% 36% 46% 54% 62% 70% 78% 84% 90% 98% 100% ]

Computing reachable states...

Reachability (BFS): 44 iterations in 2.60 seconds (average 0.059091, setup 0.00)

Time for model construction: 39.899 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 189663 nodes (15 terminal), 910872 minterms, vars: 17r/17c

Diagonals vector: 22061 nodes (128 terminal), 99535 minterms
Embedded Markov chain: 662070 nodes (681 terminal), 910872 minterms

Prob0: 23 iterations in 0.51 seconds (average 0.022174, setup 0.00)

Prob1: 1 iterations in 0.00 seconds (average 0.000000, setup 0.00)

goal = 1461, inf = 0, maybe = 98074

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=17, nodes=655007] [30.0 MB]
Adding explicit sparse matrices... [levels=2, num=47802, compact] [729.0 KB]
Creating vector for diagonals... [dist=1, compact] [194.4 KB]
Creating vector for RHS... [dist=128, compact] [195.4 KB]
Allocating iteration vectors... [2 x 777.6 KB]
TOTAL: [32.6 MB]

Starting iterations...
Iteration 168: max relative diff=0.009637, 5.01 sec so far
Iteration 337: max relative diff=0.002664, 10.04 sec so far
Iteration 506: max relative diff=0.000996, 15.07 sec so far
Iteration 675: max relative diff=0.000405, 20.10 sec so far
Iteration 844: max relative diff=0.000171, 25.13 sec so far
Iteration 1012: max relative diff=0.000073, 30.15 sec so far
Iteration 1180: max relative diff=0.000032, 35.16 sec so far
Iteration 1349: max relative diff=0.000014, 40.19 sec so far
Iteration 1517: max relative diff=0.000006, 45.20 sec so far
Iteration 1686: max relative diff=0.000003, 50.22 sec so far
Iteration 1855: max relative diff=0.000001, 55.23 sec so far

Jacobi: 1875 iterations in 767.36 seconds (average 0.029776, setup 711.53)

Value in the initial state: 40.67270371188303

Time for model checking: 769.677 seconds.

Result: 40.67270371188303 (+/- 4.0451335066928187E-4 estimated; rel err 9.945573167074662E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_mapk-cascade.4-30_rep5.log

```
Command(s):
../bin/prism  -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props
Wallclock time: 994.634 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 02:51:15 GMT+01:00 2026
Hostname: n23m0031.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [a_kkk_e1] [d_kkk_e1] [k_kkk_e1] [a_kkk_e2] [d_kkk_e2] [k_kkk_e2] [a_k_ptase] [d_k_ptase] [k_k_ptase] [a_kk_ptase] [d_kk_ptase] [k_kk_ptase] [a_k_kk] [d_k_kk] [k_k_kk] [a_kk_kkk] [d_kk_kkk] [k_kk_kkk]
Variables:   x
Labels:      "target"
Rewards:     "time"

Parsing properties file "models/mapk-cascade.4-30/property.props"...

1 property:
(1) "activated_time": R{"time"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "activated_time": R{"time"}=? [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 10% 20% 30% 38% 46% 54% 62% 70% 76% 84% 90% 98% 100% ]

Computing reachable states...

Reachability (BFS): 44 iterations in 2.56 seconds (average 0.058182, setup 0.00)

Time for model construction: 39.867 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 189663 nodes (15 terminal), 910872 minterms, vars: 17r/17c

Diagonals vector: 22061 nodes (128 terminal), 99535 minterms
Embedded Markov chain: 662070 nodes (681 terminal), 910872 minterms

Prob0: 23 iterations in 0.53 seconds (average 0.023043, setup 0.00)

Prob1: 1 iterations in 0.01 seconds (average 0.010000, setup 0.00)

goal = 1461, inf = 0, maybe = 98074

Computing remaining rewards...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=17, nodes=655007] [30.0 MB]
Adding explicit sparse matrices... [levels=2, num=47802, compact] [729.0 KB]
Creating vector for diagonals... [dist=1, compact] [194.4 KB]
Creating vector for RHS... [dist=128, compact] [195.4 KB]
Allocating iteration vectors... [2 x 777.6 KB]
TOTAL: [32.6 MB]

Starting iterations...
Iteration 130: max relative diff=0.014309, 5.03 sec so far
Iteration 260: max relative diff=0.004494, 10.07 sec so far
Iteration 389: max relative diff=0.001935, 15.09 sec so far
Iteration 518: max relative diff=0.000933, 20.11 sec so far
Iteration 647: max relative diff=0.000469, 25.12 sec so far
Iteration 776: max relative diff=0.000242, 30.15 sec so far
Iteration 905: max relative diff=0.000126, 35.16 sec so far
Iteration 1035: max relative diff=0.000065, 40.19 sec so far
Iteration 1164: max relative diff=0.000034, 45.21 sec so far
Iteration 1293: max relative diff=0.000018, 50.22 sec so far
Iteration 1423: max relative diff=0.000009, 55.26 sec so far
Iteration 1553: max relative diff=0.000005, 60.29 sec so far
Iteration 1683: max relative diff=0.000003, 65.33 sec so far
Iteration 1812: max relative diff=0.000001, 70.34 sec so far

Jacobi: 1875 iterations in 948.67 seconds (average 0.038821, setup 875.88)

Value in the initial state: 40.67270371188303

Time for model checking: 953.815 seconds.

Result: 40.67270371188303 (+/- 4.0451335066928187E-4 estimated; rel err 9.945573167074662E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

