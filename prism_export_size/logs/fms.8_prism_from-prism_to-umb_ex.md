# Log files

Tool configuration: prism_from-prism_to-umb_ex
Benchmark: [fms.8](../../models/fms.8)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_to-umb_ex_fms.8_rep1.log

```
Command(s):
../bin/prism -ex models/fms.8/model.prism -exportmodel out/prism_from-prism_to-umb_ex/fms.8/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 44.836 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:34:37 GMT+01:00 2026
Hostname: n23m0244.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/fms.8/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:explicit)...

Computing reachable states... 392805 736612 1055057 1231703 1261025 1278113 1286397 1290102 1292448 1294309 1295259 1296039 1297279
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.lang.Double.valueOf(Double.java:924)
	at prism.Evaluator$EvaluatorDouble.add(Evaluator.java:315)
	at prism.Evaluator$EvaluatorDouble.add(Evaluator.java:275)
	at simulator.Updater.processUpdatesAndCreateNewChoice(Updater.java:377)
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
out/prism_from-prism_to-umb_ex/fms.8/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_fms.8_rep2.log

```
Command(s):
../bin/prism -ex models/fms.8/model.prism -exportmodel out/prism_from-prism_to-umb_ex/fms.8/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 53.013 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:34:34 GMT+01:00 2026
Hostname: r23m0016.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/fms.8/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:explicit)...

Computing reachable states... 322140 622155 885531 1152238 1238201 1260617 1275714 1284595 1288528 1291540 1293204 1294401 1295126 1295707 1296932
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at explicit.ChoiceActionsSimple.setAction(ChoiceActionsSimple.java:142)
	at explicit.DTMCSimple.addToProbability(DTMCSimple.java:260)
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
out/prism_from-prism_to-umb_ex/fms.8/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_fms.8_rep3.log

```
Command(s):
../bin/prism -ex models/fms.8/model.prism -exportmodel out/prism_from-prism_to-umb_ex/fms.8/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 46.780 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:27 GMT+01:00 2026
Hostname: n23m0389.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/fms.8/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:explicit)...

Computing reachable states... 390308 732995 1051869 1228235 1259133 1277034 1285742 1289638 1291993 1293939 1295009 1295711 1296938
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
out/prism_from-prism_to-umb_ex/fms.8/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_fms.8_rep4.log

```
Command(s):
../bin/prism -ex models/fms.8/model.prism -exportmodel out/prism_from-prism_to-umb_ex/fms.8/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 48.438 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:09 GMT+01:00 2026
Hostname: n23m0012.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/fms.8/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:explicit)...

Computing reachable states... 375958 704402 1012483 1223038 1252841 1273197 1283715 1289032 1291966 1293690 1294880 1295573 1296592 1297518
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at simulator.ChoiceListFlexi.<init>(ChoiceListFlexi.java:78)
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
out/prism_from-prism_to-umb_ex/fms.8/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_fms.8_rep5.log

```
Command(s):
../bin/prism -ex models/fms.8/model.prism -exportmodel out/prism_from-prism_to-umb_ex/fms.8/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 53.067 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:07 GMT+01:00 2026
Hostname: r23m0029.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/fms.8/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:explicit)...

Computing reachable states... 331958 629764 909196 1173537 1243802 1263944 1278197 1286341 1289937 1292104 1293681 1294869 1295563 1296427 1297360
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
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/fms.8/model_rep5.umb:	File does not exist.
```

