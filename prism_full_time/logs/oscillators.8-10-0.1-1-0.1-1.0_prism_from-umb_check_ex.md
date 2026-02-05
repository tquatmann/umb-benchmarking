# Log files for prism_from-umb_check_ex on model [oscillators.8-10-0.1-1-0.1-1.0](../../models/oscillators.8-10-0.1-1-0.1-1.0)

Parsed values: `[1.884, 1.985, 3.322, 1.771, 2.661]`



### Log file: prism_from-umb_check_ex_oscillators.8-10-0.1-1-0.1-1.0_rep1.log

```
Command(s):
../bin/prism -ex -importmodel models/oscillators.8-10-0.1-1-0.1-1.0/prism.model.umb models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 1.884 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:30:14 GMT+01:00 2026
Hostname: r23m0206.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/oscillators.8-10-0.1-1-0.1-1.0/prism.model.umb models/oscillators.8-10-0.1-1-0.1-1.0/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     [step]
Variables:   x
Labels:      "target"
Rewards:     "time_to_synch"

Parsing properties file "models/oscillators.8-10-0.1-1-0.1-1.0/property.props"...

1 property:
(1) "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

Building model (engine:explicit)...

Time for model construction: 0.122 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623
Building reward structure...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.01 seconds)
Starting Prob1...
Prob1 took 0.011 seconds.
target=2, inf=0, rest=24309
Starting value iteration (with Jacobi) ...
Value iteration (with Jacobi) took 3154 iterations, 241662634 multiplications and 0.554 seconds.
Expected reachability took 0.587 seconds.

Value in the initial state: 6.007026913358374

Time for model checking: 0.62 seconds.

Result: 6.007026913358374 (+/- 5.972359070145227E-5 estimated; rel err 9.942287851023186E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_oscillators.8-10-0.1-1-0.1-1.0_rep2.log

```
Command(s):
../bin/prism -ex -importmodel models/oscillators.8-10-0.1-1-0.1-1.0/prism.model.umb models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 1.985 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:03 GMT+01:00 2026
Hostname: n23m0162.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/oscillators.8-10-0.1-1-0.1-1.0/prism.model.umb models/oscillators.8-10-0.1-1-0.1-1.0/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     [step]
Variables:   x
Labels:      "target"
Rewards:     "time_to_synch"

Parsing properties file "models/oscillators.8-10-0.1-1-0.1-1.0/property.props"...

1 property:
(1) "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

Building model (engine:explicit)...

Time for model construction: 0.085 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623
Building reward structure...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.012 seconds)
Starting Prob1...
Prob1 took 0.012 seconds.
target=2, inf=0, rest=24309
Starting value iteration (with Jacobi) ...
Value iteration (with Jacobi) took 3154 iterations, 241662634 multiplications and 0.598 seconds.
Expected reachability took 0.634 seconds.

Value in the initial state: 6.007026913358374

Time for model checking: 0.67 seconds.

Result: 6.007026913358374 (+/- 5.972359070145227E-5 estimated; rel err 9.942287851023186E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_oscillators.8-10-0.1-1-0.1-1.0_rep3.log

```
Command(s):
../bin/prism -ex -importmodel models/oscillators.8-10-0.1-1-0.1-1.0/prism.model.umb models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 3.322 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:28:58 GMT+01:00 2026
Hostname: n23m0119.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/oscillators.8-10-0.1-1-0.1-1.0/prism.model.umb models/oscillators.8-10-0.1-1-0.1-1.0/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     [step]
Variables:   x
Labels:      "target"
Rewards:     "time_to_synch"

Parsing properties file "models/oscillators.8-10-0.1-1-0.1-1.0/property.props"...

1 property:
(1) "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

Building model (engine:explicit)...

Time for model construction: 0.075 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623
Building reward structure...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.01 seconds)
Starting Prob1...
Prob1 took 0.011 seconds.
target=2, inf=0, rest=24309
Starting value iteration (with Jacobi) ...
Value iteration (with Jacobi) took 3154 iterations, 241662634 multiplications and 0.546 seconds.
Expected reachability took 0.577 seconds.

Value in the initial state: 6.007026913358374

Time for model checking: 0.624 seconds.

Result: 6.007026913358374 (+/- 5.972359070145227E-5 estimated; rel err 9.942287851023186E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_oscillators.8-10-0.1-1-0.1-1.0_rep4.log

```
Command(s):
../bin/prism -ex -importmodel models/oscillators.8-10-0.1-1-0.1-1.0/prism.model.umb models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 1.771 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:06 GMT+01:00 2026
Hostname: r23m0164.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/oscillators.8-10-0.1-1-0.1-1.0/prism.model.umb models/oscillators.8-10-0.1-1-0.1-1.0/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     [step]
Variables:   x
Labels:      "target"
Rewards:     "time_to_synch"

Parsing properties file "models/oscillators.8-10-0.1-1-0.1-1.0/property.props"...

1 property:
(1) "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

Building model (engine:explicit)...

Time for model construction: 0.082 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623
Building reward structure...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.011 seconds)
Starting Prob1...
Prob1 took 0.013 seconds.
target=2, inf=0, rest=24309
Starting value iteration (with Jacobi) ...
Value iteration (with Jacobi) took 3154 iterations, 241662634 multiplications and 0.558 seconds.
Expected reachability took 0.592 seconds.

Value in the initial state: 6.007026913358374

Time for model checking: 0.626 seconds.

Result: 6.007026913358374 (+/- 5.972359070145227E-5 estimated; rel err 9.942287851023186E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_oscillators.8-10-0.1-1-0.1-1.0_rep5.log

```
Command(s):
../bin/prism -ex -importmodel models/oscillators.8-10-0.1-1-0.1-1.0/prism.model.umb models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 2.661 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:14:27 GMT+01:00 2026
Hostname: n23m0101.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/oscillators.8-10-0.1-1-0.1-1.0/prism.model.umb models/oscillators.8-10-0.1-1-0.1-1.0/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     [step]
Variables:   x
Labels:      "target"
Rewards:     "time_to_synch"

Parsing properties file "models/oscillators.8-10-0.1-1-0.1-1.0/property.props"...

1 property:
(1) "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "time_to_synch": R{"time_to_synch"}=? [ F "target" ]

Building model (engine:explicit)...

Time for model construction: 0.108 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623
Building reward structure...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.014 seconds)
Starting Prob1...
Prob1 took 0.014 seconds.
target=2, inf=0, rest=24309
Starting value iteration (with Jacobi) ...
Value iteration (with Jacobi) took 3154 iterations, 241662634 multiplications and 0.658 seconds.
Expected reachability took 0.747 seconds.

Value in the initial state: 6.007026913358374

Time for model checking: 0.807 seconds.

Result: 6.007026913358374 (+/- 5.972359070145227E-5 estimated; rel err 9.942287851023186E-6)


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

