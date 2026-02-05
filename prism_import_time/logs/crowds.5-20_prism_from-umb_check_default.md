# Log files for prism_from-umb_check_default on model [crowds.5-20](../../models/crowds.5-20)

Parsed values: `[453.755, 471.631, 409.719, 501.857, 1865.831]`



### Log file: prism_from-umb_check_default_crowds.5-20_rep1.log

```
Command(s):
../bin/prism  -importmodel models/crowds.5-20/prism.model.umb models/crowds.5-20/property.props
Wallclock time: 460.852 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:17:39 GMT+01:00 2026
Hostname: r23m0129.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 47 iterations in 2.28 seconds (average 0.048511, setup 0.00)

Time for model construction: 453.755 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 329533 nodes (7 terminal), 7374951 minterms, vars: 21r/21c

Prob0: 14 iterations in 0.52 seconds (average 0.037143, setup 0.00)

Prob1: 30 iterations in 0.38 seconds (average 0.012667, setup 0.00)

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

Jacobi: 187 iterations in 5.39 seconds (average 0.017647, setup 2.09)

Value in the initial state: 0.08606841127862043

Time for model checking: 6.339 seconds.

Result: 0.08606841127862043 (+/- 7.183528306181446E-7 estimated; rel err 8.34630057586046E-6)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_crowds.5-20_rep2.log

```
Command(s):
../bin/prism  -importmodel models/crowds.5-20/prism.model.umb models/crowds.5-20/property.props
Wallclock time: 480.240 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:08 GMT+01:00 2026
Hostname: r23m0154.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 47 iterations in 2.55 seconds (average 0.054255, setup 0.00)

Time for model construction: 471.631 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 329533 nodes (7 terminal), 7374951 minterms, vars: 21r/21c

Prob0: 14 iterations in 0.59 seconds (average 0.042143, setup 0.00)

Prob1: 30 iterations in 0.40 seconds (average 0.013333, setup 0.00)

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

Jacobi: 187 iterations in 5.00 seconds (average 0.016417, setup 1.93)

Value in the initial state: 0.08606841127862043

Time for model checking: 6.08 seconds.

Result: 0.08606841127862043 (+/- 7.183528306181446E-7 estimated; rel err 8.34630057586046E-6)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_crowds.5-20_rep3.log

```
Command(s):
../bin/prism  -importmodel models/crowds.5-20/prism.model.umb models/crowds.5-20/property.props
Wallclock time: 416.319 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:04:04 GMT+01:00 2026
Hostname: n23m0175.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 47 iterations in 2.22 seconds (average 0.047234, setup 0.00)

Time for model construction: 409.719 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 329533 nodes (7 terminal), 7374951 minterms, vars: 21r/21c

Prob0: 14 iterations in 0.48 seconds (average 0.034286, setup 0.00)

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

Jacobi: 187 iterations in 4.92 seconds (average 0.016203, setup 1.89)

Value in the initial state: 0.08606841127862043

Time for model checking: 5.823 seconds.

Result: 0.08606841127862043 (+/- 7.183528306181446E-7 estimated; rel err 8.34630057586046E-6)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_crowds.5-20_rep4.log

```
Command(s):
../bin/prism  -importmodel models/crowds.5-20/prism.model.umb models/crowds.5-20/property.props
Wallclock time: 510.389 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:28:51 GMT+01:00 2026
Hostname: r23m0204.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 47 iterations in 2.27 seconds (average 0.048298, setup 0.00)

Time for model construction: 501.857 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 329533 nodes (7 terminal), 7374951 minterms, vars: 21r/21c

Prob0: 14 iterations in 0.53 seconds (average 0.037857, setup 0.00)

Prob1: 30 iterations in 0.39 seconds (average 0.013000, setup 0.00)

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

Jacobi: 187 iterations in 5.20 seconds (average 0.016898, setup 2.04)

Value in the initial state: 0.08606841127862043

Time for model checking: 6.166 seconds.

Result: 0.08606841127862043 (+/- 7.183528306181446E-7 estimated; rel err 8.34630057586046E-6)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_crowds.5-20_rep5.log

```
Command(s):
../bin/prism  -importmodel models/crowds.5-20/prism.model.umb models/crowds.5-20/property.props
Wallclock time: 1892.558 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:12:30 GMT+01:00 2026
Hostname: r23m0215.hpc.itc.rwth-aachen.de
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

Reachability (BFS): 47 iterations in 7.52 seconds (average 0.160000, setup 0.00)

Time for model construction: 1865.831 seconds.

Warning: Deadlocks detected and fixed in 53130 states

Type:        DTMC
States:      2061951 (1 initial)
Transitions: 7374951

Transition matrix: 329533 nodes (7 terminal), 7374951 minterms, vars: 21r/21c

Prob0: 14 iterations in 1.73 seconds (average 0.123571, setup 0.00)

Prob1: 30 iterations in 1.67 seconds (average 0.055667, setup 0.00)

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
Iteration 77: max relative diff=0.006081, 5.05 sec so far
Iteration 154: max relative diff=0.000015, 10.11 sec so far

Jacobi: 187 iterations in 20.20 seconds (average 0.065615, setup 7.93)

Value in the initial state: 0.08606841127862043

Time for model checking: 23.916 seconds.

Result: 0.08606841127862043 (+/- 7.183528306181446E-7 estimated; rel err 8.34630057586046E-6)

---------------------------------------------------------------------

Note: There was 1 warning during computation.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

