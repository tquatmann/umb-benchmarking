# Log files

Tool configuration: prism_from-umb_check_default
Benchmark: [resource-gathering.1300-100-100](../../models/resource-gathering.1300-100-100)
Parsed values: [208.445, 310.673, 185.294, 190.793, 202.332]



### Log file: prism_from-umb_check_default_resource-gathering.1300-100-100_rep1.log

```
Command(s):
../bin/prism  -importmodel models/resource-gathering.1300-100-100/prism.model.umb models/resource-gathering.1300-100-100/property.props
Wallclock time: 265.937 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:28:08 GMT+01:00 2026
Hostname: r23m0212.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/resource-gathering.1300-100-100/prism.model.umb models/resource-gathering.1300-100-100/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [right] [left] [top] [down]
Variables:   x
Labels:      "success"

Parsing properties file "models/resource-gathering.1300-100-100/property.props"...

1 property:
(1) "prgoldgem": Pmax=? [ F<=1300 "success" ]

---------------------------------------------------------------------

Model checking: "prgoldgem": Pmax=? [ F<=1300 "success" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 1215 iterations in 42.70 seconds (average 0.035144, setup 0.00)

Time for model construction: 208.445 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 15588 nodes (4 terminal), 3325526 minterms, vars: 20r/20c/4nd

Prob0A: 1203 iterations in 34.91 seconds (average 0.029019, setup 0.00)

yes = 94, no = 0, maybe = 958800

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=20, nodes=20399] [956.2 KB]
Adding sparse bits... [levels=10-12, num=728, compact=4/4] [2.8 MB]
Creating vector for yes... [dist=2, compact] [1.8 MB]
Allocating iteration vectors... [3 x 7.3 MB]
TOTAL: [27.5 MB]

Starting iterations...
Iteration 302 (of 1300): 5.01 sec so far
Iteration 604 (of 1300): 10.03 sec so far
Iteration 903 (of 1300): 15.04 sec so far
Iteration 1203 (of 1300): 20.05 sec so far

Iterative method: 1300 iterations in 21.69 seconds (average 0.016646, setup 0.05)

Value in the initial state: 0.6630608525241822

Time for model checking: 56.726 seconds.

Result: 0.6630608525241822 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_resource-gathering.1300-100-100_rep2.log

```
Command(s):
../bin/prism  -importmodel models/resource-gathering.1300-100-100/prism.model.umb models/resource-gathering.1300-100-100/property.props
Wallclock time: 396.599 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:09 GMT+01:00 2026
Hostname: n23m0017.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/resource-gathering.1300-100-100/prism.model.umb models/resource-gathering.1300-100-100/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [right] [left] [top] [down]
Variables:   x
Labels:      "success"

Parsing properties file "models/resource-gathering.1300-100-100/property.props"...

1 property:
(1) "prgoldgem": Pmax=? [ F<=1300 "success" ]

---------------------------------------------------------------------

Model checking: "prgoldgem": Pmax=? [ F<=1300 "success" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 1215 iterations in 57.89 seconds (average 0.047646, setup 0.00)

Time for model construction: 310.673 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 15588 nodes (4 terminal), 3325526 minterms, vars: 20r/20c/4nd

Prob0A: 1203 iterations in 45.56 seconds (average 0.037872, setup 0.00)

yes = 94, no = 0, maybe = 958800

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=20, nodes=20399] [956.2 KB]
Adding sparse bits... [levels=10-12, num=728, compact=4/4] [2.8 MB]
Creating vector for yes... [dist=2, compact] [1.8 MB]
Allocating iteration vectors... [3 x 7.3 MB]
TOTAL: [27.5 MB]

Starting iterations...
Iteration 203 (of 1300): 5.02 sec so far
Iteration 409 (of 1300): 10.05 sec so far
Iteration 612 (of 1300): 15.06 sec so far
Iteration 817 (of 1300): 20.09 sec so far
Iteration 1021 (of 1300): 25.10 sec so far
Iteration 1225 (of 1300): 30.11 sec so far

Iterative method: 1300 iterations in 32.00 seconds (average 0.024562, setup 0.07)

Value in the initial state: 0.6630608525241822

Time for model checking: 77.836 seconds.

Result: 0.6630608525241822 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_resource-gathering.1300-100-100_rep3.log

```
Command(s):
../bin/prism  -importmodel models/resource-gathering.1300-100-100/prism.model.umb models/resource-gathering.1300-100-100/property.props
Wallclock time: 232.900 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:04 GMT+01:00 2026
Hostname: n23m0267.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/resource-gathering.1300-100-100/prism.model.umb models/resource-gathering.1300-100-100/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [right] [left] [top] [down]
Variables:   x
Labels:      "success"

Parsing properties file "models/resource-gathering.1300-100-100/property.props"...

1 property:
(1) "prgoldgem": Pmax=? [ F<=1300 "success" ]

---------------------------------------------------------------------

Model checking: "prgoldgem": Pmax=? [ F<=1300 "success" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 1215 iterations in 29.91 seconds (average 0.024617, setup 0.00)

Time for model construction: 185.294 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 15588 nodes (4 terminal), 3325526 minterms, vars: 20r/20c/4nd

Prob0A: 1203 iterations in 26.05 seconds (average 0.021654, setup 0.00)

yes = 94, no = 0, maybe = 958800

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=20, nodes=20399] [956.2 KB]
Adding sparse bits... [levels=10-12, num=728, compact=4/4] [2.8 MB]
Creating vector for yes... [dist=2, compact] [1.8 MB]
Allocating iteration vectors... [3 x 7.3 MB]
TOTAL: [27.5 MB]

Starting iterations...
Iteration 315 (of 1300): 5.02 sec so far
Iteration 630 (of 1300): 10.03 sec so far
Iteration 944 (of 1300): 15.04 sec so far
Iteration 1259 (of 1300): 20.05 sec so far

Iterative method: 1300 iterations in 20.72 seconds (average 0.015908, setup 0.04)

Value in the initial state: 0.6630608525241822

Time for model checking: 46.937 seconds.

Result: 0.6630608525241822 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_resource-gathering.1300-100-100_rep4.log

```
Command(s):
../bin/prism  -importmodel models/resource-gathering.1300-100-100/prism.model.umb models/resource-gathering.1300-100-100/property.props
Wallclock time: 239.250 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:11:21 GMT+01:00 2026
Hostname: n23m0313.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/resource-gathering.1300-100-100/prism.model.umb models/resource-gathering.1300-100-100/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [right] [left] [top] [down]
Variables:   x
Labels:      "success"

Parsing properties file "models/resource-gathering.1300-100-100/property.props"...

1 property:
(1) "prgoldgem": Pmax=? [ F<=1300 "success" ]

---------------------------------------------------------------------

Model checking: "prgoldgem": Pmax=? [ F<=1300 "success" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 1215 iterations in 30.00 seconds (average 0.024691, setup 0.00)

Time for model construction: 190.793 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 15588 nodes (4 terminal), 3325526 minterms, vars: 20r/20c/4nd

Prob0A: 1203 iterations in 26.08 seconds (average 0.021679, setup 0.00)

yes = 94, no = 0, maybe = 958800

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=20, nodes=20399] [956.2 KB]
Adding sparse bits... [levels=10-12, num=728, compact=4/4] [2.8 MB]
Creating vector for yes... [dist=2, compact] [1.8 MB]
Allocating iteration vectors... [3 x 7.3 MB]
TOTAL: [27.5 MB]

Starting iterations...
Iteration 303 (of 1300): 5.02 sec so far
Iteration 609 (of 1300): 10.03 sec so far
Iteration 916 (of 1300): 15.04 sec so far
Iteration 1224 (of 1300): 20.06 sec so far

Iterative method: 1300 iterations in 21.33 seconds (average 0.016369, setup 0.05)

Value in the initial state: 0.6630608525241822

Time for model checking: 47.613 seconds.

Result: 0.6630608525241822 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_resource-gathering.1300-100-100_rep5.log

```
Command(s):
../bin/prism  -importmodel models/resource-gathering.1300-100-100/prism.model.umb models/resource-gathering.1300-100-100/property.props
Wallclock time: 259.906 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:08 GMT+01:00 2026
Hostname: r23m0118.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/resource-gathering.1300-100-100/prism.model.umb models/resource-gathering.1300-100-100/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     [] [right] [left] [top] [down]
Variables:   x
Labels:      "success"

Parsing properties file "models/resource-gathering.1300-100-100/property.props"...

1 property:
(1) "prgoldgem": Pmax=? [ F<=1300 "success" ]

---------------------------------------------------------------------

Model checking: "prgoldgem": Pmax=? [ F<=1300 "success" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 10% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 1215 iterations in 32.06 seconds (average 0.026387, setup 0.00)

Time for model construction: 202.332 seconds.

Type:        MDP
States:      958894 (1 initial)
Transitions: 3325526

Transition matrix: 15588 nodes (4 terminal), 3325526 minterms, vars: 20r/20c/4nd

Prob0A: 1203 iterations in 28.21 seconds (average 0.023450, setup 0.00)

yes = 94, no = 0, maybe = 958800

Computing probabilities...
Engine: Hybrid

Building hybrid MTBDD matrices... [nm=4, levels=20, nodes=20399] [956.2 KB]
Adding sparse bits... [levels=10-12, num=728, compact=4/4] [2.8 MB]
Creating vector for yes... [dist=2, compact] [1.8 MB]
Allocating iteration vectors... [3 x 7.3 MB]
TOTAL: [27.5 MB]

Starting iterations...
Iteration 300 (of 1300): 5.01 sec so far
Iteration 594 (of 1300): 10.03 sec so far
Iteration 875 (of 1300): 15.05 sec so far
Iteration 1178 (of 1300): 20.07 sec so far

Iterative method: 1300 iterations in 22.40 seconds (average 0.017192, setup 0.05)

Value in the initial state: 0.6630608525241822

Time for model checking: 50.772 seconds.

Result: 0.6630608525241822 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

