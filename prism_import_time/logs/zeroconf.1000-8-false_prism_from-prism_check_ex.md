# Log files for prism_from-prism_check_ex on model [zeroconf.1000-8-false](../../models/zeroconf.1000-8-false)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_check_ex_zeroconf.1000-8-false_rep1.log

```
Command(s):
../bin/prism -ex models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props
Wallclock time: 21.398 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:51:31 GMT+01:00 2026
Hostname: n23m0242.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Parsing properties file "models/zeroconf.1000-8-false/property.props"...

1 property:
(1) "correct_max": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "correct_max": Pmax=? [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 587323 1127037 1358120 1377256 1380792
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at simulator.Updater.calculateTransitions(Updater.java:218)
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



### Log file: prism_from-prism_check_ex_zeroconf.1000-8-false_rep2.log

```
Command(s):
../bin/prism -ex models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props
Wallclock time: 23.570 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:24:08 GMT+01:00 2026
Hostname: n23m0402.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Parsing properties file "models/zeroconf.1000-8-false/property.props"...

1 property:
(1) "correct_max": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "correct_max": Pmax=? [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 522532 1010207 1312729 1365153 1375760 1380626
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
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```



### Log file: prism_from-prism_check_ex_zeroconf.1000-8-false_rep3.log

```
Command(s):
../bin/prism -ex models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props
Wallclock time: 21.191 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:38:20 GMT+01:00 2026
Hostname: n23m0267.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Parsing properties file "models/zeroconf.1000-8-false/property.props"...

1 property:
(1) "correct_max": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "correct_max": Pmax=? [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 586760 1121446 1350973 1376760 1380739
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at simulator.Updater.processUpdatesAndCreateNewChoice(Updater.java:379)
	at simulator.Updater.calculateTransitions(Updater.java:216)
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



### Log file: prism_from-prism_check_ex_zeroconf.1000-8-false_rep4.log

```
Command(s):
../bin/prism -ex models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props
Wallclock time: 23.549 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 21:24:19 GMT+01:00 2026
Hostname: r23m0078.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Parsing properties file "models/zeroconf.1000-8-false/property.props"...

1 property:
(1) "correct_max": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "correct_max": Pmax=? [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 649901 1221190 1360925 1377185 1380724
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at simulator.ChoiceListFlexi.add(ChoiceListFlexi.java:132)
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
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```



### Log file: prism_from-prism_check_ex_zeroconf.1000-8-false_rep5.log

```
Command(s):
../bin/prism -ex models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props
Wallclock time: 24.297 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:15:21 GMT+01:00 2026
Hostname: n23m0402.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/zeroconf.1000-8-false/model.prism models/zeroconf.1000-8-false/property.props

Parsing PRISM model file "models/zeroconf.1000-8-false/model.prism"...

Type:        MDP
Modules:     environment host0
Actions:     [] [reset] [time] [send] [rec]
Variables:   b_ip7 b_ip6 b_ip5 b_ip4 b_ip3 b_ip2 b_ip1 b_ip0 n n0 n1 b z ip_mess x y coll probes mess defend ip l
Labels:      "target"

Parsing properties file "models/zeroconf.1000-8-false/property.props"...

1 property:
(1) "correct_max": Pmax=? [ F "target" ]

---------------------------------------------------------------------

Model checking: "correct_max": Pmax=? [ F "target" ]

Building model (engine:explicit)...

Computing reachable states... 507630 986866 1328830 1372024 1377735 1380879
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at explicit.ConstructModel.constructModel(ConstructModel.java:287)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```

