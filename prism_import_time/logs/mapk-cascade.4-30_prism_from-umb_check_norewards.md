# Log files

Tool configuration: prism_from-umb_check_norewards
Benchmark: [mapk-cascade.4-30](../../models/mapk-cascade.4-30)
Parsed values: [46.811, 38.396, 83.369, 49.699, 64.138]



### Log file: prism_from-umb_check_norewards_mapk-cascade.4-30_rep1.log

```
Command(s):
../bin/prism  -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props
Wallclock time: 1589.572 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:31:48 GMT+01:00 2026
Hostname: r23m0047.hpc.itc.rwth-aachen.de
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
Importing transitions... [ 8% 18% 26% 34% 40% 46% 54% 60% 66% 72% 78% 84% 90% 96% 100% ]

Computing reachable states...

Reachability (BFS): 44 iterations in 2.82 seconds (average 0.064091, setup 0.00)

Time for model construction: 46.811 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 189663 nodes (15 terminal), 910872 minterms, vars: 17r/17c

Diagonals vector: 22061 nodes (128 terminal), 99535 minterms
Embedded Markov chain: 662070 nodes (681 terminal), 910872 minterms

Prob0: 23 iterations in 0.58 seconds (average 0.025217, setup 0.00)

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
Iteration 132: max relative diff=0.013994, 5.02 sec so far
Iteration 264: max relative diff=0.004366, 10.05 sec so far
Iteration 396: max relative diff=0.001860, 15.07 sec so far
Iteration 528: max relative diff=0.000883, 20.09 sec so far
Iteration 660: max relative diff=0.000439, 25.12 sec so far
Iteration 792: max relative diff=0.000223, 30.14 sec so far
Iteration 925: max relative diff=0.000114, 35.15 sec so far
Iteration 1057: max relative diff=0.000059, 40.19 sec so far
Iteration 1189: max relative diff=0.000030, 45.22 sec so far
Iteration 1320: max relative diff=0.000016, 50.24 sec so far
Iteration 1453: max relative diff=0.000008, 55.27 sec so far
Iteration 1584: max relative diff=0.000004, 60.28 sec so far
Iteration 1715: max relative diff=0.000002, 65.31 sec so far
Iteration 1847: max relative diff=0.000001, 70.35 sec so far

Jacobi: 1875 iterations in 1536.66 seconds (average 0.038085, setup 1465.25)

Value in the initial state: 40.67270371188303

Time for model checking: 1541.632 seconds.

Result: 40.67270371188303 (+/- 4.0451335066928187E-4 estimated; rel err 9.945573167074662E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_mapk-cascade.4-30_rep2.log

```
Command(s):
../bin/prism  -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props
Wallclock time: 1423.563 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:51:58 GMT+01:00 2026
Hostname: n23m0341.hpc.itc.rwth-aachen.de
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
Importing transitions... [ 10% 20% 30% 38% 48% 56% 64% 72% 80% 86% 94% 100% ]

Computing reachable states...

Reachability (BFS): 44 iterations in 2.49 seconds (average 0.056591, setup 0.00)

Time for model construction: 38.396 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 189663 nodes (15 terminal), 910872 minterms, vars: 17r/17c

Diagonals vector: 22061 nodes (128 terminal), 99535 minterms
Embedded Markov chain: 662070 nodes (681 terminal), 910872 minterms

Prob0: 23 iterations in 0.50 seconds (average 0.021739, setup 0.00)

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
Iteration 135: max relative diff=0.013576, 5.01 sec so far
Iteration 271: max relative diff=0.004143, 10.04 sec so far
Iteration 407: max relative diff=0.001740, 15.08 sec so far
Iteration 542: max relative diff=0.000819, 20.09 sec so far
Iteration 678: max relative diff=0.000400, 25.11 sec so far
Iteration 814: max relative diff=0.000199, 30.14 sec so far
Iteration 950: max relative diff=0.000100, 35.17 sec so far
Iteration 1086: max relative diff=0.000051, 40.20 sec so far
Iteration 1222: max relative diff=0.000026, 45.22 sec so far
Iteration 1358: max relative diff=0.000013, 50.25 sec so far
Iteration 1493: max relative diff=0.000007, 55.26 sec so far
Iteration 1629: max relative diff=0.000003, 60.27 sec so far
Iteration 1765: max relative diff=0.000002, 65.29 sec so far

Jacobi: 1875 iterations in 1379.42 seconds (average 0.036992, setup 1310.06)

Value in the initial state: 40.67270371188303

Time for model checking: 1384.269 seconds.

Result: 40.67270371188303 (+/- 4.0451335066928187E-4 estimated; rel err 9.945573167074662E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_mapk-cascade.4-30_rep3.log

```
Command(s):
../bin/prism  -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props
Wallclock time: 1819.393 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:16:21 GMT+01:00 2026
Hostname: n23m0173.hpc.itc.rwth-aachen.de
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
Importing transitions... [ 6% 10% 16% 20% 24% 28% 32% 36% 40% 44% 48% 52% 54% 58% 62% 66% 70% 72% 76% 80% 82% 86% 90% 92% 96% 100% ]

Computing reachable states...

Reachability (BFS): 44 iterations in 4.55 seconds (average 0.103409, setup 0.00)

Time for model construction: 83.369 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 189663 nodes (15 terminal), 910872 minterms, vars: 17r/17c

Diagonals vector: 22061 nodes (128 terminal), 99535 minterms
Embedded Markov chain: 662070 nodes (681 terminal), 910872 minterms

Prob0: 23 iterations in 0.94 seconds (average 0.040870, setup 0.00)

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
Iteration 159: max relative diff=0.010507, 5.03 sec so far
Iteration 318: max relative diff=0.003016, 10.05 sec so far
Iteration 469: max relative diff=0.001220, 15.07 sec so far
Iteration 627: max relative diff=0.000521, 20.09 sec so far
Iteration 785: max relative diff=0.000230, 25.10 sec so far
Iteration 939: max relative diff=0.000106, 30.13 sec so far
Iteration 1094: max relative diff=0.000049, 35.14 sec so far
Iteration 1241: max relative diff=0.000023, 40.17 sec so far
Iteration 1367: max relative diff=0.000012, 45.21 sec so far
Iteration 1493: max relative diff=0.000007, 50.23 sec so far
Iteration 1619: max relative diff=0.000004, 55.25 sec so far
Iteration 1746: max relative diff=0.000002, 60.30 sec so far
Iteration 1872: max relative diff=0.000001, 65.31 sec so far

Jacobi: 1875 iterations in 1726.55 seconds (average 0.034896, setup 1661.12)

Value in the initial state: 40.67270371188303

Time for model checking: 1734.736 seconds.

Result: 40.67270371188303 (+/- 4.0451335066928187E-4 estimated; rel err 9.945573167074662E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_mapk-cascade.4-30_rep4.log

```
Command(s):
../bin/prism  -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props
Wallclock time: 1799.542 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:26:10 GMT+01:00 2026
Hostname: n23m0402.hpc.itc.rwth-aachen.de
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
Importing transitions... [ 8% 16% 24% 30% 38% 44% 50% 56% 62% 68% 74% 80% 86% 92% 98% 100% ]

Computing reachable states...

Reachability (BFS): 44 iterations in 2.82 seconds (average 0.064091, setup 0.00)

Time for model construction: 49.699 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 189663 nodes (15 terminal), 910872 minterms, vars: 17r/17c

Diagonals vector: 22061 nodes (128 terminal), 99535 minterms
Embedded Markov chain: 662070 nodes (681 terminal), 910872 minterms

Prob0: 23 iterations in 0.58 seconds (average 0.025217, setup 0.00)

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
Iteration 124: max relative diff=0.015314, 5.02 sec so far
Iteration 248: max relative diff=0.004911, 10.07 sec so far
Iteration 370: max relative diff=0.002174, 15.09 sec so far
Iteration 492: max relative diff=0.001076, 20.11 sec so far
Iteration 615: max relative diff=0.000554, 25.15 sec so far
Iteration 739: max relative diff=0.000292, 30.18 sec so far
Iteration 863: max relative diff=0.000155, 35.23 sec so far
Iteration 986: max relative diff=0.000084, 40.25 sec so far
Iteration 1109: max relative diff=0.000045, 45.27 sec so far
Iteration 1233: max relative diff=0.000024, 50.30 sec so far
Iteration 1357: max relative diff=0.000013, 55.34 sec so far
Iteration 1481: max relative diff=0.000007, 60.37 sec so far
Iteration 1605: max relative diff=0.000004, 65.40 sec so far
Iteration 1729: max relative diff=0.000002, 70.44 sec so far
Iteration 1852: max relative diff=0.000001, 75.45 sec so far

Jacobi: 1875 iterations in 1740.75 seconds (average 0.040741, setup 1664.36)

Value in the initial state: 40.67270371188303

Time for model checking: 1748.684 seconds.

Result: 40.67270371188303 (+/- 4.0451335066928187E-4 estimated; rel err 9.945573167074662E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_mapk-cascade.4-30_rep5.log

```
Command(s):
../bin/prism  -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props
Wallclock time: 2219.354 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:24:06 GMT+01:00 2026
Hostname: r23m0023.hpc.itc.rwth-aachen.de
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
Importing transitions... [ 8% 16% 22% 28% 34% 40% 46% 50% 56% 60% 66% 70% 76% 80% 86% 90% 94% 100% ]

Computing reachable states...

Reachability (BFS): 44 iterations in 3.25 seconds (average 0.073864, setup 0.00)

Time for model construction: 64.138 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872

Rate matrix: 189663 nodes (15 terminal), 910872 minterms, vars: 17r/17c

Diagonals vector: 22061 nodes (128 terminal), 99535 minterms
Embedded Markov chain: 662070 nodes (681 terminal), 910872 minterms

Prob0: 23 iterations in 0.66 seconds (average 0.028696, setup 0.00)

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
Iteration 126: max relative diff=0.014969, 5.03 sec so far
Iteration 251: max relative diff=0.004790, 10.04 sec so far
Iteration 376: max relative diff=0.002096, 15.08 sec so far
Iteration 501: max relative diff=0.001022, 20.11 sec so far
Iteration 626: max relative diff=0.000524, 25.14 sec so far
Iteration 752: max relative diff=0.000273, 30.18 sec so far
Iteration 878: max relative diff=0.000144, 35.19 sec so far
Iteration 1004: max relative diff=0.000076, 40.23 sec so far
Iteration 1130: max relative diff=0.000041, 45.26 sec so far
Iteration 1256: max relative diff=0.000022, 50.28 sec so far
Iteration 1381: max relative diff=0.000012, 55.30 sec so far
Iteration 1506: max relative diff=0.000006, 60.32 sec so far
Iteration 1631: max relative diff=0.000003, 65.33 sec so far
Iteration 1757: max relative diff=0.000002, 70.37 sec so far

Jacobi: 1875 iterations in 2141.83 seconds (average 0.040037, setup 2066.76)

Value in the initial state: 40.67270371188303

Time for model checking: 2154.181 seconds.

Result: 40.67270371188303 (+/- 4.0451335066928187E-4 estimated; rel err 9.945573167074662E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

