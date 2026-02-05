# Log files for prism_from-prism_check_default on model [polling.18-16](../../models/polling.18-16)

Parsed values: `[0.063, 0.043, 0.067, 0.036, 0.055]`



### Log file: prism_from-prism_check_default_polling.18-16_rep1.log

```
Command(s):
../bin/prism  models/polling.18-16/model.prism models/polling.18-16/property.props
Wallclock time: 429.351 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:20:15 GMT+01:00 2026
Hostname: r23m0071.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/polling.18-16/model.prism models/polling.18-16/property.props

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Parsing properties file "models/polling.18-16/property.props"...

1 property:
(1) "s1_before_s2": P=? [ !"serve_s2" U "serve_s1" ]

---------------------------------------------------------------------

Model checking: "s1_before_s2": P=? [ !"serve_s2" U "serve_s1" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 37 iterations in 0.05 seconds (average 0.001351, setup 0.00)

Time for model construction: 0.063 seconds.

Type:        CTMC
States:      7077888 (1 initial)
Transitions: 69599232

Rate matrix: 2745 nodes (4 terminal), 69599232 minterms, vars: 24r/24c

Diagonals vector: 1540 nodes (38 terminal), 7077888 minterms
Embedded Markov chain: 17929 nodes (72 terminal), 69599232 minterms

Prob0: 36 iterations in 0.01 seconds (average 0.000278, setup 0.00)

Prob1: 35 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 3407872, no = 262144, maybe = 3407872

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=24, nodes=16351] [766.5 KB]
Adding explicit sparse matrices... [levels=8, num=457, compact] [498.8 KB]
Creating vector for diagonals... [dist=1, compact] [13.5 MB]
Creating vector for RHS... [dist=2, compact] [13.5 MB]
Allocating iteration vectors... [2 x 54.0 MB]
TOTAL: [136.2 MB]

Starting iterations...
Iteration 57: max relative diff=0.027473, 5.04 sec so far
Iteration 116: max relative diff=0.011008, 10.13 sec so far
Iteration 174: max relative diff=0.006498, 15.21 sec so far
Iteration 233: max relative diff=0.004425, 20.29 sec so far
Iteration 291: max relative diff=0.003281, 25.30 sec so far
Iteration 348: max relative diff=0.002562, 30.37 sec so far
Iteration 407: max relative diff=0.002050, 35.45 sec so far
Iteration 466: max relative diff=0.001680, 40.53 sec so far
Iteration 523: max relative diff=0.001410, 45.54 sec so far
Iteration 582: max relative diff=0.001193, 50.57 sec so far
Iteration 640: max relative diff=0.001023, 55.59 sec so far
Iteration 698: max relative diff=0.000886, 60.63 sec so far
Iteration 755: max relative diff=0.000775, 65.71 sec so far
Iteration 813: max relative diff=0.000681, 70.72 sec so far
Iteration 871: max relative diff=0.000601, 75.74 sec so far
Iteration 929: max relative diff=0.000532, 80.75 sec so far
Iteration 987: max relative diff=0.000474, 85.76 sec so far
Iteration 1045: max relative diff=0.000422, 90.78 sec so far
Iteration 1102: max relative diff=0.000379, 95.84 sec so far
Iteration 1160: max relative diff=0.000340, 100.87 sec so far
Iteration 1217: max relative diff=0.000306, 105.93 sec so far
Iteration 1275: max relative diff=0.000276, 110.95 sec so far
Iteration 1333: max relative diff=0.000249, 116.01 sec so far
Iteration 1391: max relative diff=0.000225, 121.04 sec so far
Iteration 1449: max relative diff=0.000203, 126.07 sec so far
Iteration 1505: max relative diff=0.000185, 131.08 sec so far
Iteration 1562: max relative diff=0.000168, 136.11 sec so far
Iteration 1619: max relative diff=0.000153, 141.12 sec so far
Iteration 1677: max relative diff=0.000139, 146.21 sec so far
Iteration 1734: max relative diff=0.000126, 151.22 sec so far
Iteration 1791: max relative diff=0.000115, 156.25 sec so far
Iteration 1849: max relative diff=0.000105, 161.34 sec so far
Iteration 1906: max relative diff=0.000095, 166.42 sec so far
Iteration 1964: max relative diff=0.000087, 171.51 sec so far
Iteration 2021: max relative diff=0.000079, 176.54 sec so far
Iteration 2078: max relative diff=0.000073, 181.58 sec so far
Iteration 2135: max relative diff=0.000066, 186.60 sec so far
Iteration 2193: max relative diff=0.000060, 191.68 sec so far
Iteration 2251: max relative diff=0.000055, 196.75 sec so far
Iteration 2308: max relative diff=0.000050, 201.79 sec so far
Iteration 2365: max relative diff=0.000046, 206.82 sec so far
Iteration 2423: max relative diff=0.000042, 211.91 sec so far
Iteration 2481: max relative diff=0.000039, 217.00 sec so far
Iteration 2539: max relative diff=0.000035, 222.08 sec so far
Iteration 2596: max relative diff=0.000032, 227.10 sec so far
Iteration 2654: max relative diff=0.000030, 232.18 sec so far
Iteration 2712: max relative diff=0.000027, 237.26 sec so far
Iteration 2770: max relative diff=0.000025, 242.33 sec so far
Iteration 2828: max relative diff=0.000023, 247.42 sec so far
Iteration 2886: max relative diff=0.000021, 252.51 sec so far
Iteration 2943: max relative diff=0.000019, 257.53 sec so far
Iteration 3001: max relative diff=0.000017, 262.59 sec so far
Iteration 3059: max relative diff=0.000016, 267.64 sec so far
Iteration 3117: max relative diff=0.000015, 272.71 sec so far
Iteration 3175: max relative diff=0.000013, 277.78 sec so far
Iteration 3233: max relative diff=0.000012, 282.85 sec so far
Iteration 3290: max relative diff=0.000011, 287.86 sec so far
Iteration 3347: max relative diff=0.000010, 292.88 sec so far
Iteration 3405: max relative diff=0.000009, 297.97 sec so far
Iteration 3463: max relative diff=0.000009, 303.06 sec so far
Iteration 3521: max relative diff=0.000008, 308.13 sec so far
Iteration 3578: max relative diff=0.000007, 313.15 sec so far
Iteration 3635: max relative diff=0.000007, 318.16 sec so far
Iteration 3692: max relative diff=0.000006, 323.18 sec so far
Iteration 3750: max relative diff=0.000006, 328.27 sec so far
Iteration 3808: max relative diff=0.000005, 333.32 sec so far
Iteration 3866: max relative diff=0.000005, 338.35 sec so far
Iteration 3924: max relative diff=0.000004, 343.40 sec so far
Iteration 3981: max relative diff=0.000004, 348.47 sec so far
Iteration 4039: max relative diff=0.000004, 353.54 sec so far
Iteration 4098: max relative diff=0.000003, 358.56 sec so far
Iteration 4156: max relative diff=0.000003, 363.59 sec so far
Iteration 4214: max relative diff=0.000003, 368.61 sec so far
Iteration 4272: max relative diff=0.000003, 373.62 sec so far
Iteration 4329: max relative diff=0.000002, 378.64 sec so far
Iteration 4389: max relative diff=0.000002, 383.70 sec so far
Iteration 4447: max relative diff=0.000002, 388.72 sec so far
Iteration 4505: max relative diff=0.000002, 393.78 sec so far
Iteration 4563: max relative diff=0.000002, 398.83 sec so far
Iteration 4620: max relative diff=0.000001, 403.85 sec so far
Iteration 4677: max relative diff=0.000001, 408.86 sec so far
Iteration 4734: max relative diff=0.000001, 413.91 sec so far
Iteration 4791: max relative diff=0.000001, 418.93 sec so far
Iteration 4848: max relative diff=0.000001, 423.94 sec so far

Jacobi: 4880 iterations in 426.96 seconds (average 0.087449, setup 0.21)

Value in the initial state: 0.5386630172446204

Time for model checking: 428.638 seconds.

Result: 0.5386630172446204 (+/- 5.381007559705678E-6 estimated; rel err 9.989561910581338E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_polling.18-16_rep2.log

```
Command(s):
../bin/prism  models/polling.18-16/model.prism models/polling.18-16/property.props
Wallclock time: 412.521 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:07:31 GMT+01:00 2026
Hostname: n23m0052.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/polling.18-16/model.prism models/polling.18-16/property.props

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Parsing properties file "models/polling.18-16/property.props"...

1 property:
(1) "s1_before_s2": P=? [ !"serve_s2" U "serve_s1" ]

---------------------------------------------------------------------

Model checking: "s1_before_s2": P=? [ !"serve_s2" U "serve_s1" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 37 iterations in 0.05 seconds (average 0.001351, setup 0.00)

Time for model construction: 0.043 seconds.

Type:        CTMC
States:      7077888 (1 initial)
Transitions: 69599232

Rate matrix: 2745 nodes (4 terminal), 69599232 minterms, vars: 24r/24c

Diagonals vector: 1540 nodes (38 terminal), 7077888 minterms
Embedded Markov chain: 17929 nodes (72 terminal), 69599232 minterms

Prob0: 36 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Prob1: 35 iterations in 0.02 seconds (average 0.000571, setup 0.00)

yes = 3407872, no = 262144, maybe = 3407872

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=24, nodes=16351] [766.5 KB]
Adding explicit sparse matrices... [levels=8, num=457, compact] [498.8 KB]
Creating vector for diagonals... [dist=1, compact] [13.5 MB]
Creating vector for RHS... [dist=2, compact] [13.5 MB]
Allocating iteration vectors... [2 x 54.0 MB]
TOTAL: [136.2 MB]

Starting iterations...
Iteration 60: max relative diff=0.025756, 5.05 sec so far
Iteration 120: max relative diff=0.010534, 10.08 sec so far
Iteration 180: max relative diff=0.006216, 15.10 sec so far
Iteration 240: max relative diff=0.004254, 20.15 sec so far
Iteration 300: max relative diff=0.003147, 25.18 sec so far
Iteration 359: max relative diff=0.002452, 30.25 sec so far
Iteration 419: max relative diff=0.001965, 35.30 sec so far
Iteration 479: max relative diff=0.001612, 40.37 sec so far
Iteration 539: max relative diff=0.001346, 45.40 sec so far
Iteration 599: max relative diff=0.001139, 50.43 sec so far
Iteration 659: max relative diff=0.000975, 55.46 sec so far
Iteration 719: max relative diff=0.000842, 60.50 sec so far
Iteration 779: max relative diff=0.000734, 65.52 sec so far
Iteration 839: max relative diff=0.000643, 70.56 sec so far
Iteration 899: max relative diff=0.000566, 75.60 sec so far
Iteration 959: max relative diff=0.000501, 80.63 sec so far
Iteration 1019: max relative diff=0.000444, 85.67 sec so far
Iteration 1078: max relative diff=0.000396, 90.73 sec so far
Iteration 1138: max relative diff=0.000354, 95.78 sec so far
Iteration 1198: max relative diff=0.000317, 100.85 sec so far
Iteration 1258: max relative diff=0.000284, 105.89 sec so far
Iteration 1318: max relative diff=0.000255, 110.91 sec so far
Iteration 1378: max relative diff=0.000230, 115.95 sec so far
Iteration 1438: max relative diff=0.000207, 120.99 sec so far
Iteration 1498: max relative diff=0.000187, 126.02 sec so far
Iteration 1558: max relative diff=0.000169, 131.04 sec so far
Iteration 1618: max relative diff=0.000153, 136.08 sec so far
Iteration 1678: max relative diff=0.000138, 141.10 sec so far
Iteration 1738: max relative diff=0.000125, 146.14 sec so far
Iteration 1797: max relative diff=0.000114, 151.20 sec so far
Iteration 1857: max relative diff=0.000103, 156.25 sec so far
Iteration 1917: max relative diff=0.000094, 161.30 sec so far
Iteration 1977: max relative diff=0.000085, 166.33 sec so far
Iteration 2037: max relative diff=0.000077, 171.36 sec so far
Iteration 2097: max relative diff=0.000070, 176.39 sec so far
Iteration 2157: max relative diff=0.000064, 181.42 sec so far
Iteration 2217: max relative diff=0.000058, 186.46 sec so far
Iteration 2277: max relative diff=0.000053, 191.48 sec so far
Iteration 2337: max relative diff=0.000048, 196.51 sec so far
Iteration 2397: max relative diff=0.000044, 201.54 sec so far
Iteration 2457: max relative diff=0.000040, 206.57 sec so far
Iteration 2516: max relative diff=0.000037, 211.66 sec so far
Iteration 2576: max relative diff=0.000033, 216.71 sec so far
Iteration 2636: max relative diff=0.000030, 221.77 sec so far
Iteration 2696: max relative diff=0.000028, 226.80 sec so far
Iteration 2756: max relative diff=0.000025, 231.83 sec so far
Iteration 2816: max relative diff=0.000023, 236.86 sec so far
Iteration 2876: max relative diff=0.000021, 241.91 sec so far
Iteration 2936: max relative diff=0.000019, 246.94 sec so far
Iteration 2996: max relative diff=0.000017, 251.96 sec so far
Iteration 3056: max relative diff=0.000016, 256.99 sec so far
Iteration 3116: max relative diff=0.000015, 262.03 sec so far
Iteration 3176: max relative diff=0.000013, 267.07 sec so far
Iteration 3236: max relative diff=0.000012, 272.13 sec so far
Iteration 3296: max relative diff=0.000011, 277.19 sec so far
Iteration 3355: max relative diff=0.000010, 282.24 sec so far
Iteration 3415: max relative diff=0.000009, 287.28 sec so far
Iteration 3475: max relative diff=0.000008, 292.31 sec so far
Iteration 3535: max relative diff=0.000008, 297.35 sec so far
Iteration 3595: max relative diff=0.000007, 302.40 sec so far
Iteration 3655: max relative diff=0.000006, 307.45 sec so far
Iteration 3715: max relative diff=0.000006, 312.48 sec so far
Iteration 3775: max relative diff=0.000005, 317.52 sec so far
Iteration 3835: max relative diff=0.000005, 322.56 sec so far
Iteration 3895: max relative diff=0.000004, 327.61 sec so far
Iteration 3954: max relative diff=0.000004, 332.67 sec so far
Iteration 4014: max relative diff=0.000004, 337.72 sec so far
Iteration 4074: max relative diff=0.000003, 342.77 sec so far
Iteration 4134: max relative diff=0.000003, 347.81 sec so far
Iteration 4194: max relative diff=0.000003, 352.83 sec so far
Iteration 4254: max relative diff=0.000003, 357.87 sec so far
Iteration 4314: max relative diff=0.000002, 362.90 sec so far
Iteration 4374: max relative diff=0.000002, 367.93 sec so far
Iteration 4434: max relative diff=0.000002, 372.96 sec so far
Iteration 4494: max relative diff=0.000002, 377.99 sec so far
Iteration 4554: max relative diff=0.000002, 383.02 sec so far
Iteration 4613: max relative diff=0.000001, 388.03 sec so far
Iteration 4673: max relative diff=0.000001, 393.10 sec so far
Iteration 4733: max relative diff=0.000001, 398.17 sec so far
Iteration 4793: max relative diff=0.000001, 403.19 sec so far
Iteration 4853: max relative diff=0.000001, 408.21 sec so far

Jacobi: 4880 iterations in 410.67 seconds (average 0.084113, setup 0.20)

Value in the initial state: 0.5386630172446204

Time for model checking: 411.877 seconds.

Result: 0.5386630172446204 (+/- 5.381007559705678E-6 estimated; rel err 9.989561910581338E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_polling.18-16_rep3.log

```
Command(s):
../bin/prism  models/polling.18-16/model.prism models/polling.18-16/property.props
Wallclock time: 476.834 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:22 GMT+01:00 2026
Hostname: n23m0104.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/polling.18-16/model.prism models/polling.18-16/property.props

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Parsing properties file "models/polling.18-16/property.props"...

1 property:
(1) "s1_before_s2": P=? [ !"serve_s2" U "serve_s1" ]

---------------------------------------------------------------------

Model checking: "s1_before_s2": P=? [ !"serve_s2" U "serve_s1" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 37 iterations in 0.06 seconds (average 0.001622, setup 0.00)

Time for model construction: 0.067 seconds.

Type:        CTMC
States:      7077888 (1 initial)
Transitions: 69599232

Rate matrix: 2745 nodes (4 terminal), 69599232 minterms, vars: 24r/24c

Diagonals vector: 1540 nodes (38 terminal), 7077888 minterms
Embedded Markov chain: 17929 nodes (72 terminal), 69599232 minterms

Prob0: 36 iterations in 0.01 seconds (average 0.000278, setup 0.00)

Prob1: 35 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 3407872, no = 262144, maybe = 3407872

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=24, nodes=16351] [766.5 KB]
Adding explicit sparse matrices... [levels=8, num=457, compact] [498.8 KB]
Creating vector for diagonals... [dist=1, compact] [13.5 MB]
Creating vector for RHS... [dist=2, compact] [13.5 MB]
Allocating iteration vectors... [2 x 54.0 MB]
TOTAL: [136.2 MB]

Starting iterations...
Iteration 53: max relative diff=0.030119, 5.01 sec so far
Iteration 105: max relative diff=0.012527, 10.07 sec so far
Iteration 156: max relative diff=0.007491, 15.14 sec so far
Iteration 205: max relative diff=0.005241, 20.16 sec so far
Iteration 254: max relative diff=0.003943, 25.19 sec so far
Iteration 307: max relative diff=0.003049, 30.20 sec so far
Iteration 360: max relative diff=0.002442, 35.30 sec so far
Iteration 412: max relative diff=0.002014, 40.40 sec so far
Iteration 462: max relative diff=0.001701, 45.49 sec so far
Iteration 512: max relative diff=0.001457, 50.57 sec so far
Iteration 563: max relative diff=0.001257, 55.59 sec so far
Iteration 616: max relative diff=0.001089, 60.63 sec so far
Iteration 670: max relative diff=0.000949, 65.71 sec so far
Iteration 721: max relative diff=0.000838, 70.77 sec so far
Iteration 772: max relative diff=0.000745, 75.85 sec so far
Iteration 824: max relative diff=0.000664, 80.94 sec so far
Iteration 877: max relative diff=0.000593, 85.99 sec so far
Iteration 929: max relative diff=0.000532, 91.05 sec so far
Iteration 983: max relative diff=0.000477, 96.11 sec so far
Iteration 1035: max relative diff=0.000431, 101.18 sec so far
Iteration 1086: max relative diff=0.000390, 106.26 sec so far
Iteration 1138: max relative diff=0.000354, 111.31 sec so far
Iteration 1190: max relative diff=0.000322, 116.35 sec so far
Iteration 1243: max relative diff=0.000292, 121.36 sec so far
Iteration 1296: max relative diff=0.000266, 126.44 sec so far
Iteration 1346: max relative diff=0.000243, 131.48 sec so far
Iteration 1397: max relative diff=0.000222, 136.54 sec so far
Iteration 1451: max relative diff=0.000203, 141.59 sec so far
Iteration 1504: max relative diff=0.000185, 146.65 sec so far
Iteration 1556: max relative diff=0.000169, 151.67 sec so far
Iteration 1606: max relative diff=0.000156, 156.71 sec so far
Iteration 1657: max relative diff=0.000143, 161.75 sec so far
Iteration 1711: max relative diff=0.000131, 166.83 sec so far
Iteration 1764: max relative diff=0.000120, 171.87 sec so far
Iteration 1815: max relative diff=0.000111, 176.93 sec so far
Iteration 1864: max relative diff=0.000102, 181.98 sec so far
Iteration 1917: max relative diff=0.000094, 187.07 sec so far
Iteration 1971: max relative diff=0.000086, 192.09 sec so far
Iteration 2025: max relative diff=0.000079, 197.15 sec so far
Iteration 2074: max relative diff=0.000073, 202.17 sec so far
Iteration 2125: max relative diff=0.000067, 207.23 sec so far
Iteration 2179: max relative diff=0.000062, 212.31 sec so far
Iteration 2232: max relative diff=0.000057, 217.32 sec so far
Iteration 2282: max relative diff=0.000053, 222.33 sec so far
Iteration 2333: max relative diff=0.000049, 227.41 sec so far
Iteration 2385: max relative diff=0.000045, 232.42 sec so far
Iteration 2438: max relative diff=0.000041, 237.43 sec so far
Iteration 2490: max relative diff=0.000038, 242.51 sec so far
Iteration 2542: max relative diff=0.000035, 247.60 sec so far
Iteration 2596: max relative diff=0.000032, 252.69 sec so far
Iteration 2649: max relative diff=0.000030, 257.76 sec so far
Iteration 2698: max relative diff=0.000028, 262.77 sec so far
Iteration 2749: max relative diff=0.000026, 267.84 sec so far
Iteration 2803: max relative diff=0.000023, 272.94 sec so far
Iteration 2856: max relative diff=0.000022, 277.95 sec so far
Iteration 2906: max relative diff=0.000020, 282.98 sec so far
Iteration 2958: max relative diff=0.000019, 288.05 sec so far
Iteration 3012: max relative diff=0.000017, 293.10 sec so far
Iteration 3065: max relative diff=0.000016, 298.11 sec so far
Iteration 3115: max relative diff=0.000015, 303.13 sec so far
Iteration 3168: max relative diff=0.000013, 308.18 sec so far
Iteration 3221: max relative diff=0.000012, 313.26 sec so far
Iteration 3272: max relative diff=0.000011, 318.36 sec so far
Iteration 3325: max relative diff=0.000011, 323.42 sec so far
Iteration 3379: max relative diff=0.000010, 328.48 sec so far
Iteration 3430: max relative diff=0.000009, 333.52 sec so far
Iteration 3482: max relative diff=0.000008, 338.58 sec so far
Iteration 3535: max relative diff=0.000008, 343.60 sec so far
Iteration 3587: max relative diff=0.000007, 348.64 sec so far
Iteration 3640: max relative diff=0.000007, 353.74 sec so far
Iteration 3693: max relative diff=0.000006, 358.82 sec so far
Iteration 3746: max relative diff=0.000006, 363.88 sec so far
Iteration 3799: max relative diff=0.000005, 368.94 sec so far
Iteration 3853: max relative diff=0.000005, 374.01 sec so far
Iteration 3906: max relative diff=0.000004, 379.05 sec so far
Iteration 3959: max relative diff=0.000004, 384.14 sec so far
Iteration 4011: max relative diff=0.000004, 389.20 sec so far
Iteration 4061: max relative diff=0.000003, 394.22 sec so far
Iteration 4111: max relative diff=0.000003, 399.23 sec so far
Iteration 4161: max relative diff=0.000003, 404.34 sec so far
Iteration 4213: max relative diff=0.000003, 409.39 sec so far
Iteration 4265: max relative diff=0.000003, 414.40 sec so far
Iteration 4320: max relative diff=0.000002, 419.47 sec so far
Iteration 4375: max relative diff=0.000002, 424.56 sec so far
Iteration 4428: max relative diff=0.000002, 429.66 sec so far
Iteration 4479: max relative diff=0.000002, 434.72 sec so far
Iteration 4532: max relative diff=0.000002, 439.79 sec so far
Iteration 4582: max relative diff=0.000002, 444.84 sec so far
Iteration 4632: max relative diff=0.000001, 449.90 sec so far
Iteration 4682: max relative diff=0.000001, 454.92 sec so far
Iteration 4735: max relative diff=0.000001, 459.99 sec so far
Iteration 4788: max relative diff=0.000001, 465.04 sec so far
Iteration 4841: max relative diff=0.000001, 470.06 sec so far

Jacobi: 4880 iterations in 474.04 seconds (average 0.097092, setup 0.23)

Value in the initial state: 0.5386630172446204

Time for model checking: 475.985 seconds.

Result: 0.5386630172446204 (+/- 5.381007559705678E-6 estimated; rel err 9.989561910581338E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_polling.18-16_rep4.log

```
Command(s):
../bin/prism  models/polling.18-16/model.prism models/polling.18-16/property.props
Wallclock time: 393.751 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:10:14 GMT+01:00 2026
Hostname: n23m0028.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/polling.18-16/model.prism models/polling.18-16/property.props

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Parsing properties file "models/polling.18-16/property.props"...

1 property:
(1) "s1_before_s2": P=? [ !"serve_s2" U "serve_s1" ]

---------------------------------------------------------------------

Model checking: "s1_before_s2": P=? [ !"serve_s2" U "serve_s1" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 37 iterations in 0.03 seconds (average 0.000811, setup 0.00)

Time for model construction: 0.036 seconds.

Type:        CTMC
States:      7077888 (1 initial)
Transitions: 69599232

Rate matrix: 2745 nodes (4 terminal), 69599232 minterms, vars: 24r/24c

Diagonals vector: 1540 nodes (38 terminal), 7077888 minterms
Embedded Markov chain: 17929 nodes (72 terminal), 69599232 minterms

Prob0: 36 iterations in 0.01 seconds (average 0.000278, setup 0.00)

Prob1: 35 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 3407872, no = 262144, maybe = 3407872

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=24, nodes=16351] [766.5 KB]
Adding explicit sparse matrices... [levels=8, num=457, compact] [498.8 KB]
Creating vector for diagonals... [dist=1, compact] [13.5 MB]
Creating vector for RHS... [dist=2, compact] [13.5 MB]
Allocating iteration vectors... [2 x 54.0 MB]
TOTAL: [136.2 MB]

Starting iterations...
Iteration 63: max relative diff=0.024211, 5.01 sec so far
Iteration 127: max relative diff=0.009785, 10.09 sec so far
Iteration 191: max relative diff=0.005752, 15.17 sec so far
Iteration 255: max relative diff=0.003923, 20.25 sec so far
Iteration 319: max relative diff=0.002892, 25.32 sec so far
Iteration 383: max relative diff=0.002237, 30.39 sec so far
Iteration 447: max relative diff=0.001787, 35.47 sec so far
Iteration 511: max relative diff=0.001461, 40.54 sec so far
Iteration 573: max relative diff=0.001223, 45.57 sec so far
Iteration 636: max relative diff=0.001034, 50.63 sec so far
Iteration 699: max relative diff=0.000883, 55.66 sec so far
Iteration 763: max relative diff=0.000761, 60.74 sec so far
Iteration 826: max relative diff=0.000662, 65.75 sec so far
Iteration 890: max relative diff=0.000577, 70.83 sec so far
Iteration 954: max relative diff=0.000506, 75.90 sec so far
Iteration 1018: max relative diff=0.000445, 80.98 sec so far
Iteration 1081: max relative diff=0.000394, 85.99 sec so far
Iteration 1144: max relative diff=0.000350, 91.00 sec so far
Iteration 1207: max relative diff=0.000312, 96.01 sec so far
Iteration 1271: max relative diff=0.000278, 101.09 sec so far
Iteration 1333: max relative diff=0.000249, 106.17 sec so far
Iteration 1396: max relative diff=0.000223, 111.19 sec so far
Iteration 1459: max relative diff=0.000200, 116.21 sec so far
Iteration 1523: max relative diff=0.000179, 121.28 sec so far
Iteration 1586: max relative diff=0.000161, 126.33 sec so far
Iteration 1649: max relative diff=0.000145, 131.35 sec so far
Iteration 1712: max relative diff=0.000131, 136.40 sec so far
Iteration 1775: max relative diff=0.000118, 141.43 sec so far
Iteration 1839: max relative diff=0.000106, 146.49 sec so far
Iteration 1902: max relative diff=0.000096, 151.53 sec so far
Iteration 1965: max relative diff=0.000087, 156.56 sec so far
Iteration 2029: max relative diff=0.000078, 161.63 sec so far
Iteration 2091: max relative diff=0.000071, 166.70 sec so far
Iteration 2155: max relative diff=0.000064, 171.78 sec so far
Iteration 2218: max relative diff=0.000058, 176.79 sec so far
Iteration 2281: max relative diff=0.000053, 181.83 sec so far
Iteration 2344: max relative diff=0.000048, 186.85 sec so far
Iteration 2407: max relative diff=0.000043, 191.86 sec so far
Iteration 2471: max relative diff=0.000039, 196.94 sec so far
Iteration 2535: max relative diff=0.000035, 202.02 sec so far
Iteration 2599: max relative diff=0.000032, 207.10 sec so far
Iteration 2662: max relative diff=0.000029, 212.14 sec so far
Iteration 2726: max relative diff=0.000026, 217.22 sec so far
Iteration 2790: max relative diff=0.000024, 222.29 sec so far
Iteration 2852: max relative diff=0.000022, 227.36 sec so far
Iteration 2915: max relative diff=0.000020, 232.39 sec so far
Iteration 2978: max relative diff=0.000018, 237.46 sec so far
Iteration 3041: max relative diff=0.000016, 242.47 sec so far
Iteration 3104: max relative diff=0.000015, 247.54 sec so far
Iteration 3167: max relative diff=0.000013, 252.57 sec so far
Iteration 3230: max relative diff=0.000012, 257.60 sec so far
Iteration 3293: max relative diff=0.000011, 262.65 sec so far
Iteration 3356: max relative diff=0.000010, 267.71 sec so far
Iteration 3419: max relative diff=0.000009, 272.78 sec so far
Iteration 3481: max relative diff=0.000008, 277.82 sec so far
Iteration 3543: max relative diff=0.000008, 282.88 sec so far
Iteration 3603: max relative diff=0.000007, 287.93 sec so far
Iteration 3665: max relative diff=0.000006, 292.98 sec so far
Iteration 3727: max relative diff=0.000006, 298.04 sec so far
Iteration 3789: max relative diff=0.000005, 303.06 sec so far
Iteration 3851: max relative diff=0.000005, 308.09 sec so far
Iteration 3913: max relative diff=0.000004, 313.12 sec so far
Iteration 3975: max relative diff=0.000004, 318.15 sec so far
Iteration 4037: max relative diff=0.000004, 323.19 sec so far
Iteration 4099: max relative diff=0.000003, 328.22 sec so far
Iteration 4161: max relative diff=0.000003, 333.26 sec so far
Iteration 4223: max relative diff=0.000003, 338.29 sec so far
Iteration 4285: max relative diff=0.000002, 343.31 sec so far
Iteration 4345: max relative diff=0.000002, 348.33 sec so far
Iteration 4407: max relative diff=0.000002, 353.38 sec so far
Iteration 4469: max relative diff=0.000002, 358.42 sec so far
Iteration 4531: max relative diff=0.000002, 363.44 sec so far
Iteration 4593: max relative diff=0.000002, 368.47 sec so far
Iteration 4655: max relative diff=0.000001, 373.49 sec so far
Iteration 4717: max relative diff=0.000001, 378.52 sec so far
Iteration 4779: max relative diff=0.000001, 383.55 sec so far
Iteration 4841: max relative diff=0.000001, 388.57 sec so far

Jacobi: 4880 iterations in 391.93 seconds (average 0.080273, setup 0.20)

Value in the initial state: 0.5386630172446204

Time for model checking: 393.192 seconds.

Result: 0.5386630172446204 (+/- 5.381007559705678E-6 estimated; rel err 9.989561910581338E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_polling.18-16_rep5.log

```
Command(s):
../bin/prism  models/polling.18-16/model.prism models/polling.18-16/property.props
Wallclock time: 397.954 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:03 GMT+01:00 2026
Hostname: r23m0099.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/polling.18-16/model.prism models/polling.18-16/property.props

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Parsing properties file "models/polling.18-16/property.props"...

1 property:
(1) "s1_before_s2": P=? [ !"serve_s2" U "serve_s1" ]

---------------------------------------------------------------------

Model checking: "s1_before_s2": P=? [ !"serve_s2" U "serve_s1" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 37 iterations in 0.05 seconds (average 0.001351, setup 0.00)

Time for model construction: 0.055 seconds.

Type:        CTMC
States:      7077888 (1 initial)
Transitions: 69599232

Rate matrix: 2745 nodes (4 terminal), 69599232 minterms, vars: 24r/24c

Diagonals vector: 1540 nodes (38 terminal), 7077888 minterms
Embedded Markov chain: 17929 nodes (72 terminal), 69599232 minterms

Prob0: 36 iterations in 0.01 seconds (average 0.000278, setup 0.00)

Prob1: 35 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 3407872, no = 262144, maybe = 3407872

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=24, nodes=16351] [766.5 KB]
Adding explicit sparse matrices... [levels=8, num=457, compact] [498.8 KB]
Creating vector for diagonals... [dist=1, compact] [13.5 MB]
Creating vector for RHS... [dist=2, compact] [13.5 MB]
Allocating iteration vectors... [2 x 54.0 MB]
TOTAL: [136.2 MB]

Starting iterations...
Iteration 62: max relative diff=0.024709, 5.05 sec so far
Iteration 124: max relative diff=0.010094, 10.06 sec so far
Iteration 187: max relative diff=0.005913, 15.14 sec so far
Iteration 250: max relative diff=0.004028, 20.22 sec so far
Iteration 313: max relative diff=0.002969, 25.28 sec so far
Iteration 376: max relative diff=0.002296, 30.36 sec so far
Iteration 439: max relative diff=0.001835, 35.43 sec so far
Iteration 502: max relative diff=0.001501, 40.50 sec so far
Iteration 565: max relative diff=0.001250, 45.58 sec so far
Iteration 628: max relative diff=0.001055, 50.65 sec so far
Iteration 691: max relative diff=0.000901, 55.72 sec so far
Iteration 753: max relative diff=0.000778, 60.77 sec so far
Iteration 815: max relative diff=0.000678, 65.80 sec so far
Iteration 878: max relative diff=0.000592, 70.87 sec so far
Iteration 941: max relative diff=0.000520, 75.95 sec so far
Iteration 1004: max relative diff=0.000458, 81.02 sec so far
Iteration 1067: max relative diff=0.000405, 86.09 sec so far
Iteration 1130: max relative diff=0.000359, 91.15 sec so far
Iteration 1193: max relative diff=0.000320, 96.23 sec so far
Iteration 1256: max relative diff=0.000285, 101.30 sec so far
Iteration 1319: max relative diff=0.000255, 106.37 sec so far
Iteration 1382: max relative diff=0.000228, 111.44 sec so far
Iteration 1444: max relative diff=0.000205, 116.47 sec so far
Iteration 1506: max relative diff=0.000184, 121.49 sec so far
Iteration 1568: max relative diff=0.000166, 126.52 sec so far
Iteration 1631: max relative diff=0.000150, 131.59 sec so far
Iteration 1694: max relative diff=0.000135, 136.66 sec so far
Iteration 1757: max relative diff=0.000121, 141.73 sec so far
Iteration 1820: max relative diff=0.000110, 146.79 sec so far
Iteration 1883: max relative diff=0.000099, 151.86 sec so far
Iteration 1946: max relative diff=0.000089, 156.94 sec so far
Iteration 2009: max relative diff=0.000081, 162.01 sec so far
Iteration 2072: max relative diff=0.000073, 167.08 sec so far
Iteration 2135: max relative diff=0.000066, 172.15 sec so far
Iteration 2197: max relative diff=0.000060, 177.19 sec so far
Iteration 2259: max relative diff=0.000055, 182.20 sec so far
Iteration 2321: max relative diff=0.000049, 187.22 sec so far
Iteration 2384: max relative diff=0.000045, 192.30 sec so far
Iteration 2447: max relative diff=0.000041, 197.37 sec so far
Iteration 2510: max relative diff=0.000037, 202.44 sec so far
Iteration 2573: max relative diff=0.000033, 207.50 sec so far
Iteration 2636: max relative diff=0.000030, 212.57 sec so far
Iteration 2699: max relative diff=0.000028, 217.65 sec so far
Iteration 2762: max relative diff=0.000025, 222.72 sec so far
Iteration 2825: max relative diff=0.000023, 227.79 sec so far
Iteration 2888: max relative diff=0.000021, 232.87 sec so far
Iteration 2950: max relative diff=0.000019, 237.91 sec so far
Iteration 3013: max relative diff=0.000017, 243.00 sec so far
Iteration 3075: max relative diff=0.000015, 248.01 sec so far
Iteration 3138: max relative diff=0.000014, 253.08 sec so far
Iteration 3201: max relative diff=0.000013, 258.15 sec so far
Iteration 3264: max relative diff=0.000012, 263.22 sec so far
Iteration 3327: max relative diff=0.000011, 268.30 sec so far
Iteration 3390: max relative diff=0.000010, 273.37 sec so far
Iteration 3453: max relative diff=0.000009, 278.44 sec so far
Iteration 3516: max relative diff=0.000008, 283.51 sec so far
Iteration 3579: max relative diff=0.000007, 288.58 sec so far
Iteration 3642: max relative diff=0.000007, 293.65 sec so far
Iteration 3704: max relative diff=0.000006, 298.71 sec so far
Iteration 3766: max relative diff=0.000005, 303.72 sec so far
Iteration 3828: max relative diff=0.000005, 308.74 sec so far
Iteration 3891: max relative diff=0.000004, 313.81 sec so far
Iteration 3954: max relative diff=0.000004, 318.88 sec so far
Iteration 4017: max relative diff=0.000004, 323.95 sec so far
Iteration 4080: max relative diff=0.000003, 329.02 sec so far
Iteration 4143: max relative diff=0.000003, 334.09 sec so far
Iteration 4206: max relative diff=0.000003, 339.16 sec so far
Iteration 4269: max relative diff=0.000003, 344.23 sec so far
Iteration 4332: max relative diff=0.000002, 349.30 sec so far
Iteration 4395: max relative diff=0.000002, 354.37 sec so far
Iteration 4457: max relative diff=0.000002, 359.43 sec so far
Iteration 4519: max relative diff=0.000002, 364.45 sec so far
Iteration 4581: max relative diff=0.000002, 369.46 sec so far
Iteration 4644: max relative diff=0.000001, 374.53 sec so far
Iteration 4707: max relative diff=0.000001, 379.60 sec so far
Iteration 4770: max relative diff=0.000001, 384.67 sec so far
Iteration 4833: max relative diff=0.000001, 389.74 sec so far

Jacobi: 4880 iterations in 393.74 seconds (average 0.080641, setup 0.21)

Value in the initial state: 0.5386630172446204

Time for model checking: 394.716 seconds.

Result: 0.5386630172446204 (+/- 5.381007559705678E-6 estimated; rel err 9.989561910581338E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

