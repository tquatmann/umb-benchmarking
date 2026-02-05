# Log files

Tool configuration: prism_from-prism_to-umb_ex
Benchmark: [zeroconf.1000-8-false](../../models/zeroconf.1000-8-false)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_to-umb_ex_zeroconf.1000-8-false_rep1.log

```
Command(s):
../bin/prism -ex models/zeroconf.1000-8-false/model.prism -exportmodel out/prism_from-prism_to-umb_ex/zeroconf.1000-8-false/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 19.931 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:23:16 GMT+01:00 2026
Hostname: n23m0248.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/zeroconf.1000-8-false/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/zeroconf.1000-8-false/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 629946 1204911 1358010 1377130 1380687
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
out/prism_from-prism_to-umb_ex/zeroconf.1000-8-false/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_zeroconf.1000-8-false_rep2.log

```
Command(s):
../bin/prism -ex models/zeroconf.1000-8-false/model.prism -exportmodel out/prism_from-prism_to-umb_ex/zeroconf.1000-8-false/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 26.353 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:31:51 GMT+01:00 2026
Hostname: n23m0166.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/zeroconf.1000-8-false/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/zeroconf.1000-8-false/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 462714 921114 1292892 1366170 1377645 1380797
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
out/prism_from-prism_to-umb_ex/zeroconf.1000-8-false/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_zeroconf.1000-8-false_rep3.log

```
Command(s):
../bin/prism -ex models/zeroconf.1000-8-false/model.prism -exportmodel out/prism_from-prism_to-umb_ex/zeroconf.1000-8-false/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 21.894 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:25:25 GMT+01:00 2026
Hostname: n23m0040.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/zeroconf.1000-8-false/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/zeroconf.1000-8-false/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 617430 1169729 1348054 1375879 1380344 1381868
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
out/prism_from-prism_to-umb_ex/zeroconf.1000-8-false/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_zeroconf.1000-8-false_rep4.log

```
Command(s):
../bin/prism -ex models/zeroconf.1000-8-false/model.prism -exportmodel out/prism_from-prism_to-umb_ex/zeroconf.1000-8-false/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 20.754 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:21 GMT+01:00 2026
Hostname: r23m0072.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/zeroconf.1000-8-false/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/zeroconf.1000-8-false/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 619565 1177222 1355183 1376447 1380351
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
out/prism_from-prism_to-umb_ex/zeroconf.1000-8-false/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_zeroconf.1000-8-false_rep5.log

```
Command(s):
../bin/prism -ex models/zeroconf.1000-8-false/model.prism -exportmodel out/prism_from-prism_to-umb_ex/zeroconf.1000-8-false/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 27.014 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:22:41 GMT+01:00 2026
Hostname: r23m0016.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/zeroconf.1000-8-false/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/zeroconf.1000-8-false/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 460475 857445 1215288 1350819 1374542 1379796 1381351
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at simulator.Updater.calculateTransitions(Updater.java:202)
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
out/prism_from-prism_to-umb_ex/zeroconf.1000-8-false/model_rep5.umb:	File does not exist.
```

