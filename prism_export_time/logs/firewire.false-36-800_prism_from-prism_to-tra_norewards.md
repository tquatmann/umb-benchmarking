# Log files

Tool configuration: prism_from-prism_to-tra_norewards
Benchmark: [firewire.false-36-800](../../models/firewire.false-36-800)
Parsed values: [0.688, 0.706, 0.759, 0.857, 0.832]



### Log file: prism_from-prism_to-tra_norewards_firewire.false-36-800_rep1.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model.tra,lab:precision=17
Wallclock time: 3.205 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:41:01 GMT+01:00 2026
Hostname: r23m0139.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model.tra,lab:precision=17'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 285 iterations in 1.69 seconds (average 0.005930, setup 0.00)

Time for model construction: 1.963 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model.lab"...
Time for exporting: 0.688 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model.tra:	Size of output file is 12179076 bytes
out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model.lab:	Size of output file is 52 bytes
```



### Log file: prism_from-prism_to-tra_norewards_firewire.false-36-800_rep2.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep2.tra,lab:precision=17
Wallclock time: 3.041 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:53:46 GMT+01:00 2026
Hostname: n23m0112.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep2.tra,lab:precision=17'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 285 iterations in 1.52 seconds (average 0.005333, setup 0.00)

Time for model construction: 1.778 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep2.lab"...
Time for exporting: 0.706 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep2.tra:	Size of output file is 12179076 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep2.lab:	Size of output file is 52 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_norewards_firewire.false-36-800_rep3.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep3.tra,lab:precision=17
Wallclock time: 4.924 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:49:46 GMT+01:00 2026
Hostname: r23m0197.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep3.tra,lab:precision=17'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 285 iterations in 2.98 seconds (average 0.010456, setup 0.00)

Time for model construction: 3.423 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep3.lab"...
Time for exporting: 0.759 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep3.tra:	Size of output file is 12179076 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep3.lab:	Size of output file is 52 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_norewards_firewire.false-36-800_rep4.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep4.tra,lab:precision=17
Wallclock time: 5.529 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:27:47 GMT+01:00 2026
Hostname: n23m0096.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep4.tra,lab:precision=17'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 285 iterations in 3.50 seconds (average 0.012281, setup 0.00)

Time for model construction: 3.957 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep4.lab"...
Time for exporting: 0.857 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep4.tra:	Size of output file is 12179076 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep4.lab:	Size of output file is 52 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_norewards_firewire.false-36-800_rep5.log

```
Command(s):
../bin/prism  models/firewire.false-36-800/model.prism -exportmodel out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep5.tra,lab:precision=17
Wallclock time: 4.845 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:41 GMT+01:00 2026
Hostname: n23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/firewire.false-36-800/model.prism -exportmodel 'out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep5.tra,lab:precision=17'

Parsing PRISM model file "models/firewire.false-36-800/model.prism"...

Type:        MDP
Modules:     wire12 node1 wire21 node2
Actions:     [] [snd_req12] [snd_ack12] [snd_idle12] [time] [rec_req12] [rec_ack12] [rec_idle12] [rec_idle21] [rec_req21] [rec_ack21] [snd_req21] [snd_ack21] [snd_idle21]
Variables:   w12 y1 y2 x1 s1 w21 z1 z2 x2 s2
Labels:      "done"
Rewards:     "time"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 285 iterations in 2.91 seconds (average 0.010211, setup 0.00)

Time for model construction: 3.32 seconds.

Type:        MDP
States:      212268 (1 initial)
Transitions: 481792

Transition matrix: 88908 nodes (3 terminal), 481792 minterms, vars: 56r/56c/14nd

Exporting model in plain text format to file "out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep5.lab"...
Time for exporting: 0.832 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep5.tra:	Size of output file is 12179076 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_norewards/firewire.false-36-800/model_rep5.lab:	Size of output file is 52 bytes
Removing output file to save space for repetition #5
```

