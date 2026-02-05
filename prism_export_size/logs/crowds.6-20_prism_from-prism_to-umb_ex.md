# Log files for prism_from-prism_to-umb_ex on model [crowds.6-20](../../models/crowds.6-20)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_to-umb_ex_crowds.6-20_rep1.log

```
Command(s):
../bin/prism -ex models/crowds.6-20/model.prism -exportmodel out/prism_from-prism_to-umb_ex/crowds.6-20/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 53.852 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:33:34 GMT+01:00 2026
Hostname: n23m0242.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/crowds.6-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/crowds.6-20/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/crowds.6-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 456900 822146 1383724 1605813 1712875 1740945 1757383 1766933 1772386 1776199 1778602 1780742 1781929 1782879 1784301
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
out/prism_from-prism_to-umb_ex/crowds.6-20/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_crowds.6-20_rep2.log

```
Command(s):
../bin/prism -ex models/crowds.6-20/model.prism -exportmodel out/prism_from-prism_to-umb_ex/crowds.6-20/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 49.601 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:06 GMT+01:00 2026
Hostname: r23m0029.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/crowds.6-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/crowds.6-20/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/crowds.6-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 458918 815724 1356569 1603274 1710584 1744028 1760079 1770569 1775797 1778926 1781537 1782725 1783911 1785099
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
out/prism_from-prism_to-umb_ex/crowds.6-20/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_crowds.6-20_rep3.log

```
Command(s):
../bin/prism -ex models/crowds.6-20/model.prism -exportmodel out/prism_from-prism_to-umb_ex/crowds.6-20/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 56.581 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:47 GMT+01:00 2026
Hostname: r23m0212.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/crowds.6-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/crowds.6-20/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/crowds.6-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 412945 749140 1172583 1547340 1685969 1727506 1749896 1762959 1770600 1774638 1777756 1779904 1781564 1782517 1783463 1784416
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
out/prism_from-prism_to-umb_ex/crowds.6-20/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_crowds.6-20_rep4.log

```
Command(s):
../bin/prism -ex models/crowds.6-20/model.prism -exportmodel out/prism_from-prism_to-umb_ex/crowds.6-20/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 41.882 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:39:06 GMT+01:00 2026
Hostname: n23m0041.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/crowds.6-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/crowds.6-20/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/crowds.6-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 549366 977290 1530765 1698654 1740183 1759941 1770438 1776390 1779977 1781876 1783063 1784725
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
out/prism_from-prism_to-umb_ex/crowds.6-20/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_crowds.6-20_rep5.log

```
Command(s):
../bin/prism -ex models/crowds.6-20/model.prism -exportmodel out/prism_from-prism_to-umb_ex/crowds.6-20/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 46.642 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:31:51 GMT+01:00 2026
Hostname: n23m0166.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/crowds.6-20/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/crowds.6-20/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/crowds.6-20/model.prism"...

Type:        DTMC
Modules:     crowds
Actions:     []
Variables:   launch new runCount start run lastSeen good bad recordLast badObserve deliver done observe0 observe1 observe2 observe3 observe4 observe5 observe6 observe7 observe8 observe9 observe10 observe11 observe12 observe13 observe14 observe15 observe16 observe17 observe18 observe19
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 478958 842236 1404722 1613892 1714718 1742318 1758045 1769491 1774714 1778072 1780930 1782111 1783539 1784725
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
out/prism_from-prism_to-umb_ex/crowds.6-20/model_rep5.umb:	File does not exist.
```

