# Log files

Tool configuration: prism_from-umb_check_norewards
Benchmark: [crowds.5-20](../../models/crowds.5-20)
Parsed values: [448.006, 423.127, 608.635, 457.197, 486.237]



### Log file: prism_from-umb_check_norewards_crowds.5-20_rep1.log

```
Command(s):
../bin/prism  -importmodel models/crowds.5-20/prism.model.umb models/crowds.5-20/property.props
Wallclock time: 448.006 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:20:16 GMT+01:00 2026
Hostname: r23m0062.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/crowds.5-20/prism.model.umb models/crowds.5-20/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/crowds.5-20/property.props"...

1 property:
(1) "positive": P=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "positive": P=? [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 47 iterations in 2.35 seconds (average 0.050000, setup 0.00)

Time for model construction: 440.819 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 329533 nodes (7 terminal), 7374951 minterms, vars: 21r/21c

Prob0: 14 iterations in 0.54 seconds (average 0.038571, setup 0.00)

Prob1: 30 iterations in 0.37 seconds (average 0.012333, setup 0.00)

yes = 47399, no = 1745849, maybe = 268703

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=21, nodes=80689] [3.7 MB]
Adding explicit sparse matrices... [levels=6, num=4890, compact] [679.9 KB]
Creating vector for diagonals... [dist=1, compact] [3.9 MB]
Creating vector for RHS... [dist=2, compact] [3.9 MB]
Allocating iteration vectors... [2 x 15.7 MB]
TOTAL: [43.7 MB]

Starting iterations...

Jacobi: 187 iterations in 5.07 seconds (average 0.017005, setup 1.89)

Value in the initial state: 0.08606841127862043

Time for model checking: 6.035 seconds.

Result: 0.08606841127862043 (+/- 7.183528306181446E-7 estimated; rel err 8.34630057586046E-6)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_crowds.5-20_rep2.log

```
Command(s):
../bin/prism  -importmodel models/crowds.5-20/prism.model.umb models/crowds.5-20/property.props
Wallclock time: 423.127 seconds
Return code: 0
##############################
[0.002s][warning][perf,memops] Cannot use file /tmp/hsperfdata_tq429871/12954 because it is locked by another process (errno = 11)
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:24:29 GMT+01:00 2026
Hostname: n23m0041.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/crowds.5-20/prism.model.umb models/crowds.5-20/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/crowds.5-20/property.props"...

1 property:
(1) "positive": P=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "positive": P=? [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 47 iterations in 2.33 seconds (average 0.049574, setup 0.00)

Time for model construction: 415.223 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 329533 nodes (7 terminal), 7374951 minterms, vars: 21r/21c

Prob0: 14 iterations in 1.02 seconds (average 0.072857, setup 0.00)

Prob1: 30 iterations in 0.43 seconds (average 0.014333, setup 0.00)

yes = 47399, no = 1745849, maybe = 268703

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=21, nodes=80689] [3.7 MB]
Adding explicit sparse matrices... [levels=6, num=4890, compact] [679.9 KB]
Creating vector for diagonals... [dist=1, compact] [3.9 MB]
Creating vector for RHS... [dist=2, compact] [3.9 MB]
Allocating iteration vectors... [2 x 15.7 MB]
TOTAL: [43.7 MB]

Starting iterations...

Jacobi: 187 iterations in 5.47 seconds (average 0.018289, setup 2.05)

Value in the initial state: 0.08606841127862043

Time for model checking: 6.974 seconds.

Result: 0.08606841127862043 (+/- 7.183528306181446E-7 estimated; rel err 8.34630057586046E-6)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_crowds.5-20_rep3.log

```
Command(s):
../bin/prism  -importmodel models/crowds.5-20/prism.model.umb models/crowds.5-20/property.props
Wallclock time: 608.635 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:05 GMT+01:00 2026
Hostname: r23m0143.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/crowds.5-20/prism.model.umb models/crowds.5-20/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/crowds.5-20/property.props"...

1 property:
(1) "positive": P=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "positive": P=? [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 47 iterations in 2.86 seconds (average 0.060851, setup 0.00)

Time for model construction: 601.308 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 329533 nodes (7 terminal), 7374951 minterms, vars: 21r/21c

Prob0: 14 iterations in 0.66 seconds (average 0.047143, setup 0.00)

Prob1: 30 iterations in 0.56 seconds (average 0.018667, setup 0.00)

yes = 47399, no = 1745849, maybe = 268703

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=21, nodes=80689] [3.7 MB]
Adding explicit sparse matrices... [levels=6, num=4890, compact] [679.9 KB]
Creating vector for diagonals... [dist=1, compact] [3.9 MB]
Creating vector for RHS... [dist=2, compact] [3.9 MB]
Allocating iteration vectors... [2 x 15.7 MB]
TOTAL: [43.7 MB]

Starting iterations...

Jacobi: 187 iterations in 5.24 seconds (average 0.017219, setup 2.02)

Value in the initial state: 0.08606841127862043

Time for model checking: 6.505 seconds.

Result: 0.08606841127862043 (+/- 7.183528306181446E-7 estimated; rel err 8.34630057586046E-6)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_crowds.5-20_rep4.log

```
Command(s):
../bin/prism  -importmodel models/crowds.5-20/prism.model.umb models/crowds.5-20/property.props
Wallclock time: 457.197 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:10:45 GMT+01:00 2026
Hostname: r23m0017.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/crowds.5-20/prism.model.umb models/crowds.5-20/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/crowds.5-20/property.props"...

1 property:
(1) "positive": P=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "positive": P=? [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 47 iterations in 2.46 seconds (average 0.052340, setup 0.00)

Time for model construction: 449.733 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 329533 nodes (7 terminal), 7374951 minterms, vars: 21r/21c

Prob0: 14 iterations in 0.54 seconds (average 0.038571, setup 0.00)

Prob1: 30 iterations in 0.43 seconds (average 0.014333, setup 0.00)

yes = 47399, no = 1745849, maybe = 268703

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=21, nodes=80689] [3.7 MB]
Adding explicit sparse matrices... [levels=6, num=4890, compact] [679.9 KB]
Creating vector for diagonals... [dist=1, compact] [3.9 MB]
Creating vector for RHS... [dist=2, compact] [3.9 MB]
Allocating iteration vectors... [2 x 15.7 MB]
TOTAL: [43.7 MB]

Starting iterations...

Jacobi: 187 iterations in 5.55 seconds (average 0.018663, setup 2.06)

Value in the initial state: 0.08606841127862043

Time for model checking: 6.572 seconds.

Result: 0.08606841127862043 (+/- 7.183528306181446E-7 estimated; rel err 8.34630057586046E-6)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_crowds.5-20_rep5.log

```
Command(s):
../bin/prism  -importmodel models/crowds.5-20/prism.model.umb models/crowds.5-20/property.props
Wallclock time: 486.237 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:59:56 GMT+01:00 2026
Hostname: n23m0264.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/crowds.5-20/prism.model.umb models/crowds.5-20/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/crowds.5-20/property.props"...

1 property:
(1) "positive": P=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "positive": P=? [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 47 iterations in 2.45 seconds (average 0.052128, setup 0.00)

Time for model construction: 478.558 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 329533 nodes (7 terminal), 7374951 minterms, vars: 21r/21c

Prob0: 14 iterations in 0.55 seconds (average 0.039286, setup 0.00)

Prob1: 30 iterations in 0.42 seconds (average 0.014000, setup 0.00)

yes = 47399, no = 1745849, maybe = 268703

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=21, nodes=80689] [3.7 MB]
Adding explicit sparse matrices... [levels=6, num=4890, compact] [679.9 KB]
Creating vector for diagonals... [dist=1, compact] [3.9 MB]
Creating vector for RHS... [dist=2, compact] [3.9 MB]
Allocating iteration vectors... [2 x 15.7 MB]
TOTAL: [43.7 MB]

Starting iterations...

Jacobi: 187 iterations in 5.45 seconds (average 0.018396, setup 2.01)

Value in the initial state: 0.08606841127862043

Time for model checking: 6.501 seconds.

Result: 0.08606841127862043 (+/- 7.183528306181446E-7 estimated; rel err 8.34630057586046E-6)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

