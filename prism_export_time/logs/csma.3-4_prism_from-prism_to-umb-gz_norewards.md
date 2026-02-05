# Log files

Tool configuration: prism_from-prism_to-umb-gz_norewards
Benchmark: [csma.3-4](../../models/csma.3-4)
Parsed values: [1.832, 1.874, 2.179, 2.068, 1.85]



### Log file: prism_from-prism_to-umb-gz_norewards_csma.3-4_rep1.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/csma.3-4/model.umb.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 3.503 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:27:29 GMT+01:00 2026
Hostname: n23m0244.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/csma.3-4/model.umb.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 0.92 seconds (average 0.006815, setup 0.00)

Time for model construction: 1.12 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/csma.3-4/model.umb.gz"...
Time for exporting: 1.832 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/csma.3-4/model.umb.gz:	Size of output file is 55807758 bytes
```



### Log file: prism_from-prism_to-umb-gz_norewards_csma.3-4_rep2.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/csma.3-4/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 3.685 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:11:58 GMT+01:00 2026
Hostname: n23m0044.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/csma.3-4/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 0.93 seconds (average 0.006889, setup 0.00)

Time for model construction: 1.125 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/csma.3-4/model.umb_rep2.gz"...
Time for exporting: 1.874 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/csma.3-4/model.umb_rep2.gz:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_norewards_csma.3-4_rep3.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/csma.3-4/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 4.851 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:31:51 GMT+01:00 2026
Hostname: n23m0167.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/csma.3-4/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 1.72 seconds (average 0.012741, setup 0.00)

Time for model construction: 1.993 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/csma.3-4/model.umb_rep3.gz"...
Time for exporting: 2.179 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/csma.3-4/model.umb_rep3.gz:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_norewards_csma.3-4_rep4.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/csma.3-4/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 4.426 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:26:45 GMT+01:00 2026
Hostname: n23m0058.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/csma.3-4/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 1.48 seconds (average 0.010963, setup 0.00)

Time for model construction: 1.724 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/csma.3-4/model.umb_rep4.gz"...
Time for exporting: 2.068 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/csma.3-4/model.umb_rep4.gz:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_norewards_csma.3-4_rep5.log

```
Command(s):
../bin/prism  models/csma.3-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/csma.3-4/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 3.531 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:19:07 GMT+01:00 2026
Hostname: n23m0250.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/csma.3-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/csma.3-4/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/csma.3-4/model.prism"...

Type:        MDP
Modules:     bus station1 station2 station3
Actions:     [] [send1] [send2] [send3] [end1] [end2] [end3] [busy1] [busy2] [busy3] [cd] [time]
Variables:   b y1 y2 s1 x1 bc1 cd1 s2 x2 bc2 cd2 s3 x3 bc3 cd3
Labels:      "all_delivered" "collision_max_backoff"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 135 iterations in 0.94 seconds (average 0.006963, setup 0.00)

Time for model construction: 1.11 seconds.

Type:        MDP
States:      1460287 (1 initial)
Transitions: 2396727

Transition matrix: 75002 nodes (6 terminal), 2396727 minterms, vars: 51r/51c/13nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/csma.3-4/model.umb_rep5.gz"...
Time for exporting: 1.85 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/csma.3-4/model.umb_rep5.gz:	Size of output file is 55807758 bytes
Removing output file to save space for repetition #5
```

