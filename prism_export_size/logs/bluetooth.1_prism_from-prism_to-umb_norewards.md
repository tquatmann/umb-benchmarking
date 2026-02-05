# Log files for prism_from-prism_to-umb_norewards on model [bluetooth.1](../../models/bluetooth.1)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_to-umb_norewards_bluetooth.1_rep1.log

```
Command(s):
../bin/prism  models/bluetooth.1/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/bluetooth.1/model.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 5.227 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:39:26 GMT+01:00 2026
Hostname: n23m0385.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/bluetooth.1/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/bluetooth.1/model.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/bluetooth.1/model.prism"...

Type:        DTMC
Modules:     receiver1 frequency1 sender_frequency replies
Actions:     [] [time] [reply]
Variables:   y1 receiver freq1 train1 z1 f1 t1 send freq train c rep rec
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 50 iterations in 0.11 seconds (average 0.002200, setup 0.00)

Time for model construction: 4.562 seconds.

Type:        DTMC
States:      3411945339 (536870912 initial)
Transitions: 5035263739

Transition matrix: 14727 nodes (4 terminal), 5035263739 minterms, vars: 52r/52c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/bluetooth.1/model.umb"...

java.lang.IllegalArgumentException: Illegal Capacity: -1
    at java.base/java.util.ArrayList.<init>(ArrayList.java:161)
    at explicit.DTMCSimple.initialise(DTMCSimple.java:148)
    at explicit.DTMCSimple.<init>(DTMCSimple.java:67)
    at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:92)
    at prism.Prism.doExportBuiltModel(Prism.java:2838)
    at prism.Prism.exportBuiltModelTask(Prism.java:2804)
    at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
    at prism.PrismCL.doExports(PrismCL.java:868)
    at prism.PrismCL.run(PrismCL.java:381)
    at prism.PrismCL.go(PrismCL.java:227)
    at prism.PrismCL.main(PrismCL.java:3040)

Error: Caught unhandled exception, aborting....

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/bluetooth.1/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_bluetooth.1_rep2.log

```
Command(s):
../bin/prism  models/bluetooth.1/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/bluetooth.1/model_rep2.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 3.538 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:52:47 GMT+01:00 2026
Hostname: n23m0307.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/bluetooth.1/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/bluetooth.1/model_rep2.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/bluetooth.1/model.prism"...

Type:        DTMC
Modules:     receiver1 frequency1 sender_frequency replies
Actions:     [] [time] [reply]
Variables:   y1 receiver freq1 train1 z1 f1 t1 send freq train c rep rec
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 50 iterations in 0.09 seconds (average 0.001800, setup 0.00)

Time for model construction: 2.994 seconds.

Type:        DTMC
States:      3411945339 (536870912 initial)
Transitions: 5035263739

Transition matrix: 14727 nodes (4 terminal), 5035263739 minterms, vars: 52r/52c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/bluetooth.1/model_rep2.umb"...

java.lang.IllegalArgumentException: Illegal Capacity: -1
    at java.base/java.util.ArrayList.<init>(ArrayList.java:161)
    at explicit.DTMCSimple.initialise(DTMCSimple.java:148)
    at explicit.DTMCSimple.<init>(DTMCSimple.java:67)
    at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:92)
    at prism.Prism.doExportBuiltModel(Prism.java:2838)
    at prism.Prism.exportBuiltModelTask(Prism.java:2804)
    at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
    at prism.PrismCL.doExports(PrismCL.java:868)
    at prism.PrismCL.run(PrismCL.java:381)
    at prism.PrismCL.go(PrismCL.java:227)
    at prism.PrismCL.main(PrismCL.java:3040)

Error: Caught unhandled exception, aborting....

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/bluetooth.1/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_bluetooth.1_rep3.log

```
Command(s):
../bin/prism  models/bluetooth.1/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/bluetooth.1/model_rep3.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 4.119 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:30:19 GMT+01:00 2026
Hostname: n23m0043.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/bluetooth.1/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/bluetooth.1/model_rep3.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/bluetooth.1/model.prism"...

Type:        DTMC
Modules:     receiver1 frequency1 sender_frequency replies
Actions:     [] [time] [reply]
Variables:   y1 receiver freq1 train1 z1 f1 t1 send freq train c rep rec
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 50 iterations in 0.08 seconds (average 0.001600, setup 0.00)

Time for model construction: 3.117 seconds.

Type:        DTMC
States:      3411945339 (536870912 initial)
Transitions: 5035263739

Transition matrix: 14727 nodes (4 terminal), 5035263739 minterms, vars: 52r/52c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/bluetooth.1/model_rep3.umb"...

java.lang.IllegalArgumentException: Illegal Capacity: -1
    at java.base/java.util.ArrayList.<init>(ArrayList.java:161)
    at explicit.DTMCSimple.initialise(DTMCSimple.java:148)
    at explicit.DTMCSimple.<init>(DTMCSimple.java:67)
    at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:92)
    at prism.Prism.doExportBuiltModel(Prism.java:2838)
    at prism.Prism.exportBuiltModelTask(Prism.java:2804)
    at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
    at prism.PrismCL.doExports(PrismCL.java:868)
    at prism.PrismCL.run(PrismCL.java:381)
    at prism.PrismCL.go(PrismCL.java:227)
    at prism.PrismCL.main(PrismCL.java:3040)

Error: Caught unhandled exception, aborting....

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/bluetooth.1/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_bluetooth.1_rep4.log

```
Command(s):
../bin/prism  models/bluetooth.1/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/bluetooth.1/model_rep4.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 4.633 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:49 GMT+01:00 2026
Hostname: n23m0197.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/bluetooth.1/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/bluetooth.1/model_rep4.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/bluetooth.1/model.prism"...

Type:        DTMC
Modules:     receiver1 frequency1 sender_frequency replies
Actions:     [] [time] [reply]
Variables:   y1 receiver freq1 train1 z1 f1 t1 send freq train c rep rec
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 50 iterations in 0.10 seconds (average 0.002000, setup 0.00)

Time for model construction: 3.529 seconds.

Type:        DTMC
States:      3411945339 (536870912 initial)
Transitions: 5035263739

Transition matrix: 14727 nodes (4 terminal), 5035263739 minterms, vars: 52r/52c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/bluetooth.1/model_rep4.umb"...

java.lang.IllegalArgumentException: Illegal Capacity: -1
    at java.base/java.util.ArrayList.<init>(ArrayList.java:161)
    at explicit.DTMCSimple.initialise(DTMCSimple.java:148)
    at explicit.DTMCSimple.<init>(DTMCSimple.java:67)
    at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:92)
    at prism.Prism.doExportBuiltModel(Prism.java:2838)
    at prism.Prism.exportBuiltModelTask(Prism.java:2804)
    at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
    at prism.PrismCL.doExports(PrismCL.java:868)
    at prism.PrismCL.run(PrismCL.java:381)
    at prism.PrismCL.go(PrismCL.java:227)
    at prism.PrismCL.main(PrismCL.java:3040)

Error: Caught unhandled exception, aborting....

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/bluetooth.1/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_bluetooth.1_rep5.log

```
Command(s):
../bin/prism  models/bluetooth.1/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/bluetooth.1/model_rep5.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 3.792 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:13:00 GMT+01:00 2026
Hostname: n23m0099.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/bluetooth.1/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/bluetooth.1/model_rep5.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/bluetooth.1/model.prism"...

Type:        DTMC
Modules:     receiver1 frequency1 sender_frequency replies
Actions:     [] [time] [reply]
Variables:   y1 receiver freq1 train1 z1 f1 t1 send freq train c rep rec
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 50 iterations in 0.09 seconds (average 0.001800, setup 0.00)

Time for model construction: 3.204 seconds.

Type:        DTMC
States:      3411945339 (536870912 initial)
Transitions: 5035263739

Transition matrix: 14727 nodes (4 terminal), 5035263739 minterms, vars: 52r/52c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/bluetooth.1/model_rep5.umb"...

java.lang.IllegalArgumentException: Illegal Capacity: -1
    at java.base/java.util.ArrayList.<init>(ArrayList.java:161)
    at explicit.DTMCSimple.initialise(DTMCSimple.java:148)
    at explicit.DTMCSimple.<init>(DTMCSimple.java:67)
    at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:92)
    at prism.Prism.doExportBuiltModel(Prism.java:2838)
    at prism.Prism.exportBuiltModelTask(Prism.java:2804)
    at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
    at prism.PrismCL.doExports(PrismCL.java:868)
    at prism.PrismCL.run(PrismCL.java:381)
    at prism.PrismCL.go(PrismCL.java:227)
    at prism.PrismCL.main(PrismCL.java:3040)

Error: Caught unhandled exception, aborting....

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/bluetooth.1/model_rep5.umb:	File does not exist.
```

