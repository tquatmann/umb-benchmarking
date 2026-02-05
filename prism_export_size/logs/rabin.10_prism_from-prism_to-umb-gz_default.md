# Log files for prism_from-prism_to-umb-gz_default on model [rabin.10](../../models/rabin.10)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_to-umb-gz_default_rabin.10_rep1.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/rabin.10/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 43.560 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:43:08 GMT+01:00 2026
Hostname: r23m0065.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/rabin.10/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 40.19 seconds (average 0.956905, setup 0.00)

Time for model construction: 42.741 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/rabin.10/model.umb.gz"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 358055586147376 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/rabin.10/model.umb.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_default_rabin.10_rep2.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/rabin.10/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 48.848 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:06 GMT+01:00 2026
Hostname: n23m0364.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/rabin.10/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 45.18 seconds (average 1.075714, setup 0.00)

Time for model construction: 48.05 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/rabin.10/model.umb_rep2.gz"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 358055586147376 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/rabin.10/model.umb_rep2.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_default_rabin.10_rep3.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/rabin.10/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 45.175 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:11 GMT+01:00 2026
Hostname: n23m0073.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/rabin.10/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 41.82 seconds (average 0.995714, setup 0.00)

Time for model construction: 44.381 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/rabin.10/model.umb_rep3.gz"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 358055586147376 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/rabin.10/model.umb_rep3.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_default_rabin.10_rep4.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/rabin.10/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 50.360 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:26:01 GMT+01:00 2026
Hostname: n23m0014.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/rabin.10/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 46.64 seconds (average 1.110476, setup 0.00)

Time for model construction: 49.565 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/rabin.10/model.umb_rep4.gz"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 358055586147376 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/rabin.10/model.umb_rep4.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_default_rabin.10_rep5.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-umb-gz_default/rabin.10/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 43.819 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:53:16 GMT+01:00 2026
Hostname: n23m0313.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_default/rabin.10/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 40.71 seconds (average 0.969286, setup 0.00)

Time for model construction: 43.158 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_default/rabin.10/model.umb_rep5.gz"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 358055586147376 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_default/rabin.10/model.umb_rep5.gz:	File does not exist.
```

