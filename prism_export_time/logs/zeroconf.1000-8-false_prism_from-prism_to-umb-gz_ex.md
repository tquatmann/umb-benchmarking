# Log files for prism_from-prism_to-umb-gz_ex on model [zeroconf.1000-8-false](../../models/zeroconf.1000-8-false)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_to-umb-gz_ex_zeroconf.1000-8-false_rep1.log

```
Command(s):
../bin/prism -ex models/zeroconf.1000-8-false/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/zeroconf.1000-8-false/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 19.911 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:46:18 GMT+01:00 2026
Hostname: r23m0157.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/zeroconf.1000-8-false/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/zeroconf.1000-8-false/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 586615 1125073 1358048 1377189 1381107
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at explicit.MDPSimple.addStates(MDPSimple.java:244)
	at explicit.MDPSimple.addState(MDPSimple.java:236)
	at explicit.ConstructModel.constructModel(ConstructModel.java:302)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/zeroconf.1000-8-false/model.umb.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_zeroconf.1000-8-false_rep2.log

```
Command(s):
../bin/prism -ex models/zeroconf.1000-8-false/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/zeroconf.1000-8-false/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 20.889 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:55 GMT+01:00 2026
Hostname: n23m0171.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/zeroconf.1000-8-false/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/zeroconf.1000-8-false/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 626664 1177607 1353446 1374774 1380388
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.MDPSimple.addActionLabelledChoice(MDPSimple.java:329)
	at explicit.ConstructModel.constructModel(ConstructModel.java:353)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/zeroconf.1000-8-false/model.umb_rep2.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_zeroconf.1000-8-false_rep3.log

```
Command(s):
../bin/prism -ex models/zeroconf.1000-8-false/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/zeroconf.1000-8-false/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 27.131 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:01 GMT+01:00 2026
Hostname: n23m0113.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/zeroconf.1000-8-false/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/zeroconf.1000-8-false/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 455817 873873 1284730 1353000 1375122 1379995 1381551
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
out/prism_from-prism_to-umb-gz_ex/zeroconf.1000-8-false/model.umb_rep3.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_zeroconf.1000-8-false_rep4.log

```
Command(s):
../bin/prism -ex models/zeroconf.1000-8-false/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/zeroconf.1000-8-false/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 21.807 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:11 GMT+01:00 2026
Hostname: n23m0085.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/zeroconf.1000-8-false/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/zeroconf.1000-8-false/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 549588 1081257 1336586 1372988 1379848 1381803
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
out/prism_from-prism_to-umb-gz_ex/zeroconf.1000-8-false/model.umb_rep4.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_zeroconf.1000-8-false_rep5.log

```
Command(s):
../bin/prism -ex models/zeroconf.1000-8-false/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/zeroconf.1000-8-false/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 23.382 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:10 GMT+01:00 2026
Hostname: n23m0031.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/zeroconf.1000-8-false/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/zeroconf.1000-8-false/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Building model (engine:explicit)...

Computing reachable states... 525967 1015452 1309184 1369158 1378206 1380941
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
out/prism_from-prism_to-umb-gz_ex/zeroconf.1000-8-false/model.umb_rep5.gz:	File does not exist.
```

