# Log files

Tool configuration: prism_from-prism_to-umb_default
Benchmark: [pacman.100](../../models/pacman.100)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_to-umb_default_pacman.100_rep1.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-umb_default/pacman.100/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 1392.088 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:47:21 GMT+01:00 2026
Hostname: r23m0060.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/pacman.100/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 94.19 seconds (average 0.310858, setup 0.00)

Time for model construction: 1388.123 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/pacman.100/model.umb"...

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
out/prism_from-prism_to-umb_default/pacman.100/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_default_pacman.100_rep2.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-umb_default/pacman.100/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 1637.765 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:28:47 GMT+01:00 2026
Hostname: r23m0212.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/pacman.100/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 99.61 seconds (average 0.328746, setup 0.00)

Time for model construction: 1633.157 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/pacman.100/model_rep2.umb"...

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
out/prism_from-prism_to-umb_default/pacman.100/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_default_pacman.100_rep3.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-umb_default/pacman.100/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 1255.834 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:39:07 GMT+01:00 2026
Hostname: n23m0043.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/pacman.100/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 92.85 seconds (average 0.306436, setup 0.00)

Time for model construction: 1251.763 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/pacman.100/model_rep3.umb"...

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
out/prism_from-prism_to-umb_default/pacman.100/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_default_pacman.100_rep4.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-umb_default/pacman.100/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 3444.443 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:14:02 GMT+01:00 2026
Hostname: r23m0197.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/pacman.100/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 108.26 seconds (average 0.357294, setup 0.00)

Time for model construction: 3439.884 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/pacman.100/model_rep4.umb"...

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
out/prism_from-prism_to-umb_default/pacman.100/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_default_pacman.100_rep5.log

```
Command(s):
../bin/prism  models/pacman.100/model.prism -exportmodel out/prism_from-prism_to-umb_default/pacman.100/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 2144.540 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:29:00 GMT+01:00 2026
Hostname: n23m0058.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/pacman.100/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/pacman.100/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/pacman.100/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 303 iterations in 84.68 seconds (average 0.279472, setup 0.00)

Time for model construction: 2139.997 seconds.

Type:        MDP
States:      79440921 (1 initial)
Transitions: 109963876

Transition matrix: 3640220 nodes (44 terminal), 109963876 minterms, vars: 36r/36c/9nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/pacman.100/model_rep5.umb"...

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
out/prism_from-prism_to-umb_default/pacman.100/model_rep5.umb:	File does not exist.
```

