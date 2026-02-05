# Log files

Tool configuration: prism_from-prism_to-umb_default
Benchmark: [rabin.10](../../models/rabin.10)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_to-umb_default_rabin.10_rep1.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-umb_default/rabin.10/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 50.241 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:37:51 GMT+01:00 2026
Hostname: n23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/rabin.10/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 46.57 seconds (average 1.108810, setup 0.00)

Time for model construction: 49.492 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/rabin.10/model.umb"...

java.lang.IllegalArgumentException: Illegal Capacity: -1
    at java.base/java.util.ArrayList.<init>(ArrayList.java:161)
    at explicit.MDPSimple.initialise(MDPSimple.java:208)
    at explicit.MDPSimple.<init>(MDPSimple.java:80)
    at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:102)
    at prism.Prism.doExportBuiltModel(Prism.java:2838)
    at prism.Prism.exportBuiltModelTask(Prism.java:2804)
    at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
    at prism.PrismCL.doExports(PrismCL.java:868)
    at prism.PrismCL.run(PrismCL.java:381)
    at prism.PrismCL.go(PrismCL.java:227)
    at prism.PrismCL.main(PrismCL.java:3040)

Error: Caught unhandled exception, aborting....

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/rabin.10/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_default_rabin.10_rep2.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-umb_default/rabin.10/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 42.506 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:39:36 GMT+01:00 2026
Hostname: n23m0063.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/rabin.10/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 39.40 seconds (average 0.938095, setup 0.00)

Time for model construction: 41.863 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/rabin.10/model_rep2.umb"...

java.lang.IllegalArgumentException: Illegal Capacity: -1
    at java.base/java.util.ArrayList.<init>(ArrayList.java:161)
    at explicit.MDPSimple.initialise(MDPSimple.java:208)
    at explicit.MDPSimple.<init>(MDPSimple.java:80)
    at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:102)
    at prism.Prism.doExportBuiltModel(Prism.java:2838)
    at prism.Prism.exportBuiltModelTask(Prism.java:2804)
    at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
    at prism.PrismCL.doExports(PrismCL.java:868)
    at prism.PrismCL.run(PrismCL.java:381)
    at prism.PrismCL.go(PrismCL.java:227)
    at prism.PrismCL.main(PrismCL.java:3040)

Error: Caught unhandled exception, aborting....

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/rabin.10/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_default_rabin.10_rep3.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-umb_default/rabin.10/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 45.044 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:39 GMT+01:00 2026
Hostname: n23m0174.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/rabin.10/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 41.77 seconds (average 0.994524, setup 0.00)

Time for model construction: 44.329 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/rabin.10/model_rep3.umb"...

java.lang.IllegalArgumentException: Illegal Capacity: -1
    at java.base/java.util.ArrayList.<init>(ArrayList.java:161)
    at explicit.MDPSimple.initialise(MDPSimple.java:208)
    at explicit.MDPSimple.<init>(MDPSimple.java:80)
    at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:102)
    at prism.Prism.doExportBuiltModel(Prism.java:2838)
    at prism.Prism.exportBuiltModelTask(Prism.java:2804)
    at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
    at prism.PrismCL.doExports(PrismCL.java:868)
    at prism.PrismCL.run(PrismCL.java:381)
    at prism.PrismCL.go(PrismCL.java:227)
    at prism.PrismCL.main(PrismCL.java:3040)

Error: Caught unhandled exception, aborting....

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/rabin.10/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_default_rabin.10_rep4.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-umb_default/rabin.10/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 47.698 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:29 GMT+01:00 2026
Hostname: r23m0029.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/rabin.10/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 44.28 seconds (average 1.054286, setup 0.00)

Time for model construction: 47.009 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/rabin.10/model_rep4.umb"...

java.lang.IllegalArgumentException: Illegal Capacity: -1
    at java.base/java.util.ArrayList.<init>(ArrayList.java:161)
    at explicit.MDPSimple.initialise(MDPSimple.java:208)
    at explicit.MDPSimple.<init>(MDPSimple.java:80)
    at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:102)
    at prism.Prism.doExportBuiltModel(Prism.java:2838)
    at prism.Prism.exportBuiltModelTask(Prism.java:2804)
    at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
    at prism.PrismCL.doExports(PrismCL.java:868)
    at prism.PrismCL.run(PrismCL.java:381)
    at prism.PrismCL.go(PrismCL.java:227)
    at prism.PrismCL.main(PrismCL.java:3040)

Error: Caught unhandled exception, aborting....

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/rabin.10/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_default_rabin.10_rep5.log

```
Command(s):
../bin/prism  models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-umb_default/rabin.10/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 43.656 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:49:15 GMT+01:00 2026
Hostname: n23m0250.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/rabin.10/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 42 iterations in 40.41 seconds (average 0.962143, setup 0.00)

Time for model construction: 42.928 seconds.

Type:        MDP
States:      358055586147376 (1 initial)
Transitions: 2908346849726720

Transition matrix: 894897 nodes (9 terminal), 2908346849726720 minterms, vars: 96r/96c/10nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/rabin.10/model_rep5.umb"...

java.lang.IllegalArgumentException: Illegal Capacity: -1
    at java.base/java.util.ArrayList.<init>(ArrayList.java:161)
    at explicit.MDPSimple.initialise(MDPSimple.java:208)
    at explicit.MDPSimple.<init>(MDPSimple.java:80)
    at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:102)
    at prism.Prism.doExportBuiltModel(Prism.java:2838)
    at prism.Prism.exportBuiltModelTask(Prism.java:2804)
    at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
    at prism.PrismCL.doExports(PrismCL.java:868)
    at prism.PrismCL.run(PrismCL.java:381)
    at prism.PrismCL.go(PrismCL.java:227)
    at prism.PrismCL.main(PrismCL.java:3040)

Error: Caught unhandled exception, aborting....

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/rabin.10/model_rep5.umb:	File does not exist.
```

