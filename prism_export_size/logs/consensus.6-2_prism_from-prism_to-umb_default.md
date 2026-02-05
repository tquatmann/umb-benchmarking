# Log files for prism_from-prism_to-umb_default on model [consensus.6-2](../../models/consensus.6-2)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_to-umb_default_consensus.6-2_rep1.log

```
Command(s):
../bin/prism  models/consensus.6-2/model.prism -exportmodel out/prism_from-prism_to-umb_default/consensus.6-2/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 18.488 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:28:03 GMT+01:00 2026
Hostname: n23m0095.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.6-2/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/consensus.6-2/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 149 iterations in 0.05 seconds (average 0.000336, setup 0.00)

Time for model construction: 0.261 seconds.

Type:        MDP
States:      1258240 (1 initial)
Transitions: 6236736

Transition matrix: 7075 nodes (3 terminal), 6236736 minterms, vars: 24r/24c/6nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/consensus.6-2/model.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at jdd.JDDNode.getElse(JDDNode.java:139)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:497)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:461)
	at symbolic.build.MTBDD2ExplicitModel.convertMDPTransitions(MTBDD2ExplicitModel.java:225)
	at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:104)
	at prism.Prism.doExportBuiltModel(Prism.java:2838)
	at prism.Prism.exportBuiltModelTask(Prism.java:2804)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
	at prism.PrismCL.doExports(PrismCL.java:868)

############################## Output files ##############################
out/prism_from-prism_to-umb_default/consensus.6-2/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_default_consensus.6-2_rep2.log

```
Command(s):
../bin/prism  models/consensus.6-2/model.prism -exportmodel out/prism_from-prism_to-umb_default/consensus.6-2/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 14.210 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:10 GMT+01:00 2026
Hostname: n23m0057.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.6-2/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/consensus.6-2/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 149 iterations in 0.04 seconds (average 0.000268, setup 0.00)

Time for model construction: 0.074 seconds.

Type:        MDP
States:      1258240 (1 initial)
Transitions: 6236736

Transition matrix: 7075 nodes (3 terminal), 6236736 minterms, vars: 24r/24c/6nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/consensus.6-2/model_rep2.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at jdd.JDDNode.getElse(JDDNode.java:139)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:497)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:461)
	at symbolic.build.MTBDD2ExplicitModel.convertMDPTransitions(MTBDD2ExplicitModel.java:225)
	at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:104)
	at prism.Prism.doExportBuiltModel(Prism.java:2838)
	at prism.Prism.exportBuiltModelTask(Prism.java:2804)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
	at prism.PrismCL.doExports(PrismCL.java:868)

############################## Output files ##############################
out/prism_from-prism_to-umb_default/consensus.6-2/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_default_consensus.6-2_rep3.log

```
Command(s):
../bin/prism  models/consensus.6-2/model.prism -exportmodel out/prism_from-prism_to-umb_default/consensus.6-2/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 17.908 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:05 GMT+01:00 2026
Hostname: n23m0364.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.6-2/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/consensus.6-2/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 149 iterations in 0.05 seconds (average 0.000336, setup 0.00)

Time for model construction: 0.088 seconds.

Type:        MDP
States:      1258240 (1 initial)
Transitions: 6236736

Transition matrix: 7075 nodes (3 terminal), 6236736 minterms, vars: 24r/24c/6nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/consensus.6-2/model_rep3.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.HashMap.resize(HashMap.java:711)
	at java.base/java.util.HashMap.merge(HashMap.java:1372)
	at explicit.Distribution.add(Distribution.java:152)
	at symbolic.build.MTBDD2ExplicitModel.lambda$convertMDPTransitions$1(MTBDD2ExplicitModel.java:230)
	at symbolic.build.MTBDD2ExplicitModel$$Lambda/0x00001529df0a34a8.accept(Unknown Source)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:484)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:461)
	at symbolic.build.MTBDD2ExplicitModel.convertMDPTransitions(MTBDD2ExplicitModel.java:225)

############################## Output files ##############################
out/prism_from-prism_to-umb_default/consensus.6-2/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_default_consensus.6-2_rep4.log

```
Command(s):
../bin/prism  models/consensus.6-2/model.prism -exportmodel out/prism_from-prism_to-umb_default/consensus.6-2/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 20.157 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:59:52 GMT+01:00 2026
Hostname: n23m0275.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.6-2/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/consensus.6-2/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 149 iterations in 0.06 seconds (average 0.000403, setup 0.00)

Time for model construction: 0.097 seconds.

Type:        MDP
States:      1258240 (1 initial)
Transitions: 6236736

Transition matrix: 7075 nodes (3 terminal), 6236736 minterms, vars: 24r/24c/6nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/consensus.6-2/model_rep4.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at odd.ODDNode.getThen(ODDNode.java:71)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:461)
	at symbolic.build.MTBDD2ExplicitModel.convertMDPTransitions(MTBDD2ExplicitModel.java:225)
	at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:104)
	at prism.Prism.doExportBuiltModel(Prism.java:2838)
	at prism.Prism.exportBuiltModelTask(Prism.java:2804)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
	at prism.PrismCL.doExports(PrismCL.java:868)

############################## Output files ##############################
out/prism_from-prism_to-umb_default/consensus.6-2/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_default_consensus.6-2_rep5.log

```
Command(s):
../bin/prism  models/consensus.6-2/model.prism -exportmodel out/prism_from-prism_to-umb_default/consensus.6-2/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 13.714 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:26:08 GMT+01:00 2026
Hostname: n23m0061.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/consensus.6-2/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/consensus.6-2/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 149 iterations in 0.05 seconds (average 0.000336, setup 0.00)

Time for model construction: 0.078 seconds.

Type:        MDP
States:      1258240 (1 initial)
Transitions: 6236736

Transition matrix: 7075 nodes (3 terminal), 6236736 minterms, vars: 24r/24c/6nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/consensus.6-2/model_rep5.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at odd.ODDNode.getElse(ODDNode.java:76)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:515)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:516)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:517)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:514)
	at symbolic.build.MTBDD2ExplicitModel.traverseMatrixDD(MTBDD2ExplicitModel.java:461)
	at symbolic.build.MTBDD2ExplicitModel.convertMDPTransitions(MTBDD2ExplicitModel.java:225)
	at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:104)
	at prism.Prism.doExportBuiltModel(Prism.java:2838)
	at prism.Prism.exportBuiltModelTask(Prism.java:2804)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
	at prism.PrismCL.doExports(PrismCL.java:868)

############################## Output files ##############################
out/prism_from-prism_to-umb_default/consensus.6-2/model_rep5.umb:	File does not exist.
```

