# Log files

Tool configuration: prism_from-prism_to-umb_norewards
Benchmark: [eajs.6-300-13](../../models/eajs.6-300-13)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_to-umb_norewards_eajs.6-300-13_rep1.log

```
Command(s):
../bin/prism  models/eajs.6-300-13/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/eajs.6-300-13/model.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 67.795 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:42:09 GMT+01:00 2026
Hostname: n23m0241.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.6-300-13/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/eajs.6-300-13/model.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 89 iterations in 0.18 seconds (average 0.002022, setup 0.00)

Time for model construction: 0.563 seconds.

Type:        MDP
States:      7901694 (1 initial)
Transitions: 19722777

Transition matrix: 38911 nodes (7 terminal), 19722777 minterms, vars: 50r/50c/5nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/eajs.6-300-13/model.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at odd.ODDNode.getElse(ODDNode.java:76)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/eajs.6-300-13/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_eajs.6-300-13_rep2.log

```
Command(s):
../bin/prism  models/eajs.6-300-13/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/eajs.6-300-13/model_rep2.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 54.068 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:28:29 GMT+01:00 2026
Hostname: n23m0058.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.6-300-13/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/eajs.6-300-13/model_rep2.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 89 iterations in 0.15 seconds (average 0.001685, setup 0.00)

Time for model construction: 0.481 seconds.

Type:        MDP
States:      7901694 (1 initial)
Transitions: 19722777

Transition matrix: 38911 nodes (7 terminal), 19722777 minterms, vars: 50r/50c/5nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/eajs.6-300-13/model_rep2.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.lang.Integer.valueOf(Integer.java:1019)
	at explicit.Distribution.add(Distribution.java:152)
	at symbolic.build.MTBDD2ExplicitModel.lambda$convertMDPTransitions$1(MTBDD2ExplicitModel.java:230)
	at symbolic.build.MTBDD2ExplicitModel$$Lambda/0x000014b7bb0a36a8.accept(Unknown Source)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:484)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
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

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/eajs.6-300-13/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_eajs.6-300-13_rep3.log

```
Command(s):
../bin/prism  models/eajs.6-300-13/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/eajs.6-300-13/model_rep3.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 62.900 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:21:40 GMT+01:00 2026
Hostname: n23m0113.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.6-300-13/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/eajs.6-300-13/model_rep3.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 89 iterations in 0.20 seconds (average 0.002247, setup 0.00)

Time for model construction: 0.724 seconds.

Type:        MDP
States:      7901694 (1 initial)
Transitions: 19722777

Transition matrix: 38911 nodes (7 terminal), 19722777 minterms, vars: 50r/50c/5nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/eajs.6-300-13/model_rep3.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at jdd.JDDNode.getThen(JDDNode.java:111)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:505)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/eajs.6-300-13/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_eajs.6-300-13_rep4.log

```
Command(s):
../bin/prism  models/eajs.6-300-13/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/eajs.6-300-13/model_rep4.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 56.076 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:32:22 GMT+01:00 2026
Hostname: n23m0328.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.6-300-13/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/eajs.6-300-13/model_rep4.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 89 iterations in 0.17 seconds (average 0.001910, setup 0.00)

Time for model construction: 0.531 seconds.

Type:        MDP
States:      7901694 (1 initial)
Transitions: 19722777

Transition matrix: 38911 nodes (7 terminal), 19722777 minterms, vars: 50r/50c/5nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/eajs.6-300-13/model_rep4.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at odd.ODDNode.getElse(ODDNode.java:76)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
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
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/eajs.6-300-13/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_eajs.6-300-13_rep5.log

```
Command(s):
../bin/prism  models/eajs.6-300-13/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/eajs.6-300-13/model_rep5.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 51.402 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:08 GMT+01:00 2026
Hostname: n23m0247.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/eajs.6-300-13/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/eajs.6-300-13/model_rep5.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 89 iterations in 0.15 seconds (average 0.001685, setup 0.00)

Time for model construction: 0.441 seconds.

Type:        MDP
States:      7901694 (1 initial)
Transitions: 19722777

Transition matrix: 38911 nodes (7 terminal), 19722777 minterms, vars: 50r/50c/5nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/eajs.6-300-13/model_rep5.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.lang.Integer.valueOf(Integer.java:1019)
	at explicit.Distribution.add(Distribution.java:152)
	at symbolic.build.MTBDD2ExplicitModel.lambda$convertMDPTransitions$1(MTBDD2ExplicitModel.java:230)
	at symbolic.build.MTBDD2ExplicitModel$$Lambda/0x000014f76b0a36a8.accept(Unknown Source)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:484)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/eajs.6-300-13/model_rep5.umb:	File does not exist.
```

