# Log files for prism_from-prism_to-umb_norewards on model [pnueli-zuck.10](../../models/pnueli-zuck.10)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_to-umb_norewards_pnueli-zuck.10_rep1.log

```
Command(s):
../bin/prism  models/pnueli-zuck.10/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/pnueli-zuck.10/model.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 1.495 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:43:09 GMT+01:00 2026
Hostname: r23m0088.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.10/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/pnueli-zuck.10/model.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.84 seconds (average 0.011507, setup 0.00)

Time for model construction: 0.93 seconds.

Type:        MDP
States:      69994757110 (1 initial)
Transitions: 891923978050

Transition matrix: 22186 nodes (3 terminal), 891923978050 minterms, vars: 40r/40c/10nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/pnueli-zuck.10/model.umb"...

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
out/prism_from-prism_to-umb_norewards/pnueli-zuck.10/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_pnueli-zuck.10_rep2.log

```
Command(s):
../bin/prism  models/pnueli-zuck.10/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/pnueli-zuck.10/model_rep2.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 1.308 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:11 GMT+01:00 2026
Hostname: n23m0073.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.10/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/pnueli-zuck.10/model_rep2.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.64 seconds (average 0.008767, setup 0.00)

Time for model construction: 0.721 seconds.

Type:        MDP
States:      69994757110 (1 initial)
Transitions: 891923978050

Transition matrix: 22186 nodes (3 terminal), 891923978050 minterms, vars: 40r/40c/10nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/pnueli-zuck.10/model_rep2.umb"...

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
out/prism_from-prism_to-umb_norewards/pnueli-zuck.10/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_pnueli-zuck.10_rep3.log

```
Command(s):
../bin/prism  models/pnueli-zuck.10/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/pnueli-zuck.10/model_rep3.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 1.218 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:59:23 GMT+01:00 2026
Hostname: n23m0308.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.10/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/pnueli-zuck.10/model_rep3.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.57 seconds (average 0.007808, setup 0.00)

Time for model construction: 0.651 seconds.

Type:        MDP
States:      69994757110 (1 initial)
Transitions: 891923978050

Transition matrix: 22186 nodes (3 terminal), 891923978050 minterms, vars: 40r/40c/10nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/pnueli-zuck.10/model_rep3.umb"...

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
out/prism_from-prism_to-umb_norewards/pnueli-zuck.10/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_pnueli-zuck.10_rep4.log

```
Command(s):
../bin/prism  models/pnueli-zuck.10/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/pnueli-zuck.10/model_rep4.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 1.497 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:22:09 GMT+01:00 2026
Hostname: r23m0204.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.10/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/pnueli-zuck.10/model_rep4.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.83 seconds (average 0.011370, setup 0.00)

Time for model construction: 0.921 seconds.

Type:        MDP
States:      69994757110 (1 initial)
Transitions: 891923978050

Transition matrix: 22186 nodes (3 terminal), 891923978050 minterms, vars: 40r/40c/10nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/pnueli-zuck.10/model_rep4.umb"...

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
out/prism_from-prism_to-umb_norewards/pnueli-zuck.10/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_pnueli-zuck.10_rep5.log

```
Command(s):
../bin/prism  models/pnueli-zuck.10/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/pnueli-zuck.10/model_rep5.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 1.372 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:32:53 GMT+01:00 2026
Hostname: n23m0167.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pnueli-zuck.10/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/pnueli-zuck.10/model_rep5.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 73 iterations in 0.66 seconds (average 0.009041, setup 0.00)

Time for model construction: 0.766 seconds.

Type:        MDP
States:      69994757110 (1 initial)
Transitions: 891923978050

Transition matrix: 22186 nodes (3 terminal), 891923978050 minterms, vars: 40r/40c/10nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/pnueli-zuck.10/model_rep5.umb"...

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
out/prism_from-prism_to-umb_norewards/pnueli-zuck.10/model_rep5.umb:	File does not exist.
```

