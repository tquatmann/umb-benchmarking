# Log files

Tool configuration: prism_from-prism_check_ex
Benchmark: [consensus.6-2](../../models/consensus.6-2)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_check_ex_consensus.6-2_rep1.log

```
Command(s):
../bin/prism -ex models/consensus.6-2/model.prism models/consensus.6-2/property.props
Wallclock time: 13.846 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:47:53 GMT+01:00 2026
Hostname: n23m0175.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/consensus.6-2/model.prism models/consensus.6-2/property.props

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Parsing properties file "models/consensus.6-2/property.props"...

1 property:
(1) "disagree": Pmax=? [ F "finished"&!"agree" ]

---------------------------------------------------------------------

Model checking: "disagree": Pmax=? [ F "finished"&!"agree" ]

Building model (engine:explicit)...

Computing reachable states... 546990 816967 837870
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.Arrays.copyOf(Arrays.java:3512)
	at java.base/java.util.Arrays.copyOf(Arrays.java:3481)
	at java.base/java.util.ArrayList.grow(ArrayList.java:238)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.ChoiceActionsSimple.setAction(ChoiceActionsSimple.java:133)
	at explicit.MDPSimple.addActionLabelledChoice(MDPSimple.java:331)
	at explicit.ConstructModel.constructModel(ConstructModel.java:353)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```



### Log file: prism_from-prism_check_ex_consensus.6-2_rep2.log

```
Command(s):
../bin/prism -ex models/consensus.6-2/model.prism models/consensus.6-2/property.props
Wallclock time: 17.632 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:29:03 GMT+01:00 2026
Hostname: n23m0350.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/consensus.6-2/model.prism models/consensus.6-2/property.props

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Parsing properties file "models/consensus.6-2/property.props"...

1 property:
(1) "disagree": Pmax=? [ F "finished"&!"agree" ]

---------------------------------------------------------------------

Model checking: "disagree": Pmax=? [ F "finished"&!"agree" ]

Building model (engine:explicit)...

Computing reachable states... 458086 795309 833797 840537
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.Arrays.copyOf(Arrays.java:3512)
	at java.base/java.util.Arrays.copyOf(Arrays.java:3481)
	at java.base/java.util.ArrayList.grow(ArrayList.java:238)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.ChoiceActionsSimple.setAction(ChoiceActionsSimple.java:133)
	at explicit.MDPSimple.addActionLabelledChoice(MDPSimple.java:331)
	at explicit.ConstructModel.constructModel(ConstructModel.java:353)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```



### Log file: prism_from-prism_check_ex_consensus.6-2_rep3.log

```
Command(s):
../bin/prism -ex models/consensus.6-2/model.prism models/consensus.6-2/property.props
Wallclock time: 15.743 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:22:07 GMT+01:00 2026
Hostname: n23m0094.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/consensus.6-2/model.prism models/consensus.6-2/property.props

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Parsing properties file "models/consensus.6-2/property.props"...

1 property:
(1) "disagree": Pmax=? [ F "finished"&!"agree" ]

---------------------------------------------------------------------

Model checking: "disagree": Pmax=? [ F "finished"&!"agree" ]

Building model (engine:explicit)...

Computing reachable states... 583128 825515 839660
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.Arrays.copyOf(Arrays.java:3512)
	at java.base/java.util.Arrays.copyOf(Arrays.java:3481)
	at java.base/java.util.ArrayList.grow(ArrayList.java:238)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.ChoiceActionsSimple.setAction(ChoiceActionsSimple.java:133)
	at explicit.MDPSimple.addActionLabelledChoice(MDPSimple.java:331)
	at explicit.ConstructModel.constructModel(ConstructModel.java:353)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```



### Log file: prism_from-prism_check_ex_consensus.6-2_rep4.log

```
Command(s):
../bin/prism -ex models/consensus.6-2/model.prism models/consensus.6-2/property.props
Wallclock time: 13.049 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 02:59:58 GMT+01:00 2026
Hostname: n23m0323.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/consensus.6-2/model.prism models/consensus.6-2/property.props

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Parsing properties file "models/consensus.6-2/property.props"...

1 property:
(1) "disagree": Pmax=? [ F "finished"&!"agree" ]

---------------------------------------------------------------------

Model checking: "disagree": Pmax=? [ F "finished"&!"agree" ]

Building model (engine:explicit)...

Computing reachable states... 612282 827868 839747
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.Arrays.copyOf(Arrays.java:3512)
	at java.base/java.util.Arrays.copyOf(Arrays.java:3481)
	at java.base/java.util.ArrayList.grow(ArrayList.java:238)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.ChoiceActionsSimple.setAction(ChoiceActionsSimple.java:133)
	at explicit.MDPSimple.addActionLabelledChoice(MDPSimple.java:331)
	at explicit.ConstructModel.constructModel(ConstructModel.java:353)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```



### Log file: prism_from-prism_check_ex_consensus.6-2_rep5.log

```
Command(s):
../bin/prism -ex models/consensus.6-2/model.prism models/consensus.6-2/property.props
Wallclock time: 11.970 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 22:07:15 GMT+01:00 2026
Hostname: r23m0211.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/consensus.6-2/model.prism models/consensus.6-2/property.props

Parsing PRISM model file "models/consensus.6-2/model.prism"...

Type:        MDP
Modules:     process1 process2 process3 process4 process5 process6
Actions:     [] [done]
Variables:   counter pc1 coin1 pc2 coin2 pc3 coin3 pc4 coin4 pc5 coin5 pc6 coin6
Labels:      "finished" "agree"

Parsing properties file "models/consensus.6-2/property.props"...

1 property:
(1) "disagree": Pmax=? [ F "finished"&!"agree" ]

---------------------------------------------------------------------

Model checking: "disagree": Pmax=? [ F "finished"&!"agree" ]

Building model (engine:explicit)...

Computing reachable states... 613861 828331 840176
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.Arrays.copyOf(Arrays.java:3512)
	at java.base/java.util.Arrays.copyOf(Arrays.java:3481)
	at java.base/java.util.ArrayList.grow(ArrayList.java:238)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.ChoiceActionsSimple.setAction(ChoiceActionsSimple.java:133)
	at explicit.MDPSimple.addActionLabelledChoice(MDPSimple.java:331)
	at explicit.ConstructModel.constructModel(ConstructModel.java:353)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```

