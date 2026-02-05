# Log files for prism_from-prism_check_ex on model [bluetooth.1](../../models/bluetooth.1)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_check_ex_bluetooth.1_rep1.log

```
Command(s):
../bin/prism -ex models/bluetooth.1/model.prism models/bluetooth.1/property.props
Wallclock time: 7.717 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 02:22:58 GMT+01:00 2026
Hostname: n23m0244.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/bluetooth.1/model.prism models/bluetooth.1/property.props

Parsing PRISM model file "models/bluetooth.1/model.prism"...

Type:        DTMC
Modules:     receiver1 frequency1 sender_frequency replies
Actions:     [] [time] [reply]
Variables:   y1 receiver freq1 train1 z1 f1 t1 send freq train c rep rec
Labels:      "target"
Rewards:     "time"

Parsing properties file "models/bluetooth.1/property.props"...

1 property:
(1) "time": filter(max, R=? [ F "target" ], "init")

---------------------------------------------------------------------

Model checking: "time": filter(max, R=? [ F "target" ], "init")

Building model (engine:explicit)...

Computing reachable states...
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at parser.State.<init>(State.java:50)
	at parser.State.<init>(State.java:59)
	at parser.VarList.getAllStates(VarList.java:467)
	at simulator.ModulesFileModelGenerator.getInitialStates(ModulesFileModelGenerator.java:492)
	at explicit.ConstructModel.constructModel(ConstructModel.java:255)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```



### Log file: prism_from-prism_check_ex_bluetooth.1_rep2.log

```
Command(s):
../bin/prism -ex models/bluetooth.1/model.prism models/bluetooth.1/property.props
Wallclock time: 7.354 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 03:07:07 GMT+01:00 2026
Hostname: n23m0294.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/bluetooth.1/model.prism models/bluetooth.1/property.props

Parsing PRISM model file "models/bluetooth.1/model.prism"...

Type:        DTMC
Modules:     receiver1 frequency1 sender_frequency replies
Actions:     [] [time] [reply]
Variables:   y1 receiver freq1 train1 z1 f1 t1 send freq train c rep rec
Labels:      "target"
Rewards:     "time"

Parsing properties file "models/bluetooth.1/property.props"...

1 property:
(1) "time": filter(max, R=? [ F "target" ], "init")

---------------------------------------------------------------------

Model checking: "time": filter(max, R=? [ F "target" ], "init")

Building model (engine:explicit)...

Computing reachable states...
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at parser.State.<init>(State.java:50)
	at parser.State.<init>(State.java:59)
	at parser.VarList.getAllStates(VarList.java:467)
	at simulator.ModulesFileModelGenerator.getInitialStates(ModulesFileModelGenerator.java:492)
	at explicit.ConstructModel.constructModel(ConstructModel.java:255)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```



### Log file: prism_from-prism_check_ex_bluetooth.1_rep3.log

```
Command(s):
../bin/prism -ex models/bluetooth.1/model.prism models/bluetooth.1/property.props
Wallclock time: 9.542 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 02:50:14 GMT+01:00 2026
Hostname: r23m0016.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/bluetooth.1/model.prism models/bluetooth.1/property.props

Parsing PRISM model file "models/bluetooth.1/model.prism"...

Type:        DTMC
Modules:     receiver1 frequency1 sender_frequency replies
Actions:     [] [time] [reply]
Variables:   y1 receiver freq1 train1 z1 f1 t1 send freq train c rep rec
Labels:      "target"
Rewards:     "time"

Parsing properties file "models/bluetooth.1/property.props"...

1 property:
(1) "time": filter(max, R=? [ F "target" ], "init")

---------------------------------------------------------------------

Model checking: "time": filter(max, R=? [ F "target" ], "init")

Building model (engine:explicit)...

Computing reachable states...
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at parser.State.<init>(State.java:50)
	at parser.State.<init>(State.java:59)
	at parser.VarList.getAllStates(VarList.java:467)
	at simulator.ModulesFileModelGenerator.getInitialStates(ModulesFileModelGenerator.java:492)
	at explicit.ConstructModel.constructModel(ConstructModel.java:255)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```



### Log file: prism_from-prism_check_ex_bluetooth.1_rep4.log

```
Command(s):
../bin/prism -ex models/bluetooth.1/model.prism models/bluetooth.1/property.props
Wallclock time: 8.589 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 00:51:28 GMT+01:00 2026
Hostname: n23m0335.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/bluetooth.1/model.prism models/bluetooth.1/property.props

Parsing PRISM model file "models/bluetooth.1/model.prism"...

Type:        DTMC
Modules:     receiver1 frequency1 sender_frequency replies
Actions:     [] [time] [reply]
Variables:   y1 receiver freq1 train1 z1 f1 t1 send freq train c rep rec
Labels:      "target"
Rewards:     "time"

Parsing properties file "models/bluetooth.1/property.props"...

1 property:
(1) "time": filter(max, R=? [ F "target" ], "init")

---------------------------------------------------------------------

Model checking: "time": filter(max, R=? [ F "target" ], "init")

Building model (engine:explicit)...

Computing reachable states...
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at parser.State.<init>(State.java:50)
	at parser.State.<init>(State.java:59)
	at parser.VarList.getAllStates(VarList.java:467)
	at simulator.ModulesFileModelGenerator.getInitialStates(ModulesFileModelGenerator.java:492)
	at explicit.ConstructModel.constructModel(ConstructModel.java:255)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```



### Log file: prism_from-prism_check_ex_bluetooth.1_rep5.log

```
Command(s):
../bin/prism -ex models/bluetooth.1/model.prism models/bluetooth.1/property.props
Wallclock time: 7.463 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 20:37:50 GMT+01:00 2026
Hostname: n23m0267.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/bluetooth.1/model.prism models/bluetooth.1/property.props

Parsing PRISM model file "models/bluetooth.1/model.prism"...

Type:        DTMC
Modules:     receiver1 frequency1 sender_frequency replies
Actions:     [] [time] [reply]
Variables:   y1 receiver freq1 train1 z1 f1 t1 send freq train c rep rec
Labels:      "target"
Rewards:     "time"

Parsing properties file "models/bluetooth.1/property.props"...

1 property:
(1) "time": filter(max, R=? [ F "target" ], "init")

---------------------------------------------------------------------

Model checking: "time": filter(max, R=? [ F "target" ], "init")

Building model (engine:explicit)...

Computing reachable states...
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at parser.State.<init>(State.java:50)
	at parser.State.<init>(State.java:59)
	at parser.VarList.getAllStates(VarList.java:467)
	at simulator.ModulesFileModelGenerator.getInitialStates(ModulesFileModelGenerator.java:492)
	at explicit.ConstructModel.constructModel(ConstructModel.java:255)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.modelCheck(Prism.java:3398)
	at prism.PrismCL.run(PrismCL.java:426)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)
```

