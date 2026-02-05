# Log files for prism_from-umb_check_ex on model [mapk-cascade.4-30](../../models/mapk-cascade.4-30)

Parsed values: `[0.799, 0.766, 0.72, 0.451, 0.238]`



### Log file: prism_from-umb_check_ex_mapk-cascade.4-30_rep1.log

```
Command(s):
../bin/prism -ex -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props
Wallclock time: 274.320 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:31:54 GMT+01:00 2026
Hostname: r23m0210.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props

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

Building model (engine:explicit)...

Time for model construction: 0.799 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872
Building reward structure...
Building embedded DTMC...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.3 seconds)
Starting Prob1...
Prob1 took 0.394 seconds.
target=1461, inf=0, rest=98074
Starting value iteration (with Jacobi) ...
Iteration 34: 5.07 sec so far
Iteration 69: 10.11 sec so far
Iteration 104: 15.15 sec so far
Iteration 139: 20.22 sec so far
Iteration 174: 25.26 sec so far
Iteration 209: 30.30 sec so far
Iteration 244: 35.34 sec so far
Iteration 279: 40.37 sec so far
Iteration 314: 45.40 sec so far
Iteration 349: 50.42 sec so far
Iteration 384: 55.46 sec so far
Iteration 419: 60.48 sec so far
Iteration 454: 65.51 sec so far
Iteration 489: 70.53 sec so far
Iteration 524: 75.56 sec so far
Iteration 559: 80.58 sec so far
Iteration 594: 85.60 sec so far
Iteration 629: 90.61 sec so far
Iteration 664: 95.63 sec so far
Iteration 699: 100.63 sec so far
Iteration 734: 105.65 sec so far
Iteration 769: 110.67 sec so far
Iteration 804: 115.69 sec so far
Iteration 839: 120.72 sec so far
Iteration 874: 125.74 sec so far
Iteration 909: 130.77 sec so far
Iteration 944: 135.79 sec so far
Iteration 979: 140.81 sec so far
Iteration 1014: 145.83 sec so far
Iteration 1049: 150.84 sec so far
Iteration 1084: 155.85 sec so far
Iteration 1119: 160.88 sec so far
Iteration 1154: 165.89 sec so far
Iteration 1189: 170.90 sec so far
Iteration 1224: 175.91 sec so far
Iteration 1259: 180.93 sec so far
Iteration 1294: 185.95 sec so far
Iteration 1329: 190.98 sec so far
Iteration 1364: 196.00 sec so far
Iteration 1399: 201.02 sec so far
Iteration 1434: 206.05 sec so far
Iteration 1469: 211.08 sec so far
Iteration 1504: 216.12 sec so far
Iteration 1539: 221.14 sec so far
Iteration 1574: 226.16 sec so far
Iteration 1609: 231.18 sec so far
Iteration 1644: 236.21 sec so far
Iteration 1679: 241.24 sec so far
Iteration 1714: 246.27 sec so far
Iteration 1749: 251.29 sec so far
Iteration 1784: 256.31 sec so far
Iteration 1819: 261.33 sec so far
Iteration 1854: 266.35 sec so far
Value iteration (with Jacobi) took 1876 iterations, 1689114756 multiplications and 269.544 seconds.
Expected reachability took 270.275 seconds.

Value in the initial state: 40.672703711883116

Time for model checking: 270.924 seconds.

Result: 40.672703711883116 (+/- 4.045129484452135E-4 estimated; rel err 9.945563277786946E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_mapk-cascade.4-30_rep2.log

```
Command(s):
../bin/prism -ex -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props
Wallclock time: 279.234 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:07:25 GMT+01:00 2026
Hostname: r23m0215.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props

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

Building model (engine:explicit)...

Time for model construction: 0.766 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872
Building reward structure...
Building embedded DTMC...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.261 seconds)
Starting Prob1...
Prob1 took 0.39 seconds.
target=1461, inf=0, rest=98074
Starting value iteration (with Jacobi) ...
Iteration 34: 5.15 sec so far
Iteration 69: 10.29 sec so far
Iteration 104: 15.41 sec so far
Iteration 139: 20.53 sec so far
Iteration 174: 25.64 sec so far
Iteration 209: 30.74 sec so far
Iteration 244: 35.85 sec so far
Iteration 279: 40.98 sec so far
Iteration 314: 46.10 sec so far
Iteration 349: 51.20 sec so far
Iteration 384: 56.30 sec so far
Iteration 419: 61.42 sec so far
Iteration 454: 66.53 sec so far
Iteration 489: 71.65 sec so far
Iteration 524: 76.77 sec so far
Iteration 559: 81.89 sec so far
Iteration 594: 87.00 sec so far
Iteration 629: 92.12 sec so far
Iteration 664: 97.25 sec so far
Iteration 699: 102.38 sec so far
Iteration 734: 107.50 sec so far
Iteration 769: 112.62 sec so far
Iteration 804: 117.72 sec so far
Iteration 839: 122.83 sec so far
Iteration 874: 127.95 sec so far
Iteration 909: 133.06 sec so far
Iteration 944: 138.17 sec so far
Iteration 979: 143.29 sec so far
Iteration 1014: 148.41 sec so far
Iteration 1049: 153.52 sec so far
Iteration 1084: 158.63 sec so far
Iteration 1119: 163.74 sec so far
Iteration 1154: 168.84 sec so far
Iteration 1189: 173.96 sec so far
Iteration 1224: 179.06 sec so far
Iteration 1259: 184.17 sec so far
Iteration 1294: 189.28 sec so far
Iteration 1329: 194.38 sec so far
Iteration 1364: 199.50 sec so far
Iteration 1399: 204.61 sec so far
Iteration 1434: 209.72 sec so far
Iteration 1469: 214.86 sec so far
Iteration 1504: 219.97 sec so far
Iteration 1539: 225.07 sec so far
Iteration 1574: 230.20 sec so far
Iteration 1609: 235.31 sec so far
Iteration 1644: 240.43 sec so far
Iteration 1679: 245.55 sec so far
Iteration 1714: 250.66 sec so far
Iteration 1749: 255.77 sec so far
Iteration 1784: 260.88 sec so far
Iteration 1819: 265.99 sec so far
Iteration 1854: 271.10 sec so far
Value iteration (with Jacobi) took 1876 iterations, 1689114756 multiplications and 274.358 seconds.
Expected reachability took 275.069 seconds.

Value in the initial state: 40.672703711883116

Time for model checking: 275.787 seconds.

Result: 40.672703711883116 (+/- 4.045129484452135E-4 estimated; rel err 9.945563277786946E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_mapk-cascade.4-30_rep3.log

```
Command(s):
../bin/prism -ex -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props
Wallclock time: 274.905 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:52:35 GMT+01:00 2026
Hostname: r23m0216.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props

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

Building model (engine:explicit)...

Time for model construction: 0.72 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872
Building reward structure...
Building embedded DTMC...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.251 seconds)
Starting Prob1...
Prob1 took 0.354 seconds.
target=1461, inf=0, rest=98074
Starting value iteration (with Jacobi) ...
Iteration 34: 5.05 sec so far
Iteration 69: 10.11 sec so far
Iteration 104: 15.15 sec so far
Iteration 139: 20.19 sec so far
Iteration 174: 25.23 sec so far
Iteration 209: 30.27 sec so far
Iteration 244: 35.31 sec so far
Iteration 279: 40.34 sec so far
Iteration 314: 45.37 sec so far
Iteration 349: 50.41 sec so far
Iteration 384: 55.45 sec so far
Iteration 419: 60.48 sec so far
Iteration 454: 65.51 sec so far
Iteration 489: 70.55 sec so far
Iteration 524: 75.58 sec so far
Iteration 559: 80.62 sec so far
Iteration 594: 85.66 sec so far
Iteration 629: 90.71 sec so far
Iteration 664: 95.75 sec so far
Iteration 699: 100.79 sec so far
Iteration 734: 105.83 sec so far
Iteration 769: 110.86 sec so far
Iteration 804: 115.90 sec so far
Iteration 839: 120.93 sec so far
Iteration 874: 125.96 sec so far
Iteration 909: 131.00 sec so far
Iteration 944: 136.03 sec so far
Iteration 979: 141.07 sec so far
Iteration 1014: 146.11 sec so far
Iteration 1049: 151.15 sec so far
Iteration 1084: 156.19 sec so far
Iteration 1119: 161.23 sec so far
Iteration 1154: 166.27 sec so far
Iteration 1189: 171.31 sec so far
Iteration 1224: 176.34 sec so far
Iteration 1259: 181.37 sec so far
Iteration 1294: 186.41 sec so far
Iteration 1329: 191.44 sec so far
Iteration 1364: 196.46 sec so far
Iteration 1399: 201.51 sec so far
Iteration 1434: 206.55 sec so far
Iteration 1469: 211.59 sec so far
Iteration 1504: 216.63 sec so far
Iteration 1539: 221.67 sec so far
Iteration 1574: 226.70 sec so far
Iteration 1609: 231.74 sec so far
Iteration 1644: 236.77 sec so far
Iteration 1679: 241.81 sec so far
Iteration 1714: 246.83 sec so far
Iteration 1749: 251.87 sec so far
Iteration 1784: 256.89 sec so far
Iteration 1819: 261.93 sec so far
Iteration 1854: 266.98 sec so far
Value iteration (with Jacobi) took 1876 iterations, 1689114756 multiplications and 270.188 seconds.
Expected reachability took 270.835 seconds.

Value in the initial state: 40.672703711883116

Time for model checking: 271.489 seconds.

Result: 40.672703711883116 (+/- 4.045129484452135E-4 estimated; rel err 9.945563277786946E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_mapk-cascade.4-30_rep4.log

```
Command(s):
../bin/prism -ex -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props
Wallclock time: 78.693 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:07:19 GMT+01:00 2026
Hostname: r23m0196.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props

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

Building model (engine:explicit)...

Time for model construction: 0.451 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872
Building reward structure...
Building embedded DTMC...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.113 seconds)
Starting Prob1...
Prob1 took 0.107 seconds.
target=1461, inf=0, rest=98074
Starting value iteration (with Jacobi) ...
Iteration 124: 5.01 sec so far
Iteration 248: 10.03 sec so far
Iteration 371: 15.06 sec so far
Iteration 498: 20.07 sec so far
Iteration 626: 25.10 sec so far
Iteration 748: 30.13 sec so far
Iteration 871: 35.16 sec so far
Iteration 996: 40.19 sec so far
Iteration 1124: 45.23 sec so far
Iteration 1249: 50.24 sec so far
Iteration 1372: 55.25 sec so far
Iteration 1494: 60.26 sec so far
Iteration 1622: 65.29 sec so far
Iteration 1750: 70.29 sec so far
Iteration 1874: 75.33 sec so far
Value iteration (with Jacobi) took 1876 iterations, 1689114756 multiplications and 75.426 seconds.
Expected reachability took 75.683 seconds.

Value in the initial state: 40.672703711883116

Time for model checking: 75.914 seconds.

Result: 40.672703711883116 (+/- 4.045129484452135E-4 estimated; rel err 9.945563277786946E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_mapk-cascade.4-30_rep5.log

```
Command(s):
../bin/prism -ex -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props
Wallclock time: 74.134 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:32 GMT+01:00 2026
Hostname: n23m0109.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/mapk-cascade.4-30/prism.model.umb models/mapk-cascade.4-30/property.props

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

Building model (engine:explicit)...

Time for model construction: 0.238 seconds.

Type:        CTMC
States:      99535 (1 initial)
Transitions: 910872
Building reward structure...
Building embedded DTMC...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.103 seconds)
Starting Prob1...
Prob1 took 0.095 seconds.
target=1461, inf=0, rest=98074
Starting value iteration (with Jacobi) ...
Iteration 129: 5.04 sec so far
Iteration 260: 10.06 sec so far
Iteration 391: 15.09 sec so far
Iteration 520: 20.10 sec so far
Iteration 651: 25.11 sec so far
Iteration 781: 30.14 sec so far
Iteration 911: 35.15 sec so far
Iteration 1042: 40.17 sec so far
Iteration 1172: 45.19 sec so far
Iteration 1303: 50.23 sec so far
Iteration 1433: 55.24 sec so far
Iteration 1563: 60.24 sec so far
Iteration 1694: 65.26 sec so far
Iteration 1825: 70.28 sec so far
Value iteration (with Jacobi) took 1876 iterations, 1689114756 multiplications and 72.267 seconds.
Expected reachability took 72.482 seconds.

Value in the initial state: 40.672703711883116

Time for model checking: 72.686 seconds.

Result: 40.672703711883116 (+/- 4.045129484452135E-4 estimated; rel err 9.945563277786946E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

