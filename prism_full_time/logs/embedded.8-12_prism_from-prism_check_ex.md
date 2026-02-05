# Log files for prism_from-prism_check_ex on model [embedded.8-12](../../models/embedded.8-12)

Parsed values: `[1.539, 1.261, 1.238, 1.397, 1.267]`



### Log file: prism_from-prism_check_ex_embedded.8-12_rep1.log

```
Command(s):
../bin/prism -ex models/embedded.8-12/model.prism models/embedded.8-12/property.props
Wallclock time: 1.539 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 08:01:05 GMT+01:00 2026
Hostname: n23m0389.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/embedded.8-12/model.prism models/embedded.8-12/property.props

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

Building model (engine:explicit)...

Computing reachable states... 8548 states
Reachable states exploration and model construction done in 0.128 secs.
Sorting reachable states list...

Time for model construction: 0.289 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041
Building embedded DTMC...

Starting probabilistic reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.018 seconds)
Starting Prob0...
Prob0 took 0.005 seconds.
Starting Prob1...
Prob1 took 0.005 seconds.
target=1064, yes=1064, no=6356, maybe=1128
Starting value iteration (with Jacobi)...
Value iteration (with Jacobi) took 687 iterations, 5072808 multiplications and 0.25 seconds.
Probabilistic reachability took 0.287 seconds.

Value in the initial state: 0.10529804738524096

Time for model checking: 0.385 seconds.

Result: 0.10529804738524096 (+/- 1.0374360534628648E-6 estimated; rel err 9.85237693598748E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_embedded.8-12_rep2.log

```
Command(s):
../bin/prism -ex models/embedded.8-12/model.prism models/embedded.8-12/property.props
Wallclock time: 1.261 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:07:38 GMT+01:00 2026
Hostname: n23m0392.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/embedded.8-12/model.prism models/embedded.8-12/property.props

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

Building model (engine:explicit)...

Computing reachable states... 8548 states
Reachable states exploration and model construction done in 0.088 secs.
Sorting reachable states list...

Time for model construction: 0.118 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041
Building embedded DTMC...

Starting probabilistic reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.017 seconds)
Starting Prob0...
Prob0 took 0.003 seconds.
Starting Prob1...
Prob1 took 0.006 seconds.
target=1064, yes=1064, no=6356, maybe=1128
Starting value iteration (with Jacobi)...
Value iteration (with Jacobi) took 687 iterations, 5072808 multiplications and 0.238 seconds.
Probabilistic reachability took 0.269 seconds.

Value in the initial state: 0.10529804738524096

Time for model checking: 0.307 seconds.

Result: 0.10529804738524096 (+/- 1.0374360534628648E-6 estimated; rel err 9.85237693598748E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_embedded.8-12_rep3.log

```
Command(s):
../bin/prism -ex models/embedded.8-12/model.prism models/embedded.8-12/property.props
Wallclock time: 1.238 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:23:32 GMT+01:00 2026
Hostname: r23m0204.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/embedded.8-12/model.prism models/embedded.8-12/property.props

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

Building model (engine:explicit)...

Computing reachable states... 8548 states
Reachable states exploration and model construction done in 0.084 secs.
Sorting reachable states list...

Time for model construction: 0.112 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041
Building embedded DTMC...

Starting probabilistic reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.016 seconds)
Starting Prob0...
Prob0 took 0.004 seconds.
Starting Prob1...
Prob1 took 0.005 seconds.
target=1064, yes=1064, no=6356, maybe=1128
Starting value iteration (with Jacobi)...
Value iteration (with Jacobi) took 687 iterations, 5072808 multiplications and 0.218 seconds.
Probabilistic reachability took 0.251 seconds.

Value in the initial state: 0.10529804738524096

Time for model checking: 0.303 seconds.

Result: 0.10529804738524096 (+/- 1.0374360534628648E-6 estimated; rel err 9.85237693598748E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_embedded.8-12_rep4.log

```
Command(s):
../bin/prism -ex models/embedded.8-12/model.prism models/embedded.8-12/property.props
Wallclock time: 1.397 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:28:57 GMT+01:00 2026
Hostname: n23m0033.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/embedded.8-12/model.prism models/embedded.8-12/property.props

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

Building model (engine:explicit)...

Computing reachable states... 8548 states
Reachable states exploration and model construction done in 0.102 secs.
Sorting reachable states list...

Time for model construction: 0.17 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041
Building embedded DTMC...

Starting probabilistic reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.018 seconds)
Starting Prob0...
Prob0 took 0.004 seconds.
Starting Prob1...
Prob1 took 0.005 seconds.
target=1064, yes=1064, no=6356, maybe=1128
Starting value iteration (with Jacobi)...
Value iteration (with Jacobi) took 687 iterations, 5072808 multiplications and 0.249 seconds.
Probabilistic reachability took 0.286 seconds.

Value in the initial state: 0.10529804738524096

Time for model checking: 0.386 seconds.

Result: 0.10529804738524096 (+/- 1.0374360534628648E-6 estimated; rel err 9.85237693598748E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_embedded.8-12_rep5.log

```
Command(s):
../bin/prism -ex models/embedded.8-12/model.prism models/embedded.8-12/property.props
Wallclock time: 1.267 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:04:34 GMT+01:00 2026
Hostname: r23m0023.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/embedded.8-12/model.prism models/embedded.8-12/property.props

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

Building model (engine:explicit)...

Computing reachable states... 8548 states
Reachable states exploration and model construction done in 0.091 secs.
Sorting reachable states list...

Time for model construction: 0.123 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041
Building embedded DTMC...

Starting probabilistic reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.019 seconds)
Starting Prob0...
Prob0 took 0.003 seconds.
Starting Prob1...
Prob1 took 0.006 seconds.
target=1064, yes=1064, no=6356, maybe=1128
Starting value iteration (with Jacobi)...
Value iteration (with Jacobi) took 687 iterations, 5072808 multiplications and 0.243 seconds.
Probabilistic reachability took 0.277 seconds.

Value in the initial state: 0.10529804738524096

Time for model checking: 0.334 seconds.

Result: 0.10529804738524096 (+/- 1.0374360534628648E-6 estimated; rel err 9.85237693598748E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

