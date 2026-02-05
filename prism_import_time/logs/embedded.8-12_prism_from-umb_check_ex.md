# Log files for prism_from-umb_check_ex on model [embedded.8-12](../../models/embedded.8-12)

Parsed values: `[0.063, 0.061, 0.086, 0.122, 0.086]`



### Log file: prism_from-umb_check_ex_embedded.8-12_rep1.log

```
Command(s):
../bin/prism -ex -importmodel models/embedded.8-12/prism.model.umb models/embedded.8-12/property.props
Wallclock time: 1.274 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 08:03:39 GMT+01:00 2026
Hostname: r23m0061.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/embedded.8-12/prism.model.umb models/embedded.8-12/property.props

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

Building model (engine:explicit)...

Time for model construction: 0.063 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041
Building embedded DTMC...

Starting probabilistic reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.018 seconds)
Starting Prob0...
Prob0 took 0.003 seconds.
Starting Prob1...
Prob1 took 0.005 seconds.
target=1064, yes=1064, no=6356, maybe=1128
Starting value iteration (with Jacobi)...
Value iteration (with Jacobi) took 687 iterations, 5072808 multiplications and 0.218 seconds.
Probabilistic reachability took 0.252 seconds.

Value in the initial state: 0.10529804738524096

Time for model checking: 0.31 seconds.

Result: 0.10529804738524096 (+/- 1.0374360534628648E-6 estimated; rel err 9.85237693598748E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_embedded.8-12_rep2.log

```
Command(s):
../bin/prism -ex -importmodel models/embedded.8-12/prism.model.umb models/embedded.8-12/property.props
Wallclock time: 1.270 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:22:36 GMT+01:00 2026
Hostname: n23m0109.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/embedded.8-12/prism.model.umb models/embedded.8-12/property.props

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

Building model (engine:explicit)...

Time for model construction: 0.061 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041
Building embedded DTMC...

Starting probabilistic reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.012 seconds)
Starting Prob0...
Prob0 took 0.004 seconds.
Starting Prob1...
Prob1 took 0.005 seconds.
target=1064, yes=1064, no=6356, maybe=1128
Starting value iteration (with Jacobi)...
Value iteration (with Jacobi) took 687 iterations, 5072808 multiplications and 0.241 seconds.
Probabilistic reachability took 0.268 seconds.

Value in the initial state: 0.10529804738524096

Time for model checking: 0.295 seconds.

Result: 0.10529804738524096 (+/- 1.0374360534628648E-6 estimated; rel err 9.85237693598748E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_embedded.8-12_rep3.log

```
Command(s):
../bin/prism -ex -importmodel models/embedded.8-12/prism.model.umb models/embedded.8-12/property.props
Wallclock time: 2.529 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:38 GMT+01:00 2026
Hostname: r23m0123.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/embedded.8-12/prism.model.umb models/embedded.8-12/property.props

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

Building model (engine:explicit)...

Time for model construction: 0.086 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041
Building embedded DTMC...

Starting probabilistic reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.017 seconds)
Starting Prob0...
Prob0 took 0.004 seconds.
Starting Prob1...
Prob1 took 0.004 seconds.
target=1064, yes=1064, no=6356, maybe=1128
Starting value iteration (with Jacobi)...
Value iteration (with Jacobi) took 687 iterations, 5072808 multiplications and 0.203 seconds.
Probabilistic reachability took 0.237 seconds.

Value in the initial state: 0.10529804738524096

Time for model checking: 0.28 seconds.

Result: 0.10529804738524096 (+/- 1.0374360534628648E-6 estimated; rel err 9.85237693598748E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_embedded.8-12_rep4.log

```
Command(s):
../bin/prism -ex -importmodel models/embedded.8-12/prism.model.umb models/embedded.8-12/property.props
Wallclock time: 1.317 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:18:31 GMT+01:00 2026
Hostname: n23m0402.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/embedded.8-12/prism.model.umb models/embedded.8-12/property.props

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

Building model (engine:explicit)...

Time for model construction: 0.122 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041
Building embedded DTMC...

Starting probabilistic reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.021 seconds)
Starting Prob0...
Prob0 took 0.006 seconds.
Starting Prob1...
Prob1 took 0.01 seconds.
target=1064, yes=1064, no=6356, maybe=1128
Starting value iteration (with Jacobi)...
Value iteration (with Jacobi) took 687 iterations, 5072808 multiplications and 0.251 seconds.
Probabilistic reachability took 0.296 seconds.

Value in the initial state: 0.10529804738524096

Time for model checking: 0.368 seconds.

Result: 0.10529804738524096 (+/- 1.0374360534628648E-6 estimated; rel err 9.85237693598748E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_embedded.8-12_rep5.log

```
Command(s):
../bin/prism -ex -importmodel models/embedded.8-12/prism.model.umb models/embedded.8-12/property.props
Wallclock time: 5.951 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:06 GMT+01:00 2026
Hostname: r23m0174.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/embedded.8-12/prism.model.umb models/embedded.8-12/property.props

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

Building model (engine:explicit)...

Time for model construction: 0.086 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041
Building embedded DTMC...

Starting probabilistic reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.015 seconds)
Starting Prob0...
Prob0 took 0.004 seconds.
Starting Prob1...
Prob1 took 0.004 seconds.
target=1064, yes=1064, no=6356, maybe=1128
Starting value iteration (with Jacobi)...
Value iteration (with Jacobi) took 687 iterations, 5072808 multiplications and 0.199 seconds.
Probabilistic reachability took 0.232 seconds.

Value in the initial state: 0.10529804738524096

Time for model checking: 0.272 seconds.

Result: 0.10529804738524096 (+/- 1.0374360534628648E-6 estimated; rel err 9.85237693598748E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

