# Log files for prism_from-prism_check_norewards on model [kanban.5](../../models/kanban.5)

Parsed values: `[0.126, 0.169, 0.131, 0.179, 0.128]`



### Log file: prism_from-prism_check_norewards_kanban.5_rep1.log

```
Command(s):
../bin/prism  models/kanban.5/model.prism models/kanban.5/property.props
Wallclock time: 467.277 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:55:10 GMT+01:00 2026
Hostname: n23m0200.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/kanban.5/model.prism models/kanban.5/property.props

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Parsing properties file "models/kanban.5/property.props"...

1 property:
(1) "throughput": R{"throughput"}=? [ S ]

---------------------------------------------------------------------

Model checking: "throughput": R{"throughput"}=? [ S ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 71 iterations in 0.10 seconds (average 0.001408, setup 0.00)

Time for model construction: 0.126 seconds.

Type:        CTMC
States:      2546432 (1 initial)
Transitions: 24460016

Rate matrix: 6308 nodes (14 terminal), 24460016 minterms, vars: 48r/48c

SCCs: 1, BSCCs: 1, non-BSCC states: 0
BSCC sizes: 1:2546432

Computing steady state probabilities for BSCC 1

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=48, nodes=6308] [295.7 KB]
Adding explicit sparse matrices... [levels=27, num=165, compact] [749.6 KB]
Creating vector for diagonals... [dist=187, compact] [4.9 MB]
Allocating iteration vectors... [2 x 19.4 MB]
TOTAL: [44.7 MB]

Starting iterations...
Iteration 106: max relative diff=0.017894, 5.05 sec so far
Iteration 212: max relative diff=0.001594, 10.08 sec so far
Iteration 318: max relative diff=0.000239, 15.10 sec so far
Iteration 424: max relative diff=0.000052, 20.14 sec so far
Iteration 530: max relative diff=0.000027, 25.17 sec so far
Iteration 636: max relative diff=0.000024, 30.20 sec so far
Iteration 742: max relative diff=0.000023, 35.23 sec so far
Iteration 848: max relative diff=0.000023, 40.27 sec so far
Iteration 953: max relative diff=0.000023, 45.29 sec so far
Iteration 1059: max relative diff=0.000023, 50.33 sec so far
Iteration 1165: max relative diff=0.000023, 55.34 sec so far
Iteration 1270: max relative diff=0.000023, 60.35 sec so far
Iteration 1378: max relative diff=0.000023, 65.38 sec so far
Iteration 1486: max relative diff=0.000023, 70.39 sec so far
Iteration 1594: max relative diff=0.000023, 75.40 sec so far
Iteration 1702: max relative diff=0.000023, 80.42 sec so far
Iteration 1811: max relative diff=0.000023, 85.47 sec so far
Iteration 1920: max relative diff=0.000023, 90.51 sec so far
Iteration 2029: max relative diff=0.000023, 95.55 sec so far
Iteration 2138: max relative diff=0.000023, 100.59 sec so far
Iteration 2247: max relative diff=0.000023, 105.63 sec so far
Iteration 2354: max relative diff=0.000023, 110.65 sec so far
Iteration 2462: max relative diff=0.000023, 115.70 sec so far
Iteration 2570: max relative diff=0.000023, 120.72 sec so far
Iteration 2679: max relative diff=0.000023, 125.76 sec so far
Iteration 2788: max relative diff=0.000023, 130.78 sec so far
Iteration 2896: max relative diff=0.000023, 135.80 sec so far
Iteration 3005: max relative diff=0.000023, 140.81 sec so far
Iteration 3115: max relative diff=0.000023, 145.86 sec so far
Iteration 3224: max relative diff=0.000023, 150.87 sec so far
Iteration 3332: max relative diff=0.000023, 155.88 sec so far
Iteration 3441: max relative diff=0.000023, 160.90 sec so far
Iteration 3550: max relative diff=0.000023, 165.91 sec so far
Iteration 3658: max relative diff=0.000023, 170.95 sec so far
Iteration 3765: max relative diff=0.000023, 175.96 sec so far
Iteration 3874: max relative diff=0.000023, 181.01 sec so far
Iteration 3983: max relative diff=0.000023, 186.03 sec so far
Iteration 4092: max relative diff=0.000023, 191.06 sec so far
Iteration 4200: max relative diff=0.000023, 196.07 sec so far
Iteration 4309: max relative diff=0.000023, 201.09 sec so far
Iteration 4418: max relative diff=0.000023, 206.10 sec so far
Iteration 4527: max relative diff=0.000023, 211.14 sec so far
Iteration 4635: max relative diff=0.000023, 216.17 sec so far
Iteration 4744: max relative diff=0.000023, 221.19 sec so far
Iteration 4854: max relative diff=0.000023, 226.24 sec so far
Iteration 4962: max relative diff=0.000023, 231.27 sec so far
Iteration 5071: max relative diff=0.000023, 236.28 sec so far
Iteration 5177: max relative diff=0.000023, 241.32 sec so far
Iteration 5283: max relative diff=0.000023, 246.33 sec so far
Iteration 5389: max relative diff=0.000023, 251.34 sec so far
Iteration 5497: max relative diff=0.000023, 256.36 sec so far
Iteration 5608: max relative diff=0.000023, 261.41 sec so far
Iteration 5719: max relative diff=0.000023, 266.45 sec so far
Iteration 5830: max relative diff=0.000023, 271.46 sec so far
Iteration 5940: max relative diff=0.000023, 276.50 sec so far
Iteration 6048: max relative diff=0.000023, 281.55 sec so far
Iteration 6158: max relative diff=0.000023, 286.59 sec so far
Iteration 6265: max relative diff=0.000023, 291.60 sec so far
Iteration 6374: max relative diff=0.000023, 296.63 sec so far
Iteration 6481: max relative diff=0.000023, 301.64 sec so far
Iteration 6590: max relative diff=0.000023, 306.65 sec so far
Iteration 6699: max relative diff=0.000023, 311.66 sec so far
Iteration 6808: max relative diff=0.000023, 316.67 sec so far
Iteration 6917: max relative diff=0.000023, 321.72 sec so far
Iteration 7026: max relative diff=0.000023, 326.75 sec so far
Iteration 7135: max relative diff=0.000023, 331.77 sec so far
Iteration 7244: max relative diff=0.000023, 336.78 sec so far
Iteration 7353: max relative diff=0.000023, 341.82 sec so far
Iteration 7461: max relative diff=0.000023, 346.83 sec so far
Iteration 7568: max relative diff=0.000023, 351.85 sec so far
Iteration 7677: max relative diff=0.000023, 356.90 sec so far
Iteration 7786: max relative diff=0.000023, 361.93 sec so far
Iteration 7894: max relative diff=0.000023, 366.96 sec so far
Iteration 8003: max relative diff=0.000023, 372.00 sec so far
Iteration 8112: max relative diff=0.000023, 377.04 sec so far
Iteration 8221: max relative diff=0.000023, 382.05 sec so far
Iteration 8329: max relative diff=0.000023, 387.10 sec so far
Iteration 8438: max relative diff=0.000023, 392.11 sec so far
Iteration 8547: max relative diff=0.000023, 397.12 sec so far
Iteration 8656: max relative diff=0.000023, 402.13 sec so far
Iteration 8764: max relative diff=0.000023, 407.16 sec so far
Iteration 8871: max relative diff=0.000023, 412.18 sec so far
Iteration 8979: max relative diff=0.000023, 417.20 sec so far
Iteration 9088: max relative diff=0.000023, 422.23 sec so far
Iteration 9196: max relative diff=0.000023, 427.25 sec so far
Iteration 9305: max relative diff=0.000023, 432.28 sec so far
Iteration 9414: max relative diff=0.000023, 437.30 sec so far
Iteration 9523: max relative diff=0.000023, 442.31 sec so far
Iteration 9631: max relative diff=0.000023, 447.33 sec so far
Iteration 9740: max relative diff=0.000023, 452.35 sec so far
Iteration 9849: max relative diff=0.000023, 457.36 sec so far
Iteration 9959: max relative diff=0.000023, 462.41 sec so far

Jacobi: 10000 iterations in 464.61 seconds (average 0.046428, setup 0.33)

Error: Iterative method did not converge within 10000 iterations.
Consider using a different numerical method or increasing the maximum number of iterations.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_kanban.5_rep2.log

```
Command(s):
../bin/prism  models/kanban.5/model.prism models/kanban.5/property.props
Wallclock time: 491.171 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:17:00 GMT+01:00 2026
Hostname: r23m0214.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/kanban.5/model.prism models/kanban.5/property.props

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Parsing properties file "models/kanban.5/property.props"...

1 property:
(1) "throughput": R{"throughput"}=? [ S ]

---------------------------------------------------------------------

Model checking: "throughput": R{"throughput"}=? [ S ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 71 iterations in 0.14 seconds (average 0.001972, setup 0.00)

Time for model construction: 0.169 seconds.

Type:        CTMC
States:      2546432 (1 initial)
Transitions: 24460016

Rate matrix: 6308 nodes (14 terminal), 24460016 minterms, vars: 48r/48c

SCCs: 1, BSCCs: 1, non-BSCC states: 0
BSCC sizes: 1:2546432

Computing steady state probabilities for BSCC 1

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=48, nodes=6308] [295.7 KB]
Adding explicit sparse matrices... [levels=27, num=165, compact] [749.6 KB]
Creating vector for diagonals... [dist=187, compact] [4.9 MB]
Allocating iteration vectors... [2 x 19.4 MB]
TOTAL: [44.7 MB]

Starting iterations...
Iteration 98: max relative diff=0.023014, 5.02 sec so far
Iteration 205: max relative diff=0.001804, 10.04 sec so far
Iteration 312: max relative diff=0.000265, 15.05 sec so far
Iteration 411: max relative diff=0.000060, 20.08 sec so far
Iteration 518: max relative diff=0.000028, 25.13 sec so far
Iteration 625: max relative diff=0.000024, 30.17 sec so far
Iteration 723: max relative diff=0.000023, 35.20 sec so far
Iteration 830: max relative diff=0.000023, 40.21 sec so far
Iteration 936: max relative diff=0.000023, 45.22 sec so far
Iteration 1035: max relative diff=0.000023, 50.24 sec so far
Iteration 1144: max relative diff=0.000023, 55.25 sec so far
Iteration 1247: max relative diff=0.000023, 60.31 sec so far
Iteration 1350: max relative diff=0.000023, 65.36 sec so far
Iteration 1458: max relative diff=0.000023, 70.37 sec so far
Iteration 1559: max relative diff=0.000023, 75.38 sec so far
Iteration 1663: max relative diff=0.000023, 80.40 sec so far
Iteration 1772: max relative diff=0.000023, 85.42 sec so far
Iteration 1871: max relative diff=0.000023, 90.46 sec so far
Iteration 1982: max relative diff=0.000023, 95.49 sec so far
Iteration 2086: max relative diff=0.000023, 100.50 sec so far
Iteration 2190: max relative diff=0.000023, 105.55 sec so far
Iteration 2300: max relative diff=0.000023, 110.57 sec so far
Iteration 2400: max relative diff=0.000023, 115.63 sec so far
Iteration 2509: max relative diff=0.000023, 120.67 sec so far
Iteration 2617: max relative diff=0.000023, 125.69 sec so far
Iteration 2718: max relative diff=0.000023, 130.70 sec so far
Iteration 2822: max relative diff=0.000023, 135.75 sec so far
Iteration 2930: max relative diff=0.000023, 140.80 sec so far
Iteration 3040: max relative diff=0.000023, 145.82 sec so far
Iteration 3150: max relative diff=0.000023, 150.86 sec so far
Iteration 3258: max relative diff=0.000023, 155.88 sec so far
Iteration 3354: max relative diff=0.000023, 160.92 sec so far
Iteration 3462: max relative diff=0.000023, 165.95 sec so far
Iteration 3573: max relative diff=0.000023, 170.98 sec so far
Iteration 3682: max relative diff=0.000023, 175.99 sec so far
Iteration 3782: max relative diff=0.000023, 181.04 sec so far
Iteration 3870: max relative diff=0.000023, 186.05 sec so far
Iteration 3960: max relative diff=0.000023, 191.08 sec so far
Iteration 4071: max relative diff=0.000023, 196.09 sec so far
Iteration 4175: max relative diff=0.000023, 201.10 sec so far
Iteration 4280: max relative diff=0.000023, 206.13 sec so far
Iteration 4389: max relative diff=0.000023, 211.16 sec so far
Iteration 4499: max relative diff=0.000023, 216.17 sec so far
Iteration 4608: max relative diff=0.000023, 221.22 sec so far
Iteration 4713: max relative diff=0.000023, 226.27 sec so far
Iteration 4811: max relative diff=0.000023, 231.29 sec so far
Iteration 4918: max relative diff=0.000023, 236.31 sec so far
Iteration 5026: max relative diff=0.000023, 241.34 sec so far
Iteration 5134: max relative diff=0.000023, 246.38 sec so far
Iteration 5243: max relative diff=0.000023, 251.41 sec so far
Iteration 5339: max relative diff=0.000023, 256.42 sec so far
Iteration 5441: max relative diff=0.000023, 261.43 sec so far
Iteration 5549: max relative diff=0.000023, 266.48 sec so far
Iteration 5657: max relative diff=0.000023, 271.52 sec so far
Iteration 5765: max relative diff=0.000023, 276.56 sec so far
Iteration 5864: max relative diff=0.000023, 281.62 sec so far
Iteration 5966: max relative diff=0.000023, 286.66 sec so far
Iteration 6075: max relative diff=0.000023, 291.69 sec so far
Iteration 6179: max relative diff=0.000023, 296.70 sec so far
Iteration 6279: max relative diff=0.000023, 301.74 sec so far
Iteration 6388: max relative diff=0.000023, 306.79 sec so far
Iteration 6495: max relative diff=0.000023, 311.80 sec so far
Iteration 6594: max relative diff=0.000023, 316.83 sec so far
Iteration 6702: max relative diff=0.000023, 321.85 sec so far
Iteration 6809: max relative diff=0.000023, 326.86 sec so far
Iteration 6909: max relative diff=0.000023, 331.89 sec so far
Iteration 7013: max relative diff=0.000023, 336.90 sec so far
Iteration 7121: max relative diff=0.000023, 341.94 sec so far
Iteration 7221: max relative diff=0.000023, 346.96 sec so far
Iteration 7326: max relative diff=0.000023, 352.00 sec so far
Iteration 7433: max relative diff=0.000023, 357.04 sec so far
Iteration 7533: max relative diff=0.000023, 362.06 sec so far
Iteration 7638: max relative diff=0.000023, 367.10 sec so far
Iteration 7746: max relative diff=0.000023, 372.12 sec so far
Iteration 7848: max relative diff=0.000023, 377.14 sec so far
Iteration 7950: max relative diff=0.000023, 382.17 sec so far
Iteration 8058: max relative diff=0.000023, 387.20 sec so far
Iteration 8158: max relative diff=0.000023, 392.22 sec so far
Iteration 8261: max relative diff=0.000023, 397.25 sec so far
Iteration 8366: max relative diff=0.000023, 402.26 sec so far
Iteration 8464: max relative diff=0.000023, 407.28 sec so far
Iteration 8569: max relative diff=0.000023, 412.33 sec so far
Iteration 8675: max relative diff=0.000023, 417.38 sec so far
Iteration 8772: max relative diff=0.000023, 422.39 sec so far
Iteration 8878: max relative diff=0.000023, 427.42 sec so far
Iteration 8983: max relative diff=0.000023, 432.46 sec so far
Iteration 9079: max relative diff=0.000023, 437.47 sec so far
Iteration 9185: max relative diff=0.000023, 442.50 sec so far
Iteration 9286: max relative diff=0.000023, 447.51 sec so far
Iteration 9385: max relative diff=0.000023, 452.55 sec so far
Iteration 9491: max relative diff=0.000023, 457.56 sec so far
Iteration 9589: max relative diff=0.000023, 462.57 sec so far
Iteration 9692: max relative diff=0.000023, 467.59 sec so far
Iteration 9796: max relative diff=0.000023, 472.61 sec so far
Iteration 9892: max relative diff=0.000023, 477.62 sec so far
Iteration 9999: max relative diff=0.000023, 482.63 sec so far

Jacobi: 10000 iterations in 483.01 seconds (average 0.048267, setup 0.34)

Error: Iterative method did not converge within 10000 iterations.
Consider using a different numerical method or increasing the maximum number of iterations.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_kanban.5_rep3.log

```
Command(s):
../bin/prism  models/kanban.5/model.prism models/kanban.5/property.props
Wallclock time: 416.233 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:03 GMT+01:00 2026
Hostname: r23m0099.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/kanban.5/model.prism models/kanban.5/property.props

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Parsing properties file "models/kanban.5/property.props"...

1 property:
(1) "throughput": R{"throughput"}=? [ S ]

---------------------------------------------------------------------

Model checking: "throughput": R{"throughput"}=? [ S ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 71 iterations in 0.10 seconds (average 0.001408, setup 0.00)

Time for model construction: 0.131 seconds.

Type:        CTMC
States:      2546432 (1 initial)
Transitions: 24460016

Rate matrix: 6308 nodes (14 terminal), 24460016 minterms, vars: 48r/48c

SCCs: 1, BSCCs: 1, non-BSCC states: 0
BSCC sizes: 1:2546432

Computing steady state probabilities for BSCC 1

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=48, nodes=6308] [295.7 KB]
Adding explicit sparse matrices... [levels=27, num=165, compact] [749.6 KB]
Creating vector for diagonals... [dist=187, compact] [4.9 MB]
Allocating iteration vectors... [2 x 19.4 MB]
TOTAL: [44.7 MB]

Starting iterations...
Iteration 121: max relative diff=0.011042, 5.04 sec so far
Iteration 243: max relative diff=0.000922, 10.08 sec so far
Iteration 365: max relative diff=0.000111, 15.12 sec so far
Iteration 487: max relative diff=0.000032, 20.14 sec so far
Iteration 609: max relative diff=0.000024, 25.17 sec so far
Iteration 731: max relative diff=0.000023, 30.19 sec so far
Iteration 853: max relative diff=0.000023, 35.21 sec so far
Iteration 975: max relative diff=0.000023, 40.24 sec so far
Iteration 1097: max relative diff=0.000023, 45.26 sec so far
Iteration 1219: max relative diff=0.000023, 50.28 sec so far
Iteration 1341: max relative diff=0.000023, 55.31 sec so far
Iteration 1461: max relative diff=0.000023, 60.33 sec so far
Iteration 1582: max relative diff=0.000023, 65.36 sec so far
Iteration 1704: max relative diff=0.000023, 70.38 sec so far
Iteration 1826: max relative diff=0.000023, 75.40 sec so far
Iteration 1948: max relative diff=0.000023, 80.42 sec so far
Iteration 2070: max relative diff=0.000023, 85.45 sec so far
Iteration 2192: max relative diff=0.000023, 90.48 sec so far
Iteration 2314: max relative diff=0.000023, 95.50 sec so far
Iteration 2436: max relative diff=0.000023, 100.52 sec so far
Iteration 2558: max relative diff=0.000023, 105.55 sec so far
Iteration 2680: max relative diff=0.000023, 110.57 sec so far
Iteration 2801: max relative diff=0.000023, 115.59 sec so far
Iteration 2922: max relative diff=0.000023, 120.61 sec so far
Iteration 3043: max relative diff=0.000023, 125.63 sec so far
Iteration 3165: max relative diff=0.000023, 130.66 sec so far
Iteration 3287: max relative diff=0.000023, 135.69 sec so far
Iteration 3409: max relative diff=0.000023, 140.71 sec so far
Iteration 3531: max relative diff=0.000023, 145.74 sec so far
Iteration 3653: max relative diff=0.000023, 150.76 sec so far
Iteration 3775: max relative diff=0.000023, 155.79 sec so far
Iteration 3897: max relative diff=0.000023, 160.81 sec so far
Iteration 4019: max relative diff=0.000023, 165.83 sec so far
Iteration 4141: max relative diff=0.000023, 170.86 sec so far
Iteration 4262: max relative diff=0.000023, 175.90 sec so far
Iteration 4383: max relative diff=0.000023, 180.91 sec so far
Iteration 4504: max relative diff=0.000023, 185.92 sec so far
Iteration 4626: max relative diff=0.000023, 190.95 sec so far
Iteration 4748: max relative diff=0.000023, 195.97 sec so far
Iteration 4870: max relative diff=0.000023, 200.99 sec so far
Iteration 4992: max relative diff=0.000023, 206.02 sec so far
Iteration 5114: max relative diff=0.000023, 211.05 sec so far
Iteration 5236: max relative diff=0.000023, 216.07 sec so far
Iteration 5358: max relative diff=0.000023, 221.10 sec so far
Iteration 5480: max relative diff=0.000023, 226.12 sec so far
Iteration 5602: max relative diff=0.000023, 231.14 sec so far
Iteration 5723: max relative diff=0.000023, 236.19 sec so far
Iteration 5845: max relative diff=0.000023, 241.22 sec so far
Iteration 5966: max relative diff=0.000023, 246.25 sec so far
Iteration 6088: max relative diff=0.000023, 251.28 sec so far
Iteration 6210: max relative diff=0.000023, 256.30 sec so far
Iteration 6332: max relative diff=0.000023, 261.32 sec so far
Iteration 6454: max relative diff=0.000023, 266.34 sec so far
Iteration 6576: max relative diff=0.000023, 271.38 sec so far
Iteration 6698: max relative diff=0.000023, 276.40 sec so far
Iteration 6820: max relative diff=0.000023, 281.43 sec so far
Iteration 6942: max relative diff=0.000023, 286.45 sec so far
Iteration 7064: max relative diff=0.000023, 291.47 sec so far
Iteration 7184: max relative diff=0.000023, 296.49 sec so far
Iteration 7306: max relative diff=0.000023, 301.53 sec so far
Iteration 7427: max relative diff=0.000023, 306.55 sec so far
Iteration 7549: max relative diff=0.000023, 311.57 sec so far
Iteration 7671: max relative diff=0.000023, 316.60 sec so far
Iteration 7793: max relative diff=0.000023, 321.62 sec so far
Iteration 7915: max relative diff=0.000023, 326.65 sec so far
Iteration 8037: max relative diff=0.000023, 331.67 sec so far
Iteration 8159: max relative diff=0.000023, 336.69 sec so far
Iteration 8281: max relative diff=0.000023, 341.72 sec so far
Iteration 8403: max relative diff=0.000023, 346.74 sec so far
Iteration 8525: max relative diff=0.000023, 351.76 sec so far
Iteration 8645: max relative diff=0.000023, 356.79 sec so far
Iteration 8766: max relative diff=0.000023, 361.80 sec so far
Iteration 8887: max relative diff=0.000023, 366.81 sec so far
Iteration 9009: max relative diff=0.000023, 371.83 sec so far
Iteration 9131: max relative diff=0.000023, 376.86 sec so far
Iteration 9253: max relative diff=0.000023, 381.89 sec so far
Iteration 9375: max relative diff=0.000023, 386.91 sec so far
Iteration 9497: max relative diff=0.000023, 391.93 sec so far
Iteration 9618: max relative diff=0.000023, 396.94 sec so far
Iteration 9740: max relative diff=0.000023, 401.96 sec so far
Iteration 9862: max relative diff=0.000023, 406.98 sec so far
Iteration 9984: max relative diff=0.000023, 412.00 sec so far

Jacobi: 10000 iterations in 412.95 seconds (average 0.041266, setup 0.29)

Error: Iterative method did not converge within 10000 iterations.
Consider using a different numerical method or increasing the maximum number of iterations.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_kanban.5_rep4.log

```
Command(s):
../bin/prism  models/kanban.5/model.prism models/kanban.5/property.props
Wallclock time: 518.113 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:58:25 GMT+01:00 2026
Hostname: n23m0107.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/kanban.5/model.prism models/kanban.5/property.props

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Parsing properties file "models/kanban.5/property.props"...

1 property:
(1) "throughput": R{"throughput"}=? [ S ]

---------------------------------------------------------------------

Model checking: "throughput": R{"throughput"}=? [ S ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 71 iterations in 0.12 seconds (average 0.001690, setup 0.00)

Time for model construction: 0.179 seconds.

Type:        CTMC
States:      2546432 (1 initial)
Transitions: 24460016

Rate matrix: 6308 nodes (14 terminal), 24460016 minterms, vars: 48r/48c

SCCs: 1, BSCCs: 1, non-BSCC states: 0
BSCC sizes: 1:2546432

Computing steady state probabilities for BSCC 1

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=48, nodes=6308] [295.7 KB]
Adding explicit sparse matrices... [levels=27, num=165, compact] [749.6 KB]
Creating vector for diagonals... [dist=187, compact] [4.9 MB]
Allocating iteration vectors... [2 x 19.4 MB]
TOTAL: [44.7 MB]

Starting iterations...
Iteration 98: max relative diff=0.023014, 5.05 sec so far
Iteration 196: max relative diff=0.002096, 10.08 sec so far
Iteration 294: max relative diff=0.000365, 15.12 sec so far
Iteration 392: max relative diff=0.000075, 20.16 sec so far
Iteration 490: max relative diff=0.000031, 25.20 sec so far
Iteration 588: max relative diff=0.000025, 30.23 sec so far
Iteration 685: max relative diff=0.000023, 35.24 sec so far
Iteration 783: max relative diff=0.000023, 40.29 sec so far
Iteration 881: max relative diff=0.000023, 45.33 sec so far
Iteration 979: max relative diff=0.000023, 50.37 sec so far
Iteration 1077: max relative diff=0.000023, 55.40 sec so far
Iteration 1175: max relative diff=0.000023, 60.45 sec so far
Iteration 1273: max relative diff=0.000023, 65.49 sec so far
Iteration 1371: max relative diff=0.000023, 70.52 sec so far
Iteration 1469: max relative diff=0.000023, 75.56 sec so far
Iteration 1567: max relative diff=0.000023, 80.59 sec so far
Iteration 1665: max relative diff=0.000023, 85.62 sec so far
Iteration 1762: max relative diff=0.000023, 90.65 sec so far
Iteration 1859: max relative diff=0.000023, 95.66 sec so far
Iteration 1957: max relative diff=0.000023, 100.69 sec so far
Iteration 2055: max relative diff=0.000023, 105.74 sec so far
Iteration 2153: max relative diff=0.000023, 110.78 sec so far
Iteration 2251: max relative diff=0.000023, 115.80 sec so far
Iteration 2351: max relative diff=0.000023, 120.83 sec so far
Iteration 2451: max relative diff=0.000023, 125.85 sec so far
Iteration 2549: max relative diff=0.000023, 130.88 sec so far
Iteration 2647: max relative diff=0.000023, 135.92 sec so far
Iteration 2745: max relative diff=0.000023, 140.95 sec so far
Iteration 2843: max relative diff=0.000023, 145.98 sec so far
Iteration 2941: max relative diff=0.000023, 151.00 sec so far
Iteration 3038: max relative diff=0.000023, 156.01 sec so far
Iteration 3136: max relative diff=0.000023, 161.05 sec so far
Iteration 3234: max relative diff=0.000023, 166.07 sec so far
Iteration 3332: max relative diff=0.000023, 171.11 sec so far
Iteration 3430: max relative diff=0.000023, 176.14 sec so far
Iteration 3528: max relative diff=0.000023, 181.18 sec so far
Iteration 3626: max relative diff=0.000023, 186.21 sec so far
Iteration 3724: max relative diff=0.000023, 191.24 sec so far
Iteration 3822: max relative diff=0.000023, 196.27 sec so far
Iteration 3920: max relative diff=0.000023, 201.30 sec so far
Iteration 4018: max relative diff=0.000023, 206.33 sec so far
Iteration 4116: max relative diff=0.000023, 211.38 sec so far
Iteration 4214: max relative diff=0.000023, 216.42 sec so far
Iteration 4312: max relative diff=0.000023, 221.47 sec so far
Iteration 4410: max relative diff=0.000023, 226.52 sec so far
Iteration 4508: max relative diff=0.000023, 231.56 sec so far
Iteration 4606: max relative diff=0.000023, 236.60 sec so far
Iteration 4704: max relative diff=0.000023, 241.64 sec so far
Iteration 4802: max relative diff=0.000023, 246.68 sec so far
Iteration 4900: max relative diff=0.000023, 251.71 sec so far
Iteration 4998: max relative diff=0.000023, 256.75 sec so far
Iteration 5096: max relative diff=0.000023, 261.78 sec so far
Iteration 5194: max relative diff=0.000023, 266.82 sec so far
Iteration 5292: max relative diff=0.000023, 271.87 sec so far
Iteration 5389: max relative diff=0.000023, 276.88 sec so far
Iteration 5486: max relative diff=0.000023, 281.90 sec so far
Iteration 5584: max relative diff=0.000023, 286.93 sec so far
Iteration 5682: max relative diff=0.000023, 291.98 sec so far
Iteration 5780: max relative diff=0.000023, 297.01 sec so far
Iteration 5878: max relative diff=0.000023, 302.06 sec so far
Iteration 5976: max relative diff=0.000023, 307.09 sec so far
Iteration 6074: max relative diff=0.000023, 312.12 sec so far
Iteration 6172: max relative diff=0.000023, 317.16 sec so far
Iteration 6270: max relative diff=0.000023, 322.19 sec so far
Iteration 6368: max relative diff=0.000023, 327.24 sec so far
Iteration 6466: max relative diff=0.000023, 332.28 sec so far
Iteration 6562: max relative diff=0.000023, 337.31 sec so far
Iteration 6659: max relative diff=0.000023, 342.33 sec so far
Iteration 6757: max relative diff=0.000023, 347.35 sec so far
Iteration 6855: max relative diff=0.000023, 352.37 sec so far
Iteration 6953: max relative diff=0.000023, 357.38 sec so far
Iteration 7051: max relative diff=0.000023, 362.41 sec so far
Iteration 7148: max relative diff=0.000023, 367.44 sec so far
Iteration 7246: max relative diff=0.000023, 372.49 sec so far
Iteration 7343: max relative diff=0.000023, 377.50 sec so far
Iteration 7440: max relative diff=0.000023, 382.53 sec so far
Iteration 7537: max relative diff=0.000023, 387.55 sec so far
Iteration 7634: max relative diff=0.000023, 392.58 sec so far
Iteration 7730: max relative diff=0.000023, 397.61 sec so far
Iteration 7827: max relative diff=0.000023, 402.65 sec so far
Iteration 7924: max relative diff=0.000023, 407.69 sec so far
Iteration 8021: max relative diff=0.000023, 412.72 sec so far
Iteration 8118: max relative diff=0.000023, 417.75 sec so far
Iteration 8215: max relative diff=0.000023, 422.80 sec so far
Iteration 8312: max relative diff=0.000023, 427.84 sec so far
Iteration 8409: max relative diff=0.000023, 432.87 sec so far
Iteration 8506: max relative diff=0.000023, 437.89 sec so far
Iteration 8601: max relative diff=0.000023, 442.93 sec so far
Iteration 8699: max relative diff=0.000023, 447.97 sec so far
Iteration 8797: max relative diff=0.000023, 453.00 sec so far
Iteration 8894: max relative diff=0.000023, 458.03 sec so far
Iteration 8992: max relative diff=0.000023, 463.06 sec so far
Iteration 9090: max relative diff=0.000023, 468.07 sec so far
Iteration 9188: max relative diff=0.000023, 473.09 sec so far
Iteration 9286: max relative diff=0.000023, 478.12 sec so far
Iteration 9384: max relative diff=0.000023, 483.14 sec so far
Iteration 9481: max relative diff=0.000023, 488.18 sec so far
Iteration 9578: max relative diff=0.000023, 493.22 sec so far
Iteration 9676: max relative diff=0.000023, 498.28 sec so far
Iteration 9774: max relative diff=0.000023, 503.29 sec so far
Iteration 9872: max relative diff=0.000023, 508.32 sec so far
Iteration 9970: max relative diff=0.000023, 513.36 sec so far

Jacobi: 10000 iterations in 515.25 seconds (average 0.051490, setup 0.35)

Error: Iterative method did not converge within 10000 iterations.
Consider using a different numerical method or increasing the maximum number of iterations.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_kanban.5_rep5.log

```
Command(s):
../bin/prism  models/kanban.5/model.prism models/kanban.5/property.props
Wallclock time: 451.231 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 02:58:27 GMT+01:00 2026
Hostname: n23m0355.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/kanban.5/model.prism models/kanban.5/property.props

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Parsing properties file "models/kanban.5/property.props"...

1 property:
(1) "throughput": R{"throughput"}=? [ S ]

---------------------------------------------------------------------

Model checking: "throughput": R{"throughput"}=? [ S ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 71 iterations in 0.10 seconds (average 0.001408, setup 0.00)

Time for model construction: 0.128 seconds.

Type:        CTMC
States:      2546432 (1 initial)
Transitions: 24460016

Rate matrix: 6308 nodes (14 terminal), 24460016 minterms, vars: 48r/48c

SCCs: 1, BSCCs: 1, non-BSCC states: 0
BSCC sizes: 1:2546432

Computing steady state probabilities for BSCC 1

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=48, nodes=6308] [295.7 KB]
Adding explicit sparse matrices... [levels=27, num=165, compact] [749.6 KB]
Creating vector for diagonals... [dist=187, compact] [4.9 MB]
Allocating iteration vectors... [2 x 19.4 MB]
TOTAL: [44.7 MB]

Starting iterations...
Iteration 112: max relative diff=0.014838, 5.03 sec so far
Iteration 224: max relative diff=0.001291, 10.05 sec so far
Iteration 336: max relative diff=0.000176, 15.07 sec so far
Iteration 448: max relative diff=0.000041, 20.10 sec so far
Iteration 560: max relative diff=0.000025, 25.13 sec so far
Iteration 672: max relative diff=0.000023, 30.15 sec so far
Iteration 785: max relative diff=0.000023, 35.17 sec so far
Iteration 897: max relative diff=0.000023, 40.19 sec so far
Iteration 1007: max relative diff=0.000023, 45.20 sec so far
Iteration 1117: max relative diff=0.000023, 50.22 sec so far
Iteration 1229: max relative diff=0.000023, 55.24 sec so far
Iteration 1340: max relative diff=0.000023, 60.26 sec so far
Iteration 1451: max relative diff=0.000023, 65.27 sec so far
Iteration 1563: max relative diff=0.000023, 70.29 sec so far
Iteration 1676: max relative diff=0.000023, 75.33 sec so far
Iteration 1788: max relative diff=0.000023, 80.34 sec so far
Iteration 1900: max relative diff=0.000023, 85.36 sec so far
Iteration 2011: max relative diff=0.000023, 90.37 sec so far
Iteration 2122: max relative diff=0.000023, 95.41 sec so far
Iteration 2233: max relative diff=0.000023, 100.46 sec so far
Iteration 2344: max relative diff=0.000023, 105.48 sec so far
Iteration 2455: max relative diff=0.000023, 110.52 sec so far
Iteration 2566: max relative diff=0.000023, 115.55 sec so far
Iteration 2677: max relative diff=0.000023, 120.57 sec so far
Iteration 2788: max relative diff=0.000023, 125.61 sec so far
Iteration 2899: max relative diff=0.000023, 130.63 sec so far
Iteration 3010: max relative diff=0.000023, 135.65 sec so far
Iteration 3121: max relative diff=0.000023, 140.67 sec so far
Iteration 3232: max relative diff=0.000023, 145.70 sec so far
Iteration 3343: max relative diff=0.000023, 150.72 sec so far
Iteration 3458: max relative diff=0.000023, 155.76 sec so far
Iteration 3568: max relative diff=0.000023, 160.77 sec so far
Iteration 3679: max relative diff=0.000023, 165.81 sec so far
Iteration 3790: max relative diff=0.000023, 170.84 sec so far
Iteration 3901: max relative diff=0.000023, 175.87 sec so far
Iteration 4012: max relative diff=0.000023, 180.88 sec so far
Iteration 4123: max relative diff=0.000023, 185.90 sec so far
Iteration 4235: max relative diff=0.000023, 190.95 sec so far
Iteration 4346: max relative diff=0.000023, 195.97 sec so far
Iteration 4457: max relative diff=0.000023, 201.00 sec so far
Iteration 4568: max relative diff=0.000023, 206.02 sec so far
Iteration 4679: max relative diff=0.000023, 211.05 sec so far
Iteration 4794: max relative diff=0.000023, 216.08 sec so far
Iteration 4903: max relative diff=0.000023, 221.11 sec so far
Iteration 5014: max relative diff=0.000023, 226.12 sec so far
Iteration 5126: max relative diff=0.000023, 231.15 sec so far
Iteration 5238: max relative diff=0.000023, 236.17 sec so far
Iteration 5350: max relative diff=0.000023, 241.20 sec so far
Iteration 5461: max relative diff=0.000023, 246.22 sec so far
Iteration 5573: max relative diff=0.000023, 251.23 sec so far
Iteration 5685: max relative diff=0.000023, 256.26 sec so far
Iteration 5797: max relative diff=0.000023, 261.29 sec so far
Iteration 5909: max relative diff=0.000023, 266.32 sec so far
Iteration 6021: max relative diff=0.000023, 271.36 sec so far
Iteration 6138: max relative diff=0.000023, 276.41 sec so far
Iteration 6249: max relative diff=0.000023, 281.42 sec so far
Iteration 6361: max relative diff=0.000023, 286.45 sec so far
Iteration 6473: max relative diff=0.000023, 291.48 sec so far
Iteration 6585: max relative diff=0.000023, 296.50 sec so far
Iteration 6697: max relative diff=0.000023, 301.55 sec so far
Iteration 6809: max relative diff=0.000023, 306.56 sec so far
Iteration 6921: max relative diff=0.000023, 311.57 sec so far
Iteration 7036: max relative diff=0.000023, 316.58 sec so far
Iteration 7158: max relative diff=0.000023, 321.61 sec so far
Iteration 7275: max relative diff=0.000023, 326.64 sec so far
Iteration 7386: max relative diff=0.000023, 331.66 sec so far
Iteration 7503: max relative diff=0.000023, 336.69 sec so far
Iteration 7614: max relative diff=0.000023, 341.72 sec so far
Iteration 7726: max relative diff=0.000023, 346.74 sec so far
Iteration 7838: max relative diff=0.000023, 351.77 sec so far
Iteration 7950: max relative diff=0.000023, 356.79 sec so far
Iteration 8062: max relative diff=0.000023, 361.82 sec so far
Iteration 8174: max relative diff=0.000023, 366.84 sec so far
Iteration 8287: max relative diff=0.000023, 371.89 sec so far
Iteration 8399: max relative diff=0.000023, 376.92 sec so far
Iteration 8511: max relative diff=0.000023, 381.94 sec so far
Iteration 8623: max relative diff=0.000023, 386.97 sec so far
Iteration 8734: max relative diff=0.000023, 392.01 sec so far
Iteration 8851: max relative diff=0.000023, 397.05 sec so far
Iteration 8962: max relative diff=0.000023, 402.07 sec so far
Iteration 9074: max relative diff=0.000023, 407.10 sec so far
Iteration 9186: max relative diff=0.000023, 412.13 sec so far
Iteration 9298: max relative diff=0.000023, 417.15 sec so far
Iteration 9410: max relative diff=0.000023, 422.18 sec so far
Iteration 9522: max relative diff=0.000023, 427.20 sec so far
Iteration 9635: max relative diff=0.000023, 432.24 sec so far
Iteration 9745: max relative diff=0.000023, 437.25 sec so far
Iteration 9856: max relative diff=0.000023, 442.26 sec so far
Iteration 9968: max relative diff=0.000023, 447.30 sec so far

Jacobi: 10000 iterations in 449.02 seconds (average 0.044873, setup 0.29)

Error: Iterative method did not converge within 10000 iterations.
Consider using a different numerical method or increasing the maximum number of iterations.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

