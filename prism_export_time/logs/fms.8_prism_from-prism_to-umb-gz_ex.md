# Log files

Tool configuration: prism_from-prism_to-umb-gz_ex
Benchmark: [fms.8](../../models/fms.8)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_to-umb-gz_ex_fms.8_rep1.log

```
Command(s):
../bin/prism -ex models/fms.8/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/fms.8/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 45.726 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:46:50 GMT+01:00 2026
Hostname: r23m0157.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/fms.8/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:explicit)...

Computing reachable states... 385126 726559 1041874 1229881 1256016 1275171 1285209 1289984 1292448 1294562 1295373 1296189 1297279
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
out/prism_from-prism_to-umb-gz_ex/fms.8/model.umb.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_fms.8_rep2.log

```
Command(s):
../bin/prism -ex models/fms.8/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/fms.8/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 46.031 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:18:06 GMT+01:00 2026
Hostname: n23m0250.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/fms.8/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:explicit)...

Computing reachable states... 390882 732688 1054465 1230540 1260424 1277469 1285917 1289685 1292060 1293987 1294948 1295646 1296844
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
out/prism_from-prism_to-umb-gz_ex/fms.8/model.umb_rep2.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_fms.8_rep3.log

```
Command(s):
../bin/prism -ex models/fms.8/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/fms.8/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 48.429 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:55:50 GMT+01:00 2026
Hostname: n23m0134.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/fms.8/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:explicit)...

Computing reachable states... 384106 718840 1030709 1231584 1260980 1277912 1286351 1290061 1292401 1294267 1295221 1295828 1296741
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at simulator.ChoiceListFlexi.add(ChoiceListFlexi.java:133)
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
out/prism_from-prism_to-umb-gz_ex/fms.8/model.umb_rep3.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_fms.8_rep4.log

```
Command(s):
../bin/prism -ex models/fms.8/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/fms.8/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 45.747 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:26:26 GMT+01:00 2026
Hostname: n23m0379.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/fms.8/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:explicit)...

Computing reachable states... 387241 733500 1056555 1228314 1259308 1277197 1285895 1289770 1292179 1294201 1295160 1295747 1296980
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at simulator.Updater.processUpdatesAndCreateNewChoice(Updater.java:378)
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
out/prism_from-prism_to-umb-gz_ex/fms.8/model.umb_rep4.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_fms.8_rep5.log

```
Command(s):
../bin/prism -ex models/fms.8/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/fms.8/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 50.304 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:35:33 GMT+01:00 2026
Hostname: n23m0252.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/fms.8/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/fms.8/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/fms.8/model.prism"...

Type:        CTMC
Modules:     machine1 machine2 machine3 machine12
Actions:     [] [t1] [p1p2] [fp12] [t2] [p2p3] [t3] [t12]
Variables:   P1 P1wM1 P1M1 P1d P1s P1wP2 M1 P2 P2wM2 P2M2 P2s P2wP1 M2 P3 P3M2 P3s P12 P12wM3 P12M3 P12s M3
Rewards:     "productivity"

Building model (engine:explicit)...

Computing reachable states... 352791 669489 966276 1195434 1240940 1262408 1278793 1286788 1290078 1292420 1294285 1295127 1295852 1297097
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at simulator.Updater.processUpdatesAndCreateNewChoice(Updater.java:378)
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
out/prism_from-prism_to-umb-gz_ex/fms.8/model.umb_rep5.gz:	File does not exist.
```

