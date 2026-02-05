# Log files for prism_from-prism_to-umb_ex on model [crowds.5-20](../../models/crowds.5-20)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_to-umb_ex_crowds.5-20_rep1.log

```
Command(s):
../bin/prism -ex models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-umb_ex/crowds.5-20/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 25.814 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:23:16 GMT+01:00 2026
Hostname: r23m0134.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/crowds.5-20/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 566426 961550 1492228 1712833 1826406 1846676 1852756
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.DTMCSimple.addToProbability(DTMCSimple.java:259)
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
out/prism_from-prism_to-umb_ex/crowds.5-20/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_crowds.5-20_rep2.log

```
Command(s):
../bin/prism -ex models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-umb_ex/crowds.5-20/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 29.105 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:08 GMT+01:00 2026
Hostname: n23m0375.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/crowds.5-20/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 459432 796194 1356187 1623584 1763502 1838501 1850663
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.DTMCSimple.addToProbability(DTMCSimple.java:259)
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
out/prism_from-prism_to-umb_ex/crowds.5-20/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_crowds.5-20_rep3.log

```
Command(s):
../bin/prism -ex models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-umb_ex/crowds.5-20/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 30.194 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:42:39 GMT+01:00 2026
Hostname: r23m0212.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/crowds.5-20/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 463520 803945 1326731 1605392 1732222 1829713 1847956 1854037
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
out/prism_from-prism_to-umb_ex/crowds.5-20/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_crowds.5-20_rep4.log

```
Command(s):
../bin/prism -ex models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-umb_ex/crowds.5-20/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 31.747 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:51:47 GMT+01:00 2026
Hostname: n23m0244.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/crowds.5-20/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 526289 898965 1418108 1645857 1761519 1837531 1850707 1853747
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
out/prism_from-prism_to-umb_ex/crowds.5-20/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_crowds.5-20_rep5.log

```
Command(s):
../bin/prism -ex models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-umb_ex/crowds.5-20/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 29.648 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:22:08 GMT+01:00 2026
Hostname: n23m0063.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/crowds.5-20/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 535963 950994 1476127 1696080 1804177 1844717 1850798
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
out/prism_from-prism_to-umb_ex/crowds.5-20/model_rep5.umb:	File does not exist.
```

