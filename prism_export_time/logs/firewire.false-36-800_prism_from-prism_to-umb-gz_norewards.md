# Log files for prism_from-prism_to-umb-gz_norewards on model [firewire.false-36-800](../../models/firewire.false-36-800)

Parsed values: `[0.755, 0.75, 0.704, 0.744, 0.774]`



### Log file: prism_from-prism_to-umb-gz_norewards_firewire.false-36-800_rep1.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/firewire.false-36-800/model.umb.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 4.944 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:27:30 GMT+01:00 2026
Hostname: n23m0281.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/firewire.false-36-800/model.umb.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 285 iterations in 3.02 seconds (average 0.010596, setup 0.00)

Time for model construction: 3.459 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/firewire.false-36-800/model.umb.gz"...
Time for exporting: 0.755 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/firewire.false-36-800/model.umb.gz:	Size of output file is 12179076 bytes
```



### Log file: prism_from-prism_to-umb-gz_norewards_firewire.false-36-800_rep2.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/firewire.false-36-800/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 5.586 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:02:54 GMT+01:00 2026
Hostname: n23m0041.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/firewire.false-36-800/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 285 iterations in 3.64 seconds (average 0.012772, setup 0.00)

Time for model construction: 4.141 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/firewire.false-36-800/model.umb_rep2.gz"...
Time for exporting: 0.75 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/firewire.false-36-800/model.umb_rep2.gz:	Size of output file is 12179076 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_norewards_firewire.false-36-800_rep3.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/firewire.false-36-800/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 3.288 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:17 GMT+01:00 2026
Hostname: n23m0388.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/firewire.false-36-800/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true'

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

Time for model construction: 1.805 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/firewire.false-36-800/model.umb_rep3.gz"...
Time for exporting: 0.704 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/firewire.false-36-800/model.umb_rep3.gz:	Size of output file is 12179076 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_norewards_firewire.false-36-800_rep4.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/firewire.false-36-800/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 3.561 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:43:09 GMT+01:00 2026
Hostname: n23m0109.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/firewire.false-36-800/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 285 iterations in 1.86 seconds (average 0.006526, setup 0.00)

Time for model construction: 2.201 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/firewire.false-36-800/model.umb_rep4.gz"...
Time for exporting: 0.744 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/firewire.false-36-800/model.umb_rep4.gz:	Size of output file is 12179076 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_norewards_firewire.false-36-800_rep5.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/firewire.false-36-800/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 4.467 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:26:14 GMT+01:00 2026
Hostname: n23m0058.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/firewire.false-36-800/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 285 iterations in 2.64 seconds (average 0.009263, setup 0.00)

Time for model construction: 3.025 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/firewire.false-36-800/model.umb_rep5.gz"...
Time for exporting: 0.774 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/firewire.false-36-800/model.umb_rep5.gz:	Size of output file is 12179076 bytes
Removing output file to save space for repetition #5
```

