# Log files for prism_from-prism_to-umb_norewards on model [pacman.100](../../models/pacman.100)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_to-umb_norewards_pacman.100_rep1.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/pacman.100/model.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 1614.652 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:23:48 GMT+01:00 2026
Hostname: n23m0110.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/pacman.100/model.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 93.66 seconds (average 0.309109, setup 0.00)

Time for model construction: 1610.766 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/pacman.100/model.umb"...

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
out/prism_from-prism_to-umb_norewards/pacman.100/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_pacman.100_rep2.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/pacman.100/model_rep2.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 1147.048 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:20:07 GMT+01:00 2026
Hostname: n23m0055.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/pacman.100/model_rep2.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 84.23 seconds (average 0.277987, setup 0.00)

Time for model construction: 1143.437 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/pacman.100/model_rep2.umb"...

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
out/prism_from-prism_to-umb_norewards/pacman.100/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_pacman.100_rep3.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/pacman.100/model_rep3.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 1055.498 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:50 GMT+01:00 2026
Hostname: n23m0058.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/pacman.100/model_rep3.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 85.25 seconds (average 0.281353, setup 0.00)

Time for model construction: 1052.093 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/pacman.100/model_rep3.umb"...

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
out/prism_from-prism_to-umb_norewards/pacman.100/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_pacman.100_rep4.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/pacman.100/model_rep4.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 1165.492 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:57 GMT+01:00 2026
Hostname: n23m0343.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/pacman.100/model_rep4.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 89.03 seconds (average 0.293828, setup 0.00)

Time for model construction: 1161.546 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/pacman.100/model_rep4.umb"...

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
out/prism_from-prism_to-umb_norewards/pacman.100/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_pacman.100_rep5.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/pacman.100/model_rep5.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 1146.520 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:32:01 GMT+01:00 2026
Hostname: n23m0341.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/pacman.100/model_rep5.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 85.67 seconds (average 0.282739, setup 0.00)

Time for model construction: 1141.682 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/pacman.100/model_rep5.umb"...

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
out/prism_from-prism_to-umb_norewards/pacman.100/model_rep5.umb:	File does not exist.
```

