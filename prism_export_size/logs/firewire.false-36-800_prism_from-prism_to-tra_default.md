# Log files for prism_from-prism_to-tra_default on model [firewire.false-36-800](../../models/firewire.false-36-800)

Parsed values: `[15698447.0, 15698447.0, 15698447.0, 15698447.0, 15698447.0]`



### Log file: prism_from-prism_to-tra_default_firewire.false-36-800_rep1.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-tra_default/firewire.false-36-800/model.tra,lab,rew:precision=17
Wallclock time: 3.229 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:31:27 GMT+01:00 2026
Hostname: n23m0244.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/firewire.false-36-800/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 285 iterations in 1.48 seconds (average 0.005193, setup 0.00)

Time for model construction: 1.731 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/firewire.false-36-800/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/firewire.false-36-800/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/firewire.false-36-800/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/firewire.false-36-800/model.trew"...
Time for exporting: 0.95 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/firewire.false-36-800/model.tra:	Size of output file is 12179076 bytes
out/prism_from-prism_to-tra_default/firewire.false-36-800/model.lab:	Size of output file is 52 bytes
out/prism_from-prism_to-tra_default/firewire.false-36-800/model.srew:	Size of output file is 51 bytes
out/prism_from-prism_to-tra_default/firewire.false-36-800/model.trew:	Size of output file is 3519268 bytes
```



### Log file: prism_from-prism_to-tra_default_firewire.false-36-800_rep2.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep2.tra,lab,rew:precision=17
Wallclock time: 3.188 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:36:35 GMT+01:00 2026
Hostname: n23m0380.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 285 iterations in 1.46 seconds (average 0.005123, setup 0.00)

Time for model construction: 1.71 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep2.trew"...
Time for exporting: 0.947 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep2.tra:	Size of output file is 12179076 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep2.lab:	Size of output file is 52 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep2.srew:	Size of output file is 51 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep2.trew:	Size of output file is 3519268 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_default_firewire.false-36-800_rep3.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep3.tra,lab,rew:precision=17
Wallclock time: 3.434 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:48:44 GMT+01:00 2026
Hostname: n23m0388.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 285 iterations in 1.53 seconds (average 0.005368, setup 0.00)

Time for model construction: 1.786 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep3.trew"...
Time for exporting: 1.001 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep3.tra:	Size of output file is 12179076 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep3.lab:	Size of output file is 52 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep3.srew:	Size of output file is 51 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep3.trew:	Size of output file is 3519268 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_default_firewire.false-36-800_rep4.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep4.tra,lab,rew:precision=17
Wallclock time: 6.513 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:46:42 GMT+01:00 2026
Hostname: n23m0402.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 285 iterations in 3.99 seconds (average 0.014000, setup 0.00)

Time for model construction: 4.524 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep4.trew"...
Time for exporting: 1.247 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep4.tra:	Size of output file is 12179076 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep4.lab:	Size of output file is 52 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep4.srew:	Size of output file is 51 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep4.trew:	Size of output file is 3519268 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_default_firewire.false-36-800_rep5.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep5.tra,lab,rew:precision=17
Wallclock time: 3.806 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:26 GMT+01:00 2026
Hostname: n23m0244.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 285 iterations in 1.95 seconds (average 0.006842, setup 0.00)

Time for model construction: 2.244 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep5.trew"...
Time for exporting: 1.001 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep5.tra:	Size of output file is 12179076 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep5.lab:	Size of output file is 52 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep5.srew:	Size of output file is 51 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/firewire.false-36-800/model_rep5.trew:	Size of output file is 3519268 bytes
Removing output file to save space for repetition #5
```

