# Log files for prism_from-prism_check_norewards on model [polling.18-16](../../models/polling.18-16)

Parsed values: `[424.178, 397.52, 453.139, 402.032, 522.846]`



### Log file: prism_from-prism_check_norewards_polling.18-16_rep1.log

```
Command(s):
../bin/prism  models/polling.18-16/model.prism models/polling.18-16/property.props
Wallclock time: 424.178 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:47:53 GMT+01:00 2026
Hostname: r23m0077.hpc.itc.rwth-aachen.de
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

Time for model construction: 0.039 seconds.

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
Iteration 62: max relative diff=0.024709, 5.08 sec so far
Iteration 123: max relative diff=0.010201, 10.14 sec so far
Iteration 184: max relative diff=0.006040, 15.16 sec so far
Iteration 246: max relative diff=0.004116, 20.25 sec so far
Iteration 308: max relative diff=0.003035, 25.31 sec so far
Iteration 368: max relative diff=0.002368, 30.35 sec so far
Iteration 429: max relative diff=0.001898, 35.37 sec so far
Iteration 490: max relative diff=0.001558, 40.38 sec so far
Iteration 551: max relative diff=0.001300, 45.41 sec so far
Iteration 612: max relative diff=0.001101, 50.43 sec so far
Iteration 673: max relative diff=0.000942, 55.44 sec so far
Iteration 734: max relative diff=0.000813, 60.52 sec so far
Iteration 792: max relative diff=0.000713, 65.60 sec so far
Iteration 850: max relative diff=0.000628, 70.67 sec so far
Iteration 907: max relative diff=0.000557, 75.72 sec so far
Iteration 963: max relative diff=0.000497, 80.75 sec so far
Iteration 1020: max relative diff=0.000444, 85.78 sec so far
Iteration 1077: max relative diff=0.000397, 90.81 sec so far
Iteration 1135: max relative diff=0.000356, 95.89 sec so far
Iteration 1192: max relative diff=0.000320, 100.97 sec so far
Iteration 1248: max relative diff=0.000289, 105.99 sec so far
Iteration 1304: max relative diff=0.000262, 111.00 sec so far
Iteration 1361: max relative diff=0.000237, 116.03 sec so far
Iteration 1419: max relative diff=0.000214, 121.12 sec so far
Iteration 1476: max relative diff=0.000194, 126.18 sec so far
Iteration 1533: max relative diff=0.000176, 131.27 sec so far
Iteration 1590: max relative diff=0.000160, 136.31 sec so far
Iteration 1647: max relative diff=0.000146, 141.39 sec so far
Iteration 1705: max relative diff=0.000132, 146.47 sec so far
Iteration 1762: max relative diff=0.000120, 151.49 sec so far
Iteration 1819: max relative diff=0.000110, 156.51 sec so far
Iteration 1876: max relative diff=0.000100, 161.52 sec so far
Iteration 1935: max relative diff=0.000091, 166.61 sec so far
Iteration 1993: max relative diff=0.000083, 171.62 sec so far
Iteration 2050: max relative diff=0.000076, 176.64 sec so far
Iteration 2108: max relative diff=0.000069, 181.70 sec so far
Iteration 2165: max relative diff=0.000063, 186.72 sec so far
Iteration 2223: max relative diff=0.000058, 191.74 sec so far
Iteration 2281: max relative diff=0.000053, 196.79 sec so far
Iteration 2339: max relative diff=0.000048, 201.86 sec so far
Iteration 2397: max relative diff=0.000044, 206.93 sec so far
Iteration 2454: max relative diff=0.000040, 211.94 sec so far
Iteration 2511: max relative diff=0.000037, 216.98 sec so far
Iteration 2569: max relative diff=0.000034, 222.01 sec so far
Iteration 2626: max relative diff=0.000031, 227.03 sec so far
Iteration 2683: max relative diff=0.000028, 232.06 sec so far
Iteration 2741: max relative diff=0.000026, 237.15 sec so far
Iteration 2798: max relative diff=0.000024, 242.20 sec so far
Iteration 2855: max relative diff=0.000022, 247.25 sec so far
Iteration 2913: max relative diff=0.000020, 252.34 sec so far
Iteration 2971: max relative diff=0.000018, 257.38 sec so far
Iteration 3029: max relative diff=0.000017, 262.47 sec so far
Iteration 3086: max relative diff=0.000015, 267.49 sec so far
Iteration 3143: max relative diff=0.000014, 272.50 sec so far
Iteration 3200: max relative diff=0.000013, 277.51 sec so far
Iteration 3257: max relative diff=0.000012, 282.57 sec so far
Iteration 3313: max relative diff=0.000011, 287.58 sec so far
Iteration 3369: max relative diff=0.000010, 292.60 sec so far
Iteration 3426: max relative diff=0.000009, 297.67 sec so far
Iteration 3483: max relative diff=0.000008, 302.70 sec so far
Iteration 3540: max relative diff=0.000008, 307.75 sec so far
Iteration 3597: max relative diff=0.000007, 312.77 sec so far
Iteration 3654: max relative diff=0.000006, 317.78 sec so far
Iteration 3712: max relative diff=0.000006, 322.80 sec so far
Iteration 3770: max relative diff=0.000005, 327.88 sec so far
Iteration 3828: max relative diff=0.000005, 332.97 sec so far
Iteration 3886: max relative diff=0.000005, 338.03 sec so far
Iteration 3944: max relative diff=0.000004, 343.05 sec so far
Iteration 4002: max relative diff=0.000004, 348.12 sec so far
Iteration 4060: max relative diff=0.000003, 353.16 sec so far
Iteration 4118: max relative diff=0.000003, 358.23 sec so far
Iteration 4176: max relative diff=0.000003, 363.30 sec so far
Iteration 4234: max relative diff=0.000003, 368.35 sec so far
Iteration 4292: max relative diff=0.000002, 373.42 sec so far
Iteration 4350: max relative diff=0.000002, 378.49 sec so far
Iteration 4407: max relative diff=0.000002, 383.58 sec so far
Iteration 4464: max relative diff=0.000002, 388.66 sec so far
Iteration 4526: max relative diff=0.000002, 393.69 sec so far
Iteration 4588: max relative diff=0.000002, 398.72 sec so far
Iteration 4651: max relative diff=0.000001, 403.75 sec so far
Iteration 4714: max relative diff=0.000001, 408.80 sec so far
Iteration 4777: max relative diff=0.000001, 413.85 sec so far
Iteration 4840: max relative diff=0.000001, 418.91 sec so far

Jacobi: 4880 iterations in 422.40 seconds (average 0.086514, setup 0.21)

Value in the initial state: 0.5386630172446204

Time for model checking: 423.572 seconds.

Result: 0.5386630172446204 (+/- 5.381007559705678E-6 estimated; rel err 9.989561910581338E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_polling.18-16_rep2.log

```
Command(s):
../bin/prism  models/polling.18-16/model.prism models/polling.18-16/property.props
Wallclock time: 397.520 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:19:31 GMT+01:00 2026
Hostname: n23m0341.hpc.itc.rwth-aachen.de
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

Prob0: 36 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Prob1: 35 iterations in 0.01 seconds (average 0.000286, setup 0.00)

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
Iteration 63: max relative diff=0.024211, 5.05 sec so far
Iteration 126: max relative diff=0.009887, 10.09 sec so far
Iteration 189: max relative diff=0.005832, 15.13 sec so far
Iteration 252: max relative diff=0.003985, 20.16 sec so far
Iteration 315: max relative diff=0.002943, 25.20 sec so far
Iteration 376: max relative diff=0.002296, 30.23 sec so far
Iteration 438: max relative diff=0.001841, 35.31 sec so far
Iteration 500: max relative diff=0.001511, 40.36 sec so far
Iteration 562: max relative diff=0.001261, 45.38 sec so far
Iteration 624: max relative diff=0.001067, 50.41 sec so far
Iteration 686: max relative diff=0.000912, 55.43 sec so far
Iteration 748: max relative diff=0.000787, 60.47 sec so far
Iteration 810: max relative diff=0.000685, 65.50 sec so far
Iteration 872: max relative diff=0.000600, 70.53 sec so far
Iteration 934: max relative diff=0.000527, 75.57 sec so far
Iteration 996: max relative diff=0.000465, 80.61 sec so far
Iteration 1058: max relative diff=0.000412, 85.65 sec so far
Iteration 1119: max relative diff=0.000367, 90.70 sec so far
Iteration 1180: max relative diff=0.000328, 95.76 sec so far
Iteration 1242: max relative diff=0.000293, 100.82 sec so far
Iteration 1304: max relative diff=0.000262, 105.89 sec so far
Iteration 1366: max relative diff=0.000235, 110.93 sec so far
Iteration 1428: max relative diff=0.000211, 115.98 sec so far
Iteration 1490: max relative diff=0.000190, 121.03 sec so far
Iteration 1552: max relative diff=0.000171, 126.07 sec so far
Iteration 1614: max relative diff=0.000154, 131.11 sec so far
Iteration 1676: max relative diff=0.000139, 136.17 sec so far
Iteration 1738: max relative diff=0.000125, 141.21 sec so far
Iteration 1800: max relative diff=0.000113, 146.25 sec so far
Iteration 1861: max relative diff=0.000103, 151.30 sec so far
Iteration 1923: max relative diff=0.000093, 156.37 sec so far
Iteration 1985: max relative diff=0.000084, 161.43 sec so far
Iteration 2047: max relative diff=0.000076, 166.48 sec so far
Iteration 2110: max relative diff=0.000069, 171.53 sec so far
Iteration 2173: max relative diff=0.000062, 176.54 sec so far
Iteration 2236: max relative diff=0.000057, 181.56 sec so far
Iteration 2297: max relative diff=0.000051, 186.59 sec so far
Iteration 2359: max relative diff=0.000047, 191.63 sec so far
Iteration 2421: max relative diff=0.000042, 196.66 sec so far
Iteration 2483: max relative diff=0.000038, 201.67 sec so far
Iteration 2545: max relative diff=0.000035, 206.72 sec so far
Iteration 2606: max relative diff=0.000032, 211.74 sec so far
Iteration 2668: max relative diff=0.000029, 216.77 sec so far
Iteration 2730: max relative diff=0.000026, 221.78 sec so far
Iteration 2793: max relative diff=0.000024, 226.86 sec so far
Iteration 2856: max relative diff=0.000022, 231.94 sec so far
Iteration 2919: max relative diff=0.000020, 237.02 sec so far
Iteration 2982: max relative diff=0.000018, 242.10 sec so far
Iteration 3045: max relative diff=0.000016, 247.17 sec so far
Iteration 3108: max relative diff=0.000015, 252.25 sec so far
Iteration 3171: max relative diff=0.000013, 257.33 sec so far
Iteration 3234: max relative diff=0.000012, 262.41 sec so far
Iteration 3297: max relative diff=0.000011, 267.49 sec so far
Iteration 3358: max relative diff=0.000010, 272.50 sec so far
Iteration 3420: max relative diff=0.000009, 277.54 sec so far
Iteration 3483: max relative diff=0.000008, 282.62 sec so far
Iteration 3546: max relative diff=0.000008, 287.70 sec so far
Iteration 3609: max relative diff=0.000007, 292.78 sec so far
Iteration 3672: max relative diff=0.000006, 297.86 sec so far
Iteration 3735: max relative diff=0.000006, 302.94 sec so far
Iteration 3798: max relative diff=0.000005, 308.02 sec so far
Iteration 3861: max relative diff=0.000005, 313.10 sec so far
Iteration 3924: max relative diff=0.000004, 318.18 sec so far
Iteration 3986: max relative diff=0.000004, 323.19 sec so far
Iteration 4048: max relative diff=0.000004, 328.27 sec so far
Iteration 4110: max relative diff=0.000003, 333.28 sec so far
Iteration 4172: max relative diff=0.000003, 338.32 sec so far
Iteration 4234: max relative diff=0.000003, 343.38 sec so far
Iteration 4295: max relative diff=0.000002, 348.41 sec so far
Iteration 4358: max relative diff=0.000002, 353.49 sec so far
Iteration 4420: max relative diff=0.000002, 358.50 sec so far
Iteration 4482: max relative diff=0.000002, 363.51 sec so far
Iteration 4544: max relative diff=0.000002, 368.52 sec so far
Iteration 4607: max relative diff=0.000002, 373.60 sec so far
Iteration 4670: max relative diff=0.000001, 378.68 sec so far
Iteration 4733: max relative diff=0.000001, 383.75 sec so far
Iteration 4795: max relative diff=0.000001, 388.83 sec so far
Iteration 4857: max relative diff=0.000001, 393.85 sec so far

Jacobi: 4880 iterations in 395.91 seconds (average 0.081088, setup 0.20)

Value in the initial state: 0.5386630172446204

Time for model checking: 396.933 seconds.

Result: 0.5386630172446204 (+/- 5.381007559705678E-6 estimated; rel err 9.989561910581338E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_polling.18-16_rep3.log

```
Command(s):
../bin/prism  models/polling.18-16/model.prism models/polling.18-16/property.props
Wallclock time: 453.139 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:38:01 GMT+01:00 2026
Hostname: r23m0203.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 37 iterations in 0.04 seconds (average 0.001081, setup 0.00)

Time for model construction: 0.061 seconds.

Type:        CTMC
States:      7077888 (1 initial)
Transitions: 69599232

Rate matrix: 2745 nodes (4 terminal), 69599232 minterms, vars: 24r/24c

Diagonals vector: 1540 nodes (38 terminal), 7077888 minterms
Embedded Markov chain: 17929 nodes (72 terminal), 69599232 minterms

Prob0: 36 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Prob1: 35 iterations in 0.01 seconds (average 0.000286, setup 0.00)

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
Iteration 54: max relative diff=0.029412, 5.04 sec so far
Iteration 108: max relative diff=0.012076, 10.08 sec so far
Iteration 162: max relative diff=0.007132, 15.11 sec so far
Iteration 216: max relative diff=0.004892, 20.15 sec so far
Iteration 270: max relative diff=0.003632, 25.16 sec so far
Iteration 324: max relative diff=0.002830, 30.17 sec so far
Iteration 378: max relative diff=0.002279, 35.23 sec so far
Iteration 432: max relative diff=0.001879, 40.27 sec so far
Iteration 487: max relative diff=0.001572, 45.34 sec so far
Iteration 541: max relative diff=0.001338, 50.35 sec so far
Iteration 595: max relative diff=0.001152, 55.37 sec so far
Iteration 650: max relative diff=0.000998, 60.45 sec so far
Iteration 705: max relative diff=0.000871, 65.49 sec so far
Iteration 760: max relative diff=0.000766, 70.56 sec so far
Iteration 816: max relative diff=0.000676, 75.59 sec so far
Iteration 871: max relative diff=0.000601, 80.64 sec so far
Iteration 926: max relative diff=0.000536, 85.69 sec so far
Iteration 981: max relative diff=0.000479, 90.74 sec so far
Iteration 1036: max relative diff=0.000430, 95.77 sec so far
Iteration 1091: max relative diff=0.000387, 100.83 sec so far
Iteration 1146: max relative diff=0.000349, 105.87 sec so far
Iteration 1201: max relative diff=0.000315, 110.91 sec so far
Iteration 1256: max relative diff=0.000285, 115.98 sec so far
Iteration 1311: max relative diff=0.000259, 121.05 sec so far
Iteration 1366: max relative diff=0.000235, 126.08 sec so far
Iteration 1421: max relative diff=0.000213, 131.15 sec so far
Iteration 1476: max relative diff=0.000194, 136.21 sec so far
Iteration 1531: max relative diff=0.000177, 141.26 sec so far
Iteration 1586: max relative diff=0.000161, 146.30 sec so far
Iteration 1641: max relative diff=0.000147, 151.35 sec so far
Iteration 1695: max relative diff=0.000134, 156.36 sec so far
Iteration 1750: max relative diff=0.000123, 161.40 sec so far
Iteration 1805: max relative diff=0.000112, 166.42 sec so far
Iteration 1861: max relative diff=0.000103, 171.50 sec so far
Iteration 1916: max relative diff=0.000094, 176.54 sec so far
Iteration 1971: max relative diff=0.000086, 181.55 sec so far
Iteration 2026: max relative diff=0.000079, 186.57 sec so far
Iteration 2081: max relative diff=0.000072, 191.61 sec so far
Iteration 2136: max relative diff=0.000066, 196.63 sec so far
Iteration 2191: max relative diff=0.000061, 201.68 sec so far
Iteration 2246: max relative diff=0.000056, 206.73 sec so far
Iteration 2301: max relative diff=0.000051, 211.79 sec so far
Iteration 2356: max relative diff=0.000047, 216.82 sec so far
Iteration 2411: max relative diff=0.000043, 221.89 sec so far
Iteration 2466: max relative diff=0.000039, 226.95 sec so far
Iteration 2521: max relative diff=0.000036, 231.97 sec so far
Iteration 2577: max relative diff=0.000033, 237.06 sec so far
Iteration 2632: max relative diff=0.000031, 242.10 sec so far
Iteration 2687: max relative diff=0.000028, 247.12 sec so far
Iteration 2742: max relative diff=0.000026, 252.16 sec so far
Iteration 2797: max relative diff=0.000024, 257.20 sec so far
Iteration 2853: max relative diff=0.000022, 262.28 sec so far
Iteration 2908: max relative diff=0.000020, 267.31 sec so far
Iteration 2963: max relative diff=0.000018, 272.32 sec so far
Iteration 3018: max relative diff=0.000017, 277.36 sec so far
Iteration 3074: max relative diff=0.000015, 282.43 sec so far
Iteration 3129: max relative diff=0.000014, 287.44 sec so far
Iteration 3184: max relative diff=0.000013, 292.47 sec so far
Iteration 3239: max relative diff=0.000012, 297.52 sec so far
Iteration 3295: max relative diff=0.000011, 302.57 sec so far
Iteration 3350: max relative diff=0.000010, 307.60 sec so far
Iteration 3406: max relative diff=0.000009, 312.65 sec so far
Iteration 3462: max relative diff=0.000009, 317.73 sec so far
Iteration 3518: max relative diff=0.000008, 322.77 sec so far
Iteration 3574: max relative diff=0.000007, 327.82 sec so far
Iteration 3629: max relative diff=0.000007, 332.83 sec so far
Iteration 3685: max relative diff=0.000006, 337.92 sec so far
Iteration 3741: max relative diff=0.000006, 343.00 sec so far
Iteration 3797: max relative diff=0.000005, 348.07 sec so far
Iteration 3853: max relative diff=0.000005, 353.12 sec so far
Iteration 3908: max relative diff=0.000004, 358.17 sec so far
Iteration 3963: max relative diff=0.000004, 363.20 sec so far
Iteration 4018: max relative diff=0.000004, 368.21 sec so far
Iteration 4073: max relative diff=0.000003, 373.23 sec so far
Iteration 4129: max relative diff=0.000003, 378.32 sec so far
Iteration 4184: max relative diff=0.000003, 383.36 sec so far
Iteration 4239: max relative diff=0.000003, 388.37 sec so far
Iteration 4295: max relative diff=0.000002, 393.44 sec so far
Iteration 4350: max relative diff=0.000002, 398.45 sec so far
Iteration 4405: max relative diff=0.000002, 403.47 sec so far
Iteration 4461: max relative diff=0.000002, 408.53 sec so far
Iteration 4517: max relative diff=0.000002, 413.62 sec so far
Iteration 4572: max relative diff=0.000002, 418.68 sec so far
Iteration 4627: max relative diff=0.000001, 423.76 sec so far
Iteration 4682: max relative diff=0.000001, 428.83 sec so far
Iteration 4737: max relative diff=0.000001, 433.84 sec so far
Iteration 4793: max relative diff=0.000001, 438.91 sec so far
Iteration 4849: max relative diff=0.000001, 443.99 sec so far

Jacobi: 4880 iterations in 447.06 seconds (average 0.091564, setup 0.23)

Value in the initial state: 0.5386630172446204

Time for model checking: 448.941 seconds.

Result: 0.5386630172446204 (+/- 5.381007559705678E-6 estimated; rel err 9.989561910581338E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_polling.18-16_rep4.log

```
Command(s):
../bin/prism  models/polling.18-16/model.prism models/polling.18-16/property.props
Wallclock time: 402.032 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:49:24 GMT+01:00 2026
Hostname: n23m0386.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 37 iterations in 0.02 seconds (average 0.000541, setup 0.00)

Time for model construction: 0.079 seconds.

Type:        CTMC
States:      7077888 (1 initial)
Transitions: 69599232

Rate matrix: 2745 nodes (4 terminal), 69599232 minterms, vars: 24r/24c

Diagonals vector: 1540 nodes (38 terminal), 7077888 minterms
Embedded Markov chain: 17929 nodes (72 terminal), 69599232 minterms

Prob0: 36 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Prob1: 35 iterations in 0.01 seconds (average 0.000286, setup 0.00)

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
Iteration 59: max relative diff=0.026308, 5.02 sec so far
Iteration 119: max relative diff=0.010649, 10.08 sec so far
Iteration 179: max relative diff=0.006261, 15.10 sec so far
Iteration 240: max relative diff=0.004254, 20.18 sec so far
Iteration 300: max relative diff=0.003147, 25.21 sec so far
Iteration 360: max relative diff=0.002442, 30.24 sec so far
Iteration 420: max relative diff=0.001958, 35.33 sec so far
Iteration 481: max relative diff=0.001602, 40.38 sec so far
Iteration 541: max relative diff=0.001338, 45.45 sec so far
Iteration 601: max relative diff=0.001133, 50.53 sec so far
Iteration 660: max relative diff=0.000973, 55.54 sec so far
Iteration 719: max relative diff=0.000842, 60.56 sec so far
Iteration 778: max relative diff=0.000735, 65.59 sec so far
Iteration 837: max relative diff=0.000646, 70.63 sec so far
Iteration 897: max relative diff=0.000569, 75.70 sec so far
Iteration 957: max relative diff=0.000503, 80.78 sec so far
Iteration 1016: max relative diff=0.000447, 85.81 sec so far
Iteration 1076: max relative diff=0.000398, 90.86 sec so far
Iteration 1135: max relative diff=0.000356, 95.93 sec so far
Iteration 1194: max relative diff=0.000319, 100.94 sec so far
Iteration 1254: max relative diff=0.000286, 106.00 sec so far
Iteration 1313: max relative diff=0.000258, 111.01 sec so far
Iteration 1372: max relative diff=0.000232, 116.03 sec so far
Iteration 1431: max relative diff=0.000210, 121.05 sec so far
Iteration 1491: max relative diff=0.000189, 126.13 sec so far
Iteration 1550: max relative diff=0.000171, 131.14 sec so far
Iteration 1610: max relative diff=0.000155, 136.19 sec so far
Iteration 1670: max relative diff=0.000140, 141.23 sec so far
Iteration 1730: max relative diff=0.000127, 146.30 sec so far
Iteration 1790: max relative diff=0.000115, 151.31 sec so far
Iteration 1852: max relative diff=0.000104, 156.38 sec so far
Iteration 1915: max relative diff=0.000094, 161.44 sec so far
Iteration 1978: max relative diff=0.000085, 166.52 sec so far
Iteration 2041: max relative diff=0.000077, 171.56 sec so far
Iteration 2104: max relative diff=0.000070, 176.59 sec so far
Iteration 2167: max relative diff=0.000063, 181.65 sec so far
Iteration 2230: max relative diff=0.000057, 186.73 sec so far
Iteration 2293: max relative diff=0.000052, 191.77 sec so far
Iteration 2356: max relative diff=0.000047, 196.82 sec so far
Iteration 2419: max relative diff=0.000042, 201.86 sec so far
Iteration 2482: max relative diff=0.000039, 206.90 sec so far
Iteration 2545: max relative diff=0.000035, 211.95 sec so far
Iteration 2606: max relative diff=0.000032, 217.00 sec so far
Iteration 2669: max relative diff=0.000029, 222.07 sec so far
Iteration 2732: max relative diff=0.000026, 227.13 sec so far
Iteration 2795: max relative diff=0.000024, 232.16 sec so far
Iteration 2858: max relative diff=0.000022, 237.19 sec so far
Iteration 2921: max relative diff=0.000020, 242.25 sec so far
Iteration 2984: max relative diff=0.000018, 247.31 sec so far
Iteration 3047: max relative diff=0.000016, 252.34 sec so far
Iteration 3110: max relative diff=0.000015, 257.36 sec so far
Iteration 3173: max relative diff=0.000013, 262.39 sec so far
Iteration 3236: max relative diff=0.000012, 267.41 sec so far
Iteration 3299: max relative diff=0.000011, 272.45 sec so far
Iteration 3361: max relative diff=0.000010, 277.53 sec so far
Iteration 3424: max relative diff=0.000009, 282.59 sec so far
Iteration 3486: max relative diff=0.000008, 287.61 sec so far
Iteration 3549: max relative diff=0.000008, 292.67 sec so far
Iteration 3612: max relative diff=0.000007, 297.70 sec so far
Iteration 3675: max relative diff=0.000006, 302.78 sec so far
Iteration 3738: max relative diff=0.000006, 307.84 sec so far
Iteration 3801: max relative diff=0.000005, 312.89 sec so far
Iteration 3864: max relative diff=0.000005, 317.92 sec so far
Iteration 3927: max relative diff=0.000004, 322.95 sec so far
Iteration 3990: max relative diff=0.000004, 327.98 sec so far
Iteration 4053: max relative diff=0.000003, 333.01 sec so far
Iteration 4114: max relative diff=0.000003, 338.02 sec so far
Iteration 4177: max relative diff=0.000003, 343.09 sec so far
Iteration 4240: max relative diff=0.000003, 348.16 sec so far
Iteration 4303: max relative diff=0.000002, 353.19 sec so far
Iteration 4366: max relative diff=0.000002, 358.22 sec so far
Iteration 4429: max relative diff=0.000002, 363.24 sec so far
Iteration 4492: max relative diff=0.000002, 368.30 sec so far
Iteration 4555: max relative diff=0.000002, 373.33 sec so far
Iteration 4618: max relative diff=0.000001, 378.38 sec so far
Iteration 4681: max relative diff=0.000001, 383.42 sec so far
Iteration 4744: max relative diff=0.000001, 388.46 sec so far
Iteration 4807: max relative diff=0.000001, 393.50 sec so far
Iteration 4869: max relative diff=0.000001, 398.55 sec so far

Jacobi: 4880 iterations in 399.66 seconds (average 0.081855, setup 0.21)

Value in the initial state: 0.5386630172446204

Time for model checking: 400.787 seconds.

Result: 0.5386630172446204 (+/- 5.381007559705678E-6 estimated; rel err 9.989561910581338E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_norewards_polling.18-16_rep5.log

```
Command(s):
../bin/prism  models/polling.18-16/model.prism models/polling.18-16/property.props
Wallclock time: 522.846 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:00:30 GMT+01:00 2026
Hostname: n23m0396.hpc.itc.rwth-aachen.de
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

Time for model construction: 0.093 seconds.

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
Iteration 47: max relative diff=0.035022, 5.02 sec so far
Iteration 94: max relative diff=0.014459, 10.05 sec so far
Iteration 142: max relative diff=0.008465, 15.15 sec so far
Iteration 189: max relative diff=0.005832, 20.16 sec so far
Iteration 236: max relative diff=0.004350, 25.17 sec so far
Iteration 283: max relative diff=0.003408, 30.19 sec so far
Iteration 330: max relative diff=0.002759, 35.20 sec so far
Iteration 378: max relative diff=0.002279, 40.30 sec so far
Iteration 425: max relative diff=0.001925, 45.31 sec so far
Iteration 473: max relative diff=0.001643, 50.40 sec so far
Iteration 520: max relative diff=0.001423, 55.41 sec so far
Iteration 567: max relative diff=0.001243, 60.42 sec so far
Iteration 615: max relative diff=0.001092, 65.52 sec so far
Iteration 663: max relative diff=0.000965, 70.62 sec so far
Iteration 710: max relative diff=0.000860, 75.66 sec so far
Iteration 758: max relative diff=0.000769, 80.76 sec so far
Iteration 806: max relative diff=0.000691, 85.88 sec so far
Iteration 854: max relative diff=0.000623, 90.98 sec so far
Iteration 901: max relative diff=0.000564, 95.99 sec so far
Iteration 948: max relative diff=0.000512, 101.00 sec so far
Iteration 996: max relative diff=0.000465, 106.10 sec so far
Iteration 1043: max relative diff=0.000424, 111.13 sec so far
Iteration 1091: max relative diff=0.000387, 116.23 sec so far
Iteration 1138: max relative diff=0.000354, 121.24 sec so far
Iteration 1185: max relative diff=0.000325, 126.25 sec so far
Iteration 1232: max relative diff=0.000298, 131.26 sec so far
Iteration 1279: max relative diff=0.000274, 136.28 sec so far
Iteration 1327: max relative diff=0.000251, 141.36 sec so far
Iteration 1374: max relative diff=0.000231, 146.37 sec so far
Iteration 1421: max relative diff=0.000213, 151.38 sec so far
Iteration 1468: max relative diff=0.000197, 156.40 sec so far
Iteration 1516: max relative diff=0.000181, 161.50 sec so far
Iteration 1564: max relative diff=0.000167, 166.61 sec so far
Iteration 1612: max relative diff=0.000154, 171.71 sec so far
Iteration 1660: max relative diff=0.000142, 176.82 sec so far
Iteration 1708: max relative diff=0.000132, 181.93 sec so far
Iteration 1755: max relative diff=0.000122, 186.94 sec so far
Iteration 1802: max relative diff=0.000113, 191.95 sec so far
Iteration 1850: max relative diff=0.000104, 197.04 sec so far
Iteration 1897: max relative diff=0.000097, 202.05 sec so far
Iteration 1948: max relative diff=0.000089, 207.08 sec so far
Iteration 1999: max relative diff=0.000082, 212.15 sec so far
Iteration 2047: max relative diff=0.000076, 217.25 sec so far
Iteration 2094: max relative diff=0.000071, 222.26 sec so far
Iteration 2141: max relative diff=0.000066, 227.27 sec so far
Iteration 2188: max relative diff=0.000061, 232.28 sec so far
Iteration 2235: max relative diff=0.000057, 237.29 sec so far
Iteration 2283: max relative diff=0.000053, 242.40 sec so far
Iteration 2331: max relative diff=0.000049, 247.51 sec so far
Iteration 2379: max relative diff=0.000045, 252.61 sec so far
Iteration 2426: max relative diff=0.000042, 257.62 sec so far
Iteration 2474: max relative diff=0.000039, 262.72 sec so far
Iteration 2521: max relative diff=0.000036, 267.74 sec so far
Iteration 2569: max relative diff=0.000034, 272.84 sec so far
Iteration 2616: max relative diff=0.000031, 277.85 sec so far
Iteration 2664: max relative diff=0.000029, 282.95 sec so far
Iteration 2712: max relative diff=0.000027, 288.06 sec so far
Iteration 2759: max relative diff=0.000025, 293.07 sec so far
Iteration 2807: max relative diff=0.000023, 298.18 sec so far
Iteration 2854: max relative diff=0.000022, 303.19 sec so far
Iteration 2901: max relative diff=0.000020, 308.20 sec so far
Iteration 2949: max relative diff=0.000019, 313.30 sec so far
Iteration 2997: max relative diff=0.000017, 318.41 sec so far
Iteration 3044: max relative diff=0.000016, 323.42 sec so far
Iteration 3092: max relative diff=0.000015, 328.52 sec so far
Iteration 3139: max relative diff=0.000014, 333.53 sec so far
Iteration 3186: max relative diff=0.000013, 338.55 sec so far
Iteration 3233: max relative diff=0.000012, 343.56 sec so far
Iteration 3281: max relative diff=0.000011, 348.67 sec so far
Iteration 3328: max relative diff=0.000011, 353.68 sec so far
Iteration 3376: max relative diff=0.000010, 358.78 sec so far
Iteration 3423: max relative diff=0.000009, 363.79 sec so far
Iteration 3471: max relative diff=0.000008, 368.90 sec so far
Iteration 3519: max relative diff=0.000008, 374.00 sec so far
Iteration 3567: max relative diff=0.000007, 379.11 sec so far
Iteration 3615: max relative diff=0.000007, 384.21 sec so far
Iteration 3663: max relative diff=0.000006, 389.31 sec so far
Iteration 3710: max relative diff=0.000006, 394.34 sec so far
Iteration 3757: max relative diff=0.000005, 399.35 sec so far
Iteration 3805: max relative diff=0.000005, 404.45 sec so far
Iteration 3852: max relative diff=0.000005, 409.46 sec so far
Iteration 3900: max relative diff=0.000004, 414.57 sec so far
Iteration 3948: max relative diff=0.000004, 419.66 sec so far
Iteration 3995: max relative diff=0.000004, 424.67 sec so far
Iteration 4042: max relative diff=0.000004, 429.68 sec so far
Iteration 4090: max relative diff=0.000003, 434.78 sec so far
Iteration 4137: max relative diff=0.000003, 439.79 sec so far
Iteration 4185: max relative diff=0.000003, 444.89 sec so far
Iteration 4232: max relative diff=0.000003, 449.90 sec so far
Iteration 4279: max relative diff=0.000002, 454.92 sec so far
Iteration 4327: max relative diff=0.000002, 460.02 sec so far
Iteration 4375: max relative diff=0.000002, 465.11 sec so far
Iteration 4422: max relative diff=0.000002, 470.13 sec so far
Iteration 4470: max relative diff=0.000002, 475.24 sec so far
Iteration 4517: max relative diff=0.000002, 480.25 sec so far
Iteration 4564: max relative diff=0.000002, 485.26 sec so far
Iteration 4612: max relative diff=0.000001, 490.35 sec so far
Iteration 4660: max relative diff=0.000001, 495.46 sec so far
Iteration 4707: max relative diff=0.000001, 500.47 sec so far
Iteration 4755: max relative diff=0.000001, 505.57 sec so far
Iteration 4802: max relative diff=0.000001, 510.60 sec so far
Iteration 4850: max relative diff=0.000001, 515.70 sec so far

Jacobi: 4880 iterations in 519.15 seconds (average 0.106332, setup 0.25)

Value in the initial state: 0.5386630172446204

Time for model checking: 521.449 seconds.

Result: 0.5386630172446204 (+/- 5.381007559705678E-6 estimated; rel err 9.989561910581338E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

