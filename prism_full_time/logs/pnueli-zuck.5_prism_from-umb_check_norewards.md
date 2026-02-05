# Log files

Tool configuration: prism_from-umb_check_norewards
Benchmark: [pnueli-zuck.5](../../models/pnueli-zuck.5)
Parsed values: [114.06, 114.922, 111.663, 104.504, 153.869]



### Log file: prism_from-umb_check_norewards_pnueli-zuck.5_rep1.log

```
Command(s):
../bin/prism  -importmodel models/pnueli-zuck.5/prism.model.umb models/pnueli-zuck.5/property.props
Wallclock time: 114.060 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:57:14 GMT+01:00 2026
Hostname: n23m0288.hpc.itc.rwth-aachen.de
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
Importing transitions... [ 2% 6% 10% 14% 18% 20% 24% 28% 30% 34% 36% 40% 42% 44% 48% 50% 54% 56% 58% 62% 64% 66% 68% 72% 74% 76% 78% 80% 84% 86% 88% 90% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 38 iterations in 3.05 seconds (average 0.080263, setup 0.00)

Time for model construction: 108.659 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2313746

Transition matrix: 173726 nodes (3 terminal), 2313746 minterms, vars: 19r/19c/10nd

Prob0A: 45 iterations in 2.62 seconds (average 0.058222, setup 0.00)

Prob1E: 46 iterations in 1.97 seconds (average 0.042826, setup 0.00)

yes = 397435, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 4.614 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_pnueli-zuck.5_rep2.log

```
Command(s):
../bin/prism  -importmodel models/pnueli-zuck.5/prism.model.umb models/pnueli-zuck.5/property.props
Wallclock time: 114.922 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:22:01 GMT+01:00 2026
Hostname: r23m0204.hpc.itc.rwth-aachen.de
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
Importing transitions... [ 2% 6% 10% 14% 16% 18% 22% 26% 28% 32% 34% 36% 38% 40% 44% 48% 50% 54% 56% 60% 62% 66% 68% 70% 74% 76% 78% 80% 84% 86% 88% 90% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 38 iterations in 2.91 seconds (average 0.076579, setup 0.00)

Time for model construction: 109.117 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2313746

Transition matrix: 173726 nodes (3 terminal), 2313746 minterms, vars: 19r/19c/10nd

Prob0A: 45 iterations in 2.60 seconds (average 0.057778, setup 0.00)

Prob1E: 46 iterations in 2.37 seconds (average 0.051522, setup 0.00)

yes = 397435, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 4.98 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_pnueli-zuck.5_rep3.log

```
Command(s):
../bin/prism  -importmodel models/pnueli-zuck.5/prism.model.umb models/pnueli-zuck.5/property.props
Wallclock time: 111.663 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:36:53 GMT+01:00 2026
Hostname: n23m0328.hpc.itc.rwth-aachen.de
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
Importing transitions... [ 2% 6% 10% 14% 16% 20% 24% 26% 30% 32% 36% 38% 42% 44% 48% 50% 52% 56% 58% 62% 64% 68% 70% 72% 76% 78% 80% 82% 86% 88% 90% 92% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 38 iterations in 2.94 seconds (average 0.077368, setup 0.00)

Time for model construction: 106.254 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2313746

Transition matrix: 173726 nodes (3 terminal), 2313746 minterms, vars: 19r/19c/10nd

Prob0A: 45 iterations in 2.63 seconds (average 0.058444, setup 0.00)

Prob1E: 46 iterations in 1.98 seconds (average 0.043043, setup 0.00)

yes = 397435, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 4.623 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_pnueli-zuck.5_rep4.log

```
Command(s):
../bin/prism  -importmodel models/pnueli-zuck.5/prism.model.umb models/pnueli-zuck.5/property.props
Wallclock time: 104.504 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:21 GMT+01:00 2026
Hostname: n23m0340.hpc.itc.rwth-aachen.de
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
Importing transitions... [ 2% 6% 10% 14% 18% 20% 24% 28% 30% 34% 38% 40% 44% 46% 50% 54% 56% 60% 62% 66% 68% 72% 74% 78% 80% 82% 86% 88% 90% 94% 96% 100% ]

Computing reachable states...

Reachability (BFS): 38 iterations in 2.88 seconds (average 0.075789, setup 0.00)

Time for model construction: 99.033 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2313746

Transition matrix: 173726 nodes (3 terminal), 2313746 minterms, vars: 19r/19c/10nd

Prob0A: 45 iterations in 2.56 seconds (average 0.056889, setup 0.00)

Prob1E: 46 iterations in 2.07 seconds (average 0.045000, setup 0.00)

yes = 397435, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 4.639 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_norewards_pnueli-zuck.5_rep5.log

```
Command(s):
../bin/prism  -importmodel models/pnueli-zuck.5/prism.model.umb models/pnueli-zuck.5/property.props
Wallclock time: 153.869 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:10:51 GMT+01:00 2026
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
Importing transitions... [ 2% 6% 8% 12% 14% 18% 20% 22% 24% 28% 30% 32% 34% 36% 38% 40% 42% 44% 46% 48% 50% 52% 54% 56% 58% 60% 62% 64% 66% 68% 70% 72% 74% 76% 78% 80% 82% 84% 86% 88% 90% 92% 94% 96% 98% 100% ]

Computing reachable states...

Reachability (BFS): 38 iterations in 3.69 seconds (average 0.097105, setup 0.00)

Time for model construction: 147.346 seconds.

Type:        MDP
States:      397435 (1 initial)
Transitions: 2313746

Transition matrix: 173726 nodes (3 terminal), 2313746 minterms, vars: 19r/19c/10nd

Prob0A: 45 iterations in 3.19 seconds (average 0.070889, setup 0.00)

Prob1E: 46 iterations in 2.60 seconds (average 0.056522, setup 0.00)

yes = 397435, no = 0, maybe = 0

Value in the initial state: 1.0

Time for model checking: 5.798 seconds.

Result: 1.0 (exact floating point)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

