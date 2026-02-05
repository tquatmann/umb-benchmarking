# Log files for prism_from-prism_to-umb-gz_ex on model [nand.40-4](../../models/nand.40-4)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_to-umb-gz_ex_nand.40-4_rep1.log

```
Command(s):
../bin/prism -ex models/nand.40-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/nand.40-4/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 23.490 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:37:50 GMT+01:00 2026
Hostname: n23m0120.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/nand.40-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/nand.40-4/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/nand.40-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 2051698 2939070 3003272 3014408 3020688
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at parser.ast.Update.update(Update.java:215)
	at simulator.ChoiceListFlexi.computeTarget(ChoiceListFlexi.java:259)
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
out/prism_from-prism_to-umb-gz_ex/nand.40-4/model.umb.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_nand.40-4_rep2.log

```
Command(s):
../bin/prism -ex models/nand.40-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/nand.40-4/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 22.382 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:00 GMT+01:00 2026
Hostname: r23m0197.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/nand.40-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/nand.40-4/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/nand.40-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 2031224 2931819 2996601 3014026 3020889
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
out/prism_from-prism_to-umb-gz_ex/nand.40-4/model.umb_rep2.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_nand.40-4_rep3.log

```
Command(s):
../bin/prism -ex models/nand.40-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/nand.40-4/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 23.306 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:27:59 GMT+01:00 2026
Hostname: n23m0256.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/nand.40-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/nand.40-4/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/nand.40-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 1977150 2881188 2994119 3013646 3020511
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at simulator.ChoiceListFlexi.<init>(ChoiceListFlexi.java:77)
	at simulator.Updater.processUpdatesAndCreateNewChoice(Updater.java:353)
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
out/prism_from-prism_to-umb-gz_ex/nand.40-4/model.umb_rep3.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_nand.40-4_rep4.log

```
Command(s):
../bin/prism -ex models/nand.40-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/nand.40-4/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 28.652 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:44:10 GMT+01:00 2026
Hostname: n23m0241.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/nand.40-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/nand.40-4/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/nand.40-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 1878557 2876417 2983041 3009188 3017527 3020626
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space: failed reallocation of scalar replaced objects
	at java.base/java.lang.Double.valueOf(Double.java:924)
	at prism.Evaluator$EvaluatorDouble.multiply(Evaluator.java:327)
	at prism.Evaluator$EvaluatorDouble.multiply(Evaluator.java:275)
	at simulator.ChoiceListFlexi.scaleProbabilitiesBy(ChoiceListFlexi.java:142)
	at simulator.TransitionList.scaleProbabilitiesBy(TransitionList.java:96)
	at simulator.Updater.calculateTransitions(Updater.java:266)
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
out/prism_from-prism_to-umb-gz_ex/nand.40-4/model.umb_rep4.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_nand.40-4_rep5.log

```
Command(s):
../bin/prism -ex models/nand.40-4/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/nand.40-4/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 21.338 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:58:22 GMT+01:00 2026
Hostname: n23m0247.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/nand.40-4/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/nand.40-4/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/nand.40-4/model.prism"...

Type:        DTMC
Modules:     multiplex
Actions:     []
Variables:   u c s z zx zy x y
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 2170688 2942399 3000059 3015365 3020299
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
out/prism_from-prism_to-umb-gz_ex/nand.40-4/model.umb_rep5.gz:	File does not exist.
```

