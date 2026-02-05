# Log files for prism_from-prism_check_ex on model [rabin.10](../../models/rabin.10)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_check_ex_rabin.10_rep1.log

```
Command(s):
../bin/prism -ex models/rabin.10/model.prism models/rabin.10/property.props
Wallclock time: 18.066 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:26:04 GMT+01:00 2026
Hostname: r23m0080.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/rabin.10/model.prism models/rabin.10/property.props

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Parsing properties file "models/rabin.10/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 200687 377035 407066 410456 411101
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
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```



### Log file: prism_from-prism_check_ex_rabin.10_rep2.log

```
Command(s):
../bin/prism -ex models/rabin.10/model.prism models/rabin.10/property.props
Wallclock time: 21.932 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:01 GMT+01:00 2026
Hostname: n23m0003.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/rabin.10/model.prism models/rabin.10/property.props

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Parsing properties file "models/rabin.10/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 179584 351733 401047 409279 410818
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at explicit.MDPSimple.addStates(MDPSimple.java:244)
	at explicit.MDPSimple.addState(MDPSimple.java:236)
	at explicit.ConstructModel.constructModel(ConstructModel.java:302)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```



### Log file: prism_from-prism_check_ex_rabin.10_rep3.log

```
Command(s):
../bin/prism -ex models/rabin.10/model.prism models/rabin.10/property.props
Wallclock time: 70.628 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:36:38 GMT+01:00 2026
Hostname: r23m0215.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/rabin.10/model.prism models/rabin.10/property.props

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Parsing properties file "models/rabin.10/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 44506 92299 140450 186478 231667 278461 326623 370074 390410 400245 405728 408315 409509 410410 410792 411048
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
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```



### Log file: prism_from-prism_check_ex_rabin.10_rep4.log

```
Command(s):
../bin/prism -ex models/rabin.10/model.prism models/rabin.10/property.props
Wallclock time: 23.679 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:03 GMT+01:00 2026
Hostname: n23m0350.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/rabin.10/model.prism models/rabin.10/property.props

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Parsing properties file "models/rabin.10/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 162381 317679 400605 408293 410389 411026
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
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```



### Log file: prism_from-prism_check_ex_rabin.10_rep5.log

```
Command(s):
../bin/prism -ex models/rabin.10/model.prism models/rabin.10/property.props
Wallclock time: 18.900 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:19 GMT+01:00 2026
Hostname: n23m0204.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/rabin.10/model.prism models/rabin.10/property.props

Parsing PRISM model file "models/rabin.10/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6 process7 process8 process9 process10
Actions:     []
Variables:   c b r p1 b1 r1 draw1 p2 b2 r2 draw2 p3 b3 r3 draw3 p4 b4 r4 draw4 p5 b5 r5 draw5 p6 b6 r6 draw6 p7 b7 r7 draw7 p8 b8 r8 draw8 p9 b9 r9 draw9 p10 b10 r10 draw10
Labels:      "target"

Parsing properties file "models/rabin.10/property.props"...

1 property:
(1) "live": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "live": Pmax=? [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 196110 377990 408606 410678
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at parser.State.<init>(State.java:50)
	at parser.State.<init>(State.java:59)
	at simulator.ChoiceListFlexi.computeTarget(ChoiceListFlexi.java:257)
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

