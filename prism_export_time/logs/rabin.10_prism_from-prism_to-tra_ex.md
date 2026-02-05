# Log files

Tool configuration: prism_from-prism_to-tra_ex
Benchmark: [rabin.10](../../models/rabin.10)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_to-tra_ex_rabin.10_rep1.log

```
Command(s):
../bin/prism -ex models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-tra_ex/rabin.10/model.tra,lab,rew:precision=17
Wallclock time: 22.342 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:23:17 GMT+01:00 2026
Hostname: n23m0113.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/rabin.10/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 161480 320016 401012 409245 410660 411173
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
out/prism_from-prism_to-tra_ex/rabin.10/model.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/rabin.10/model.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/rabin.10/model.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/rabin.10/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_rabin.10_rep2.log

```
Command(s):
../bin/prism -ex models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-tra_ex/rabin.10/model_rep2.tra,lab,rew:precision=17
Wallclock time: 20.083 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:55 GMT+01:00 2026
Hostname: n23m0003.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/rabin.10/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 174590 346824 403977 409852 411005
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
out/prism_from-prism_to-tra_ex/rabin.10/model_rep2.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/rabin.10/model_rep2.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/rabin.10/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/rabin.10/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_rabin.10_rep3.log

```
Command(s):
../bin/prism -ex models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-tra_ex/rabin.10/model_rep3.tra,lab,rew:precision=17
Wallclock time: 23.077 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:57 GMT+01:00 2026
Hostname: r23m0177.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/rabin.10/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 152386 306586 392622 408115 410595 411112
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.lang.invoke.DirectMethodHandle.allocateInstance(DirectMethodHandle.java:500)
	at java.base/java.lang.invoke.DirectMethodHandle$Holder.newInvokeSpecial(DirectMethodHandle$Holder)
	at java.base/java.lang.invoke.Invokers$Holder.linkToTargetMethod(Invokers$Holder)
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
out/prism_from-prism_to-tra_ex/rabin.10/model_rep3.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/rabin.10/model_rep3.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/rabin.10/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/rabin.10/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_rabin.10_rep4.log

```
Command(s):
../bin/prism -ex models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-tra_ex/rabin.10/model_rep4.tra,lab,rew:precision=17
Wallclock time: 17.558 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:26:14 GMT+01:00 2026
Hostname: n23m0249.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/rabin.10/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 191164 375680 406288 410452
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
out/prism_from-prism_to-tra_ex/rabin.10/model_rep4.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/rabin.10/model_rep4.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/rabin.10/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/rabin.10/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_rabin.10_rep5.log

```
Command(s):
../bin/prism -ex models/rabin.10/model.prism -exportmodel out/prism_from-prism_to-tra_ex/rabin.10/model_rep5.tra,lab,rew:precision=17
Wallclock time: 20.224 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:02 GMT+01:00 2026
Hostname: r23m0052.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/rabin.10/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/rabin.10/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 175131 346500 403646 409912 411067
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.lang.invoke.DirectMethodHandle.allocateInstance(DirectMethodHandle.java:500)
	at java.base/java.lang.invoke.DirectMethodHandle$Holder.newInvokeSpecial(DirectMethodHandle$Holder)
	at java.base/java.lang.invoke.Invokers$Holder.linkToTargetMethod(Invokers$Holder)
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
out/prism_from-prism_to-tra_ex/rabin.10/model_rep5.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/rabin.10/model_rep5.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/rabin.10/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/rabin.10/model_rep5.trew:	File does not exist.
```

