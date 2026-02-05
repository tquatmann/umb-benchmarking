# Log files for prism_from-prism_to-umb_norewards on model [nand.60-4](../../models/nand.60-4)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_to-umb_norewards_nand.60-4_rep1.log

```
Command(s):
../bin/prism  models/nand.60-4/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/nand.60-4/model.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 25.486 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:25:24 GMT+01:00 2026
Hostname: r23m0138.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.60-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/nand.60-4/model.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2162 iterations in 7.48 seconds (average 0.003460, setup 0.00)

Time for model construction: 7.72 seconds.

Type:        DTMC
States:      18826082 (1 initial)
Transitions: 29772212

Transition matrix: 97452 nodes (1103 terminal), 29772212 minterms, vars: 33r/33c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/nand.60-4/model.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at odd.ODDNode.getThen(ODDNode.java:71)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
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
out/prism_from-prism_to-umb_norewards/nand.60-4/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_nand.60-4_rep2.log

```
Command(s):
../bin/prism  models/nand.60-4/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/nand.60-4/model_rep2.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 123.062 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:51:24 GMT+01:00 2026
Hostname: r23m0217.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.60-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/nand.60-4/model_rep2.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2162 iterations in 34.38 seconds (average 0.015902, setup 0.00)

Time for model construction: 35.625 seconds.

Type:        DTMC
States:      18826082 (1 initial)
Transitions: 29772212

Transition matrix: 97452 nodes (1103 terminal), 29772212 minterms, vars: 33r/33c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/nand.60-4/model_rep2.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at odd.ODDNode.getElse(ODDNode.java:76)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
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

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/nand.60-4/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_nand.60-4_rep3.log

```
Command(s):
../bin/prism  models/nand.60-4/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/nand.60-4/model_rep3.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 35.657 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:37 GMT+01:00 2026
Hostname: n23m0410.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.60-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/nand.60-4/model_rep3.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2162 iterations in 8.54 seconds (average 0.003950, setup 0.00)

Time for model construction: 8.845 seconds.

Type:        DTMC
States:      18826082 (1 initial)
Transitions: 29772212

Transition matrix: 97452 nodes (1103 terminal), 29772212 minterms, vars: 33r/33c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/nand.60-4/model_rep3.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at jdd.JDDNode.getThen(JDDNode.java:111)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:503)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
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
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:461)

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/nand.60-4/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_nand.60-4_rep4.log

```
Command(s):
../bin/prism  models/nand.60-4/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/nand.60-4/model_rep4.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 30.254 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:43:09 GMT+01:00 2026
Hostname: n23m0120.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.60-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/nand.60-4/model_rep4.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2162 iterations in 7.99 seconds (average 0.003696, setup 0.00)

Time for model construction: 8.238 seconds.

Type:        DTMC
States:      18826082 (1 initial)
Transitions: 29772212

Transition matrix: 97452 nodes (1103 terminal), 29772212 minterms, vars: 33r/33c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/nand.60-4/model_rep4.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at jdd.JDDNode.getThen(JDDNode.java:111)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:505)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
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
out/prism_from-prism_to-umb_norewards/nand.60-4/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_nand.60-4_rep5.log

```
Command(s):
../bin/prism  models/nand.60-4/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/nand.60-4/model_rep5.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 42.651 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:38 GMT+01:00 2026
Hostname: n23m0061.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.60-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/nand.60-4/model_rep5.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/nand.60-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 2162 iterations in 17.37 seconds (average 0.008034, setup 0.00)

Time for model construction: 17.8 seconds.

Type:        DTMC
States:      18826082 (1 initial)
Transitions: 29772212

Transition matrix: 97452 nodes (1103 terminal), 29772212 minterms, vars: 33r/33c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/nand.60-4/model_rep5.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at odd.ODDNode.getThen(ODDNode.java:71)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
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
out/prism_from-prism_to-umb_norewards/nand.60-4/model_rep5.umb:	File does not exist.
```

