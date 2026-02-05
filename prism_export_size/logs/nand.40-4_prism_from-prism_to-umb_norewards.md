# Log files for prism_from-prism_to-umb_norewards on model [nand.40-4](../../models/nand.40-4)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_to-umb_norewards_nand.40-4_rep1.log

```
Command(s):
../bin/prism  models/nand.40-4/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/nand.40-4/model.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 24.107 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:41:33 GMT+01:00 2026
Hostname: r23m0139.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.40-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/nand.40-4/model.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/nand.40-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1442 iterations in 2.52 seconds (average 0.001748, setup 0.00)

Time for model construction: 2.615 seconds.

Type:        DTMC
States:      3999522 (1 initial)
Transitions: 6288542

Transition matrix: 49073 nodes (493 terminal), 6288542 minterms, vars: 33r/33c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/nand.40-4/model.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:423)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/nand.40-4/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_nand.40-4_rep2.log

```
Command(s):
../bin/prism  models/nand.40-4/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/nand.40-4/model_rep2.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 26.401 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:29:49 GMT+01:00 2026
Hostname: n23m0167.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.40-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/nand.40-4/model_rep2.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/nand.40-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1442 iterations in 2.84 seconds (average 0.001969, setup 0.00)

Time for model construction: 2.997 seconds.

Type:        DTMC
States:      3999522 (1 initial)
Transitions: 6288542

Transition matrix: 49073 nodes (493 terminal), 6288542 minterms, vars: 33r/33c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/nand.40-4/model_rep2.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at jdd.JDDNode.getElse(JDDNode.java:139)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:436)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/nand.40-4/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_nand.40-4_rep3.log

```
Command(s):
../bin/prism  models/nand.40-4/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/nand.40-4/model_rep3.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 23.419 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:37 GMT+01:00 2026
Hostname: n23m0040.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.40-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/nand.40-4/model_rep3.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/nand.40-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1442 iterations in 2.49 seconds (average 0.001727, setup 0.00)

Time for model construction: 2.607 seconds.

Type:        DTMC
States:      3999522 (1 initial)
Transitions: 6288542

Transition matrix: 49073 nodes (493 terminal), 6288542 minterms, vars: 33r/33c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/nand.40-4/model_rep3.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at odd.ODDNode.getElse(ODDNode.java:76)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:439)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStates(StateListMTBDD.java:402)
	at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:126)
	at prism.Prism.doExportBuiltModel(Prism.java:2838)

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/nand.40-4/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_nand.40-4_rep4.log

```
Command(s):
../bin/prism  models/nand.40-4/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/nand.40-4/model_rep4.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 24.560 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:10 GMT+01:00 2026
Hostname: n23m0160.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.40-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/nand.40-4/model_rep4.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/nand.40-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1442 iterations in 2.67 seconds (average 0.001852, setup 0.00)

Time for model construction: 2.8 seconds.

Type:        DTMC
States:      3999522 (1 initial)
Transitions: 6288542

Transition matrix: 49073 nodes (493 terminal), 6288542 minterms, vars: 33r/33c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/nand.40-4/model_rep4.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at jdd.JDDNode.getElse(JDDNode.java:139)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:436)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/nand.40-4/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_nand.40-4_rep5.log

```
Command(s):
../bin/prism  models/nand.40-4/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/nand.40-4/model_rep5.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 22.215 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:21:09 GMT+01:00 2026
Hostname: n23m0313.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/nand.40-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/nand.40-4/model_rep5.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/nand.40-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 1442 iterations in 2.52 seconds (average 0.001748, setup 0.00)

Time for model construction: 2.618 seconds.

Type:        DTMC
States:      3999522 (1 initial)
Transitions: 6288542

Transition matrix: 49073 nodes (493 terminal), 6288542 minterms, vars: 33r/33c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/nand.40-4/model_rep5.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at jdd.JDDNode.getThen(JDDNode.java:111)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:437)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:447)
	at symbolic.states.StateListMTBDD.getAsListOfStatesRec(StateListMTBDD.java:443)

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/nand.40-4/model_rep5.umb:	File does not exist.
```

