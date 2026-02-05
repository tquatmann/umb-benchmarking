# Log files

Tool configuration: prism_from-prism_to-tra_ex
Benchmark: [eajs.6-300-13](../../models/eajs.6-300-13)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_to-tra_ex_eajs.6-300-13_rep1.log

```
Command(s):
../bin/prism -ex models/eajs.6-300-13/model.prism -exportmodel out/prism_from-prism_to-tra_ex/eajs.6-300-13/model.tra,lab,rew:precision=17
Wallclock time: 48.829 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:41:39 GMT+01:00 2026
Hostname: n23m0273.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/eajs.6-300-13/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/eajs.6-300-13/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:explicit)...

Computing reachable states... 384384 771625 1145879 1308383 1334633 1350479 1359146 1363703 1366116 1367977 1369484 1370448 1371297
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
out/prism_from-prism_to-tra_ex/eajs.6-300-13/model.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/eajs.6-300-13/model.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/eajs.6-300-13/model.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/eajs.6-300-13/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_eajs.6-300-13_rep2.log

```
Command(s):
../bin/prism -ex models/eajs.6-300-13/model.prism -exportmodel out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep2.tra,lab,rew:precision=17
Wallclock time: 47.001 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:39:07 GMT+01:00 2026
Hostname: n23m0043.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/eajs.6-300-13/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:explicit)...

Computing reachable states... 364666 729511 1089473 1305081 1334834 1350734 1359219 1363644 1365918 1367805 1369177 1370381 1370989
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at simulator.ChoiceListFlexi.add(ChoiceListFlexi.java:132)
	at simulator.Updater.processUpdatesAndCreateNewChoice(Updater.java:380)
	at simulator.Updater.calculateTransitions(Updater.java:216)
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
out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep2.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep2.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_eajs.6-300-13_rep3.log

```
Command(s):
../bin/prism -ex models/eajs.6-300-13/model.prism -exportmodel out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep3.tra,lab,rew:precision=17
Wallclock time: 45.177 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:27 GMT+01:00 2026
Hostname: n23m0058.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/eajs.6-300-13/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:explicit)...

Computing reachable states... 378275 760560 1136226 1310120 1337671 1352039 1360894 1364898 1367115 1368745 1369959 1370846 1371579
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at simulator.ChoiceListFlexi.<init>(ChoiceListFlexi.java:77)
	at simulator.Updater.processUpdatesAndCreateNewChoice(Updater.java:353)
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
out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep3.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep3.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_eajs.6-300-13_rep4.log

```
Command(s):
../bin/prism -ex models/eajs.6-300-13/model.prism -exportmodel out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep4.tra,lab,rew:precision=17
Wallclock time: 53.453 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:29 GMT+01:00 2026
Hostname: n23m0346.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/eajs.6-300-13/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:explicit)...

Computing reachable states... 346157 693391 1034440 1290682 1324755 1342342 1353596 1360772 1364253 1366021 1367540 1368553 1369759 1371097
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space: failed reallocation of scalar replaced objects
	at simulator.Updater.calculateTransitions(Updater.java:244)
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
out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep4.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep4.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_eajs.6-300-13_rep5.log

```
Command(s):
../bin/prism -ex models/eajs.6-300-13/model.prism -exportmodel out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep5.tra,lab,rew:precision=17
Wallclock time: 41.325 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:34:33 GMT+01:00 2026
Hostname: n23m0247.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/eajs.6-300-13/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/eajs.6-300-13/model.prism"...

Type:        MDP
Modules:     Battery Process_1 Process_2 Resources Process_3 Process_4 Process_6 Process_5
Actions:     [tick]
Variables:   battery_load failure_1 loc_1 t_1 t_2 loc_2 boost_1 user_1 t_3 loc_3 t_4 loc_4 loc_6 t_6 t_5 loc_5
Labels:      "emptyBattery"
Rewards:     "utilityLocal"

Building model (engine:explicit)...

Computing reachable states... 432973 861218 1228316 1327254 1348507 1358134 1363512 1366334 1368060 1369411 1370518 1371378
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at parser.ast.ExpressionFunc.evaluate(ExpressionFunc.java:184)
	at parser.ast.UpdateElement.update(UpdateElement.java:148)
	at parser.ast.Update.update(Update.java:218)
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
out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep5.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep5.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/eajs.6-300-13/model_rep5.trew:	File does not exist.
```

