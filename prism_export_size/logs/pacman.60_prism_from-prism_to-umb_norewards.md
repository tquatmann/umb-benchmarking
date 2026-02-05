# Log files for prism_from-prism_to-umb_norewards on model [pacman.60](../../models/pacman.60)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_to-umb_norewards_pacman.60_rep1.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/pacman.60/model.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 2325.247 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:34:37 GMT+01:00 2026
Hostname: n23m0389.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/pacman.60/model.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 55.56 seconds (average 0.303607, setup 0.00)

Time for model construction: 2320.166 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/pacman.60/model.umb"...

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
out/prism_from-prism_to-umb_norewards/pacman.60/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_pacman.60_rep2.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/pacman.60/model_rep2.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 1140.798 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:58:53 GMT+01:00 2026
Hostname: n23m0109.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/pacman.60/model_rep2.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 47.38 seconds (average 0.258907, setup 0.00)

Time for model construction: 1135.82 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/pacman.60/model_rep2.umb"...

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
out/prism_from-prism_to-umb_norewards/pacman.60/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_pacman.60_rep3.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/pacman.60/model_rep3.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 1311.497 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:32:31 GMT+01:00 2026
Hostname: n23m0383.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/pacman.60/model_rep3.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 60.37 seconds (average 0.329891, setup 0.00)

Time for model construction: 1307.316 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/pacman.60/model_rep3.umb"...

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
out/prism_from-prism_to-umb_norewards/pacman.60/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_pacman.60_rep4.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/pacman.60/model_rep4.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 1072.255 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:52 GMT+01:00 2026
Hostname: r23m0090.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/pacman.60/model_rep4.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 46.59 seconds (average 0.254590, setup 0.00)

Time for model construction: 1067.335 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/pacman.60/model_rep4.umb"...

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
out/prism_from-prism_to-umb_norewards/pacman.60/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_pacman.60_rep5.log

```
Command(s):
../bin/prism  models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/pacman.60/model_rep5.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 1137.139 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:12 GMT+01:00 2026
Hostname: n23m0161.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/pacman.60/model_rep5.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 183 iterations in 55.07 seconds (average 0.300929, setup 0.00)

Time for model construction: 1130.665 seconds.

Type:        MDP
States:      38786521 (1 initial)
Transitions: 53648196

Transition matrix: 3640092 nodes (44 terminal), 53648196 minterms, vars: 35r/35c/9nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/pacman.60/model_rep5.umb"...

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
out/prism_from-prism_to-umb_norewards/pacman.60/model_rep5.umb:	File does not exist.
```

