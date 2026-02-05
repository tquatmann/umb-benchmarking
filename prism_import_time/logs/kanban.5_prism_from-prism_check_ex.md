# Log files

Tool configuration: prism_from-prism_check_ex
Benchmark: [kanban.5](../../models/kanban.5)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_check_ex_kanban.5_rep1.log

```
Command(s):
../bin/prism -ex models/kanban.5/model.prism models/kanban.5/property.props
Wallclock time: 39.903 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:26:05 GMT+01:00 2026
Hostname: n23m0175.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/kanban.5/model.prism models/kanban.5/property.props

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Parsing properties file "models/kanban.5/property.props"...

1 property:
(1) "throughput": R{"throughput"}=? [ S ]

---------------------------------------------------------------------

Model checking: "throughput": R{"throughput"}=? [ S ]

Building model (engine:explicit)...

Computing reachable states... 449900 809051 1130691 1242433 1269009 1282164 1288135 1291976 1294039 1295388 1296257
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



### Log file: prism_from-prism_check_ex_kanban.5_rep2.log

```
Command(s):
../bin/prism -ex models/kanban.5/model.prism models/kanban.5/property.props
Wallclock time: 49.838 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:21:35 GMT+01:00 2026
Hostname: n23m0242.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/kanban.5/model.prism models/kanban.5/property.props

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Parsing properties file "models/kanban.5/property.props"...

1 property:
(1) "throughput": R{"throughput"}=? [ S ]

---------------------------------------------------------------------

Model checking: "throughput": R{"throughput"}=? [ S ]

Building model (engine:explicit)...

Computing reachable states... 381013 686174 949888 1171842 1247208 1268244 1279737 1285840 1289054 1291829 1293586 1294576 1295406 1296427
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.LinkedList.linkLast(LinkedList.java:154)
	at java.base/java.util.LinkedList.add(LinkedList.java:350)
	at explicit.ConstructModel.constructModel(ConstructModel.java:299)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```



### Log file: prism_from-prism_check_ex_kanban.5_rep3.log

```
Command(s):
../bin/prism -ex models/kanban.5/model.prism models/kanban.5/property.props
Wallclock time: 45.262 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:40 GMT+01:00 2026
Hostname: r23m0135.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/kanban.5/model.prism models/kanban.5/property.props

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Parsing properties file "models/kanban.5/property.props"...

1 property:
(1) "throughput": R{"throughput"}=? [ S ]

---------------------------------------------------------------------

Model checking: "throughput": R{"throughput"}=? [ S ]

Building model (engine:explicit)...

Computing reachable states... 449949 815372 1138450 1240435 1267717 1281041 1286332 1290067 1292396 1293798 1294652 1296011 1296844
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



### Log file: prism_from-prism_check_ex_kanban.5_rep4.log

```
Command(s):
../bin/prism -ex models/kanban.5/model.prism models/kanban.5/property.props
Wallclock time: 50.166 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:16:22 GMT+01:00 2026
Hostname: n23m0166.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/kanban.5/model.prism models/kanban.5/property.props

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Parsing properties file "models/kanban.5/property.props"...

1 property:
(1) "throughput": R{"throughput"}=? [ S ]

---------------------------------------------------------------------

Model checking: "throughput": R{"throughput"}=? [ S ]

Building model (engine:explicit)...

Computing reachable states... 349108 647583 894020 1126274 1233080 1261692 1276306 1284292 1288184 1291179 1293157 1294449 1295263 1296305
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.TreeMap.addEntry(TreeMap.java:801)
	at java.base/java.util.TreeMap.put(TreeMap.java:864)
	at java.base/java.util.TreeMap.put(TreeMap.java:570)
	at explicit.IndexedSet.add(IndexedSet.java:72)
	at explicit.ConstructModel.constructModel(ConstructModel.java:297)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```



### Log file: prism_from-prism_check_ex_kanban.5_rep5.log

```
Command(s):
../bin/prism -ex models/kanban.5/model.prism models/kanban.5/property.props
Wallclock time: 43.103 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:11:16 GMT+01:00 2026
Hostname: n23m0406.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/kanban.5/model.prism models/kanban.5/property.props

Parsing PRISM model file "models/kanban.5/model.prism"...

Type:        CTMC
Modules:     k1 k2 k3 k4
Actions:     [] [in] [s1] [s2]
Variables:   w1 x1 y1 z1 w2 x2 y2 z2 w3 x3 y3 z3 w4 x4 y4 z4
Rewards:     "throughput"

Parsing properties file "models/kanban.5/property.props"...

1 property:
(1) "throughput": R{"throughput"}=? [ S ]

---------------------------------------------------------------------

Model checking: "throughput": R{"throughput"}=? [ S ]

Building model (engine:explicit)...

Computing reachable states... 422916 754050 1057248 1237681 1266483 1280861 1286479 1290215 1292851 1294306 1295127 1296483
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

