# Log files for prism_from-prism_to-umb_default on model [wlan.6-0](../../models/wlan.6-0)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_to-umb_default_wlan.6-0_rep1.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-umb_default/wlan.6-0/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 23.870 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:29:05 GMT+01:00 2026
Hostname: n23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/wlan.6-0/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.34 seconds (average 0.001744, setup 0.00)

Time for model construction: 0.414 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/wlan.6-0/model.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.MDPSimple.addActionLabelledChoice(MDPSimple.java:329)
	at symbolic.build.MTBDD2ExplicitModel.lambda$convertMDPTransitions$3(MTBDD2ExplicitModel.java:245)
	at symbolic.build.MTBDD2ExplicitModel$$Lambda/0x000014916709c428.accept(Unknown Source)
	at java.base/java.util.HashMap.forEach(HashMap.java:1430)
	at symbolic.build.MTBDD2ExplicitModel.convertMDPTransitions(MTBDD2ExplicitModel.java:245)
	at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:104)
	at prism.Prism.doExportBuiltModel(Prism.java:2838)
	at prism.Prism.exportBuiltModelTask(Prism.java:2804)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_default/wlan.6-0/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_default_wlan.6-0_rep2.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-umb_default/wlan.6-0/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 25.029 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:39:37 GMT+01:00 2026
Hostname: n23m0166.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/wlan.6-0/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.43 seconds (average 0.002205, setup 0.00)

Time for model construction: 0.517 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/wlan.6-0/model_rep2.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.MDPSimple.addActionLabelledChoice(MDPSimple.java:329)
	at symbolic.build.MTBDD2ExplicitModel.lambda$convertMDPTransitions$3(MTBDD2ExplicitModel.java:245)
	at symbolic.build.MTBDD2ExplicitModel$$Lambda/0x000014d84f09c428.accept(Unknown Source)
	at java.base/java.util.HashMap.forEach(HashMap.java:1430)
	at symbolic.build.MTBDD2ExplicitModel.convertMDPTransitions(MTBDD2ExplicitModel.java:245)
	at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:104)
	at prism.Prism.doExportBuiltModel(Prism.java:2838)
	at prism.Prism.exportBuiltModelTask(Prism.java:2804)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_default/wlan.6-0/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_default_wlan.6-0_rep3.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-umb_default/wlan.6-0/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 23.840 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:52 GMT+01:00 2026
Hostname: r23m0198.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/wlan.6-0/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.35 seconds (average 0.001795, setup 0.00)

Time for model construction: 0.438 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/wlan.6-0/model_rep3.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.MDPSimple.addActionLabelledChoice(MDPSimple.java:329)
	at symbolic.build.MTBDD2ExplicitModel.lambda$convertMDPTransitions$3(MTBDD2ExplicitModel.java:245)
	at symbolic.build.MTBDD2ExplicitModel$$Lambda/0x00001512e709c428.accept(Unknown Source)
	at java.base/java.util.HashMap.forEach(HashMap.java:1430)
	at symbolic.build.MTBDD2ExplicitModel.convertMDPTransitions(MTBDD2ExplicitModel.java:245)
	at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:104)
	at prism.Prism.doExportBuiltModel(Prism.java:2838)
	at prism.Prism.exportBuiltModelTask(Prism.java:2804)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_default/wlan.6-0/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_default_wlan.6-0_rep4.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-umb_default/wlan.6-0/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 20.047 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:59 GMT+01:00 2026
Hostname: n23m0058.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/wlan.6-0/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.30 seconds (average 0.001538, setup 0.00)

Time for model construction: 0.352 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/wlan.6-0/model_rep4.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.MDPSimple.addActionLabelledChoice(MDPSimple.java:329)
	at symbolic.build.MTBDD2ExplicitModel.lambda$convertMDPTransitions$3(MTBDD2ExplicitModel.java:245)
	at symbolic.build.MTBDD2ExplicitModel$$Lambda/0x00001520c309c428.accept(Unknown Source)
	at java.base/java.util.HashMap.forEach(HashMap.java:1430)
	at symbolic.build.MTBDD2ExplicitModel.convertMDPTransitions(MTBDD2ExplicitModel.java:245)
	at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:104)
	at prism.Prism.doExportBuiltModel(Prism.java:2838)
	at prism.Prism.exportBuiltModelTask(Prism.java:2804)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_default/wlan.6-0/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_default_wlan.6-0_rep5.log

```
Command(s):
../bin/prism  models/wlan.6-0/model.prism -exportmodel out/prism_from-prism_to-umb_default/wlan.6-0/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 27.426 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:35:05 GMT+01:00 2026
Hostname: r23m0196.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/wlan.6-0/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/wlan.6-0/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/wlan.6-0/model.prism"...

Type:        MDP
Modules:     medium station1 station2
Actions:     [] [send1] [send2] [finish1] [finish2] [time]
Variables:   col c1 c2 x1 s1 slot1 backoff1 bc1 x2 s2 slot2 backoff2 bc2
Labels:      "target"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 195 iterations in 0.57 seconds (average 0.002923, setup 0.00)

Time for model construction: 0.701 seconds.

Type:        MDP
States:      5007548 (1 initial)
Transitions: 11475748

Transition matrix: 20377 nodes (8 terminal), 11475748 minterms, vars: 47r/47c/7nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/wlan.6-0/model_rep5.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.MDPSimple.addActionLabelledChoice(MDPSimple.java:329)
	at symbolic.build.MTBDD2ExplicitModel.lambda$convertMDPTransitions$3(MTBDD2ExplicitModel.java:245)
	at symbolic.build.MTBDD2ExplicitModel$$Lambda/0x00001550af09c428.accept(Unknown Source)
	at java.base/java.util.HashMap.forEach(HashMap.java:1430)
	at symbolic.build.MTBDD2ExplicitModel.convertMDPTransitions(MTBDD2ExplicitModel.java:245)
	at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:104)
	at prism.Prism.doExportBuiltModel(Prism.java:2838)
	at prism.Prism.exportBuiltModelTask(Prism.java:2804)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_default/wlan.6-0/model_rep5.umb:	File does not exist.
```

