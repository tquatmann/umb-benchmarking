# Log files

Tool configuration: prism_from-prism_to-umb_norewards
Benchmark: [crowds.6-20](../../models/crowds.6-20)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_to-umb_norewards_crowds.6-20_rep1.log

```
Command(s):
../bin/prism  models/crowds.6-20/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/crowds.6-20/model.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 131.114 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:38:22 GMT+01:00 2026
Hostname: n23m0242.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.6-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/crowds.6-20/model.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/crowds.6-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 56 iterations in 0.16 seconds (average 0.002857, setup 0.00)

Time for model construction: 0.273 seconds.

Warning: Deadlocks detected and fixed in 230230 states

Type:        DTMC
States:      10633591 (1 initial)
Transitions: 38261191

Transition matrix: 40814 nodes (7 terminal), 38261191 minterms, vars: 78r/78c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/crowds.6-20/model.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at odd.ODDNode.getThen(ODDNode.java:71)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/crowds.6-20/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_crowds.6-20_rep2.log

```
Command(s):
../bin/prism  models/crowds.6-20/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/crowds.6-20/model_rep2.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 140.182 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:10:59 GMT+01:00 2026
Hostname: n23m0063.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.6-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/crowds.6-20/model_rep2.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/crowds.6-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 56 iterations in 0.33 seconds (average 0.005893, setup 0.00)

Time for model construction: 0.541 seconds.

Warning: Deadlocks detected and fixed in 230230 states

Type:        DTMC
States:      10633591 (1 initial)
Transitions: 38261191

Transition matrix: 40814 nodes (7 terminal), 38261191 minterms, vars: 78r/78c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/crowds.6-20/model_rep2.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at odd.ODDNode.getElse(ODDNode.java:76)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/crowds.6-20/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_crowds.6-20_rep3.log

```
Command(s):
../bin/prism  models/crowds.6-20/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/crowds.6-20/model_rep3.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 131.530 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:26:08 GMT+01:00 2026
Hostname: n23m0167.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.6-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/crowds.6-20/model_rep3.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/crowds.6-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 56 iterations in 0.19 seconds (average 0.003393, setup 0.00)

Time for model construction: 0.337 seconds.

Warning: Deadlocks detected and fixed in 230230 states

Type:        DTMC
States:      10633591 (1 initial)
Transitions: 38261191

Transition matrix: 40814 nodes (7 terminal), 38261191 minterms, vars: 78r/78c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/crowds.6-20/model_rep3.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at jdd.JDDNode.getElse(JDDNode.java:139)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:502)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/crowds.6-20/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_crowds.6-20_rep4.log

```
Command(s):
../bin/prism  models/crowds.6-20/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/crowds.6-20/model_rep4.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 123.844 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:00:23 GMT+01:00 2026
Hostname: n23m0279.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.6-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/crowds.6-20/model_rep4.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/crowds.6-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 56 iterations in 0.16 seconds (average 0.002857, setup 0.00)

Time for model construction: 0.293 seconds.

Warning: Deadlocks detected and fixed in 230230 states

Type:        DTMC
States:      10633591 (1 initial)
Transitions: 38261191

Transition matrix: 40814 nodes (7 terminal), 38261191 minterms, vars: 78r/78c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/crowds.6-20/model_rep4.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at jdd.JDDNode.getElse(JDDNode.java:139)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:502)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/crowds.6-20/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_crowds.6-20_rep5.log

```
Command(s):
../bin/prism  models/crowds.6-20/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/crowds.6-20/model_rep5.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 120.621 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:47:41 GMT+01:00 2026
Hostname: r23m0015.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/crowds.6-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/crowds.6-20/model_rep5.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/crowds.6-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:symbolic)...

Warning: Guard for command 6 of module "crowds" is never satisfied.

Warning: Guard for command 7 of module "crowds" is never satisfied.

Warning: Guard for command 8 of module "crowds" is never satisfied.

Warning: Guard for command 9 of module "crowds" is never satisfied.

Warning: Guard for command 10 of module "crowds" is never satisfied.

Warning: Guard for command 2 of module "crowds" overlaps with previous commands.

Warning: Guard for command 3 of module "crowds" overlaps with previous commands.

Warning: Guard for command 4 of module "crowds" overlaps with previous commands.

Warning: Guard for command 5 of module "crowds" overlaps with previous commands.

Warning: Guard for command 11 of module "crowds" overlaps with previous commands.

Warning: Guard for command 12 of module "crowds" overlaps with previous commands.

Warning: Guard for command 13 of module "crowds" overlaps with previous commands.

Warning: Guard for command 14 of module "crowds" overlaps with previous commands.

Warning: Guard for command 15 of module "crowds" overlaps with previous commands.

Warning: Guard for command 16 of module "crowds" overlaps with previous commands.

Warning: Guard for command 17 of module "crowds" overlaps with previous commands.

Warning: Guard for command 18 of module "crowds" overlaps with previous commands.

Warning: Guard for command 19 of module "crowds" overlaps with previous commands.

Warning: Guard for command 20 of module "crowds" overlaps with previous commands.

Warning: Guard for command 21 of module "crowds" overlaps with previous commands.

Warning: Guard for command 22 of module "crowds" overlaps with previous commands.

Warning: Guard for command 23 of module "crowds" overlaps with previous commands.

Warning: Guard for command 24 of module "crowds" overlaps with previous commands.

Warning: Guard for command 25 of module "crowds" overlaps with previous commands.

Warning: Guard for command 26 of module "crowds" overlaps with previous commands.

Warning: Guard for command 27 of module "crowds" overlaps with previous commands.

Warning: Guard for command 28 of module "crowds" overlaps with previous commands.

Warning: Guard for command 29 of module "crowds" overlaps with previous commands.

Warning: Guard for command 30 of module "crowds" overlaps with previous commands.

Warning: Guard for command 31 of module "crowds" overlaps with previous commands.

Warning: Guard for command 32 of module "crowds" overlaps with previous commands.

Warning: Guard for command 33 of module "crowds" overlaps with previous commands.

Computing reachable states...

Reachability (BFS): 56 iterations in 0.13 seconds (average 0.002321, setup 0.00)

Time for model construction: 0.246 seconds.

Warning: Deadlocks detected and fixed in 230230 states

Type:        DTMC
States:      10633591 (1 initial)
Transitions: 38261191

Transition matrix: 40814 nodes (7 terminal), 38261191 minterms, vars: 78r/78c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/crowds.6-20/model_rep5.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at jdd.JDDNode.getThen(JDDNode.java:111)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:503)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/crowds.6-20/model_rep5.umb:	File does not exist.
```

