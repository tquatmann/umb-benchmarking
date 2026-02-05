# Log files

Tool configuration: prism_from-umb_check_ex
Benchmark: [herman.15](../../models/herman.15)
Parsed values: [0.707, 0.435, 0.481, 0.63, 0.538]



### Log file: prism_from-umb_check_ex_herman.15_rep1.log

```
Command(s):
../bin/prism -ex -importmodel models/herman.15/prism.model.umb models/herman.15/property.props
Wallclock time: 5.917 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:19:12 GMT+01:00 2026
Hostname: r23m0071.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/herman.15/prism.model.umb models/herman.15/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     [step]
Variables:   x
Labels:      "stable"
Rewards:     "steps"

Parsing properties file "models/herman.15/property.props"...

1 property:
(1) "steps": filter(max, R=? [ F "stable" ], "init")

---------------------------------------------------------------------

Model checking: "steps": filter(max, R=? [ F "stable" ], "init")

Building model (engine:explicit)...

Time for model construction: 0.707 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908
Building reward structure...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.54 seconds)
Starting Prob1...
Prob1 took 0.2 seconds.
target=30, inf=0, rest=32738
Starting value iteration (with Jacobi) ...
Value iteration (with Jacobi) took 246 iterations, 3529816608 multiplications and 3.176 seconds.
Expected reachability took 3.928 seconds.

Maximum value over states satisfying filter: 33.332616661835104

There are 10 states with (approximately) this value:
5285:(5285)
9513:(9513)
10570:(10570)
11627:(11627)
13741:(13741)
19026:(19026)
21140:(21140)
22197:(22197)
23254:(23254)
27482:(27482)

Time for model checking: 4.238 seconds.

Result: 33.332616661835104


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_herman.15_rep2.log

```
Command(s):
../bin/prism -ex -importmodel models/herman.15/prism.model.umb models/herman.15/property.props
Wallclock time: 5.807 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:08:06 GMT+01:00 2026
Hostname: r23m0141.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/herman.15/prism.model.umb models/herman.15/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     [step]
Variables:   x
Labels:      "stable"
Rewards:     "steps"

Parsing properties file "models/herman.15/property.props"...

1 property:
(1) "steps": filter(max, R=? [ F "stable" ], "init")

---------------------------------------------------------------------

Model checking: "steps": filter(max, R=? [ F "stable" ], "init")

Building model (engine:explicit)...

Time for model construction: 0.435 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908
Building reward structure...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.521 seconds)
Starting Prob1...
Prob1 took 0.194 seconds.
target=30, inf=0, rest=32738
Starting value iteration (with Jacobi) ...
Value iteration (with Jacobi) took 246 iterations, 3529816608 multiplications and 3.262 seconds.
Expected reachability took 3.99 seconds.

Maximum value over states satisfying filter: 33.332616661835104

There are 10 states with (approximately) this value:
5285:(5285)
9513:(9513)
10570:(10570)
11627:(11627)
13741:(13741)
19026:(19026)
21140:(21140)
22197:(22197)
23254:(23254)
27482:(27482)

Time for model checking: 4.274 seconds.

Result: 33.332616661835104


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_herman.15_rep3.log

```
Command(s):
../bin/prism -ex -importmodel models/herman.15/prism.model.umb models/herman.15/property.props
Wallclock time: 13.322 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:10 GMT+01:00 2026
Hostname: r23m0110.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/herman.15/prism.model.umb models/herman.15/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     [step]
Variables:   x
Labels:      "stable"
Rewards:     "steps"

Parsing properties file "models/herman.15/property.props"...

1 property:
(1) "steps": filter(max, R=? [ F "stable" ], "init")

---------------------------------------------------------------------

Model checking: "steps": filter(max, R=? [ F "stable" ], "init")

Building model (engine:explicit)...

Time for model construction: 0.481 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908
Building reward structure...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.548 seconds)
Starting Prob1...
Prob1 took 0.217 seconds.
target=30, inf=0, rest=32738
Starting value iteration (with Jacobi) ...
Value iteration (with Jacobi) took 246 iterations, 3529816608 multiplications and 3.622 seconds.
Expected reachability took 4.4 seconds.

Maximum value over states satisfying filter: 33.332616661835104

There are 10 states with (approximately) this value:
5285:(5285)
9513:(9513)
10570:(10570)
11627:(11627)
13741:(13741)
19026:(19026)
21140:(21140)
22197:(22197)
23254:(23254)
27482:(27482)

Time for model checking: 4.689 seconds.

Result: 33.332616661835104


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_herman.15_rep4.log

```
Command(s):
../bin/prism -ex -importmodel models/herman.15/prism.model.umb models/herman.15/property.props
Wallclock time: 7.439 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:02 GMT+01:00 2026
Hostname: n23m0006.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/herman.15/prism.model.umb models/herman.15/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     [step]
Variables:   x
Labels:      "stable"
Rewards:     "steps"

Parsing properties file "models/herman.15/property.props"...

1 property:
(1) "steps": filter(max, R=? [ F "stable" ], "init")

---------------------------------------------------------------------

Model checking: "steps": filter(max, R=? [ F "stable" ], "init")

Building model (engine:explicit)...

Time for model construction: 0.63 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908
Building reward structure...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.584 seconds)
Starting Prob1...
Prob1 took 0.215 seconds.
target=30, inf=0, rest=32738
Starting value iteration (with Jacobi) ...
Value iteration (with Jacobi) took 246 iterations, 3529816608 multiplications and 3.892 seconds.
Expected reachability took 4.708 seconds.

Maximum value over states satisfying filter: 33.332616661835104

There are 10 states with (approximately) this value:
5285:(5285)
9513:(9513)
10570:(10570)
11627:(11627)
13741:(13741)
19026:(19026)
21140:(21140)
22197:(22197)
23254:(23254)
27482:(27482)

Time for model checking: 5.072 seconds.

Result: 33.332616661835104


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-umb_check_ex_herman.15_rep5.log

```
Command(s):
../bin/prism -ex -importmodel models/herman.15/prism.model.umb models/herman.15/property.props
Wallclock time: 7.325 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:57:24 GMT+01:00 2026
Hostname: n23m0028.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex -importmodel models/herman.15/prism.model.umb models/herman.15/property.props

Importing model from "prism.model.umb"...

Type:        DTMC
Actions:     [step]
Variables:   x
Labels:      "stable"
Rewards:     "steps"

Parsing properties file "models/herman.15/property.props"...

1 property:
(1) "steps": filter(max, R=? [ F "stable" ], "init")

---------------------------------------------------------------------

Model checking: "steps": filter(max, R=? [ F "stable" ], "init")

Building model (engine:explicit)...

Time for model construction: 0.538 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908
Building reward structure...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.502 seconds)
Starting Prob1...
Prob1 took 0.191 seconds.
target=30, inf=0, rest=32738
Starting value iteration (with Jacobi) ...
Value iteration (with Jacobi) took 246 iterations, 3529816608 multiplications and 3.256 seconds.
Expected reachability took 3.976 seconds.

Maximum value over states satisfying filter: 33.332616661835104

There are 10 states with (approximately) this value:
5285:(5285)
9513:(9513)
10570:(10570)
11627:(11627)
13741:(13741)
19026:(19026)
21140:(21140)
22197:(22197)
23254:(23254)
27482:(27482)

Time for model checking: 4.275 seconds.

Result: 33.332616661835104


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

