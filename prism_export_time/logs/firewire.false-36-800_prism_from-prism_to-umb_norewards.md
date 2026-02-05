# Log files for prism_from-prism_to-umb_norewards on model [firewire.false-36-800](../../models/firewire.false-36-800)

Parsed values: `[3.061, 3.161, 3.139, 2.981, 3.549]`



### Log file: prism_from-prism_to-umb_norewards_firewire.false-36-800_rep1.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/firewire.false-36-800/model.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 5.414 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:27:29 GMT+01:00 2026
Hostname: r23m0131.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/firewire.false-36-800/model.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 285 iterations in 1.54 seconds (average 0.005404, setup 0.00)

Time for model construction: 1.809 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/firewire.false-36-800/model.umb"...
Model export size: 14857 Kb
Time for exporting: 3.061 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/firewire.false-36-800/model.umb:	Size of output file is 15214080 bytes
```



### Log file: prism_from-prism_to-umb_norewards_firewire.false-36-800_rep2.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/firewire.false-36-800/model_rep2.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 5.611 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:43:09 GMT+01:00 2026
Hostname: n23m0113.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/firewire.false-36-800/model_rep2.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 285 iterations in 1.58 seconds (average 0.005544, setup 0.00)

Time for model construction: 1.89 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/firewire.false-36-800/model_rep2.umb"...
Model export size: 14857 Kb
Time for exporting: 3.161 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/firewire.false-36-800/model_rep2.umb:	Size of output file is 15214080 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_norewards_firewire.false-36-800_rep3.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/firewire.false-36-800/model_rep3.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 5.998 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:51 GMT+01:00 2026
Hostname: r23m0080.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/firewire.false-36-800/model_rep3.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 285 iterations in 1.51 seconds (average 0.005298, setup 0.00)

Time for model construction: 1.804 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/firewire.false-36-800/model_rep3.umb"...
Model export size: 14857 Kb
Time for exporting: 3.139 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/firewire.false-36-800/model_rep3.umb:	Size of output file is 15214080 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_norewards_firewire.false-36-800_rep4.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/firewire.false-36-800/model_rep4.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 5.689 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:19 GMT+01:00 2026
Hostname: n23m0138.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/firewire.false-36-800/model_rep4.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 285 iterations in 1.66 seconds (average 0.005825, setup 0.00)

Time for model construction: 1.964 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/firewire.false-36-800/model_rep4.umb"...
Model export size: 14857 Kb
Time for exporting: 2.981 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/firewire.false-36-800/model_rep4.umb:	Size of output file is 15214080 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_norewards_firewire.false-36-800_rep5.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/firewire.false-36-800/model_rep5.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 7.291 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:42:09 GMT+01:00 2026
Hostname: r23m0212.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/firewire.false-36-800/model_rep5.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 285 iterations in 2.67 seconds (average 0.009368, setup 0.00)

Time for model construction: 3.118 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/firewire.false-36-800/model_rep5.umb"...
Model export size: 14857 Kb
Time for exporting: 3.549 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/firewire.false-36-800/model_rep5.umb:	Size of output file is 15214080 bytes
Removing output file to save space for repetition #5
```

