# Log files

Tool configuration: prism_from-prism_to-tra_norewards
Benchmark: [csma.4-2](../../models/csma.4-2)
Parsed values: [1.183, 1.232, 5.569, 1.314, 1.463]



### Log file: prism_from-prism_to-tra_norewards_csma.4-2_rep1.log

```
Command(s):
../bin/prism  models/csma.4-2/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/csma.4-2/model.tra,lab:precision=17
Wallclock time: 2.781 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:25:55 GMT+01:00 2026
Hostname: r23m0138.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.4-2/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/csma.4-2/model.tra,lab:precision=17'

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 193 iterations in 0.98 seconds (average 0.005078, setup 0.00)

Time for model construction: 1.093 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 52233 nodes (4 terminal), 1327068 minterms, vars: 54r/54c/17nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/csma.4-2/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/csma.4-2/model.lab"...
Time for exporting: 1.183 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/csma.4-2/model.tra:	Size of output file is 28902491 bytes
out/prism_from-prism_to-tra_norewards/csma.4-2/model.lab:	Size of output file is 34592 bytes
```



### Log file: prism_from-prism_to-tra_norewards_csma.4-2_rep2.log

```
Command(s):
../bin/prism  models/csma.4-2/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep2.tra,lab:precision=17
Wallclock time: 2.937 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:52 GMT+01:00 2026
Hostname: r23m0072.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.4-2/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep2.tra,lab:precision=17'

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 193 iterations in 1.00 seconds (average 0.005181, setup 0.00)

Time for model construction: 1.117 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 52233 nodes (4 terminal), 1327068 minterms, vars: 54r/54c/17nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep2.lab"...
Time for exporting: 1.232 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep2.tra:	Size of output file is 28902491 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep2.lab:	Size of output file is 34592 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_norewards_csma.4-2_rep3.log

```
Command(s):
../bin/prism  models/csma.4-2/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep3.tra,lab:precision=17
Wallclock time: 11.947 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:50:53 GMT+01:00 2026
Hostname: r23m0215.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.4-2/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep3.tra,lab:precision=17'

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 193 iterations in 3.96 seconds (average 0.020518, setup 0.00)

Time for model construction: 4.331 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 52233 nodes (4 terminal), 1327068 minterms, vars: 54r/54c/17nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep3.lab"...
Time for exporting: 5.569 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep3.tra:	Size of output file is 28902491 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep3.lab:	Size of output file is 34592 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_norewards_csma.4-2_rep4.log

```
Command(s):
../bin/prism  models/csma.4-2/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep4.tra,lab:precision=17
Wallclock time: 3.305 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:20 GMT+01:00 2026
Hostname: n23m0109.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.4-2/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep4.tra,lab:precision=17'

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 193 iterations in 1.06 seconds (average 0.005492, setup 0.00)

Time for model construction: 1.176 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 52233 nodes (4 terminal), 1327068 minterms, vars: 54r/54c/17nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep4.lab"...
Time for exporting: 1.314 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep4.tra:	Size of output file is 28902491 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep4.lab:	Size of output file is 34592 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_norewards_csma.4-2_rep5.log

```
Command(s):
../bin/prism  models/csma.4-2/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep5.tra,lab:precision=17
Wallclock time: 4.344 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:11 GMT+01:00 2026
Hostname: n23m0227.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.4-2/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep5.tra,lab:precision=17'

Parsing PRISM model file "models/csma.4-2/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3 station4
Actions:     [] [send1] [send2] [send3] [send4] [end1] [end2] [end3] [end4] [busy1] [busy2] [busy3] [busy4] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3 s4 x4 bc4 cd4
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 193 iterations in 1.89 seconds (average 0.009793, setup 0.00)

Time for model construction: 2.034 seconds.

Type:        MDP
States:      761962 (1 initial)
Transitions: 1327068

Transition matrix: 52233 nodes (4 terminal), 1327068 minterms, vars: 54r/54c/17nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep5.lab"...
Time for exporting: 1.463 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep5.tra:	Size of output file is 28902491 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_norewards/csma.4-2/model_rep5.lab:	Size of output file is 34592 bytes
Removing output file to save space for repetition #5
```

