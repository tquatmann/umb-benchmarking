# Log files for prism_from-prism_check_default on model [consensus.6-2](../../models/consensus.6-2)

Parsed values: `[0.072, 0.103, 0.073, 0.08, 0.101]`



### Log file: prism_from-prism_check_default_consensus.6-2_rep1.log

```
Command(s):
../bin/prism  models/consensus.6-2/model.prism models/consensus.6-2/property.props
Wallclock time: 168.150 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:46:51 GMT+01:00 2026
Hostname: r23m0219.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.6-2/model.prism models/consensus.6-2/property.props

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Parsing properties file "models/consensus.6-2/property.props"...

1 property:
(1) "disagree": Pmax=? [ F "finished"&!"agree" ]

---------------------------------------------------------------------

Model checking: "disagree": Pmax=? [ F "finished"&!"agree" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 149 iterations in 0.05 seconds (average 0.000336, setup 0.00)

Time for model construction: 0.072 seconds.

Type:        MDP
States:      1258240 (1 initial)
Transitions: 6236736

Transition matrix: 7075 nodes (3 terminal), 6236736 minterms, vars: 24r/24c/6nd

Prob0A: 115 iterations in 0.45 seconds (average 0.003913, setup 0.00)

Prob1E: 1925 iterations in 14.90 seconds (average 0.007740, setup 0.00)

yes = 583956, no = 27270, maybe = 647014

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=6, levels=24, nodes=27117] [1.2 MB]
Adding sparse bits... [levels=14-15, num=958, compact=6/6] [5.4 MB]
Creating vector for yes... [dist=2, compact] [2.4 MB]
Allocating iteration vectors... [3 x 9.6 MB]
TOTAL: [37.8 MB]

Starting iterations...
Iteration 123: max relative diff=0.795820, 5.02 sec so far
Iteration 248: max relative diff=0.095238, 10.03 sec so far
Iteration 374: max relative diff=0.039152, 15.06 sec so far
Iteration 499: max relative diff=0.020492, 20.10 sec so far
Iteration 623: max relative diff=0.012048, 25.13 sec so far
Iteration 747: max relative diff=0.007420, 30.15 sec so far
Iteration 871: max relative diff=0.004803, 35.18 sec so far
Iteration 995: max relative diff=0.003174, 40.21 sec so far
Iteration 1119: max relative diff=0.002118, 45.23 sec so far
Iteration 1244: max relative diff=0.001447, 50.28 sec so far
Iteration 1368: max relative diff=0.000987, 55.29 sec so far
Iteration 1495: max relative diff=0.000677, 60.31 sec so far
Iteration 1620: max relative diff=0.000467, 65.34 sec so far
Iteration 1744: max relative diff=0.000325, 70.35 sec so far
Iteration 1869: max relative diff=0.000225, 75.39 sec so far
Iteration 1993: max relative diff=0.000158, 80.41 sec so far
Iteration 2117: max relative diff=0.000111, 85.44 sec so far
Iteration 2241: max relative diff=0.000077, 90.47 sec so far
Iteration 2365: max relative diff=0.000054, 95.50 sec so far
Iteration 2489: max relative diff=0.000038, 100.52 sec so far
Iteration 2613: max relative diff=0.000026, 105.55 sec so far
Iteration 2738: max relative diff=0.000019, 110.59 sec so far
Iteration 2864: max relative diff=0.000013, 115.63 sec so far
Iteration 2991: max relative diff=0.000009, 120.68 sec so far
Iteration 3117: max relative diff=0.000006, 125.72 sec so far
Iteration 3242: max relative diff=0.000004, 130.74 sec so far
Iteration 3366: max relative diff=0.000003, 135.76 sec so far
Iteration 3490: max relative diff=0.000002, 140.79 sec so far
Iteration 3613: max relative diff=0.000002, 145.80 sec so far
Iteration 3737: max relative diff=0.000001, 150.82 sec so far

Iterative method: 3759 iterations in 151.74 seconds (average 0.040346, setup 0.08)

Value in the initial state: 0.36362423396240773

Time for model checking: 167.514 seconds.

Result: 0.36362423396240773 (+/- 3.607106234271578E-6 estimated; rel err 9.91987303751732E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_consensus.6-2_rep2.log

```
Command(s):
../bin/prism  models/consensus.6-2/model.prism models/consensus.6-2/property.props
Wallclock time: 187.487 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:36:43 GMT+01:00 2026
Hostname: n23m0053.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.6-2/model.prism models/consensus.6-2/property.props

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Parsing properties file "models/consensus.6-2/property.props"...

1 property:
(1) "disagree": Pmax=? [ F "finished"&!"agree" ]

---------------------------------------------------------------------

Model checking: "disagree": Pmax=? [ F "finished"&!"agree" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 149 iterations in 0.05 seconds (average 0.000336, setup 0.00)

Time for model construction: 0.103 seconds.

Type:        MDP
States:      1258240 (1 initial)
Transitions: 6236736

Transition matrix: 7075 nodes (3 terminal), 6236736 minterms, vars: 24r/24c/6nd

Prob0A: 115 iterations in 0.70 seconds (average 0.006087, setup 0.00)

Prob1E: 1925 iterations in 15.96 seconds (average 0.008291, setup 0.00)

yes = 583956, no = 27270, maybe = 647014

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=6, levels=24, nodes=27117] [1.2 MB]
Adding sparse bits... [levels=14-15, num=958, compact=6/6] [5.4 MB]
Creating vector for yes... [dist=2, compact] [2.4 MB]
Allocating iteration vectors... [3 x 9.6 MB]
TOTAL: [37.8 MB]

Starting iterations...
Iteration 116: max relative diff=2.146781, 5.03 sec so far
Iteration 233: max relative diff=0.110939, 10.05 sec so far
Iteration 357: max relative diff=0.042886, 15.08 sec so far
Iteration 480: max relative diff=0.022313, 20.12 sec so far
Iteration 598: max relative diff=0.013290, 25.15 sec so far
Iteration 721: max relative diff=0.008214, 30.16 sec so far
Iteration 840: max relative diff=0.005331, 35.20 sec so far
Iteration 960: max relative diff=0.003547, 40.22 sec so far
Iteration 1083: max relative diff=0.002374, 45.24 sec so far
Iteration 1203: max relative diff=0.001629, 50.26 sec so far
Iteration 1322: max relative diff=0.001140, 55.28 sec so far
Iteration 1442: max relative diff=0.000795, 60.31 sec so far
Iteration 1567: max relative diff=0.000547, 65.35 sec so far
Iteration 1689: max relative diff=0.000381, 70.38 sec so far
Iteration 1803: max relative diff=0.000273, 75.43 sec so far
Iteration 1910: max relative diff=0.000202, 80.45 sec so far
Iteration 2016: max relative diff=0.000148, 85.47 sec so far
Iteration 2123: max relative diff=0.000109, 90.48 sec so far
Iteration 2232: max relative diff=0.000079, 95.50 sec so far
Iteration 2338: max relative diff=0.000058, 100.54 sec so far
Iteration 2447: max relative diff=0.000043, 105.58 sec so far
Iteration 2555: max relative diff=0.000031, 110.59 sec so far
Iteration 2664: max relative diff=0.000023, 115.62 sec so far
Iteration 2765: max relative diff=0.000017, 120.64 sec so far
Iteration 2873: max relative diff=0.000013, 125.68 sec so far
Iteration 2980: max relative diff=0.000009, 130.73 sec so far
Iteration 3084: max relative diff=0.000007, 135.76 sec so far
Iteration 3192: max relative diff=0.000005, 140.80 sec so far
Iteration 3297: max relative diff=0.000004, 145.81 sec so far
Iteration 3400: max relative diff=0.000003, 150.82 sec so far
Iteration 3509: max relative diff=0.000002, 155.87 sec so far
Iteration 3616: max relative diff=0.000001, 160.90 sec so far
Iteration 3724: max relative diff=0.000001, 165.92 sec so far

Iterative method: 3759 iterations in 167.66 seconds (average 0.044581, setup 0.08)

Value in the initial state: 0.36362423396240773

Time for model checking: 185.289 seconds.

Result: 0.36362423396240773 (+/- 3.607106234271578E-6 estimated; rel err 9.91987303751732E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_consensus.6-2_rep3.log

```
Command(s):
../bin/prism  models/consensus.6-2/model.prism models/consensus.6-2/property.props
Wallclock time: 250.519 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:24:19 GMT+01:00 2026
Hostname: n23m0324.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.6-2/model.prism models/consensus.6-2/property.props

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Parsing properties file "models/consensus.6-2/property.props"...

1 property:
(1) "disagree": Pmax=? [ F "finished"&!"agree" ]

---------------------------------------------------------------------

Model checking: "disagree": Pmax=? [ F "finished"&!"agree" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 149 iterations in 0.04 seconds (average 0.000268, setup 0.00)

Time for model construction: 0.073 seconds.

Type:        MDP
States:      1258240 (1 initial)
Transitions: 6236736

Transition matrix: 7075 nodes (3 terminal), 6236736 minterms, vars: 24r/24c/6nd

Prob0A: 115 iterations in 0.47 seconds (average 0.004087, setup 0.00)

Prob1E: 1925 iterations in 12.94 seconds (average 0.006722, setup 0.00)

yes = 583956, no = 27270, maybe = 647014

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=6, levels=24, nodes=27117] [1.2 MB]
Adding sparse bits... [levels=14-15, num=958, compact=6/6] [5.4 MB]
Creating vector for yes... [dist=2, compact] [2.4 MB]
Allocating iteration vectors... [3 x 9.6 MB]
TOTAL: [37.8 MB]

Starting iterations...
Iteration 137: max relative diff=0.479395, 5.04 sec so far
Iteration 258: max relative diff=0.085916, 10.09 sec so far
Iteration 369: max relative diff=0.039926, 15.19 sec so far
Iteration 485: max relative diff=0.021975, 20.23 sec so far
Iteration 602: max relative diff=0.013142, 25.28 sec so far
Iteration 718: max relative diff=0.008294, 30.32 sec so far
Iteration 833: max relative diff=0.005490, 35.33 sec so far
Iteration 948: max relative diff=0.003691, 40.34 sec so far
Iteration 1066: max relative diff=0.002515, 45.37 sec so far
Iteration 1175: max relative diff=0.001788, 50.40 sec so far
Iteration 1246: max relative diff=0.001431, 55.41 sec so far
Iteration 1318: max relative diff=0.001149, 60.47 sec so far
Iteration 1390: max relative diff=0.000925, 65.53 sec so far
Iteration 1461: max relative diff=0.000745, 70.55 sec so far
Iteration 1533: max relative diff=0.000602, 75.61 sec so far
Iteration 1605: max relative diff=0.000487, 80.67 sec so far
Iteration 1676: max relative diff=0.000398, 85.68 sec so far
Iteration 1748: max relative diff=0.000323, 90.73 sec so far
Iteration 1816: max relative diff=0.000264, 95.77 sec so far
Iteration 1884: max relative diff=0.000216, 100.82 sec so far
Iteration 1954: max relative diff=0.000177, 105.88 sec so far
Iteration 2024: max relative diff=0.000145, 110.95 sec so far
Iteration 2094: max relative diff=0.000118, 115.98 sec so far
Iteration 2164: max relative diff=0.000096, 121.02 sec so far
Iteration 2234: max relative diff=0.000079, 126.06 sec so far
Iteration 2305: max relative diff=0.000064, 131.15 sec so far
Iteration 2375: max relative diff=0.000053, 136.21 sec so far
Iteration 2445: max relative diff=0.000043, 141.22 sec so far
Iteration 2515: max relative diff=0.000035, 146.23 sec so far
Iteration 2586: max relative diff=0.000029, 151.31 sec so far
Iteration 2657: max relative diff=0.000023, 156.37 sec so far
Iteration 2727: max relative diff=0.000019, 161.38 sec so far
Iteration 2798: max relative diff=0.000016, 166.43 sec so far
Iteration 2868: max relative diff=0.000013, 171.44 sec so far
Iteration 2939: max relative diff=0.000010, 176.53 sec so far
Iteration 3010: max relative diff=0.000009, 181.57 sec so far
Iteration 3081: max relative diff=0.000007, 186.62 sec so far
Iteration 3151: max relative diff=0.000006, 191.63 sec so far
Iteration 3221: max relative diff=0.000005, 196.65 sec so far
Iteration 3291: max relative diff=0.000004, 201.72 sec so far
Iteration 3361: max relative diff=0.000003, 206.76 sec so far
Iteration 3432: max relative diff=0.000003, 211.83 sec so far
Iteration 3502: max relative diff=0.000002, 216.86 sec so far
Iteration 3572: max relative diff=0.000002, 221.90 sec so far
Iteration 3643: max relative diff=0.000001, 226.95 sec so far
Iteration 3713: max relative diff=0.000001, 231.98 sec so far

Iterative method: 3759 iterations in 235.33 seconds (average 0.062586, setup 0.07)

Value in the initial state: 0.36362423396240773

Time for model checking: 249.476 seconds.

Result: 0.36362423396240773 (+/- 3.607106234271578E-6 estimated; rel err 9.91987303751732E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_consensus.6-2_rep4.log

```
Command(s):
../bin/prism  models/consensus.6-2/model.prism models/consensus.6-2/property.props
Wallclock time: 183.414 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:00:27 GMT+01:00 2026
Hostname: n23m0132.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.6-2/model.prism models/consensus.6-2/property.props

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Parsing properties file "models/consensus.6-2/property.props"...

1 property:
(1) "disagree": Pmax=? [ F "finished"&!"agree" ]

---------------------------------------------------------------------

Model checking: "disagree": Pmax=? [ F "finished"&!"agree" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 149 iterations in 0.05 seconds (average 0.000336, setup 0.00)

Time for model construction: 0.08 seconds.

Type:        MDP
States:      1258240 (1 initial)
Transitions: 6236736

Transition matrix: 7075 nodes (3 terminal), 6236736 minterms, vars: 24r/24c/6nd

Prob0A: 115 iterations in 0.69 seconds (average 0.006000, setup 0.00)

Prob1E: 1925 iterations in 19.89 seconds (average 0.010332, setup 0.00)

yes = 583956, no = 27270, maybe = 647014

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=6, levels=24, nodes=27117] [1.2 MB]
Adding sparse bits... [levels=14-15, num=958, compact=6/6] [5.4 MB]
Creating vector for yes... [dist=2, compact] [2.4 MB]
Allocating iteration vectors... [3 x 9.6 MB]
TOTAL: [37.8 MB]

Starting iterations...
Iteration 119: max relative diff=1.085561, 5.02 sec so far
Iteration 238: max relative diff=0.104682, 10.04 sec so far
Iteration 356: max relative diff=0.043556, 15.06 sec so far
Iteration 473: max relative diff=0.023273, 20.07 sec so far
Iteration 592: max relative diff=0.013625, 25.11 sec so far
Iteration 711: max relative diff=0.008483, 30.12 sec so far
Iteration 830: max relative diff=0.005557, 35.13 sec so far
Iteration 946: max relative diff=0.003720, 40.16 sec so far
Iteration 1065: max relative diff=0.002515, 45.17 sec so far
Iteration 1185: max relative diff=0.001723, 50.22 sec so far
Iteration 1304: max relative diff=0.001205, 55.26 sec so far
Iteration 1420: max relative diff=0.000845, 60.27 sec so far
Iteration 1536: max relative diff=0.000598, 65.31 sec so far
Iteration 1650: max relative diff=0.000428, 70.32 sec so far
Iteration 1763: max relative diff=0.000308, 75.35 sec so far
Iteration 1877: max relative diff=0.000221, 80.38 sec so far
Iteration 1991: max relative diff=0.000159, 85.42 sec so far
Iteration 2105: max relative diff=0.000115, 90.45 sec so far
Iteration 2220: max relative diff=0.000082, 95.49 sec so far
Iteration 2335: max relative diff=0.000059, 100.54 sec so far
Iteration 2452: max relative diff=0.000042, 105.59 sec so far
Iteration 2567: max relative diff=0.000030, 110.62 sec so far
Iteration 2682: max relative diff=0.000022, 115.65 sec so far
Iteration 2797: max relative diff=0.000016, 120.69 sec so far
Iteration 2912: max relative diff=0.000011, 125.70 sec so far
Iteration 3028: max relative diff=0.000008, 130.73 sec so far
Iteration 3141: max relative diff=0.000006, 135.76 sec so far
Iteration 3260: max relative diff=0.000004, 140.79 sec so far
Iteration 3379: max relative diff=0.000003, 145.80 sec so far
Iteration 3498: max relative diff=0.000002, 150.81 sec so far
Iteration 3618: max relative diff=0.000001, 155.85 sec so far
Iteration 3738: max relative diff=0.000001, 160.89 sec so far

Iterative method: 3759 iterations in 161.86 seconds (average 0.043038, setup 0.08)

Value in the initial state: 0.36362423396240773

Time for model checking: 182.757 seconds.

Result: 0.36362423396240773 (+/- 3.607106234271578E-6 estimated; rel err 9.91987303751732E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_consensus.6-2_rep5.log

```
Command(s):
../bin/prism  models/consensus.6-2/model.prism models/consensus.6-2/property.props
Wallclock time: 172.746 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:38:19 GMT+01:00 2026
Hostname: r23m0058.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.6-2/model.prism models/consensus.6-2/property.props

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Parsing properties file "models/consensus.6-2/property.props"...

1 property:
(1) "disagree": Pmax=? [ F "finished"&!"agree" ]

---------------------------------------------------------------------

Model checking: "disagree": Pmax=? [ F "finished"&!"agree" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 149 iterations in 0.05 seconds (average 0.000336, setup 0.00)

Time for model construction: 0.101 seconds.

Type:        MDP
States:      1258240 (1 initial)
Transitions: 6236736

Transition matrix: 7075 nodes (3 terminal), 6236736 minterms, vars: 24r/24c/6nd

Prob0A: 115 iterations in 0.47 seconds (average 0.004087, setup 0.00)

Prob1E: 1925 iterations in 13.47 seconds (average 0.006997, setup 0.00)

yes = 583956, no = 27270, maybe = 647014

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=6, levels=24, nodes=27117] [1.2 MB]
Adding sparse bits... [levels=14-15, num=958, compact=6/6] [5.4 MB]
Creating vector for yes... [dist=2, compact] [2.4 MB]
Allocating iteration vectors... [3 x 9.6 MB]
TOTAL: [37.8 MB]

Starting iterations...
Iteration 121: max relative diff=0.992552, 5.02 sec so far
Iteration 241: max relative diff=0.100651, 10.04 sec so far
Iteration 361: max relative diff=0.042013, 15.06 sec so far
Iteration 481: max relative diff=0.022296, 20.07 sec so far
Iteration 601: max relative diff=0.013142, 25.11 sec so far
Iteration 720: max relative diff=0.008218, 30.16 sec so far
Iteration 841: max relative diff=0.005329, 35.20 sec so far
Iteration 961: max relative diff=0.003545, 40.23 sec so far
Iteration 1081: max relative diff=0.002401, 45.24 sec so far
Iteration 1201: max relative diff=0.001647, 50.25 sec so far
Iteration 1322: max relative diff=0.001140, 55.29 sec so far
Iteration 1442: max relative diff=0.000795, 60.31 sec so far
Iteration 1562: max relative diff=0.000557, 65.32 sec so far
Iteration 1683: max relative diff=0.000387, 70.37 sec so far
Iteration 1803: max relative diff=0.000273, 75.38 sec so far
Iteration 1923: max relative diff=0.000193, 80.39 sec so far
Iteration 2043: max relative diff=0.000136, 85.40 sec so far
Iteration 2162: max relative diff=0.000097, 90.44 sec so far
Iteration 2282: max relative diff=0.000069, 95.47 sec so far
Iteration 2402: max relative diff=0.000049, 100.49 sec so far
Iteration 2522: max relative diff=0.000035, 105.50 sec so far
Iteration 2642: max relative diff=0.000025, 110.51 sec so far
Iteration 2762: max relative diff=0.000017, 115.53 sec so far
Iteration 2882: max relative diff=0.000012, 120.55 sec so far
Iteration 3003: max relative diff=0.000009, 125.60 sec so far
Iteration 3124: max relative diff=0.000006, 130.62 sec so far
Iteration 3244: max relative diff=0.000004, 135.64 sec so far
Iteration 3364: max relative diff=0.000003, 140.65 sec so far
Iteration 3484: max relative diff=0.000002, 145.66 sec so far
Iteration 3603: max relative diff=0.000002, 150.69 sec so far
Iteration 3723: max relative diff=0.000001, 155.70 sec so far

Iterative method: 3759 iterations in 157.28 seconds (average 0.041820, setup 0.08)

Value in the initial state: 0.36362423396240773

Time for model checking: 171.589 seconds.

Result: 0.36362423396240773 (+/- 3.607106234271578E-6 estimated; rel err 9.91987303751732E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

