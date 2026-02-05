# Log files for prism_from-prism_to-tra_ex on model [kanban.5](../../models/kanban.5)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_to-tra_ex_kanban.5_rep1.log

```
Command(s):
../bin/prism -ex models/kanban.5/model.prism -exportmodel out/prism_from-prism_to-tra_ex/kanban.5/model.tra,lab,rew:precision=17
Wallclock time: 41.320 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:45:46 GMT+01:00 2026
Hostname: n23m0383.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/kanban.5/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/kanban.5/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Building model (engine:explicit)...

Computing reachable states... 423264 777875 1088881 1240674 1266889 1280705 1287012 1290787 1293018 1294295 1295465 1296634
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.DTMCSimple.addToProbability(DTMCSimple.java:259)
	at explicit.ConstructModel.constructModel(ConstructModel.java:319)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/kanban.5/model.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/kanban.5/model.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/kanban.5/model.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/kanban.5/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_kanban.5_rep2.log

```
Command(s):
../bin/prism -ex models/kanban.5/model.prism -exportmodel out/prism_from-prism_to-tra_ex/kanban.5/model_rep2.tra,lab,rew:precision=17
Wallclock time: 41.283 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:23:53 GMT+01:00 2026
Hostname: n23m0351.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/kanban.5/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/kanban.5/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Building model (engine:explicit)...

Computing reachable states... 436762 779126 1088717 1239220 1266522 1280620 1287079 1290862 1293234 1294523 1295544 1296702
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at simulator.Updater.processUpdatesAndCreateNewChoice(Updater.java:379)
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
out/prism_from-prism_to-tra_ex/kanban.5/model_rep2.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/kanban.5/model_rep2.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/kanban.5/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/kanban.5/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_kanban.5_rep3.log

```
Command(s):
../bin/prism -ex models/kanban.5/model.prism -exportmodel out/prism_from-prism_to-tra_ex/kanban.5/model_rep3.tra,lab,rew:precision=17
Wallclock time: 42.668 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:29:48 GMT+01:00 2026
Hostname: n23m0166.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/kanban.5/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/kanban.5/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Building model (engine:explicit)...

Computing reachable states... 419870 756213 1064797 1233091 1261567 1278042 1286317 1290212 1293025 1294635 1295475 1296642
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
out/prism_from-prism_to-tra_ex/kanban.5/model_rep3.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/kanban.5/model_rep3.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/kanban.5/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/kanban.5/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_kanban.5_rep4.log

```
Command(s):
../bin/prism -ex models/kanban.5/model.prism -exportmodel out/prism_from-prism_to-tra_ex/kanban.5/model_rep4.tra,lab,rew:precision=17
Wallclock time: 46.195 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:58:52 GMT+01:00 2026
Hostname: n23m0142.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/kanban.5/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/kanban.5/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Building model (engine:explicit)...

Computing reachable states... 386014 701788 977355 1189297 1252217 1271315 1281799 1287596 1291203 1293637 1294810 1295658 1296642
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
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
out/prism_from-prism_to-tra_ex/kanban.5/model_rep4.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/kanban.5/model_rep4.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/kanban.5/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/kanban.5/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_kanban.5_rep5.log

```
Command(s):
../bin/prism -ex models/kanban.5/model.prism -exportmodel out/prism_from-prism_to-tra_ex/kanban.5/model_rep5.tra,lab,rew:precision=17
Wallclock time: 41.250 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:19:37 GMT+01:00 2026
Hostname: n23m0313.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/kanban.5/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/kanban.5/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Building model (engine:explicit)...

Computing reachable states... 443335 795232 1110210 1240131 1268043 1281401 1287472 1291218 1293504 1294825 1295846 1296840
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
out/prism_from-prism_to-tra_ex/kanban.5/model_rep5.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/kanban.5/model_rep5.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/kanban.5/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/kanban.5/model_rep5.trew:	File does not exist.
```

