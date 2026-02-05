# Log files

Tool configuration: prism_from-prism_to-umb-gz_norewards
Benchmark: [bluetooth.1](../../models/bluetooth.1)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_to-umb-gz_norewards_bluetooth.1_rep1.log

```
Command(s):
../bin/prism  models/bluetooth.1/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/bluetooth.1/model.umb.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 4.618 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:26:27 GMT+01:00 2026
Hostname: n23m0281.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/bluetooth.1/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/bluetooth.1/model.umb.gz:states=false,obs=false,rewards=false,zip=true'

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

Time for model construction: 3.877 seconds.

Type:        DTMC
States:      3411945339 (536870912 initial)
Transitions: 5035263739

Transition matrix: 14727 nodes (4 terminal), 5035263739 minterms, vars: 52r/52c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/bluetooth.1/model.umb.gz"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 3411945339 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/bluetooth.1/model.umb.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_norewards_bluetooth.1_rep2.log

```
Command(s):
../bin/prism  models/bluetooth.1/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/bluetooth.1/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 4.689 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:38 GMT+01:00 2026
Hostname: n23m0402.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/bluetooth.1/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/bluetooth.1/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/bluetooth.1/model.prism"...

Type:        DTMC
Modules:     receiver1 frequency1 sender_frequency replies
Actions:     [] [time] [reply]
Variables:   y1 receiver freq1 train1 z1 f1 t1 send freq train c rep rec
Labels:      "target"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 50 iterations in 0.12 seconds (average 0.002400, setup 0.00)

Time for model construction: 4.005 seconds.

Type:        DTMC
States:      3411945339 (536870912 initial)
Transitions: 5035263739

Transition matrix: 14727 nodes (4 terminal), 5035263739 minterms, vars: 52r/52c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/bluetooth.1/model.umb_rep2.gz"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 3411945339 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/bluetooth.1/model.umb_rep2.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_norewards_bluetooth.1_rep3.log

```
Command(s):
../bin/prism  models/bluetooth.1/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/bluetooth.1/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 3.864 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:21 GMT+01:00 2026
Hostname: n23m0112.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/bluetooth.1/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/bluetooth.1/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true'

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

Time for model construction: 2.961 seconds.

Type:        DTMC
States:      3411945339 (536870912 initial)
Transitions: 5035263739

Transition matrix: 14727 nodes (4 terminal), 5035263739 minterms, vars: 52r/52c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/bluetooth.1/model.umb_rep3.gz"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 3411945339 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/bluetooth.1/model.umb_rep3.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_norewards_bluetooth.1_rep4.log

```
Command(s):
../bin/prism  models/bluetooth.1/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/bluetooth.1/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 3.987 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:40 GMT+01:00 2026
Hostname: n23m0218.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/bluetooth.1/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/bluetooth.1/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true'

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

Time for model construction: 3.372 seconds.

Type:        DTMC
States:      3411945339 (536870912 initial)
Transitions: 5035263739

Transition matrix: 14727 nodes (4 terminal), 5035263739 minterms, vars: 52r/52c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/bluetooth.1/model.umb_rep4.gz"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 3411945339 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/bluetooth.1/model.umb_rep4.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_norewards_bluetooth.1_rep5.log

```
Command(s):
../bin/prism  models/bluetooth.1/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/bluetooth.1/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 4.860 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:24:54 GMT+01:00 2026
Hostname: r23m0016.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/bluetooth.1/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/bluetooth.1/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true'

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

Time for model construction: 4.259 seconds.

Type:        DTMC
States:      3411945339 (536870912 initial)
Transitions: 5035263739

Transition matrix: 14727 nodes (4 terminal), 5035263739 minterms, vars: 52r/52c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/bluetooth.1/model.umb_rep5.gz"...

Error: Currently, the sparse engine cannot handle models with more than 2147483647 states, have 3411945339 states.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/bluetooth.1/model.umb_rep5.gz:	File does not exist.
```

