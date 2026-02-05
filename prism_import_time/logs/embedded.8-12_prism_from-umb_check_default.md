# Log files

Tool configuration: prism_from-umb_check_default
Benchmark: [embedded.8-12](../../models/embedded.8-12)
Parsed values: [0.914, 1.022, 1.006, 1.02, 0.886]



### Log file: prism_from-umb_check_default_embedded.8-12_rep1.log

```
Command(s):
../bin/prism  -importmodel models/embedded.8-12/prism.model.umb models/embedded.8-12/property.props
Wallclock time: 1.583 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 08:04:10 GMT+01:00 2026
Hostname: r23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/embedded.8-12/prism.model.umb models/embedded.8-12/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   x
Labels:      "fail_actuators" "l_down"

Parsing properties file "models/embedded.8-12/property.props"...

1 property:
(1) "actuators": P=? [ !"l_down" U "fail_actuators" ]

---------------------------------------------------------------------

Model checking: "actuators": P=? [ !"l_down" U "fail_actuators" ]

Building model (engine:symbolic)...
Importing transitions... [ 100% ]

Computing reachable states...

Reachability (BFS): 21 iterations in 0.05 seconds (average 0.002381, setup 0.00)

Time for model construction: 0.914 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 9323 nodes (9 terminal), 36041 minterms, vars: 14r/14c

Diagonals vector: 768 nodes (69 terminal), 8548 minterms
Embedded Markov chain: 30780 nodes (309 terminal), 36041 minterms

Prob0: 4 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Prob1: 2 iterations in 0.01 seconds (average 0.005000, setup 0.00)

yes = 1064, no = 6356, maybe = 1128

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=14, nodes=10937] [512.7 KB]
Adding explicit sparse matrices... [levels=14, num=1, compact] [38.1 KB]
Creating vector for diagonals... [dist=5, compact] [16.7 KB]
Creating vector for RHS... [dist=2, compact] [16.7 KB]
Allocating iteration vectors... [2 x 66.8 KB]
TOTAL: [717.8 KB]

Starting iterations...

Jacobi: 687 iterations in 0.06 seconds (average 0.000044, setup 0.03)

Value in the initial state: 0.10529804738570939

Time for model checking: 0.081 seconds.

Result: 0.10529804738570939 (+/- 1.0374370755849761E-6 estimated; rel err 9.85238664288634E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_embedded.8-12_rep2.log

```
Command(s):
../bin/prism  -importmodel models/embedded.8-12/prism.model.umb models/embedded.8-12/property.props
Wallclock time: 1.919 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:00:30 GMT+01:00 2026
Hostname: n23m0072.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/embedded.8-12/prism.model.umb models/embedded.8-12/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   x
Labels:      "fail_actuators" "l_down"

Parsing properties file "models/embedded.8-12/property.props"...

1 property:
(1) "actuators": P=? [ !"l_down" U "fail_actuators" ]

---------------------------------------------------------------------

Model checking: "actuators": P=? [ !"l_down" U "fail_actuators" ]

Building model (engine:symbolic)...
Importing transitions... [ 100% ]

Computing reachable states...

Reachability (BFS): 21 iterations in 0.07 seconds (average 0.003333, setup 0.00)

Time for model construction: 1.022 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 9323 nodes (9 terminal), 36041 minterms, vars: 14r/14c

Diagonals vector: 768 nodes (69 terminal), 8548 minterms
Embedded Markov chain: 30780 nodes (309 terminal), 36041 minterms

Prob0: 4 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Prob1: 2 iterations in 0.01 seconds (average 0.005000, setup 0.00)

yes = 1064, no = 6356, maybe = 1128

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=14, nodes=10937] [512.7 KB]
Adding explicit sparse matrices... [levels=14, num=1, compact] [38.1 KB]
Creating vector for diagonals... [dist=5, compact] [16.7 KB]
Creating vector for RHS... [dist=2, compact] [16.7 KB]
Allocating iteration vectors... [2 x 66.8 KB]
TOTAL: [717.8 KB]

Starting iterations...

Jacobi: 687 iterations in 0.06 seconds (average 0.000044, setup 0.03)

Value in the initial state: 0.10529804738570939

Time for model checking: 0.093 seconds.

Result: 0.10529804738570939 (+/- 1.0374370755849761E-6 estimated; rel err 9.85238664288634E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_embedded.8-12_rep3.log

```
Command(s):
../bin/prism  -importmodel models/embedded.8-12/prism.model.umb models/embedded.8-12/property.props
Wallclock time: 5.733 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:08 GMT+01:00 2026
Hostname: n23m0157.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/embedded.8-12/prism.model.umb models/embedded.8-12/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   x
Labels:      "fail_actuators" "l_down"

Parsing properties file "models/embedded.8-12/property.props"...

1 property:
(1) "actuators": P=? [ !"l_down" U "fail_actuators" ]

---------------------------------------------------------------------

Model checking: "actuators": P=? [ !"l_down" U "fail_actuators" ]

Building model (engine:symbolic)...
Importing transitions... [ 100% ]

Computing reachable states...

Reachability (BFS): 21 iterations in 0.05 seconds (average 0.002381, setup 0.00)

Time for model construction: 1.006 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 9323 nodes (9 terminal), 36041 minterms, vars: 14r/14c

Diagonals vector: 768 nodes (69 terminal), 8548 minterms
Embedded Markov chain: 30780 nodes (309 terminal), 36041 minterms

Prob0: 4 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Prob1: 2 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1064, no = 6356, maybe = 1128

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=14, nodes=10937] [512.7 KB]
Adding explicit sparse matrices... [levels=14, num=1, compact] [38.1 KB]
Creating vector for diagonals... [dist=5, compact] [16.7 KB]
Creating vector for RHS... [dist=2, compact] [16.7 KB]
Allocating iteration vectors... [2 x 66.8 KB]
TOTAL: [717.8 KB]

Starting iterations...

Jacobi: 687 iterations in 0.06 seconds (average 0.000044, setup 0.03)

Value in the initial state: 0.10529804738570939

Time for model checking: 0.094 seconds.

Result: 0.10529804738570939 (+/- 1.0374370755849761E-6 estimated; rel err 9.85238664288634E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_embedded.8-12_rep4.log

```
Command(s):
../bin/prism  -importmodel models/embedded.8-12/prism.model.umb models/embedded.8-12/property.props
Wallclock time: 2.318 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:11:21 GMT+01:00 2026
Hostname: n23m0309.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/embedded.8-12/prism.model.umb models/embedded.8-12/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   x
Labels:      "fail_actuators" "l_down"

Parsing properties file "models/embedded.8-12/property.props"...

1 property:
(1) "actuators": P=? [ !"l_down" U "fail_actuators" ]

---------------------------------------------------------------------

Model checking: "actuators": P=? [ !"l_down" U "fail_actuators" ]

Building model (engine:symbolic)...
Importing transitions... [ 100% ]

Computing reachable states...

Reachability (BFS): 21 iterations in 0.06 seconds (average 0.002857, setup 0.00)

Time for model construction: 1.02 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 9323 nodes (9 terminal), 36041 minterms, vars: 14r/14c

Diagonals vector: 768 nodes (69 terminal), 8548 minterms
Embedded Markov chain: 30780 nodes (309 terminal), 36041 minterms

Prob0: 4 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Prob1: 2 iterations in 0.01 seconds (average 0.005000, setup 0.00)

yes = 1064, no = 6356, maybe = 1128

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=14, nodes=10937] [512.7 KB]
Adding explicit sparse matrices... [levels=14, num=1, compact] [38.1 KB]
Creating vector for diagonals... [dist=5, compact] [16.7 KB]
Creating vector for RHS... [dist=2, compact] [16.7 KB]
Allocating iteration vectors... [2 x 66.8 KB]
TOTAL: [717.8 KB]

Starting iterations...

Jacobi: 687 iterations in 0.06 seconds (average 0.000044, setup 0.03)

Value in the initial state: 0.10529804738570939

Time for model checking: 0.088 seconds.

Result: 0.10529804738570939 (+/- 1.0374370755849761E-6 estimated; rel err 9.85238664288634E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_default_embedded.8-12_rep5.log

```
Command(s):
../bin/prism  -importmodel models/embedded.8-12/prism.model.umb models/embedded.8-12/property.props
Wallclock time: 1.536 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:07:07 GMT+01:00 2026
Hostname: n23m0294.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -importmodel models/embedded.8-12/prism.model.umb models/embedded.8-12/property.props

Importing model from "prism.model.umb"...

Type:        CTMC
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   x
Labels:      "fail_actuators" "l_down"

Parsing properties file "models/embedded.8-12/property.props"...

1 property:
(1) "actuators": P=? [ !"l_down" U "fail_actuators" ]

---------------------------------------------------------------------

Model checking: "actuators": P=? [ !"l_down" U "fail_actuators" ]

Building model (engine:symbolic)...
Importing transitions... [ 100% ]

Computing reachable states...

Reachability (BFS): 21 iterations in 0.05 seconds (average 0.002381, setup 0.00)

Time for model construction: 0.886 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 9323 nodes (9 terminal), 36041 minterms, vars: 14r/14c

Diagonals vector: 768 nodes (69 terminal), 8548 minterms
Embedded Markov chain: 30780 nodes (309 terminal), 36041 minterms

Prob0: 4 iterations in 0.01 seconds (average 0.002500, setup 0.00)

Prob1: 2 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1064, no = 6356, maybe = 1128

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=14, nodes=10937] [512.7 KB]
Adding explicit sparse matrices... [levels=14, num=1, compact] [38.1 KB]
Creating vector for diagonals... [dist=5, compact] [16.7 KB]
Creating vector for RHS... [dist=2, compact] [16.7 KB]
Allocating iteration vectors... [2 x 66.8 KB]
TOTAL: [717.8 KB]

Starting iterations...

Jacobi: 687 iterations in 0.06 seconds (average 0.000044, setup 0.03)

Value in the initial state: 0.10529804738570939

Time for model checking: 0.077 seconds.

Result: 0.10529804738570939 (+/- 1.0374370755849761E-6 estimated; rel err 9.85238664288634E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

