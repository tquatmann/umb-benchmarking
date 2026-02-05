# Log files

Tool configuration: prism_from-prism_to-tra_ex
Benchmark: [embedded.8-12](../../models/embedded.8-12)
Parsed values: [1324048.0, 1324048.0, 1324048.0, 1324048.0, 1324048.0]



### Log file: prism_from-prism_to-tra_ex_embedded.8-12_rep1.log

```
Command(s):
../bin/prism -ex models/embedded.8-12/model.prism -exportmodel out/prism_from-prism_to-tra_ex/embedded.8-12/model.tra,lab,rew:precision=17
Wallclock time: 2.480 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Wed Jan 28 07:40:06 GMT+01:00 2026
Hostname: n23m0244.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/embedded.8-12/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/embedded.8-12/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Building model (engine:explicit)...

Computing reachable states... 8548 states
Reachable states exploration and model construction done in 0.126 secs.
Sorting reachable states list...

Time for model construction: 0.328 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/embedded.8-12/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/embedded.8-12/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/embedded.8-12/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/embedded.8-12/model.trew"...
Time for exporting: 0.254 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/embedded.8-12/model.tra:	Size of output file is 1275512 bytes
out/prism_from-prism_to-tra_ex/embedded.8-12/model.lab:	Size of output file is 48536 bytes
out/prism_from-prism_to-tra_ex/embedded.8-12/model.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/embedded.8-12/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_embedded.8-12_rep2.log

```
Command(s):
../bin/prism -ex models/embedded.8-12/model.prism -exportmodel out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep2.tra,lab,rew:precision=17
Wallclock time: 1.370 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:11:30 GMT+01:00 2026
Hostname: r23m0203.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/embedded.8-12/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Building model (engine:explicit)...

Computing reachable states... 8548 states
Reachable states exploration and model construction done in 0.117 secs.
Sorting reachable states list...

Time for model construction: 0.17 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep2.trew"...
Time for exporting: 0.253 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep2.tra:	Size of output file is 1275512 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep2.lab:	Size of output file is 48536 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_embedded.8-12_rep3.log

```
Command(s):
../bin/prism -ex models/embedded.8-12/model.prism -exportmodel out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep3.tra,lab,rew:precision=17
Wallclock time: 1.559 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:16 GMT+01:00 2026
Hostname: n23m0250.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/embedded.8-12/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Building model (engine:explicit)...

Computing reachable states... 8548 states
Reachable states exploration and model construction done in 0.096 secs.
Sorting reachable states list...

Time for model construction: 0.163 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep3.trew"...
Time for exporting: 0.275 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep3.tra:	Size of output file is 1275512 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep3.lab:	Size of output file is 48536 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_embedded.8-12_rep4.log

```
Command(s):
../bin/prism -ex models/embedded.8-12/model.prism -exportmodel out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep4.tra,lab,rew:precision=17
Wallclock time: 3.593 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:49:52 GMT+01:00 2026
Hostname: r23m0217.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/embedded.8-12/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Building model (engine:explicit)...

Computing reachable states... 8548 states
Reachable states exploration and model construction done in 0.402 secs.
Sorting reachable states list...

Time for model construction: 0.526 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep4.trew"...
Time for exporting: 0.855 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep4.tra:	Size of output file is 1275512 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep4.lab:	Size of output file is 48536 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_embedded.8-12_rep5.log

```
Command(s):
../bin/prism -ex models/embedded.8-12/model.prism -exportmodel out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep5.tra,lab,rew:precision=17
Wallclock time: 1.297 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:23:11 GMT+01:00 2026
Hostname: n23m0063.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/embedded.8-12/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/embedded.8-12/model.prism"...

Type:        CTMC
Modules:     sensors proci actuators proco procm bus
Actions:     [] [input_reboot] [output_reboot] [timeout]
Variables:   s i a o m count comp reqi reqo
Labels:      "fail_actuators" "l_down"

Building model (engine:explicit)...

Computing reachable states... 8548 states
Reachable states exploration and model construction done in 0.105 secs.
Sorting reachable states list...

Time for model construction: 0.136 seconds.

Type:        CTMC
States:      8548 (1 initial)
Transitions: 36041

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep5.trew"...
Time for exporting: 0.189 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep5.tra:	Size of output file is 1275512 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep5.lab:	Size of output file is 48536 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/embedded.8-12/model_rep5.trew:	File does not exist.
```

