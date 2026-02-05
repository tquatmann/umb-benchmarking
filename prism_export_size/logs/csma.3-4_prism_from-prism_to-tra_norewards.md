# Log files

Tool configuration: prism_from-prism_to-tra_norewards
Benchmark: [csma.3-4](../../models/csma.3-4)
Parsed values: [55823656.0, 55823656.0, 55823656.0, 55823656.0, 55823656.0]



### Log file: prism_from-prism_to-tra_norewards_csma.3-4_rep1.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/csma.3-4/model.tra,lab:precision=17
Wallclock time: 3.803 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:25:23 GMT+01:00 2026
Hostname: n23m0242.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/csma.3-4/model.tra,lab:precision=17'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 0.96 seconds (average 0.007111, setup 0.00)

Time for model construction: 1.144 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/csma.3-4/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/csma.3-4/model.lab"...
Time for exporting: 2.018 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/csma.3-4/model.tra:	Size of output file is 55807758 bytes
out/prism_from-prism_to-tra_norewards/csma.3-4/model.lab:	Size of output file is 15898 bytes
```



### Log file: prism_from-prism_to-tra_norewards_csma.3-4_rep2.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep2.tra,lab:precision=17
Wallclock time: 7.468 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:12 GMT+01:00 2026
Hostname: n23m0290.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep2.tra,lab:precision=17'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 2.18 seconds (average 0.016148, setup 0.00)

Time for model construction: 2.54 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep2.lab"...
Time for exporting: 2.464 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep2.tra:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep2.lab:	Size of output file is 15898 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_norewards_csma.3-4_rep3.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep3.tra,lab:precision=17
Wallclock time: 3.596 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:26:24 GMT+01:00 2026
Hostname: n23m0351.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep3.tra,lab:precision=17'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 1.00 seconds (average 0.007407, setup 0.00)

Time for model construction: 1.192 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep3.lab"...
Time for exporting: 1.865 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep3.tra:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep3.lab:	Size of output file is 15898 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_norewards_csma.3-4_rep4.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep4.tra,lab:precision=17
Wallclock time: 5.462 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:29 GMT+01:00 2026
Hostname: n23m0003.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep4.tra,lab:precision=17'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 1.97 seconds (average 0.014593, setup 0.00)

Time for model construction: 2.271 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep4.lab"...
Time for exporting: 2.433 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep4.tra:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep4.lab:	Size of output file is 15898 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_norewards_csma.3-4_rep5.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep5.tra,lab:precision=17
Wallclock time: 4.382 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:44:09 GMT+01:00 2026
Hostname: n23m0252.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep5.tra,lab:precision=17'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 1.39 seconds (average 0.010296, setup 0.00)

Time for model construction: 1.65 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep5.lab"...
Time for exporting: 2.077 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep5.tra:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_norewards/csma.3-4/model_rep5.lab:	Size of output file is 15898 bytes
Removing output file to save space for repetition #5
```

