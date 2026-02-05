# Log files for prism_from-prism_to-umb-gz_ex on model [pacman.60](../../models/pacman.60)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_to-umb-gz_ex_pacman.60_rep1.log

```
Command(s):
../bin/prism -ex models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/pacman.60/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 50.638 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:29:04 GMT+01:00 2026
Hostname: r23m0129.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/pacman.60/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:explicit)...

Computing reachable states... 139421 283660 427872 573304 713006 857028 994283 1140647 1282999 1418880 1560667 1653566 1710135 1721710 1726423
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at simulator.Updater.processUpdatesAndCreateNewChoice(Updater.java:378)
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
out/prism_from-prism_to-umb-gz_ex/pacman.60/model.umb.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_pacman.60_rep2.log

```
Command(s):
../bin/prism -ex models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/pacman.60/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 46.752 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:38 GMT+01:00 2026
Hostname: r23m0044.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/pacman.60/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:explicit)...

Computing reachable states... 158206 321171 479289 637100 799879 956459 1114157 1267329 1417316 1572385 1668242 1708027 1722042 1726696
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.lang.Integer.valueOf(Integer.java:1019)
	at explicit.IndexedSet.add(IndexedSet.java:72)
	at explicit.ConstructModel.constructModel(ConstructModel.java:297)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/pacman.60/model.umb_rep2.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_pacman.60_rep3.log

```
Command(s):
../bin/prism -ex models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/pacman.60/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 52.202 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:09:59 GMT+01:00 2026
Hostname: r23m0195.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/pacman.60/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:explicit)...

Computing reachable states... 141519 284375 426428 570466 708103 850348 987531 1130473 1269010 1401878 1541364 1648962 1704567 1721199 1725945
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
out/prism_from-prism_to-umb-gz_ex/pacman.60/model.umb_rep3.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_pacman.60_rep4.log

```
Command(s):
../bin/prism -ex models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/pacman.60/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 53.806 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:31:51 GMT+01:00 2026
Hostname: n23m0166.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/pacman.60/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:explicit)...

Computing reachable states... 141569 286653 424353 567129 699333 835966 965591 1103673 1242283 1380987 1524260 1635653 1690321 1715983 1724131 1726423
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at simulator.Updater.processUpdatesAndCreateNewChoice(Updater.java:378)
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
out/prism_from-prism_to-umb-gz_ex/pacman.60/model.umb_rep4.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_pacman.60_rep5.log

```
Command(s):
../bin/prism -ex models/pacman.60/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/pacman.60/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 51.286 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:55:49 GMT+01:00 2026
Hostname: n23m0043.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pacman.60/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/pacman.60/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pacman.60/model.prism"...

Type:        MDP
Modules:     arbiter ghost0 ghost1 pacman
Actions:     [] [g0] [stop0] [g1] [stop1] [p] [left] [right] [up] [down]
Variables:   pMove steps xG0 yG0 dG0 xG1 yG1 dG1 xP yP dP
Labels:      "Crash"

Building model (engine:explicit)...

Computing reachable states... 143484 289448 434881 580491 720345 865197 1002854 1150736 1292878 1427432 1569513 1655144 1710101 1722897 1725838
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at simulator.ChoiceListFlexi.<init>(ChoiceListFlexi.java:78)
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
out/prism_from-prism_to-umb-gz_ex/pacman.60/model.umb_rep5.gz:	File does not exist.
```

