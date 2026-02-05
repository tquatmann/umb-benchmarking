# Log files for prism_from-prism_to-umb_ex on model [kanban.5](../../models/kanban.5)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_to-umb_ex_kanban.5_rep1.log

```
Command(s):
../bin/prism -ex models/kanban.5/model.prism -exportmodel out/prism_from-prism_to-umb_ex/kanban.5/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 43.396 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:33:03 GMT+01:00 2026
Hostname: r23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/kanban.5/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/kanban.5/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Building model (engine:explicit)...

Computing reachable states... 418346 751388 1050079 1233088 1265027 1279918 1286952 1290727 1293123 1294417 1295407 1296585
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at simulator.ChoiceListFlexi.add(ChoiceListFlexi.java:132)
	at simulator.Updater.processUpdatesAndCreateNewChoice(Updater.java:380)
	at simulator.Updater.calculateTransitions(Updater.java:196)
	at simulator.ModulesFileModelGenerator.getTransitionListScalars(ModulesFileModelGenerator.java:827)
	at simulator.ModulesFileModelGenerator.getTransitionList(ModulesFileModelGenerator.java:814)
	at simulator.ModulesFileModelGenerator.getNumChoices(ModulesFileModelGenerator.java:513)
	at explicit.ConstructModel.constructModel(ConstructModel.java:273)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/kanban.5/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_kanban.5_rep2.log

```
Command(s):
../bin/prism -ex models/kanban.5/model.prism -exportmodel out/prism_from-prism_to-umb_ex/kanban.5/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 41.909 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:20 GMT+01:00 2026
Hostname: n23m0138.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/kanban.5/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/kanban.5/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Building model (engine:explicit)...

Computing reachable states... 440837 804042 1129674 1243138 1269359 1282126 1287944 1291589 1293820 1294851 1295871 1296869
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.lang.Double.valueOf(Double.java:924)
	at prism.Evaluator$EvaluatorDouble.multiply(Evaluator.java:327)
	at prism.Evaluator$EvaluatorDouble.multiply(Evaluator.java:275)
	at simulator.ChoiceListFlexi.productWith(ChoiceListFlexi.java:179)
	at simulator.Updater.processUpdatesAndAddToProduct(Updater.java:418)
	at simulator.Updater.calculateTransitions(Updater.java:224)
	at simulator.ModulesFileModelGenerator.getTransitionListScalars(ModulesFileModelGenerator.java:827)
	at simulator.ModulesFileModelGenerator.getTransitionList(ModulesFileModelGenerator.java:814)
	at simulator.ModulesFileModelGenerator.getNumChoices(ModulesFileModelGenerator.java:513)
	at explicit.ConstructModel.constructModel(ConstructModel.java:273)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/kanban.5/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_kanban.5_rep3.log

```
Command(s):
../bin/prism -ex models/kanban.5/model.prism -exportmodel out/prism_from-prism_to-umb_ex/kanban.5/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 45.509 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:26:01 GMT+01:00 2026
Hostname: n23m0008.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/kanban.5/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/kanban.5/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Building model (engine:explicit)...

Computing reachable states... 404000 731554 1035818 1225154 1258317 1275780 1282826 1288052 1291003 1293339 1294476 1295662 1296647
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.lang.Double.valueOf(Double.java:924)
	at prism.Evaluator$EvaluatorDouble.evaluate(Evaluator.java:368)
	at prism.Evaluator$EvaluatorDouble.evaluate(Evaluator.java:275)
	at prism.Evaluator.evaluate(Evaluator.java:164)
	at simulator.Updater.getProbabilityInState(Updater.java:333)
	at simulator.Updater.processUpdatesAndCreateNewChoice(Updater.java:359)
	at simulator.Updater.calculateTransitions(Updater.java:196)
	at simulator.ModulesFileModelGenerator.getTransitionListScalars(ModulesFileModelGenerator.java:827)
	at simulator.ModulesFileModelGenerator.getTransitionList(ModulesFileModelGenerator.java:814)
	at simulator.ModulesFileModelGenerator.getNumChoices(ModulesFileModelGenerator.java:513)
	at explicit.ConstructModel.constructModel(ConstructModel.java:273)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/kanban.5/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_kanban.5_rep4.log

```
Command(s):
../bin/prism -ex models/kanban.5/model.prism -exportmodel out/prism_from-prism_to-umb_ex/kanban.5/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 55.879 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:41:08 GMT+01:00 2026
Hostname: n23m0165.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/kanban.5/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/kanban.5/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Building model (engine:explicit)...

Computing reachable states... 324973 596246 820520 1024641 1187021 1248891 1266965 1276968 1283344 1287681 1290901 1292936 1294218 1295043 1295747 1296564
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at parser.State.<init>(State.java:50)
	at parser.State.<init>(State.java:59)
	at simulator.ChoiceListFlexi.computeTarget(ChoiceListFlexi.java:257)
	at simulator.ModulesFileModelGenerator.computeTransitionTarget(ModulesFileModelGenerator.java:664)
	at explicit.ConstructModel.constructModel(ConstructModel.java:295)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/kanban.5/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_kanban.5_rep5.log

```
Command(s):
../bin/prism -ex models/kanban.5/model.prism -exportmodel out/prism_from-prism_to-umb_ex/kanban.5/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 47.661 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:12 GMT+01:00 2026
Hostname: n23m0289.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/kanban.5/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/kanban.5/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Building model (engine:explicit)...

Computing reachable states... 386820 700750 991225 1209912 1252163 1272892 1282618 1287991 1291128 1292950 1294565 1295394 1296418
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at parser.State.<init>(State.java:50)
	at parser.State.<init>(State.java:59)
	at simulator.ChoiceListFlexi.computeTarget(ChoiceListFlexi.java:257)
	at simulator.ModulesFileModelGenerator.computeTransitionTarget(ModulesFileModelGenerator.java:664)
	at explicit.ConstructModel.constructModel(ConstructModel.java:295)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/kanban.5/model_rep5.umb:	File does not exist.
```

