# Log files

Tool configuration: prism_from-prism_to-umb-gz_norewards
Benchmark: [rabin.10](../../models/rabin.10)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_to-umb-gz_norewards_rabin.10_rep1.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/rabin.10/model.umb.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 44.867 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:22:13 GMT+01:00 2026
Hostname: n23m0248.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/rabin.10/model.umb.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 41.53 seconds (average 0.988810, setup 0.00)

Time for model construction: 44.012 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/rabin.10/model.umb.gz"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 358055586147376 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/rabin.10/model.umb.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_norewards_rabin.10_rep2.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/rabin.10/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 48.426 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:03 GMT+01:00 2026
Hostname: r23m0014.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/rabin.10/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 43.49 seconds (average 1.035476, setup 0.00)

Time for model construction: 46.268 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/rabin.10/model.umb_rep2.gz"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 358055586147376 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/rabin.10/model.umb_rep2.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_norewards_rabin.10_rep3.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/rabin.10/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 43.162 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:01 GMT+01:00 2026
Hostname: n23m0192.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/rabin.10/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 39.74 seconds (average 0.946190, setup 0.00)

Time for model construction: 42.178 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/rabin.10/model.umb_rep3.gz"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 358055586147376 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/rabin.10/model.umb_rep3.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_norewards_rabin.10_rep4.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/rabin.10/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 56.946 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:52 GMT+01:00 2026
Hostname: n23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/rabin.10/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 52.98 seconds (average 1.261429, setup 0.00)

Time for model construction: 56.133 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/rabin.10/model.umb_rep4.gz"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 358055586147376 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/rabin.10/model.umb_rep4.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_norewards_rabin.10_rep5.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/rabin.10/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 52.596 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:12:29 GMT+01:00 2026
Hostname: n23m0134.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/rabin.10/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 48.59 seconds (average 1.156905, setup 0.00)

Time for model construction: 51.647 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/rabin.10/model.umb_rep5.gz"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 358055586147376 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/rabin.10/model.umb_rep5.gz:	File does not exist.
```

