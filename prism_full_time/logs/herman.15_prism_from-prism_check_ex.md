# Log files

Tool configuration: prism_from-prism_check_ex
Benchmark: [herman.15](../../models/herman.15)
Parsed values: [25.645, 27.943, 24.14, 25.73, 25.152]



### Log file: prism_from-prism_check_ex_herman.15_rep1.log

```
Command(s):
../bin/prism -ex models/herman.15/model.prism models/herman.15/property.props
Wallclock time: 25.645 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:29:42 GMT+01:00 2026
Hostname: r23m0211.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/herman.15/model.prism models/herman.15/property.props

Parsing PRISM model file "models/herman.15/model.prism"...

Type:        DTMC
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10 process11 process12 process13 process14 process15
Actions:     [step]
Variables:   x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15
Labels:      "stable"
Rewards:     "steps"

Parsing properties file "models/herman.15/property.props"...

1 property:
(1) "steps": filter(max, R=? [ F "stable" ], "init")

---------------------------------------------------------------------

Model checking: "steps": filter(max, R=? [ F "stable" ], "init")

Building model (engine:explicit)...

Computing reachable states... 1020 6924 16093 24516 30598 32710 32768 states
Reachable states exploration and model construction done in 19.01 secs.
Sorting reachable states list...

Time for model construction: 20.201 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908
Building reward structure...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.291 seconds)
Starting Prob1...
Prob1 took 0.559 seconds.
target=30, inf=0, rest=32738
Starting value iteration (with Jacobi) ...
Value iteration (with Jacobi) took 246 iterations, 3529816608 multiplications and 3.382 seconds.
Expected reachability took 4.248 seconds.

Maximum value over states satisfying filter: 33.332616661835104

There are 10 states with (approximately) this value:
5285:(0,0,1,0,1,0,0,1,0,1,0,0,1,0,1)
9513:(0,1,0,0,1,0,1,0,0,1,0,1,0,0,1)
10570:(0,1,0,1,0,0,1,0,1,0,0,1,0,1,0)
11627:(0,1,0,1,1,0,1,0,1,1,0,1,0,1,1)
13741:(0,1,1,0,1,0,1,1,0,1,0,1,1,0,1)
19026:(1,0,0,1,0,1,0,0,1,0,1,0,0,1,0)
21140:(1,0,1,0,0,1,0,1,0,0,1,0,1,0,0)
22197:(1,0,1,0,1,1,0,1,0,1,1,0,1,0,1)
23254:(1,0,1,1,0,1,0,1,1,0,1,0,1,1,0)
27482:(1,1,0,1,0,1,1,0,1,0,1,1,0,1,0)

Time for model checking: 4.592 seconds.

Result: 33.332616661835104


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_herman.15_rep2.log

```
Command(s):
../bin/prism -ex models/herman.15/model.prism models/herman.15/property.props
Wallclock time: 27.943 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:06:06 GMT+01:00 2026
Hostname: n23m0392.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/herman.15/model.prism models/herman.15/property.props

Parsing PRISM model file "models/herman.15/model.prism"...

Type:        DTMC
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10 process11 process12 process13 process14 process15
Actions:     [step]
Variables:   x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15
Labels:      "stable"
Rewards:     "steps"

Parsing properties file "models/herman.15/property.props"...

1 property:
(1) "steps": filter(max, R=? [ F "stable" ], "init")

---------------------------------------------------------------------

Model checking: "steps": filter(max, R=? [ F "stable" ], "init")

Building model (engine:explicit)...

Computing reachable states... 911 5061 14361 19976 28680 32274 32768 states
Reachable states exploration and model construction done in 20.169 secs.
Sorting reachable states list...

Time for model construction: 21.409 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908
Building reward structure...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.367 seconds)
Starting Prob1...
Prob1 took 0.595 seconds.
target=30, inf=0, rest=32738
Starting value iteration (with Jacobi) ...
Value iteration (with Jacobi) took 246 iterations, 3529816608 multiplications and 4.115 seconds.
Expected reachability took 5.09 seconds.

Maximum value over states satisfying filter: 33.332616661835104

There are 10 states with (approximately) this value:
5285:(0,0,1,0,1,0,0,1,0,1,0,0,1,0,1)
9513:(0,1,0,0,1,0,1,0,0,1,0,1,0,0,1)
10570:(0,1,0,1,0,0,1,0,1,0,0,1,0,1,0)
11627:(0,1,0,1,1,0,1,0,1,1,0,1,0,1,1)
13741:(0,1,1,0,1,0,1,1,0,1,0,1,1,0,1)
19026:(1,0,0,1,0,1,0,0,1,0,1,0,0,1,0)
21140:(1,0,1,0,0,1,0,1,0,0,1,0,1,0,0)
22197:(1,0,1,0,1,1,0,1,0,1,1,0,1,0,1)
23254:(1,0,1,1,0,1,0,1,1,0,1,0,1,1,0)
27482:(1,1,0,1,0,1,1,0,1,0,1,1,0,1,0)

Time for model checking: 5.459 seconds.

Result: 33.332616661835104


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_herman.15_rep3.log

```
Command(s):
../bin/prism -ex models/herman.15/model.prism models/herman.15/property.props
Wallclock time: 24.140 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:24:20 GMT+01:00 2026
Hostname: n23m0309.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/herman.15/model.prism models/herman.15/property.props

Parsing PRISM model file "models/herman.15/model.prism"...

Type:        DTMC
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10 process11 process12 process13 process14 process15
Actions:     [step]
Variables:   x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15
Labels:      "stable"
Rewards:     "steps"

Parsing properties file "models/herman.15/property.props"...

1 property:
(1) "steps": filter(max, R=? [ F "stable" ], "init")

---------------------------------------------------------------------

Model checking: "steps": filter(max, R=? [ F "stable" ], "init")

Building model (engine:explicit)...

Computing reachable states... 1025 7681 16385 25568 31768 32768 states
Reachable states exploration and model construction done in 17.664 secs.
Sorting reachable states list...

Time for model construction: 18.825 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908
Building reward structure...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.459 seconds)
Starting Prob1...
Prob1 took 0.184 seconds.
target=30, inf=0, rest=32738
Starting value iteration (with Jacobi) ...
Value iteration (with Jacobi) took 246 iterations, 3529816608 multiplications and 3.395 seconds.
Expected reachability took 4.053 seconds.

Maximum value over states satisfying filter: 33.332616661835104

There are 10 states with (approximately) this value:
5285:(0,0,1,0,1,0,0,1,0,1,0,0,1,0,1)
9513:(0,1,0,0,1,0,1,0,0,1,0,1,0,0,1)
10570:(0,1,0,1,0,0,1,0,1,0,0,1,0,1,0)
11627:(0,1,0,1,1,0,1,0,1,1,0,1,0,1,1)
13741:(0,1,1,0,1,0,1,1,0,1,0,1,1,0,1)
19026:(1,0,0,1,0,1,0,0,1,0,1,0,0,1,0)
21140:(1,0,1,0,0,1,0,1,0,0,1,0,1,0,0)
22197:(1,0,1,0,1,1,0,1,0,1,1,0,1,0,1)
23254:(1,0,1,1,0,1,0,1,1,0,1,0,1,1,0)
27482:(1,1,0,1,0,1,1,0,1,0,1,1,0,1,0)

Time for model checking: 4.396 seconds.

Result: 33.332616661835104


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_herman.15_rep4.log

```
Command(s):
../bin/prism -ex models/herman.15/model.prism models/herman.15/property.props
Wallclock time: 25.730 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:23:06 GMT+01:00 2026
Hostname: r23m0023.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/herman.15/model.prism models/herman.15/property.props

Parsing PRISM model file "models/herman.15/model.prism"...

Type:        DTMC
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10 process11 process12 process13 process14 process15
Actions:     [step]
Variables:   x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15
Labels:      "stable"
Rewards:     "steps"

Parsing properties file "models/herman.15/property.props"...

1 property:
(1) "steps": filter(max, R=? [ F "stable" ], "init")

---------------------------------------------------------------------

Model checking: "steps": filter(max, R=? [ F "stable" ], "init")

Building model (engine:explicit)...

Computing reachable states... 985 6650 16141 24590 30728 32753 32768 states
Reachable states exploration and model construction done in 18.831 secs.
Sorting reachable states list...

Time for model construction: 20.074 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908
Building reward structure...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.535 seconds)
Starting Prob1...
Prob1 took 0.163 seconds.
target=30, inf=0, rest=32738
Starting value iteration (with Jacobi) ...
Value iteration (with Jacobi) took 246 iterations, 3529816608 multiplications and 3.718 seconds.
Expected reachability took 4.427 seconds.

Maximum value over states satisfying filter: 33.332616661835104

There are 10 states with (approximately) this value:
5285:(0,0,1,0,1,0,0,1,0,1,0,0,1,0,1)
9513:(0,1,0,0,1,0,1,0,0,1,0,1,0,0,1)
10570:(0,1,0,1,0,0,1,0,1,0,0,1,0,1,0)
11627:(0,1,0,1,1,0,1,0,1,1,0,1,0,1,1)
13741:(0,1,1,0,1,0,1,1,0,1,0,1,1,0,1)
19026:(1,0,0,1,0,1,0,0,1,0,1,0,0,1,0)
21140:(1,0,1,0,0,1,0,1,0,0,1,0,1,0,0)
22197:(1,0,1,0,1,1,0,1,0,1,1,0,1,0,1)
23254:(1,0,1,1,0,1,0,1,1,0,1,0,1,1,0)
27482:(1,1,0,1,0,1,1,0,1,0,1,1,0,1,0)

Time for model checking: 4.81 seconds.

Result: 33.332616661835104


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```



### Log file: prism_from-prism_check_ex_herman.15_rep5.log

```
Command(s):
../bin/prism -ex models/herman.15/model.prism models/herman.15/property.props
Wallclock time: 25.152 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:04 GMT+01:00 2026
Hostname: n23m0013.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/herman.15/model.prism models/herman.15/property.props

Parsing PRISM model file "models/herman.15/model.prism"...

Type:        DTMC
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10 process11 process12 process13 process14 process15
Actions:     [step]
Variables:   x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15
Labels:      "stable"
Rewards:     "steps"

Parsing properties file "models/herman.15/property.props"...

1 property:
(1) "steps": filter(max, R=? [ F "stable" ], "init")

---------------------------------------------------------------------

Model checking: "steps": filter(max, R=? [ F "stable" ], "init")

Building model (engine:explicit)...

Computing reachable states... 1024 7396 16376 25062 31296 32768 states
Reachable states exploration and model construction done in 18.052 secs.
Sorting reachable states list...

Time for model construction: 19.184 seconds.

Type:        DTMC
States:      32768 (32768 initial)
Transitions: 14348908
Building reward structure...

Starting expected reachability...
Calculating predecessor relation for discrete-time Markov chain...  done (0.508 seconds)
Starting Prob1...
Prob1 took 0.185 seconds.
target=30, inf=0, rest=32738
Starting value iteration (with Jacobi) ...
Value iteration (with Jacobi) took 246 iterations, 3529816608 multiplications and 4.228 seconds.
Expected reachability took 4.936 seconds.

Maximum value over states satisfying filter: 33.332616661835104

There are 10 states with (approximately) this value:
5285:(0,0,1,0,1,0,0,1,0,1,0,0,1,0,1)
9513:(0,1,0,0,1,0,1,0,0,1,0,1,0,0,1)
10570:(0,1,0,1,0,0,1,0,1,0,0,1,0,1,0)
11627:(0,1,0,1,1,0,1,0,1,1,0,1,0,1,1)
13741:(0,1,1,0,1,0,1,1,0,1,0,1,1,0,1)
19026:(1,0,0,1,0,1,0,0,1,0,1,0,0,1,0)
21140:(1,0,1,0,0,1,0,1,0,0,1,0,1,0,0)
22197:(1,0,1,0,1,1,0,1,0,1,1,0,1,0,1)
23254:(1,0,1,1,0,1,0,1,1,0,1,0,1,1,0)
27482:(1,1,0,1,0,1,1,0,1,0,1,1,0,1,0)

Time for model checking: 5.263 seconds.

Result: 33.332616661835104


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
```

