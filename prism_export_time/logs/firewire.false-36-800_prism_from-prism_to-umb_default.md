# Log files for prism_from-prism_to-umb_default on model [firewire.false-36-800](../../models/firewire.false-36-800)

Parsed values: `[3.582, 3.083, 3.012, 2.947, 3.006]`



### Log file: prism_from-prism_to-umb_default_firewire.false-36-800_rep1.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb_default/firewire.false-36-800/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 7.132 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:39:26 GMT+01:00 2026
Hostname: r23m0005.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/firewire.false-36-800/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 285 iterations in 2.42 seconds (average 0.008491, setup 0.00)

Time for model construction: 2.794 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/firewire.false-36-800/model.umb"...
Model export size: 18598 Kb
Time for exporting: 3.582 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/firewire.false-36-800/model.umb:	Size of output file is 19044864 bytes
```



### Log file: prism_from-prism_to-umb_default_firewire.false-36-800_rep2.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb_default/firewire.false-36-800/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 5.488 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:26:59 GMT+01:00 2026
Hostname: n23m0112.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/firewire.false-36-800/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 285 iterations in 1.60 seconds (average 0.005614, setup 0.00)

Time for model construction: 1.878 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/firewire.false-36-800/model_rep2.umb"...
Model export size: 18598 Kb
Time for exporting: 3.083 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/firewire.false-36-800/model_rep2.umb:	Size of output file is 19044864 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb_default_firewire.false-36-800_rep3.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb_default/firewire.false-36-800/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 5.480 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:53:16 GMT+01:00 2026
Hostname: n23m0307.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/firewire.false-36-800/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 285 iterations in 1.70 seconds (average 0.005965, setup 0.00)

Time for model construction: 1.981 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/firewire.false-36-800/model_rep3.umb"...
Model export size: 18598 Kb
Time for exporting: 3.012 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/firewire.false-36-800/model_rep3.umb:	Size of output file is 19044864 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb_default_firewire.false-36-800_rep4.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb_default/firewire.false-36-800/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 5.226 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:46:11 GMT+01:00 2026
Hostname: n23m0055.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/firewire.false-36-800/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 285 iterations in 1.49 seconds (average 0.005228, setup 0.00)

Time for model construction: 1.744 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/firewire.false-36-800/model_rep4.umb"...
Model export size: 18598 Kb
Time for exporting: 2.947 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/firewire.false-36-800/model_rep4.umb:	Size of output file is 19044864 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb_default_firewire.false-36-800_rep5.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb_default/firewire.false-36-800/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 5.659 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:25 GMT+01:00 2026
Hostname: r23m0197.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb_default/firewire.false-36-800/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

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

Time for model construction: 1.828 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in UMB format to file "out/prism_from-prism_to-umb_default/firewire.false-36-800/model_rep5.umb"...
Model export size: 18598 Kb
Time for exporting: 3.006 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb_default/firewire.false-36-800/model_rep5.umb:	Size of output file is 19044864 bytes
Removing output file to save space for repetition #5
```

