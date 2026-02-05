# Log files

Tool configuration: prism_from-prism_to-tra_default
Benchmark: [csma.3-4](../../models/csma.3-4)
Parsed values: [55823656.0, 55823656.0, 55823656.0, 55823656.0, 55823656.0]



### Log file: prism_from-prism_to-tra_default_csma.3-4_rep1.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-tra_default/csma.3-4/model.tra,lab,rew:precision=17
Wallclock time: 5.154 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:21:42 GMT+01:00 2026
Hostname: n23m0128.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/csma.3-4/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 1.16 seconds (average 0.008593, setup 0.00)

Time for model construction: 1.463 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/csma.3-4/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/csma.3-4/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/csma.3-4/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/csma.3-4/model.trew"...
Time for exporting: 1.887 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/csma.3-4/model.tra:	Size of output file is 55807758 bytes
out/prism_from-prism_to-tra_default/csma.3-4/model.lab:	Size of output file is 15898 bytes
out/prism_from-prism_to-tra_default/csma.3-4/model.srew:	File does not exist.
out/prism_from-prism_to-tra_default/csma.3-4/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_csma.3-4_rep2.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-tra_default/csma.3-4/model_rep2.tra,lab,rew:precision=17
Wallclock time: 3.502 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:37 GMT+01:00 2026
Hostname: r23m0197.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/csma.3-4/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 0.93 seconds (average 0.006889, setup 0.00)

Time for model construction: 1.109 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/csma.3-4/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/csma.3-4/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/csma.3-4/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/csma.3-4/model_rep2.trew"...
Time for exporting: 1.868 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/csma.3-4/model_rep2.tra:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/csma.3-4/model_rep2.lab:	Size of output file is 15898 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/csma.3-4/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_default/csma.3-4/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_csma.3-4_rep3.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-tra_default/csma.3-4/model_rep3.tra,lab,rew:precision=17
Wallclock time: 4.098 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:46 GMT+01:00 2026
Hostname: n23m0196.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/csma.3-4/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 1.06 seconds (average 0.007852, setup 0.00)

Time for model construction: 1.272 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/csma.3-4/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/csma.3-4/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/csma.3-4/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/csma.3-4/model_rep3.trew"...
Time for exporting: 2.216 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/csma.3-4/model_rep3.tra:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/csma.3-4/model_rep3.lab:	Size of output file is 15898 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/csma.3-4/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_default/csma.3-4/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_csma.3-4_rep4.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-tra_default/csma.3-4/model_rep4.tra,lab,rew:precision=17
Wallclock time: 4.744 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:38:06 GMT+01:00 2026
Hostname: r23m0212.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/csma.3-4/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 1.56 seconds (average 0.011556, setup 0.00)

Time for model construction: 1.811 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/csma.3-4/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/csma.3-4/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/csma.3-4/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/csma.3-4/model_rep4.trew"...
Time for exporting: 2.273 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/csma.3-4/model_rep4.tra:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/csma.3-4/model_rep4.lab:	Size of output file is 15898 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/csma.3-4/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_default/csma.3-4/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_csma.3-4_rep5.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-tra_default/csma.3-4/model_rep5.tra,lab,rew:precision=17
Wallclock time: 7.210 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:27 GMT+01:00 2026
Hostname: n23m0344.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/csma.3-4/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 1.79 seconds (average 0.013259, setup 0.00)

Time for model construction: 2.098 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/csma.3-4/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/csma.3-4/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/csma.3-4/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/csma.3-4/model_rep5.trew"...
Time for exporting: 2.391 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/csma.3-4/model_rep5.tra:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/csma.3-4/model_rep5.lab:	Size of output file is 15898 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/csma.3-4/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_default/csma.3-4/model_rep5.trew:	File does not exist.
```

