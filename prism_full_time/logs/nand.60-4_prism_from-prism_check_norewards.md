# Log files

Tool configuration: prism_from-prism_check_norewards
Benchmark: [nand.60-4](../../models/nand.60-4)
Parsed values: [303.98, 292.507, 331.193, 302.674, 336.732]



### Log file: prism_from-prism_check_norewards_nand.60-4_rep1.log

```
Command(s):
../bin/prism  models/nand.60-4/model.prism models/nand.60-4/property.props
Wallclock time: 303.980 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:29:42 GMT+01:00 2026
Hostname: r23m0062.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.60-4/model.prism models/nand.60-4/property.props

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Parsing properties file "models/nand.60-4/property.props"...

1 property:
(1) "reliable": P=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "reliable": P=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2162 iterations in 7.81 seconds (average 0.003612, setup 0.00)

Time for model construction: 8.059 seconds.

Type:        DTMC
States:      18826082 (1 initial)
Transitions: 29772212

Transition matrix: 97452 nodes (1103 terminal), 29772212 minterms, vars: 33r/33c

Prob0: 2162 iterations in 6.50 seconds (average 0.003006, setup 0.00)

Prob1: 1945 iterations in 6.09 seconds (average 0.003131, setup 0.00)

yes = 547, no = 1757695, maybe = 17067840

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=33, nodes=136740] [6.3 MB]
Adding explicit sparse matrices... [levels=14, num=365, compact] [769.2 KB]
Creating vector for diagonals... [dist=1, compact] [35.9 MB]
Creating vector for RHS... [dist=2, compact] [35.9 MB]
Allocating iteration vectors... [2 x 143.6 MB]
TOTAL: [366.1 MB]

Starting iterations...
Iteration 40: max relative diff=inf, 5.13 sec so far
Iteration 80: max relative diff=inf, 10.22 sec so far
Iteration 120: max relative diff=inf, 15.28 sec so far
Iteration 160: max relative diff=inf, 20.34 sec so far
Iteration 200: max relative diff=inf, 25.45 sec so far
Iteration 240: max relative diff=inf, 30.49 sec so far
Iteration 280: max relative diff=inf, 35.62 sec so far
Iteration 320: max relative diff=inf, 40.69 sec so far
Iteration 360: max relative diff=inf, 45.80 sec so far
Iteration 400: max relative diff=inf, 50.94 sec so far
Iteration 440: max relative diff=inf, 56.06 sec so far
Iteration 480: max relative diff=inf, 61.16 sec so far
Iteration 520: max relative diff=inf, 66.24 sec so far
Iteration 560: max relative diff=inf, 71.33 sec so far
Iteration 600: max relative diff=inf, 76.43 sec so far
Iteration 640: max relative diff=inf, 81.50 sec so far
Iteration 680: max relative diff=inf, 86.59 sec so far
Iteration 720: max relative diff=inf, 91.68 sec so far
Iteration 760: max relative diff=inf, 96.79 sec so far
Iteration 800: max relative diff=inf, 101.89 sec so far
Iteration 840: max relative diff=inf, 106.97 sec so far
Iteration 879: max relative diff=inf, 112.01 sec so far
Iteration 919: max relative diff=inf, 117.10 sec so far
Iteration 959: max relative diff=inf, 122.19 sec so far
Iteration 999: max relative diff=inf, 127.31 sec so far
Iteration 1039: max relative diff=inf, 132.40 sec so far
Iteration 1079: max relative diff=inf, 137.50 sec so far
Iteration 1119: max relative diff=inf, 142.57 sec so far
Iteration 1159: max relative diff=inf, 147.66 sec so far
Iteration 1199: max relative diff=inf, 152.74 sec so far
Iteration 1239: max relative diff=inf, 157.84 sec so far
Iteration 1279: max relative diff=inf, 162.92 sec so far
Iteration 1319: max relative diff=inf, 168.02 sec so far
Iteration 1358: max relative diff=inf, 173.10 sec so far
Iteration 1398: max relative diff=inf, 178.17 sec so far
Iteration 1438: max relative diff=inf, 183.28 sec so far
Iteration 1478: max relative diff=inf, 188.38 sec so far
Iteration 1518: max relative diff=inf, 193.45 sec so far
Iteration 1558: max relative diff=inf, 198.54 sec so far
Iteration 1598: max relative diff=inf, 203.65 sec so far
Iteration 1638: max relative diff=inf, 208.71 sec so far
Iteration 1678: max relative diff=inf, 213.80 sec so far
Iteration 1718: max relative diff=inf, 218.89 sec so far
Iteration 1758: max relative diff=inf, 223.96 sec so far
Iteration 1798: max relative diff=inf, 229.03 sec so far
Iteration 1837: max relative diff=inf, 234.12 sec so far
Iteration 1877: max relative diff=inf, 239.23 sec so far
Iteration 1917: max relative diff=inf, 244.32 sec so far
Iteration 1957: max relative diff=inf, 249.40 sec so far
Iteration 1997: max relative diff=inf, 254.47 sec so far
Iteration 2037: max relative diff=inf, 259.54 sec so far
Iteration 2077: max relative diff=inf, 264.64 sec so far
Iteration 2117: max relative diff=inf, 269.75 sec so far
Iteration 2157: max relative diff=0.004582, 274.87 sec so far

Jacobi: 2161 iterations in 281.72 seconds (average 0.127427, setup 6.35)

Value in the initial state: 0.6867214589192238

Time for model checking: 295.312 seconds.

Result: 0.6867214589192238 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_nand.60-4_rep2.log

```
Command(s):
../bin/prism  models/nand.60-4/model.prism models/nand.60-4/property.props
Wallclock time: 292.507 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:06:37 GMT+01:00 2026
Hostname: n23m0061.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.60-4/model.prism models/nand.60-4/property.props

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Parsing properties file "models/nand.60-4/property.props"...

1 property:
(1) "reliable": P=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "reliable": P=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2162 iterations in 7.45 seconds (average 0.003446, setup 0.00)

Time for model construction: 7.683 seconds.

Type:        DTMC
States:      18826082 (1 initial)
Transitions: 29772212

Transition matrix: 97452 nodes (1103 terminal), 29772212 minterms, vars: 33r/33c

Prob0: 2162 iterations in 6.34 seconds (average 0.002932, setup 0.00)

Prob1: 1945 iterations in 5.80 seconds (average 0.002982, setup 0.00)

yes = 547, no = 1757695, maybe = 17067840

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=33, nodes=136740] [6.3 MB]
Adding explicit sparse matrices... [levels=14, num=365, compact] [769.2 KB]
Creating vector for diagonals... [dist=1, compact] [35.9 MB]
Creating vector for RHS... [dist=2, compact] [35.9 MB]
Allocating iteration vectors... [2 x 143.6 MB]
TOTAL: [366.1 MB]

Starting iterations...
Iteration 41: max relative diff=inf, 5.06 sec so far
Iteration 82: max relative diff=inf, 10.09 sec so far
Iteration 123: max relative diff=inf, 15.12 sec so far
Iteration 164: max relative diff=inf, 20.14 sec so far
Iteration 205: max relative diff=inf, 25.15 sec so far
Iteration 246: max relative diff=inf, 30.17 sec so far
Iteration 287: max relative diff=inf, 35.19 sec so far
Iteration 328: max relative diff=inf, 40.21 sec so far
Iteration 369: max relative diff=inf, 45.23 sec so far
Iteration 410: max relative diff=inf, 50.25 sec so far
Iteration 451: max relative diff=inf, 55.27 sec so far
Iteration 491: max relative diff=inf, 60.28 sec so far
Iteration 532: max relative diff=inf, 65.32 sec so far
Iteration 573: max relative diff=inf, 70.35 sec so far
Iteration 614: max relative diff=inf, 75.38 sec so far
Iteration 655: max relative diff=inf, 80.40 sec so far
Iteration 696: max relative diff=inf, 85.42 sec so far
Iteration 737: max relative diff=inf, 90.45 sec so far
Iteration 778: max relative diff=inf, 95.47 sec so far
Iteration 819: max relative diff=inf, 100.49 sec so far
Iteration 860: max relative diff=inf, 105.51 sec so far
Iteration 901: max relative diff=inf, 110.53 sec so far
Iteration 943: max relative diff=inf, 115.66 sec so far
Iteration 984: max relative diff=inf, 120.77 sec so far
Iteration 1025: max relative diff=inf, 125.82 sec so far
Iteration 1066: max relative diff=inf, 130.83 sec so far
Iteration 1107: max relative diff=inf, 135.87 sec so far
Iteration 1148: max relative diff=inf, 140.89 sec so far
Iteration 1189: max relative diff=inf, 145.90 sec so far
Iteration 1230: max relative diff=inf, 150.93 sec so far
Iteration 1271: max relative diff=inf, 155.94 sec so far
Iteration 1312: max relative diff=inf, 160.95 sec so far
Iteration 1353: max relative diff=inf, 165.98 sec so far
Iteration 1394: max relative diff=inf, 171.00 sec so far
Iteration 1435: max relative diff=inf, 176.06 sec so far
Iteration 1476: max relative diff=inf, 181.14 sec so far
Iteration 1517: max relative diff=inf, 186.19 sec so far
Iteration 1558: max relative diff=inf, 191.21 sec so far
Iteration 1599: max relative diff=inf, 196.25 sec so far
Iteration 1640: max relative diff=inf, 201.28 sec so far
Iteration 1681: max relative diff=inf, 206.29 sec so far
Iteration 1722: max relative diff=inf, 211.31 sec so far
Iteration 1763: max relative diff=inf, 216.33 sec so far
Iteration 1804: max relative diff=inf, 221.34 sec so far
Iteration 1845: max relative diff=inf, 226.36 sec so far
Iteration 1886: max relative diff=inf, 231.37 sec so far
Iteration 1927: max relative diff=inf, 236.47 sec so far
Iteration 1968: max relative diff=inf, 241.50 sec so far
Iteration 2009: max relative diff=inf, 246.55 sec so far
Iteration 2050: max relative diff=inf, 251.56 sec so far
Iteration 2091: max relative diff=inf, 256.58 sec so far
Iteration 2132: max relative diff=inf, 261.59 sec so far

Jacobi: 2161 iterations in 271.11 seconds (average 0.122689, setup 5.98)

Value in the initial state: 0.6867214589192238

Time for model checking: 284.246 seconds.

Result: 0.6867214589192238 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_nand.60-4_rep3.log

```
Command(s):
../bin/prism  models/nand.60-4/model.prism models/nand.60-4/property.props
Wallclock time: 331.193 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:09 GMT+01:00 2026
Hostname: r23m0177.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.60-4/model.prism models/nand.60-4/property.props

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Parsing properties file "models/nand.60-4/property.props"...

1 property:
(1) "reliable": P=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "reliable": P=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2162 iterations in 8.53 seconds (average 0.003945, setup 0.00)

Time for model construction: 8.822 seconds.

Type:        DTMC
States:      18826082 (1 initial)
Transitions: 29772212

Transition matrix: 97452 nodes (1103 terminal), 29772212 minterms, vars: 33r/33c

Prob0: 2162 iterations in 7.25 seconds (average 0.003353, setup 0.00)

Prob1: 1945 iterations in 6.68 seconds (average 0.003434, setup 0.00)

yes = 547, no = 1757695, maybe = 17067840

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=33, nodes=136740] [6.3 MB]
Adding explicit sparse matrices... [levels=14, num=365, compact] [769.2 KB]
Creating vector for diagonals... [dist=1, compact] [35.9 MB]
Creating vector for RHS... [dist=2, compact] [35.9 MB]
Allocating iteration vectors... [2 x 143.6 MB]
TOTAL: [366.1 MB]

Starting iterations...
Iteration 36: max relative diff=inf, 5.01 sec so far
Iteration 73: max relative diff=inf, 10.13 sec so far
Iteration 109: max relative diff=inf, 15.15 sec so far
Iteration 146: max relative diff=inf, 20.26 sec so far
Iteration 182: max relative diff=inf, 25.29 sec so far
Iteration 219: max relative diff=inf, 30.43 sec so far
Iteration 256: max relative diff=inf, 35.54 sec so far
Iteration 293: max relative diff=inf, 40.65 sec so far
Iteration 330: max relative diff=inf, 45.78 sec so far
Iteration 367: max relative diff=inf, 50.91 sec so far
Iteration 404: max relative diff=inf, 56.02 sec so far
Iteration 441: max relative diff=inf, 61.15 sec so far
Iteration 478: max relative diff=inf, 66.29 sec so far
Iteration 515: max relative diff=inf, 71.43 sec so far
Iteration 552: max relative diff=inf, 76.57 sec so far
Iteration 589: max relative diff=inf, 81.71 sec so far
Iteration 626: max relative diff=inf, 86.81 sec so far
Iteration 662: max relative diff=inf, 91.82 sec so far
Iteration 699: max relative diff=inf, 96.94 sec so far
Iteration 737: max relative diff=inf, 102.04 sec so far
Iteration 774: max relative diff=inf, 107.06 sec so far
Iteration 812: max relative diff=inf, 112.18 sec so far
Iteration 850: max relative diff=inf, 117.29 sec so far
Iteration 888: max relative diff=inf, 122.41 sec so far
Iteration 926: max relative diff=inf, 127.54 sec so far
Iteration 964: max relative diff=inf, 132.67 sec so far
Iteration 1001: max relative diff=inf, 137.69 sec so far
Iteration 1037: max relative diff=inf, 142.70 sec so far
Iteration 1074: max relative diff=inf, 147.84 sec so far
Iteration 1110: max relative diff=inf, 152.85 sec so far
Iteration 1147: max relative diff=inf, 157.98 sec so far
Iteration 1183: max relative diff=inf, 162.99 sec so far
Iteration 1220: max relative diff=inf, 168.11 sec so far
Iteration 1257: max relative diff=inf, 173.25 sec so far
Iteration 1294: max relative diff=inf, 178.37 sec so far
Iteration 1330: max relative diff=inf, 183.38 sec so far
Iteration 1367: max relative diff=inf, 188.51 sec so far
Iteration 1404: max relative diff=inf, 193.63 sec so far
Iteration 1441: max relative diff=inf, 198.76 sec so far
Iteration 1477: max relative diff=inf, 203.77 sec so far
Iteration 1513: max relative diff=inf, 208.78 sec so far
Iteration 1550: max relative diff=inf, 213.90 sec so far
Iteration 1587: max relative diff=inf, 219.03 sec so far
Iteration 1624: max relative diff=inf, 224.15 sec so far
Iteration 1661: max relative diff=inf, 229.26 sec so far
Iteration 1698: max relative diff=inf, 234.38 sec so far
Iteration 1735: max relative diff=inf, 239.50 sec so far
Iteration 1772: max relative diff=inf, 244.61 sec so far
Iteration 1809: max relative diff=inf, 249.73 sec so far
Iteration 1846: max relative diff=inf, 254.84 sec so far
Iteration 1883: max relative diff=inf, 259.96 sec so far
Iteration 1919: max relative diff=inf, 265.00 sec so far
Iteration 1955: max relative diff=inf, 270.02 sec so far
Iteration 1991: max relative diff=inf, 275.03 sec so far
Iteration 2028: max relative diff=inf, 280.15 sec so far
Iteration 2065: max relative diff=inf, 285.28 sec so far
Iteration 2102: max relative diff=inf, 290.39 sec so far
Iteration 2139: max relative diff=inf, 295.53 sec so far

Jacobi: 2161 iterations in 305.33 seconds (average 0.138172, setup 6.74)

Value in the initial state: 0.6867214589192238

Time for model checking: 320.532 seconds.

Result: 0.6867214589192238 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_nand.60-4_rep4.log

```
Command(s):
../bin/prism  models/nand.60-4/model.prism models/nand.60-4/property.props
Wallclock time: 302.674 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:09:40 GMT+01:00 2026
Hostname: n23m0237.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.60-4/model.prism models/nand.60-4/property.props

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Parsing properties file "models/nand.60-4/property.props"...

1 property:
(1) "reliable": P=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "reliable": P=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2162 iterations in 7.31 seconds (average 0.003381, setup 0.00)

Time for model construction: 7.56 seconds.

Type:        DTMC
States:      18826082 (1 initial)
Transitions: 29772212

Transition matrix: 97452 nodes (1103 terminal), 29772212 minterms, vars: 33r/33c

Prob0: 2162 iterations in 6.27 seconds (average 0.002900, setup 0.00)

Prob1: 1945 iterations in 5.72 seconds (average 0.002941, setup 0.00)

yes = 547, no = 1757695, maybe = 17067840

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=33, nodes=136740] [6.3 MB]
Adding explicit sparse matrices... [levels=14, num=365, compact] [769.2 KB]
Creating vector for diagonals... [dist=1, compact] [35.9 MB]
Creating vector for RHS... [dist=2, compact] [35.9 MB]
Allocating iteration vectors... [2 x 143.6 MB]
TOTAL: [366.1 MB]

Starting iterations...
Iteration 40: max relative diff=inf, 5.11 sec so far
Iteration 80: max relative diff=inf, 10.20 sec so far
Iteration 120: max relative diff=inf, 15.28 sec so far
Iteration 160: max relative diff=inf, 20.36 sec so far
Iteration 200: max relative diff=inf, 25.44 sec so far
Iteration 240: max relative diff=inf, 30.52 sec so far
Iteration 280: max relative diff=inf, 35.60 sec so far
Iteration 320: max relative diff=inf, 40.68 sec so far
Iteration 360: max relative diff=inf, 45.76 sec so far
Iteration 400: max relative diff=inf, 50.84 sec so far
Iteration 439: max relative diff=inf, 55.88 sec so far
Iteration 479: max relative diff=inf, 60.98 sec so far
Iteration 519: max relative diff=inf, 66.09 sec so far
Iteration 559: max relative diff=inf, 71.17 sec so far
Iteration 599: max relative diff=inf, 76.25 sec so far
Iteration 639: max relative diff=inf, 81.32 sec so far
Iteration 679: max relative diff=inf, 86.40 sec so far
Iteration 719: max relative diff=inf, 91.48 sec so far
Iteration 759: max relative diff=inf, 96.57 sec so far
Iteration 799: max relative diff=inf, 101.65 sec so far
Iteration 839: max relative diff=inf, 106.73 sec so far
Iteration 879: max relative diff=inf, 111.81 sec so far
Iteration 918: max relative diff=inf, 116.84 sec so far
Iteration 958: max relative diff=inf, 121.94 sec so far
Iteration 998: max relative diff=inf, 127.04 sec so far
Iteration 1038: max relative diff=inf, 132.12 sec so far
Iteration 1078: max relative diff=inf, 137.20 sec so far
Iteration 1118: max relative diff=inf, 142.28 sec so far
Iteration 1158: max relative diff=inf, 147.36 sec so far
Iteration 1198: max relative diff=inf, 152.44 sec so far
Iteration 1238: max relative diff=inf, 157.52 sec so far
Iteration 1278: max relative diff=inf, 162.61 sec so far
Iteration 1318: max relative diff=inf, 167.69 sec so far
Iteration 1358: max relative diff=inf, 172.77 sec so far
Iteration 1397: max relative diff=inf, 177.80 sec so far
Iteration 1437: max relative diff=inf, 182.90 sec so far
Iteration 1477: max relative diff=inf, 187.99 sec so far
Iteration 1517: max relative diff=inf, 193.07 sec so far
Iteration 1557: max relative diff=inf, 198.16 sec so far
Iteration 1597: max relative diff=inf, 203.24 sec so far
Iteration 1637: max relative diff=inf, 208.32 sec so far
Iteration 1677: max relative diff=inf, 213.40 sec so far
Iteration 1717: max relative diff=inf, 218.48 sec so far
Iteration 1757: max relative diff=inf, 223.56 sec so far
Iteration 1797: max relative diff=inf, 228.64 sec so far
Iteration 1837: max relative diff=inf, 233.76 sec so far
Iteration 1877: max relative diff=inf, 238.88 sec so far
Iteration 1917: max relative diff=inf, 243.99 sec so far
Iteration 1957: max relative diff=inf, 249.08 sec so far
Iteration 1997: max relative diff=inf, 254.16 sec so far
Iteration 2037: max relative diff=inf, 259.24 sec so far
Iteration 2077: max relative diff=inf, 264.32 sec so far
Iteration 2117: max relative diff=inf, 269.40 sec so far
Iteration 2157: max relative diff=0.004582, 274.48 sec so far

Jacobi: 2161 iterations in 281.49 seconds (average 0.127251, setup 6.50)

Value in the initial state: 0.6867214589192238

Time for model checking: 294.454 seconds.

Result: 0.6867214589192238 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_nand.60-4_rep5.log

```
Command(s):
../bin/prism  models/nand.60-4/model.prism models/nand.60-4/property.props
Wallclock time: 336.732 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:29:13 GMT+01:00 2026
Hostname: r23m0214.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.60-4/model.prism models/nand.60-4/property.props

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Parsing properties file "models/nand.60-4/property.props"...

1 property:
(1) "reliable": P=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "reliable": P=? [ F "target" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2162 iterations in 10.18 seconds (average 0.004709, setup 0.00)

Time for model construction: 10.478 seconds.

Type:        DTMC
States:      18826082 (1 initial)
Transitions: 29772212

Transition matrix: 97452 nodes (1103 terminal), 29772212 minterms, vars: 33r/33c

Prob0: 2162 iterations in 8.63 seconds (average 0.003992, setup 0.00)

Prob1: 1945 iterations in 7.05 seconds (average 0.003625, setup 0.00)

yes = 547, no = 1757695, maybe = 17067840

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=33, nodes=136740] [6.3 MB]
Adding explicit sparse matrices... [levels=14, num=365, compact] [769.2 KB]
Creating vector for diagonals... [dist=1, compact] [35.9 MB]
Creating vector for RHS... [dist=2, compact] [35.9 MB]
Allocating iteration vectors... [2 x 143.6 MB]
TOTAL: [366.1 MB]

Starting iterations...
Iteration 38: max relative diff=inf, 5.04 sec so far
Iteration 76: max relative diff=inf, 10.09 sec so far
Iteration 110: max relative diff=inf, 15.15 sec so far
Iteration 147: max relative diff=inf, 20.19 sec so far
Iteration 185: max relative diff=inf, 25.21 sec so far
Iteration 224: max relative diff=inf, 30.29 sec so far
Iteration 261: max relative diff=inf, 35.33 sec so far
Iteration 290: max relative diff=inf, 40.51 sec so far
Iteration 318: max relative diff=inf, 45.53 sec so far
Iteration 355: max relative diff=inf, 50.61 sec so far
Iteration 390: max relative diff=inf, 55.68 sec so far
Iteration 428: max relative diff=inf, 60.71 sec so far
Iteration 467: max relative diff=inf, 65.80 sec so far
Iteration 505: max relative diff=inf, 70.94 sec so far
Iteration 539: max relative diff=inf, 76.00 sec so far
Iteration 578: max relative diff=inf, 81.10 sec so far
Iteration 616: max relative diff=inf, 86.14 sec so far
Iteration 651: max relative diff=inf, 91.20 sec so far
Iteration 687: max relative diff=inf, 96.21 sec so far
Iteration 726: max relative diff=inf, 101.33 sec so far
Iteration 762: max relative diff=inf, 106.41 sec so far
Iteration 797: max relative diff=inf, 111.42 sec so far
Iteration 835: max relative diff=inf, 116.45 sec so far
Iteration 872: max relative diff=inf, 121.52 sec so far
Iteration 906: max relative diff=inf, 126.60 sec so far
Iteration 944: max relative diff=inf, 131.62 sec so far
Iteration 982: max relative diff=inf, 136.69 sec so far
Iteration 1015: max relative diff=inf, 141.83 sec so far
Iteration 1054: max relative diff=inf, 146.94 sec so far
Iteration 1093: max relative diff=inf, 152.05 sec so far
Iteration 1125: max relative diff=inf, 157.10 sec so far
Iteration 1164: max relative diff=inf, 162.23 sec so far
Iteration 1202: max relative diff=inf, 167.31 sec so far
Iteration 1234: max relative diff=inf, 172.32 sec so far
Iteration 1273: max relative diff=inf, 177.44 sec so far
Iteration 1311: max relative diff=inf, 182.57 sec so far
Iteration 1344: max relative diff=inf, 187.59 sec so far
Iteration 1382: max relative diff=inf, 192.63 sec so far
Iteration 1419: max relative diff=inf, 197.74 sec so far
Iteration 1453: max relative diff=inf, 202.85 sec so far
Iteration 1492: max relative diff=inf, 207.95 sec so far
Iteration 1527: max relative diff=inf, 212.96 sec so far
Iteration 1563: max relative diff=inf, 218.09 sec so far
Iteration 1601: max relative diff=inf, 223.16 sec so far
Iteration 1635: max relative diff=inf, 228.21 sec so far
Iteration 1672: max relative diff=inf, 233.23 sec so far
Iteration 1710: max relative diff=inf, 238.37 sec so far
Iteration 1744: max relative diff=inf, 243.49 sec so far
Iteration 1782: max relative diff=inf, 248.51 sec so far
Iteration 1818: max relative diff=inf, 253.66 sec so far
Iteration 1854: max relative diff=inf, 258.79 sec so far
Iteration 1892: max relative diff=inf, 263.83 sec so far
Iteration 1926: max relative diff=inf, 268.95 sec so far
Iteration 1964: max relative diff=inf, 274.05 sec so far
Iteration 2000: max relative diff=inf, 279.09 sec so far
Iteration 2035: max relative diff=inf, 284.20 sec so far
Iteration 2073: max relative diff=inf, 289.31 sec so far
Iteration 2106: max relative diff=inf, 294.34 sec so far
Iteration 2143: max relative diff=2.464689, 299.37 sec so far

Jacobi: 2161 iterations in 308.32 seconds (average 0.139662, setup 6.51)

Value in the initial state: 0.6867214589192238

Time for model checking: 325.426 seconds.

Result: 0.6867214589192238 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

