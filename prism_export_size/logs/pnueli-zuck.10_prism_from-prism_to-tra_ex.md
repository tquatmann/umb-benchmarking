# Log files

Tool configuration: prism_from-prism_to-tra_ex
Benchmark: [pnueli-zuck.10](../../models/pnueli-zuck.10)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_to-tra_ex_pnueli-zuck.10_rep1.log

```
Command(s):
../bin/prism -ex models/pnueli-zuck.10/model.prism -exportmodel out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model.tra,lab,rew:precision=17
Wallclock time: 16.331 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:23:16 GMT+01:00 2026
Hostname: r23m0134.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pnueli-zuck.10/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 246607 405722 415793 417364
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
out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_pnueli-zuck.10_rep2.log

```
Command(s):
../bin/prism -ex models/pnueli-zuck.10/model.prism -exportmodel out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep2.tra,lab,rew:precision=17
Wallclock time: 21.177 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:40:07 GMT+01:00 2026
Hostname: n23m0252.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pnueli-zuck.10/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 219162 398449 415165 417069 417413
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
out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep2.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep2.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_pnueli-zuck.10_rep3.log

```
Command(s):
../bin/prism -ex models/pnueli-zuck.10/model.prism -exportmodel out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep3.tra,lab,rew:precision=17
Wallclock time: 16.461 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:28:46 GMT+01:00 2026
Hostname: r23m0204.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pnueli-zuck.10/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 238647 404363 415999 417463
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
out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep3.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep3.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_pnueli-zuck.10_rep4.log

```
Command(s):
../bin/prism -ex models/pnueli-zuck.10/model.prism -exportmodel out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep4.tra,lab,rew:precision=17
Wallclock time: 21.146 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:41:39 GMT+01:00 2026
Hostname: n23m0396.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pnueli-zuck.10/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 198412 387008 413283 416637 417417
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at explicit.Distribution.<init>(Distribution.java:75)
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
out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep4.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep4.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_pnueli-zuck.10_rep5.log

```
Command(s):
../bin/prism -ex models/pnueli-zuck.10/model.prism -exportmodel out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep5.tra,lab,rew:precision=17
Wallclock time: 17.034 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:21 GMT+01:00 2026
Hostname: n23m0133.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/pnueli-zuck.10/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/pnueli-zuck.10/model.prism"...

Type:        MDP
Modules:     process0 process1 process2 process3 process4 process5 process6 process7 process8 process9
Actions:     []
Variables:   p0 p1 p2 p3 p4 p5 p6 p7 p8 p9
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 232741 400391 415679 417348
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.HashMap.newNode(HashMap.java:1910)
	at java.base/java.util.HashMap.merge(HashMap.java:1410)
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
out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep5.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep5.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/pnueli-zuck.10/model_rep5.trew:	File does not exist.
```

