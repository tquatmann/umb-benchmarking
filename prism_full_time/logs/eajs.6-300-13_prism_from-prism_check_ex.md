# Log files for prism_from-prism_check_ex on model [eajs.6-300-13](../../models/eajs.6-300-13)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_check_ex_eajs.6-300-13_rep1.log

```
Command(s):
../bin/prism -ex models/eajs.6-300-13/model.prism models/eajs.6-300-13/property.props
Wallclock time: 44.716 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 08:01:05 GMT+01:00 2026
Hostname: r23m0136.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/eajs.6-300-13/model.prism models/eajs.6-300-13/property.props

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Parsing properties file "models/eajs.6-300-13/property.props"...

1 property:
(1) "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

---------------------------------------------------------------------

Model checking: "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

Building model (engine:explicit)...

Computing reachable states... 412793 799511 1183942 1315360 1342721 1356410 1361476 1364726 1366677 1368116 1369286 1370449 1371433
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
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```



### Log file: prism_from-prism_check_ex_eajs.6-300-13_rep2.log

```
Command(s):
../bin/prism -ex models/eajs.6-300-13/model.prism models/eajs.6-300-13/property.props
Wallclock time: 48.668 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:36:54 GMT+01:00 2026
Hostname: n23m0053.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/eajs.6-300-13/model.prism models/eajs.6-300-13/property.props

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Parsing properties file "models/eajs.6-300-13/property.props"...

1 property:
(1) "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

---------------------------------------------------------------------

Model checking: "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

Building model (engine:explicit)...

Computing reachable states... 336962 673732 1017504 1291398 1325844 1345715 1356595 1362142 1365190 1367140 1368563 1369779 1370860 1371601
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.lang.Double.valueOf(Double.java:924)
	at prism.Evaluator$EvaluatorDouble.multiply(Evaluator.java:327)
	at prism.Evaluator$EvaluatorDouble.multiply(Evaluator.java:275)
	at simulator.ChoiceListFlexi.productWith(ChoiceListFlexi.java:170)
	at simulator.Updater.processUpdatesAndAddToProduct(Updater.java:418)
	at simulator.Updater.calculateTransitions(Updater.java:224)
	at simulator.ModulesFileModelGenerator.getTransitionListScalars(ModulesFileModelGenerator.java:827)
	at simulator.ModulesFileModelGenerator.getTransitionList(ModulesFileModelGenerator.java:814)
	at simulator.ModulesFileModelGenerator.getNumChoices(ModulesFileModelGenerator.java:513)
	at explicit.ConstructModel.constructModel(ConstructModel.java:273)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```



### Log file: prism_from-prism_check_ex_eajs.6-300-13_rep3.log

```
Command(s):
../bin/prism -ex models/eajs.6-300-13/model.prism models/eajs.6-300-13/property.props
Wallclock time: 42.866 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:13:24 GMT+01:00 2026
Hostname: n23m0333.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/eajs.6-300-13/model.prism models/eajs.6-300-13/property.props

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Parsing properties file "models/eajs.6-300-13/property.props"...

1 property:
(1) "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

---------------------------------------------------------------------

Model checking: "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

Building model (engine:explicit)...

Computing reachable states... 425049 847241 1235128 1324839 1347352 1358619 1363803 1366478 1368424 1369842 1371023
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
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```



### Log file: prism_from-prism_check_ex_eajs.6-300-13_rep4.log

```
Command(s):
../bin/prism -ex models/eajs.6-300-13/model.prism models/eajs.6-300-13/property.props
Wallclock time: 44.156 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:05 GMT+01:00 2026
Hostname: n23m0153.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/eajs.6-300-13/model.prism models/eajs.6-300-13/property.props

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Parsing properties file "models/eajs.6-300-13/property.props"...

1 property:
(1) "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

---------------------------------------------------------------------

Model checking: "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

Building model (engine:explicit)...

Computing reachable states... 426571 843139 1228808 1324043 1345719 1357830 1362761 1365448 1367425 1369178 1370499 1371487
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at simulator.Updater.processUpdatesAndCreateNewChoice(Updater.java:353)
	at simulator.Updater.calculateTransitions(Updater.java:216)
	at simulator.ModulesFileModelGenerator.getTransitionListScalars(ModulesFileModelGenerator.java:827)
	at simulator.ModulesFileModelGenerator.getTransitionList(ModulesFileModelGenerator.java:814)
	at simulator.ModulesFileModelGenerator.getNumChoices(ModulesFileModelGenerator.java:513)
	at explicit.ConstructModel.constructModel(ConstructModel.java:273)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```



### Log file: prism_from-prism_check_ex_eajs.6-300-13_rep5.log

```
Command(s):
../bin/prism -ex models/eajs.6-300-13/model.prism models/eajs.6-300-13/property.props
Wallclock time: 52.370 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:25 GMT+01:00 2026
Hostname: n23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/eajs.6-300-13/model.prism models/eajs.6-300-13/property.props

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Parsing properties file "models/eajs.6-300-13/property.props"...

1 property:
(1) "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

---------------------------------------------------------------------

Model checking: "ExpUtil": R{"utilityLocal"}max=? [ F "emptyBattery" ]

Building model (engine:explicit)...

Computing reachable states... 338110 687229 1031010 1298433 1328467 1347167 1356867 1361974 1365174 1367115 1368550 1369346 1370367 1371097
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space: failed reallocation of scalar replaced objects
	at java.base/java.util.Arrays.copyOf(Arrays.java:3481)
	at java.base/java.util.ArrayList.grow(ArrayList.java:238)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at simulator.ChoiceListFlexi.productWith(ChoiceListFlexi.java:177)
	at simulator.Updater.processUpdatesAndAddToProduct(Updater.java:418)
	at simulator.Updater.calculateTransitions(Updater.java:224)
	at simulator.ModulesFileModelGenerator.getTransitionListScalars(ModulesFileModelGenerator.java:827)
	at simulator.ModulesFileModelGenerator.getTransitionList(ModulesFileModelGenerator.java:814)
	at simulator.ModulesFileModelGenerator.getNumChoices(ModulesFileModelGenerator.java:513)
	at explicit.ConstructModel.constructModel(ConstructModel.java:273)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```

