# Log files for prism_from-prism_to-umb_ex on model [eajs.5-250-11](../../models/eajs.5-250-11)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_to-umb_ex_eajs.5-250-11_rep1.log

```
Command(s):
../bin/prism -ex models/eajs.5-250-11/model.prism -exportmodel out/prism_from-prism_to-umb_ex/eajs.5-250-11/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 44.552 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:43:42 GMT+01:00 2026
Hostname: n23m0276.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/eajs.5-250-11/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/eajs.5-250-11/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/eajs.5-250-11/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_5 Process_4
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 loc_5 t_5 t_4 loc_4
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:explicit)...

Computing reachable states... 395021 811452 1227542 1420399 1447929 1463985 1474273 1478478 1481437 1482731 1483831 1485176
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.lang.Integer.valueOf(Integer.java:1019)
	at explicit.Distribution.add(Distribution.java:152)
	at explicit.ConstructModel.constructModel(ConstructModel.java:327)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/eajs.5-250-11/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_eajs.5-250-11_rep2.log

```
Command(s):
../bin/prism -ex models/eajs.5-250-11/model.prism -exportmodel out/prism_from-prism_to-umb_ex/eajs.5-250-11/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 40.239 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:06 GMT+01:00 2026
Hostname: n23m0362.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/eajs.5-250-11/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/eajs.5-250-11/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/eajs.5-250-11/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_5 Process_4
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 loc_5 t_5 t_4 loc_4
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:explicit)...

Computing reachable states... 459429 923759 1347575 1438740 1461355 1472943 1477843 1481379 1482666 1483614 1484798
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at simulator.ChoiceListFlexi.add(ChoiceListFlexi.java:133)
	at simulator.Updater.processUpdatesAndCreateNewChoice(Updater.java:380)
	at simulator.Updater.processUpdatesAndAddToProduct(Updater.java:416)
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
out/prism_from-prism_to-umb_ex/eajs.5-250-11/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_eajs.5-250-11_rep3.log

```
Command(s):
../bin/prism -ex models/eajs.5-250-11/model.prism -exportmodel out/prism_from-prism_to-umb_ex/eajs.5-250-11/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 49.069 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:29 GMT+01:00 2026
Hostname: n23m0003.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/eajs.5-250-11/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/eajs.5-250-11/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/eajs.5-250-11/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_5 Process_4
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 loc_5 t_5 t_4 loc_4
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:explicit)...

Computing reachable states... 377085 774299 1158636 1408971 1443626 1461663 1471393 1476698 1479811 1481874 1482762 1483733 1484907
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space: failed reallocation of scalar replaced objects
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
out/prism_from-prism_to-umb_ex/eajs.5-250-11/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_eajs.5-250-11_rep4.log

```
Command(s):
../bin/prism -ex models/eajs.5-250-11/model.prism -exportmodel out/prism_from-prism_to-umb_ex/eajs.5-250-11/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 35.931 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:01 GMT+01:00 2026
Hostname: n23m0168.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/eajs.5-250-11/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/eajs.5-250-11/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/eajs.5-250-11/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_5 Process_4
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 loc_5 t_5 t_4 loc_4
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:explicit)...

Computing reachable states... 518005 1033942 1409186 1452240 1470129 1477370 1480983 1482528 1483604 1485097
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at simulator.ChoiceListFlexi.add(ChoiceListFlexi.java:132)
	at simulator.Updater.processUpdatesAndCreateNewChoice(Updater.java:380)
	at simulator.Updater.processUpdatesAndAddToProduct(Updater.java:416)
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
out/prism_from-prism_to-umb_ex/eajs.5-250-11/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_eajs.5-250-11_rep5.log

```
Command(s):
../bin/prism -ex models/eajs.5-250-11/model.prism -exportmodel out/prism_from-prism_to-umb_ex/eajs.5-250-11/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 150.287 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:42:47 GMT+01:00 2026
Hostname: r23m0217.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/eajs.5-250-11/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/eajs.5-250-11/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/eajs.5-250-11/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_5 Process_4
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 loc_5 t_5 t_4 loc_4
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:explicit)...

Computing reachable states... 100576 223565 347507 463688 579460 700823 813831 939157 1046435 1163593 1271976 1338045 1408279 1427345 1438681 1447628 1455242 1461127 1465636 1469290 1472292 1474705 1476165 1477503 1478853 1480184 1481118 1481737 1482174 1482480 1482745 1483150 1483997 1484601 1484896 1485203 1485477
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at simulator.ChoiceListFlexi.add(ChoiceListFlexi.java:133)
	at simulator.Updater.processUpdatesAndCreateNewChoice(Updater.java:380)
	at simulator.Updater.processUpdatesAndAddToProduct(Updater.java:416)
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
out/prism_from-prism_to-umb_ex/eajs.5-250-11/model_rep5.umb:	File does not exist.
```

