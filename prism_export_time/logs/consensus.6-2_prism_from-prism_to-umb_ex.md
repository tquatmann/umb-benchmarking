# Log files for prism_from-prism_to-umb_ex on model [consensus.6-2](../../models/consensus.6-2)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_to-umb_ex_consensus.6-2_rep1.log

```
Command(s):
../bin/prism -ex models/consensus.6-2/model.prism -exportmodel out/prism_from-prism_to-umb_ex/consensus.6-2/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 12.602 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:49:58 GMT+01:00 2026
Hostname: n23m0383.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/consensus.6-2/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/consensus.6-2/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Building model (engine:explicit)...

Computing reachable states... 610167 826435 840342
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.Arrays.copyOf(Arrays.java:3512)
	at java.base/java.util.Arrays.copyOf(Arrays.java:3481)
	at java.base/java.util.ArrayList.grow(ArrayList.java:238)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.ChoiceActionsSimple.setAction(ChoiceActionsSimple.java:133)
	at explicit.MDPSimple.addActionLabelledChoice(MDPSimple.java:331)
	at explicit.ConstructModel.constructModel(ConstructModel.java:353)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/consensus.6-2/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_consensus.6-2_rep2.log

```
Command(s):
../bin/prism -ex models/consensus.6-2/model.prism -exportmodel out/prism_from-prism_to-umb_ex/consensus.6-2/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 12.957 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:30:50 GMT+01:00 2026
Hostname: n23m0379.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/consensus.6-2/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/consensus.6-2/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Building model (engine:explicit)...

Computing reachable states... 613381 825415 839541
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.Arrays.copyOf(Arrays.java:3512)
	at java.base/java.util.Arrays.copyOf(Arrays.java:3481)
	at java.base/java.util.ArrayList.grow(ArrayList.java:238)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.ChoiceActionsSimple.setAction(ChoiceActionsSimple.java:133)
	at explicit.MDPSimple.addActionLabelledChoice(MDPSimple.java:331)
	at explicit.ConstructModel.constructModel(ConstructModel.java:353)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/consensus.6-2/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_consensus.6-2_rep3.log

```
Command(s):
../bin/prism -ex models/consensus.6-2/model.prism -exportmodel out/prism_from-prism_to-umb_ex/consensus.6-2/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 12.906 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:19:08 GMT+01:00 2026
Hostname: n23m0099.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/consensus.6-2/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/consensus.6-2/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Building model (engine:explicit)...

Computing reachable states... 546896 822289 838910
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.Arrays.copyOf(Arrays.java:3512)
	at java.base/java.util.Arrays.copyOf(Arrays.java:3481)
	at java.base/java.util.ArrayList.grow(ArrayList.java:238)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.ChoiceActionsSimple.setAction(ChoiceActionsSimple.java:133)
	at explicit.MDPSimple.addActionLabelledChoice(MDPSimple.java:331)
	at explicit.ConstructModel.constructModel(ConstructModel.java:353)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/consensus.6-2/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_consensus.6-2_rep4.log

```
Command(s):
../bin/prism -ex models/consensus.6-2/model.prism -exportmodel out/prism_from-prism_to-umb_ex/consensus.6-2/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 14.469 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:26:56 GMT+01:00 2026
Hostname: n23m0252.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/consensus.6-2/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/consensus.6-2/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Building model (engine:explicit)...

Computing reachable states... 549508 820310 838431 841617
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.Arrays.copyOf(Arrays.java:3512)
	at java.base/java.util.Arrays.copyOf(Arrays.java:3481)
	at java.base/java.util.ArrayList.grow(ArrayList.java:238)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.ChoiceActionsSimple.setAction(ChoiceActionsSimple.java:133)
	at explicit.MDPSimple.addActionLabelledChoice(MDPSimple.java:331)
	at explicit.ConstructModel.constructModel(ConstructModel.java:353)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/consensus.6-2/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_consensus.6-2_rep5.log

```
Command(s):
../bin/prism -ex models/consensus.6-2/model.prism -exportmodel out/prism_from-prism_to-umb_ex/consensus.6-2/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 14.388 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:09:59 GMT+01:00 2026
Hostname: n23m0058.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/consensus.6-2/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/consensus.6-2/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Building model (engine:explicit)...

Computing reachable states... 524034 822359 838163 841636
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.Arrays.copyOf(Arrays.java:3512)
	at java.base/java.util.Arrays.copyOf(Arrays.java:3481)
	at java.base/java.util.ArrayList.grow(ArrayList.java:238)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.ChoiceActionsSimple.setAction(ChoiceActionsSimple.java:133)
	at explicit.MDPSimple.addActionLabelledChoice(MDPSimple.java:331)
	at explicit.ConstructModel.constructModel(ConstructModel.java:353)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/consensus.6-2/model_rep5.umb:	File does not exist.
```

