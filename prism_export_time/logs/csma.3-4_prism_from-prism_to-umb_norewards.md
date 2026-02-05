# Log files for prism_from-prism_to-umb_norewards on model [csma.3-4](../../models/csma.3-4)

Parsed values: `[7.426, 10.113, 6.929, 7.032, 7.143]`



### Log file: prism_from-prism_to-umb_norewards_csma.3-4_rep1.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/csma.3-4/model.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 11.738 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:45:49 GMT+01:00 2026
Hostname: r23m0017.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/csma.3-4/model.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 0.91 seconds (average 0.006741, setup 0.00)

Time for model construction: 1.173 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/csma.3-4/model.umb"...
Model export size: 66641 Kb
Time for exporting: 7.426 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/csma.3-4/model.umb:	Size of output file is 68240384 bytes
```



### Log file: prism_from-prism_to-umb_norewards_csma.3-4_rep2.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/csma.3-4/model_rep2.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 12.979 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:01 GMT+01:00 2026
Hostname: n23m0350.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/csma.3-4/model_rep2.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 1.79 seconds (average 0.013259, setup 0.00)

Time for model construction: 2.089 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/csma.3-4/model_rep2.umb"...
Model export size: 66641 Kb
Time for exporting: 10.113 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/csma.3-4/model_rep2.umb:	Size of output file is 68240384 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_norewards_csma.3-4_rep3.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/csma.3-4/model_rep3.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 8.620 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:55:18 GMT+01:00 2026
Hostname: n23m0313.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/csma.3-4/model_rep3.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 0.90 seconds (average 0.006667, setup 0.00)

Time for model construction: 1.078 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/csma.3-4/model_rep3.umb"...
Model export size: 66641 Kb
Time for exporting: 6.929 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/csma.3-4/model_rep3.umb:	Size of output file is 68240384 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_norewards_csma.3-4_rep4.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/csma.3-4/model_rep4.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 8.568 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:36:35 GMT+01:00 2026
Hostname: r23m0015.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/csma.3-4/model_rep4.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 0.88 seconds (average 0.006519, setup 0.00)

Time for model construction: 1.049 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/csma.3-4/model_rep4.umb"...
Model export size: 66641 Kb
Time for exporting: 7.032 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/csma.3-4/model_rep4.umb:	Size of output file is 68240384 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_norewards_csma.3-4_rep5.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/csma.3-4/model_rep5.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 9.074 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:31:00 GMT+01:00 2026
Hostname: n23m0041.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/csma.3-4/model_rep5.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 1.22 seconds (average 0.009037, setup 0.00)

Time for model construction: 1.423 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/csma.3-4/model_rep5.umb"...
Model export size: 66641 Kb
Time for exporting: 7.143 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/csma.3-4/model_rep5.umb:	Size of output file is 68240384 bytes
Removing output file to save space for repetition #5
```

