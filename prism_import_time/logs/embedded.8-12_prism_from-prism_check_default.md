# Log files

Tool configuration: prism_from-prism_check_default
Benchmark: [embedded.8-12](../../models/embedded.8-12)
Parsed values: [0.091, 0.03, 0.119, 0.033, 0.016]



### Log file: prism_from-prism_check_default_embedded.8-12_rep1.log

```
Command(s):
../bin/prism  models/embedded.8-12/model.prism models/embedded.8-12/property.props
Wallclock time: 1.497 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 08:03:07 GMT+01:00 2026
Hostname: r23m0016.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/embedded.8-12/model.prism models/embedded.8-12/property.props

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Parsing properties file "models/embedded.8-12/property.props"...

1 property:
(1) "actuators": P=? [ !"l_down" U "fail_actuators" ]

---------------------------------------------------------------------

Model checking: "actuators": P=? [ !"l_down" U "fail_actuators" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 21 iterations in 0.01 seconds (average 0.000476, setup 0.00)

Time for model construction: 0.091 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 1819 nodes (9 terminal), 36041 minterms, vars: 16r/16c

Diagonals vector: 841 nodes (69 terminal), 8548 minterms
Embedded Markov chain: 14290 nodes (309 terminal), 36041 minterms

Prob0: 4 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Prob1: 2 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1064, no = 6356, maybe = 1128

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=16, nodes=7951] [372.7 KB]
Adding explicit sparse matrices... [levels=16, num=1, compact] [38.1 KB]
Creating vector for diagonals... [dist=5, compact] [16.7 KB]
Creating vector for RHS... [dist=2, compact] [16.7 KB]
Allocating iteration vectors... [2 x 66.8 KB]
TOTAL: [577.8 KB]

Starting iterations...

Jacobi: 687 iterations in 0.05 seconds (average 0.000058, setup 0.01)

Value in the initial state: 0.10529804738570911

Time for model checking: 0.095 seconds.

Result: 0.10529804738570911 (+/- 1.037437075584976E-6 estimated; rel err 9.852386642886364E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_embedded.8-12_rep2.log

```
Command(s):
../bin/prism  models/embedded.8-12/model.prism models/embedded.8-12/property.props
Wallclock time: 1.487 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:04 GMT+01:00 2026
Hostname: n23m0220.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/embedded.8-12/model.prism models/embedded.8-12/property.props

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Parsing properties file "models/embedded.8-12/property.props"...

1 property:
(1) "actuators": P=? [ !"l_down" U "fail_actuators" ]

---------------------------------------------------------------------

Model checking: "actuators": P=? [ !"l_down" U "fail_actuators" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 21 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.03 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 1819 nodes (9 terminal), 36041 minterms, vars: 16r/16c

Diagonals vector: 841 nodes (69 terminal), 8548 minterms
Embedded Markov chain: 14290 nodes (309 terminal), 36041 minterms

Prob0: 4 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Prob1: 2 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1064, no = 6356, maybe = 1128

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=16, nodes=7951] [372.7 KB]
Adding explicit sparse matrices... [levels=16, num=1, compact] [38.1 KB]
Creating vector for diagonals... [dist=5, compact] [16.7 KB]
Creating vector for RHS... [dist=2, compact] [16.7 KB]
Allocating iteration vectors... [2 x 66.8 KB]
TOTAL: [577.8 KB]

Starting iterations...

Jacobi: 687 iterations in 0.04 seconds (average 0.000044, setup 0.01)

Value in the initial state: 0.10529804738570911

Time for model checking: 0.054 seconds.

Result: 0.10529804738570911 (+/- 1.037437075584976E-6 estimated; rel err 9.852386642886364E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_embedded.8-12_rep3.log

```
Command(s):
../bin/prism  models/embedded.8-12/model.prism models/embedded.8-12/property.props
Wallclock time: 0.726 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:08:12 GMT+01:00 2026
Hostname: n23m0028.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/embedded.8-12/model.prism models/embedded.8-12/property.props

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Parsing properties file "models/embedded.8-12/property.props"...

1 property:
(1) "actuators": P=? [ !"l_down" U "fail_actuators" ]

---------------------------------------------------------------------

Model checking: "actuators": P=? [ !"l_down" U "fail_actuators" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 21 iterations in 0.01 seconds (average 0.000476, setup 0.00)

Time for model construction: 0.119 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 1819 nodes (9 terminal), 36041 minterms, vars: 16r/16c

Diagonals vector: 841 nodes (69 terminal), 8548 minterms
Embedded Markov chain: 14290 nodes (309 terminal), 36041 minterms

Prob0: 4 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Prob1: 2 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1064, no = 6356, maybe = 1128

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=16, nodes=7951] [372.7 KB]
Adding explicit sparse matrices... [levels=16, num=1, compact] [38.1 KB]
Creating vector for diagonals... [dist=5, compact] [16.7 KB]
Creating vector for RHS... [dist=2, compact] [16.7 KB]
Allocating iteration vectors... [2 x 66.8 KB]
TOTAL: [577.8 KB]

Starting iterations...

Jacobi: 687 iterations in 0.04 seconds (average 0.000044, setup 0.01)

Value in the initial state: 0.10529804738570911

Time for model checking: 0.065 seconds.

Result: 0.10529804738570911 (+/- 1.037437075584976E-6 estimated; rel err 9.852386642886364E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_embedded.8-12_rep4.log

```
Command(s):
../bin/prism  models/embedded.8-12/model.prism models/embedded.8-12/property.props
Wallclock time: 0.997 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:01 GMT+01:00 2026
Hostname: n23m0249.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/embedded.8-12/model.prism models/embedded.8-12/property.props

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Parsing properties file "models/embedded.8-12/property.props"...

1 property:
(1) "actuators": P=? [ !"l_down" U "fail_actuators" ]

---------------------------------------------------------------------

Model checking: "actuators": P=? [ !"l_down" U "fail_actuators" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 21 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.033 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 1819 nodes (9 terminal), 36041 minterms, vars: 16r/16c

Diagonals vector: 841 nodes (69 terminal), 8548 minterms
Embedded Markov chain: 14290 nodes (309 terminal), 36041 minterms

Prob0: 4 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Prob1: 2 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1064, no = 6356, maybe = 1128

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=16, nodes=7951] [372.7 KB]
Adding explicit sparse matrices... [levels=16, num=1, compact] [38.1 KB]
Creating vector for diagonals... [dist=5, compact] [16.7 KB]
Creating vector for RHS... [dist=2, compact] [16.7 KB]
Allocating iteration vectors... [2 x 66.8 KB]
TOTAL: [577.8 KB]

Starting iterations...

Jacobi: 687 iterations in 0.04 seconds (average 0.000044, setup 0.01)

Value in the initial state: 0.10529804738570911

Time for model checking: 0.072 seconds.

Result: 0.10529804738570911 (+/- 1.037437075584976E-6 estimated; rel err 9.852386642886364E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_default_embedded.8-12_rep5.log

```
Command(s):
../bin/prism  models/embedded.8-12/model.prism models/embedded.8-12/property.props
Wallclock time: 0.608 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:15:26 GMT+01:00 2026
Hostname: n23m0313.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/embedded.8-12/model.prism models/embedded.8-12/property.props

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Parsing properties file "models/embedded.8-12/property.props"...

1 property:
(1) "actuators": P=? [ !"l_down" U "fail_actuators" ]

---------------------------------------------------------------------

Model checking: "actuators": P=? [ !"l_down" U "fail_actuators" ]

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 21 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Time for model construction: 0.016 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Rate matrix: 1819 nodes (9 terminal), 36041 minterms, vars: 16r/16c

Diagonals vector: 841 nodes (69 terminal), 8548 minterms
Embedded Markov chain: 14290 nodes (309 terminal), 36041 minterms

Prob0: 4 iterations in 0.00 seconds (average 0.000000, setup 0.00)

Prob1: 2 iterations in 0.00 seconds (average 0.000000, setup 0.00)

yes = 1064, no = 6356, maybe = 1128

Computing remaining probabilities...
Engine: Hybrid

Building hybrid MTBDD matrix... [levels=16, nodes=7951] [372.7 KB]
Adding explicit sparse matrices... [levels=16, num=1, compact] [38.1 KB]
Creating vector for diagonals... [dist=5, compact] [16.7 KB]
Creating vector for RHS... [dist=2, compact] [16.7 KB]
Allocating iteration vectors... [2 x 66.8 KB]
TOTAL: [577.8 KB]

Starting iterations...

Jacobi: 687 iterations in 0.04 seconds (average 0.000044, setup 0.01)

Value in the initial state: 0.10529804738570911

Time for model checking: 0.048 seconds.

Result: 0.10529804738570911 (+/- 1.037437075584976E-6 estimated; rel err 9.852386642886364E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

