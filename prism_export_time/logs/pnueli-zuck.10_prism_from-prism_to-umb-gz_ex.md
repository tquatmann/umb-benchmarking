# Log files

Tool configuration: prism_from-prism_to-umb-gz_ex
Benchmark: [pnueli-zuck.10](../../models/pnueli-zuck.10)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_to-umb-gz_ex_pnueli-zuck.10_rep1.log

```
Command(s):
../bin/prism -ex models/pnueli-zuck.10/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.10/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 15.385 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:48:24 GMT+01:00 2026
Hostname: n23m0275.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pnueli-zuck.10/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.10/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 246437 405055 415760 417555
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
out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.10/model.umb.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_pnueli-zuck.10_rep2.log

```
Command(s):
../bin/prism -ex models/pnueli-zuck.10/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.10/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 17.454 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:10 GMT+01:00 2026
Hostname: n23m0073.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pnueli-zuck.10/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.10/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 212462 387118 413446 417228
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at explicit.ConstructModel.constructModel(ConstructModel.java:287)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.10/model.umb_rep2.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_pnueli-zuck.10_rep3.log

```
Command(s):
../bin/prism -ex models/pnueli-zuck.10/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.10/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 20.871 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:55 GMT+01:00 2026
Hostname: n23m0364.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pnueli-zuck.10/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.10/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 177123 361591 407371 415439 417221
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
out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.10/model.umb_rep3.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_pnueli-zuck.10_rep4.log

```
Command(s):
../bin/prism -ex models/pnueli-zuck.10/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.10/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 16.061 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:39:06 GMT+01:00 2026
Hostname: n23m0041.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pnueli-zuck.10/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.10/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 238341 405749 415900 417479
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.HashMap.resize(HashMap.java:711)
	at java.base/java.util.HashMap.merge(HashMap.java:1372)
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
out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.10/model.umb_rep4.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_pnueli-zuck.10_rep5.log

```
Command(s):
../bin/prism -ex models/pnueli-zuck.10/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.10/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 19.150 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:30:00 GMT+01:00 2026
Hostname: n23m0042.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pnueli-zuck.10/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.10/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 207392 387008 413245 416602 417497
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
out/prism_from-prism_to-umb-gz_ex/pnueli-zuck.10/model.umb_rep5.gz:	File does not exist.
```

