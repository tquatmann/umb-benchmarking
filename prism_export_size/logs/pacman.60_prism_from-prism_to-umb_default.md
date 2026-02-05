# Log files for prism_from-prism_to-umb_default on model [pacman.60](../../models/pacman.60)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_to-umb_default_pacman.60_rep1.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-umb_default/pacman.60/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 1047.530 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:39:57 GMT+01:00 2026
Hostname: n23m0273.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/pacman.60/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 47.37 seconds (average 0.258852, setup 0.00)

Time for model construction: 1041.693 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/pacman.60/model.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at explicit.MDPSimple.initialise(MDPSimple.java:210)
	at explicit.MDPSimple.<init>(MDPSimple.java:80)
	at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:102)
	at prism.Prism.doExportBuiltModel(Prism.java:2838)
	at prism.Prism.exportBuiltModelTask(Prism.java:2804)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_default/pacman.60/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_default_pacman.60_rep2.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-umb_default/pacman.60/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 2275.927 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:42:09 GMT+01:00 2026
Hostname: n23m0281.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/pacman.60/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 52.71 seconds (average 0.288033, setup 0.00)

Time for model construction: 2271.581 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/pacman.60/model_rep2.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at explicit.MDPSimple.initialise(MDPSimple.java:210)
	at explicit.MDPSimple.<init>(MDPSimple.java:80)
	at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:102)
	at prism.Prism.doExportBuiltModel(Prism.java:2838)
	at prism.Prism.exportBuiltModelTask(Prism.java:2804)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_default/pacman.60/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_default_pacman.60_rep3.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-umb_default/pacman.60/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 3415.005 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:36:05 GMT+01:00 2026
Hostname: n23m0072.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/pacman.60/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 73.61 seconds (average 0.402240, setup 0.00)

Time for model construction: 3408.711 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/pacman.60/model_rep3.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at explicit.MDPSimple.initialise(MDPSimple.java:210)
	at explicit.MDPSimple.<init>(MDPSimple.java:80)
	at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:102)
	at prism.Prism.doExportBuiltModel(Prism.java:2838)
	at prism.Prism.exportBuiltModelTask(Prism.java:2804)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_default/pacman.60/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_default_pacman.60_rep4.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-umb_default/pacman.60/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 1753.139 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:14:02 GMT+01:00 2026
Hostname: n23m0109.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/pacman.60/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 54.36 seconds (average 0.297049, setup 0.00)

Time for model construction: 1748.369 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/pacman.60/model_rep4.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at explicit.MDPSimple.initialise(MDPSimple.java:210)
	at explicit.MDPSimple.<init>(MDPSimple.java:80)
	at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:102)
	at prism.Prism.doExportBuiltModel(Prism.java:2838)
	at prism.Prism.exportBuiltModelTask(Prism.java:2804)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_default/pacman.60/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_default_pacman.60_rep5.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-umb_default/pacman.60/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 3312.120 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:01 GMT+01:00 2026
Hostname: n23m0350.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/pacman.60/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 66.87 seconds (average 0.365410, setup 0.00)

Time for model construction: 3303.443 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/pacman.60/model_rep5.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at explicit.MDPSimple.initialise(MDPSimple.java:210)
	at explicit.MDPSimple.<init>(MDPSimple.java:80)
	at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:102)
	at prism.Prism.doExportBuiltModel(Prism.java:2838)
	at prism.Prism.exportBuiltModelTask(Prism.java:2804)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_default/pacman.60/model_rep5.umb:	File does not exist.
```

