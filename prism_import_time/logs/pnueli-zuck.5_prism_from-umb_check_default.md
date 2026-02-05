# Log files

Tool configuration: prism_from-umb_check_default
Benchmark: [pnueli-zuck.5](../../models/pnueli-zuck.5)
Parsed values: [122.978, 101.76, 191.64, 161.699, 162.426]



### Log file: prism_from-umb_check_default_pnueli-zuck.5_rep1.log

```
Command(s):
../bin/prism  -importmodel models/pnueli-zuck.5/prism.model.umb models/pnueli-zuck.5/property.props
Wallclock time: 129.327 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:31:15 GMT+01:00 2026
Hostname: r23m0066.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/pnueli-zuck.5/prism.model.umb models/pnueli-zuck.5/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/pnueli-zuck.5/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 6% 10% 14% 16% 20% 22% 26% 28% 32% 34% 36% 40% 42% 44% 46% 50% 52% 54% 58% 60% 62% 64% 66% 68% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 38 iterations in 3.53 seconds (average 0.092895, setup 0.00)

Time for model construction: 122.978 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2313746

Transition matrix: 173726 nodes (3 terminal), 2313746 minterms, vars: 19r/19c/10nd

Prob0A: 45 iterations in 3.05 seconds (average 0.067778, setup 0.00)

Prob1E: 46 iterations in 2.41 seconds (average 0.052391, setup 0.00)

yes = 397435, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 5.484 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_pnueli-zuck.5_rep2.log

```
Command(s):
../bin/prism  -importmodel models/pnueli-zuck.5/prism.model.umb models/pnueli-zuck.5/property.props
Wallclock time: 107.425 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:09:50 GMT+01:00 2026
Hostname: r23m0203.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/pnueli-zuck.5/prism.model.umb models/pnueli-zuck.5/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/pnueli-zuck.5/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 6% 10% 14% 18% 20% 24% 28% 30% 34% 36% 40% 44% 46% 50% 54% 56% 60% 62% 66% 68% 72% 74% 76% 78% 82% 84% 86% 90% 92% 94% 98% 100% ]

Computing reachable states...

Reachability (BFS): 38 iterations in 2.95 seconds (average 0.077632, setup 0.00)

Time for model construction: 101.76 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2313746

Transition matrix: 173726 nodes (3 terminal), 2313746 minterms, vars: 19r/19c/10nd

Prob0A: 45 iterations in 2.61 seconds (average 0.058000, setup 0.00)

Prob1E: 46 iterations in 1.83 seconds (average 0.039783, setup 0.00)

yes = 397435, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 4.445 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_pnueli-zuck.5_rep3.log

```
Command(s):
../bin/prism  -importmodel models/pnueli-zuck.5/prism.model.umb models/pnueli-zuck.5/property.props
Wallclock time: 200.026 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:03:01 GMT+01:00 2026
Hostname: n23m0279.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/pnueli-zuck.5/prism.model.umb models/pnueli-zuck.5/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/pnueli-zuck.5/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 6% 8% 12% 14% 16% 18% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 38 iterations in 4.50 seconds (average 0.118421, setup 0.00)

Time for model construction: 191.64 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2313746

Transition matrix: 173726 nodes (3 terminal), 2313746 minterms, vars: 19r/19c/10nd

Prob0A: 45 iterations in 3.99 seconds (average 0.088667, setup 0.00)

Prob1E: 46 iterations in 3.29 seconds (average 0.071522, setup 0.00)

yes = 397435, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 7.322 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_pnueli-zuck.5_rep4.log

```
Command(s):
../bin/prism  -importmodel models/pnueli-zuck.5/prism.model.umb models/pnueli-zuck.5/property.props
Wallclock time: 169.086 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 01:10:41 GMT+01:00 2026
Hostname: n23m0107.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/pnueli-zuck.5/prism.model.umb models/pnueli-zuck.5/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/pnueli-zuck.5/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 4% 8% 10% 12% 14% 16% 20% 22% 24% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 38 iterations in 4.03 seconds (average 0.106053, setup 0.00)

Time for model construction: 161.699 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2313746

Transition matrix: 173726 nodes (3 terminal), 2313746 minterms, vars: 19r/19c/10nd

Prob0A: 45 iterations in 3.52 seconds (average 0.078222, setup 0.00)

Prob1E: 46 iterations in 2.86 seconds (average 0.062174, setup 0.00)

yes = 397435, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 6.394 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_pnueli-zuck.5_rep5.log

```
Command(s):
../bin/prism  -importmodel models/pnueli-zuck.5/prism.model.umb models/pnueli-zuck.5/property.props
Wallclock time: 170.167 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:07:17 GMT+01:00 2026
Hostname: n23m0386.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/pnueli-zuck.5/prism.model.umb models/pnueli-zuck.5/property.props

Importing model from "prism.model.umb"...

Type:        MDP
Actions:     []
Variables:   x
Labels:      "target"

Parsing properties file "models/pnueli-zuck.5/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:symbolic)...
Importing transitions... [ 2% 6% 8% 12% 14% 18% 20% 22% 26% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 38 iterations in 3.90 seconds (average 0.102632, setup 0.00)

Time for model construction: 162.426 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2313746

Transition matrix: 173726 nodes (3 terminal), 2313746 minterms, vars: 19r/19c/10nd

Prob0A: 45 iterations in 3.34 seconds (average 0.074222, setup 0.00)

Prob1E: 46 iterations in 2.61 seconds (average 0.056739, setup 0.00)

yes = 397435, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 6.001 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

