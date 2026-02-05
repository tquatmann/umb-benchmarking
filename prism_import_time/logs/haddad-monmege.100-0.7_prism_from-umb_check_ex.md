# Log files

Tool configuration: prism_from-umb_check_ex
Benchmark: [haddad-monmege.100-0.7](../../models/haddad-monmege.100-0.7)
Parsed values: [0.192, 0.068, 0.067, 0.055, 0.061]



### Log file: prism_from-umb_check_ex_haddad-monmege.100-0.7_rep1.log

```
Command(s):
../bin/prism -ex -importmodel models/haddad-monmege.100-0.7/prism.model.umb models/haddad-monmege.100-0.7/property.props
Wallclock time: 1.751 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:28:40 GMT+01:00 2026
Hostname: n23m0288.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/haddad-monmege.100-0.7/prism.model.umb models/haddad-monmege.100-0.7/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     []
Variables:   x
Labels:      "Target"

Parsing properties file "models/haddad-monmege.100-0.7/property.props"...

1 property:
(1) "target": P=? [ F "Target" ]

---------------------------------------------------------------------

Model checking: "target": P=? [ F "Target" ]

Building model (engine:explicit)...

Time for model construction: 0.192 seconds.

Type:        DTMC
States:      201 (1 initial)
Transitions: 400

Starting probabilistic reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.001 seconds)
Starting Prob0...
Prob0 took 0.003 seconds.
Starting Prob1...
Prob1 took 0.0 seconds.
target=1, yes=1, no=1, maybe=199
Starting value iteration (with Jacobi)...
Value iteration (with Jacobi) took 10000 iterations, 3980000 multiplications and 0.028 seconds.

Error: Iterative method did not converge within 10000 iterations.
Consider using a different numerical method or increasing the maximum number of iterations.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_haddad-monmege.100-0.7_rep2.log

```
Command(s):
../bin/prism -ex -importmodel models/haddad-monmege.100-0.7/prism.model.umb models/haddad-monmege.100-0.7/property.props
Wallclock time: 1.255 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:02:32 GMT+01:00 2026
Hostname: r23m0023.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/haddad-monmege.100-0.7/prism.model.umb models/haddad-monmege.100-0.7/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     []
Variables:   x
Labels:      "Target"

Parsing properties file "models/haddad-monmege.100-0.7/property.props"...

1 property:
(1) "target": P=? [ F "Target" ]

---------------------------------------------------------------------

Model checking: "target": P=? [ F "Target" ]

Building model (engine:explicit)...

Time for model construction: 0.068 seconds.

Type:        DTMC
States:      201 (1 initial)
Transitions: 400

Starting probabilistic reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.001 seconds)
Starting Prob0...
Prob0 took 0.001 seconds.
Starting Prob1...
Prob1 took 0.001 seconds.
target=1, yes=1, no=1, maybe=199
Starting value iteration (with Jacobi)...
Value iteration (with Jacobi) took 10000 iterations, 3980000 multiplications and 0.025 seconds.

Error: Iterative method did not converge within 10000 iterations.
Consider using a different numerical method or increasing the maximum number of iterations.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_haddad-monmege.100-0.7_rep3.log

```
Command(s):
../bin/prism -ex -importmodel models/haddad-monmege.100-0.7/prism.model.umb models/haddad-monmege.100-0.7/property.props
Wallclock time: 1.282 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:06 GMT+01:00 2026
Hostname: n23m0059.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/haddad-monmege.100-0.7/prism.model.umb models/haddad-monmege.100-0.7/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     []
Variables:   x
Labels:      "Target"

Parsing properties file "models/haddad-monmege.100-0.7/property.props"...

1 property:
(1) "target": P=? [ F "Target" ]

---------------------------------------------------------------------

Model checking: "target": P=? [ F "Target" ]

Building model (engine:explicit)...

Time for model construction: 0.067 seconds.

Type:        DTMC
States:      201 (1 initial)
Transitions: 400

Starting probabilistic reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.002 seconds)
Starting Prob0...
Prob0 took 0.003 seconds.
Starting Prob1...
Prob1 took 0.0 seconds.
target=1, yes=1, no=1, maybe=199
Starting value iteration (with Jacobi)...
Value iteration (with Jacobi) took 10000 iterations, 3980000 multiplications and 0.029 seconds.

Error: Iterative method did not converge within 10000 iterations.
Consider using a different numerical method or increasing the maximum number of iterations.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_haddad-monmege.100-0.7_rep4.log

```
Command(s):
../bin/prism -ex -importmodel models/haddad-monmege.100-0.7/prism.model.umb models/haddad-monmege.100-0.7/property.props
Wallclock time: 1.564 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:06 GMT+01:00 2026
Hostname: r23m0136.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/haddad-monmege.100-0.7/prism.model.umb models/haddad-monmege.100-0.7/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     []
Variables:   x
Labels:      "Target"

Parsing properties file "models/haddad-monmege.100-0.7/property.props"...

1 property:
(1) "target": P=? [ F "Target" ]

---------------------------------------------------------------------

Model checking: "target": P=? [ F "Target" ]

Building model (engine:explicit)...

Time for model construction: 0.055 seconds.

Type:        DTMC
States:      201 (1 initial)
Transitions: 400

Starting probabilistic reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.001 seconds)
Starting Prob0...
Prob0 took 0.002 seconds.
Starting Prob1...
Prob1 took 0.0 seconds.
target=1, yes=1, no=1, maybe=199
Starting value iteration (with Jacobi)...
Value iteration (with Jacobi) took 10000 iterations, 3980000 multiplications and 0.026 seconds.

Error: Iterative method did not converge within 10000 iterations.
Consider using a different numerical method or increasing the maximum number of iterations.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_haddad-monmege.100-0.7_rep5.log

```
Command(s):
../bin/prism -ex -importmodel models/haddad-monmege.100-0.7/prism.model.umb models/haddad-monmege.100-0.7/property.props
Wallclock time: 1.676 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:37 GMT+01:00 2026
Hostname: r23m0093.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/haddad-monmege.100-0.7/prism.model.umb models/haddad-monmege.100-0.7/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     []
Variables:   x
Labels:      "Target"

Parsing properties file "models/haddad-monmege.100-0.7/property.props"...

1 property:
(1) "target": P=? [ F "Target" ]

---------------------------------------------------------------------

Model checking: "target": P=? [ F "Target" ]

Building model (engine:explicit)...

Time for model construction: 0.061 seconds.

Type:        DTMC
States:      201 (1 initial)
Transitions: 400

Starting probabilistic reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.001 seconds)
Starting Prob0...
Prob0 took 0.002 seconds.
Starting Prob1...
Prob1 took 0.001 seconds.
target=1, yes=1, no=1, maybe=199
Starting value iteration (with Jacobi)...
Value iteration (with Jacobi) took 10000 iterations, 3980000 multiplications and 0.031 seconds.

Error: Iterative method did not converge within 10000 iterations.
Consider using a different numerical method or increasing the maximum number of iterations.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

