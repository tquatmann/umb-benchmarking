# Log files

Tool configuration: prism_from-prism_to-umb_norewards
Benchmark: [fms.8](../../models/fms.8)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_to-umb_norewards_fms.8_rep1.log

```
Command(s):
../bin/prism  models/fms.8/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/fms.8/model.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 163.383 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:32:30 GMT+01:00 2026
Hostname: r23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/fms.8/model.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 65 iterations in 3.26 seconds (average 0.050154, setup 0.00)

Time for model construction: 3.439 seconds.

Type:        CTMC
States:      4459455 (1 initial)
Transitions: 38533968

Rate matrix: 215250 nodes (84 terminal), 38533968 minterms, vars: 70r/70c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/fms.8/model.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at jdd.JDDNode.getThen(JDDNode.java:111)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:505)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
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
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/fms.8/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_fms.8_rep2.log

```
Command(s):
../bin/prism  models/fms.8/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/fms.8/model_rep2.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 170.159 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:32 GMT+01:00 2026
Hostname: n23m0234.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/fms.8/model_rep2.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 65 iterations in 3.80 seconds (average 0.058462, setup 0.00)

Time for model construction: 4.042 seconds.

Type:        CTMC
States:      4459455 (1 initial)
Transitions: 38533968

Rate matrix: 215250 nodes (84 terminal), 38533968 minterms, vars: 70r/70c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/fms.8/model_rep2.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at odd.ODDNode.getElse(ODDNode.java:76)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
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
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
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

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/fms.8/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_fms.8_rep3.log

```
Command(s):
../bin/prism  models/fms.8/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/fms.8/model_rep3.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 190.832 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:38 GMT+01:00 2026
Hostname: r23m0016.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/fms.8/model_rep3.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 65 iterations in 7.61 seconds (average 0.117077, setup 0.00)

Time for model construction: 8.01 seconds.

Type:        CTMC
States:      4459455 (1 initial)
Transitions: 38533968

Rate matrix: 215250 nodes (84 terminal), 38533968 minterms, vars: 70r/70c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/fms.8/model_rep3.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at odd.ODDNode.getThen(ODDNode.java:71)
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
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
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
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/fms.8/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_fms.8_rep4.log

```
Command(s):
../bin/prism  models/fms.8/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/fms.8/model_rep4.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 223.662 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:04 GMT+01:00 2026
Hostname: r23m0088.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/fms.8/model_rep4.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 65 iterations in 3.11 seconds (average 0.047846, setup 0.00)

Time for model construction: 3.294 seconds.

Type:        CTMC
States:      4459455 (1 initial)
Transitions: 38533968

Rate matrix: 215250 nodes (84 terminal), 38533968 minterms, vars: 70r/70c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/fms.8/model_rep4.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at odd.ODDNode.getElse(ODDNode.java:76)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
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
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/fms.8/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_fms.8_rep5.log

```
Command(s):
../bin/prism  models/fms.8/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/fms.8/model_rep5.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 174.162 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:01 GMT+01:00 2026
Hostname: r23m0076.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/fms.8/model_rep5.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 65 iterations in 3.23 seconds (average 0.049692, setup 0.00)

Time for model construction: 3.408 seconds.

Type:        CTMC
States:      4459455 (1 initial)
Transitions: 38533968

Rate matrix: 215250 nodes (84 terminal), 38533968 minterms, vars: 70r/70c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/fms.8/model_rep5.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at odd.ODDNode.getElse(ODDNode.java:76)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
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
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
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

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/fms.8/model_rep5.umb:	File does not exist.
```

