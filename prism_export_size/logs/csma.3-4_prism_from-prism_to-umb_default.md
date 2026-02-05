# Log files

Tool configuration: prism_from-prism_to-umb_default
Benchmark: [csma.3-4](../../models/csma.3-4)
Parsed values: [68240384.0, 68240384.0, 68240384.0, 68240384.0, 68240384.0]



### Log file: prism_from-prism_to-umb_default_csma.3-4_rep1.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb_default/csma.3-4/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 8.698 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:24:51 GMT+01:00 2026
Hostname: n23m0133.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/csma.3-4/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 0.92 seconds (average 0.006815, setup 0.00)

Time for model construction: 1.094 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/csma.3-4/model.umb"...
Model export size: 66641 Kb
Time for exporting: 7.12 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/csma.3-4/model.umb:	Size of output file is 68240384 bytes
```



### Log file: prism_from-prism_to-umb_default_csma.3-4_rep2.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb_default/csma.3-4/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 9.308 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:32:55 GMT+01:00 2026
Hostname: n23m0166.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/csma.3-4/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 0.98 seconds (average 0.007259, setup 0.00)

Time for model construction: 1.168 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/csma.3-4/model_rep2.umb"...
Model export size: 66641 Kb
Time for exporting: 7.546 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/csma.3-4/model_rep2.umb:	Size of output file is 68240384 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_default_csma.3-4_rep3.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb_default/csma.3-4/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 8.961 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:28:29 GMT+01:00 2026
Hostname: n23m0041.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/csma.3-4/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 1.24 seconds (average 0.009185, setup 0.00)

Time for model construction: 1.461 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/csma.3-4/model_rep3.umb"...
Model export size: 66641 Kb
Time for exporting: 6.966 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/csma.3-4/model_rep3.umb:	Size of output file is 68240384 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_default_csma.3-4_rep4.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb_default/csma.3-4/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 9.583 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:34 GMT+01:00 2026
Hostname: n23m0242.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/csma.3-4/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 1.17 seconds (average 0.008667, setup 0.00)

Time for model construction: 1.379 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/csma.3-4/model_rep4.umb"...
Model export size: 66641 Kb
Time for exporting: 7.647 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/csma.3-4/model_rep4.umb:	Size of output file is 68240384 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_default_csma.3-4_rep5.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb_default/csma.3-4/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 8.929 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:50 GMT+01:00 2026
Hostname: n23m0111.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/csma.3-4/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 0.91 seconds (average 0.006741, setup 0.00)

Time for model construction: 1.09 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/csma.3-4/model_rep5.umb"...
Model export size: 66641 Kb
Time for exporting: 7.301 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/csma.3-4/model_rep5.umb:	Size of output file is 68240384 bytes
Removing output file to save space for repetition #5
```

