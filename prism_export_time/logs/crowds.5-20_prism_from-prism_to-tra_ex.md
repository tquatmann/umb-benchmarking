# Log files

Tool configuration: prism_from-prism_to-tra_ex
Benchmark: [crowds.5-20](../../models/crowds.5-20)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_to-tra_ex_crowds.5-20_rep1.log

```
Command(s):
../bin/prism -ex models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-tra_ex/crowds.5-20/model.tra,lab,rew:precision=17
Wallclock time: 29.223 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:35:40 GMT+01:00 2026
Hostname: n23m0113.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/crowds.5-20/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 554895 971496 1491822 1720840 1819270 1847648 1853729
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
out/prism_from-prism_to-tra_ex/crowds.5-20/model.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/crowds.5-20/model.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/crowds.5-20/model.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/crowds.5-20/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_crowds.5-20_rep2.log

```
Command(s):
../bin/prism -ex models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep2.tra,lab,rew:precision=17
Wallclock time: 29.644 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:36 GMT+01:00 2026
Hostname: n23m0205.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 552895 940585 1466929 1710040 1796204 1842825 1850933
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
out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep2.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep2.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_crowds.5-20_rep3.log

```
Command(s):
../bin/prism -ex models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep3.tra,lab,rew:precision=17
Wallclock time: 25.194 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:29:49 GMT+01:00 2026
Hostname: n23m0288.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 520169 953443 1466995 1686901 1798698 1845319 1851400
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
out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep3.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep3.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_crowds.5-20_rep4.log

```
Command(s):
../bin/prism -ex models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep4.tra,lab,rew:precision=17
Wallclock time: 32.440 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:55 GMT+01:00 2026
Hostname: r23m0030.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 442711 791652 1308417 1602814 1735894 1821851 1846175 1853269
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
out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep4.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep4.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_crowds.5-20_rep5.log

```
Command(s):
../bin/prism -ex models/crowds.5-20/model.prism -exportmodel out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep5.tra,lab,rew:precision=17
Wallclock time: 30.731 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:48:44 GMT+01:00 2026
Hostname: n23m0275.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/crowds.5-20/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/crowds.5-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 443880 780457 1308626 1616449 1735000 1830377 1848620 1851661
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
out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep5.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep5.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/crowds.5-20/model_rep5.trew:	File does not exist.
```

