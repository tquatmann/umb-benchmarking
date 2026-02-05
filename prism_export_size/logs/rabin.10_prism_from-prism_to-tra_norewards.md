# Log files

Tool configuration: prism_from-prism_to-tra_norewards
Benchmark: [rabin.10](../../models/rabin.10)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_to-tra_norewards_rabin.10_rep1.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/rabin.10/model.tra,lab:precision=17
Wallclock time: 48.863 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:44:12 GMT+01:00 2026
Hostname: r23m0008.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/rabin.10/model.tra,lab:precision=17'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 43.93 seconds (average 1.045952, setup 0.00)

Time for model construction: 46.798 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/rabin.10/model.tra"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 358055586147376 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/rabin.10/model.tra:	File does not exist.
out/prism_from-prism_to-tra_norewards/rabin.10/model.lab:	File does not exist.
```



### Log file: prism_from-prism_to-tra_norewards_rabin.10_rep2.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/rabin.10/model_rep2.tra,lab:precision=17
Wallclock time: 42.512 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:58:22 GMT+01:00 2026
Hostname: n23m0380.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/rabin.10/model_rep2.tra,lab:precision=17'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 39.25 seconds (average 0.934524, setup 0.00)

Time for model construction: 41.686 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/rabin.10/model_rep2.tra"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 358055586147376 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/rabin.10/model_rep2.tra:	File does not exist.
out/prism_from-prism_to-tra_norewards/rabin.10/model_rep2.lab:	File does not exist.
```



### Log file: prism_from-prism_to-tra_norewards_rabin.10_rep3.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/rabin.10/model_rep3.tra,lab:precision=17
Wallclock time: 43.267 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:01:55 GMT+01:00 2026
Hostname: n23m0138.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/rabin.10/model_rep3.tra,lab:precision=17'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 40.08 seconds (average 0.954286, setup 0.00)

Time for model construction: 42.567 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/rabin.10/model_rep3.tra"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 358055586147376 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/rabin.10/model_rep3.tra:	File does not exist.
out/prism_from-prism_to-tra_norewards/rabin.10/model_rep3.lab:	File does not exist.
```



### Log file: prism_from-prism_to-tra_norewards_rabin.10_rep4.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/rabin.10/model_rep4.tra,lab:precision=17
Wallclock time: 49.019 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:26:12 GMT+01:00 2026
Hostname: n23m0247.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/rabin.10/model_rep4.tra,lab:precision=17'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 45.40 seconds (average 1.080952, setup 0.00)

Time for model construction: 48.238 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/rabin.10/model_rep4.tra"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 358055586147376 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/rabin.10/model_rep4.tra:	File does not exist.
out/prism_from-prism_to-tra_norewards/rabin.10/model_rep4.lab:	File does not exist.
```



### Log file: prism_from-prism_to-tra_norewards_rabin.10_rep5.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/rabin.10/model_rep5.tra,lab:precision=17
Wallclock time: 43.206 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:11:59 GMT+01:00 2026
Hostname: n23m0044.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/rabin.10/model_rep5.tra,lab:precision=17'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 40.14 seconds (average 0.955714, setup 0.00)

Time for model construction: 42.576 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/rabin.10/model_rep5.tra"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 358055586147376 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/rabin.10/model_rep5.tra:	File does not exist.
out/prism_from-prism_to-tra_norewards/rabin.10/model_rep5.lab:	File does not exist.
```

