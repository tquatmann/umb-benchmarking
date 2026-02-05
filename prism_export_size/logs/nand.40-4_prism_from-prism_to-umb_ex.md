# Log files for prism_from-prism_to-umb_ex on model [nand.40-4](../../models/nand.40-4)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_to-umb_ex_nand.40-4_rep1.log

```
Command(s):
../bin/prism -ex models/nand.40-4/model.prism -exportmodel out/prism_from-prism_to-umb_ex/nand.40-4/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 21.406 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:30:56 GMT+01:00 2026
Hostname: n23m0244.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/nand.40-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/nand.40-4/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/nand.40-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 2216703 2941675 2996752 3015542 3020428
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.DTMCSimple.addToProbability(DTMCSimple.java:258)
	at explicit.ConstructModel.constructModel(ConstructModel.java:316)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/nand.40-4/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_nand.40-4_rep2.log

```
Command(s):
../bin/prism -ex models/nand.40-4/model.prism -exportmodel out/prism_from-prism_to-umb_ex/nand.40-4/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 28.736 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:32:32 GMT+01:00 2026
Hostname: n23m0072.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/nand.40-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/nand.40-4/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/nand.40-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 1750969 2899026 2979110 3006297 3014807 3019524
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at simulator.ChoiceListFlexi.add(ChoiceListFlexi.java:133)
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
out/prism_from-prism_to-umb_ex/nand.40-4/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_nand.40-4_rep3.log

```
Command(s):
../bin/prism -ex models/nand.40-4/model.prism -exportmodel out/prism_from-prism_to-umb_ex/nand.40-4/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 23.420 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:16:03 GMT+01:00 2026
Hostname: n23m0273.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/nand.40-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/nand.40-4/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/nand.40-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 1802924 2891542 2986400 3010852 3020018 3021948
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.TreeMap.addEntry(TreeMap.java:801)
	at java.base/java.util.TreeMap.put(TreeMap.java:864)
	at java.base/java.util.TreeMap.put(TreeMap.java:570)
	at explicit.IndexedSet.add(IndexedSet.java:72)
	at explicit.ConstructModel.constructModel(ConstructModel.java:297)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/nand.40-4/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_nand.40-4_rep4.log

```
Command(s):
../bin/prism -ex models/nand.40-4/model.prism -exportmodel out/prism_from-prism_to-umb_ex/nand.40-4/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 24.969 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:54 GMT+01:00 2026
Hostname: n23m0375.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/nand.40-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/nand.40-4/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/nand.40-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 1838424 2877828 2981513 3008259 3016340 3020427
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.lang.Double.valueOf(Double.java:924)
	at prism.Evaluator$EvaluatorDouble.add(Evaluator.java:315)
	at prism.Evaluator$EvaluatorDouble.add(Evaluator.java:275)
	at simulator.Updater.processUpdatesAndCreateNewChoice(Updater.java:377)
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
out/prism_from-prism_to-umb_ex/nand.40-4/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_nand.40-4_rep5.log

```
Command(s):
../bin/prism -ex models/nand.40-4/model.prism -exportmodel out/prism_from-prism_to-umb_ex/nand.40-4/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 27.282 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:58:53 GMT+01:00 2026
Hostname: r23m0195.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/nand.40-4/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/nand.40-4/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/nand.40-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 1949630 2927484 2994390 3010835 3018850 3021301
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space: failed reallocation of scalar replaced objects
	at java.base/java.lang.Double.valueOf(Double.java:924)
	at prism.Evaluator$EvaluatorDouble.add(Evaluator.java:315)
	at prism.Evaluator$EvaluatorDouble.add(Evaluator.java:275)
	at simulator.TransitionList.getProbabilitySum(TransitionList.java:125)
	at simulator.Updater.calculateTransitions(Updater.java:265)
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
out/prism_from-prism_to-umb_ex/nand.40-4/model_rep5.umb:	File does not exist.
```

