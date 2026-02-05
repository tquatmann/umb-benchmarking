# Log files for prism_from-prism_to-tra_ex on model [oscillators.8-10-0.1-1-0.1-1.0](../../models/oscillators.8-10-0.1-1-0.1-1.0)

Parsed values: `[2424732.0, 2424732.0, 2424732.0, 2424732.0, 2424732.0]`



### Log file: prism_from-prism_to-tra_ex_oscillators.8-10-0.1-1-0.1-1.0_rep1.log

```
Command(s):
../bin/prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model.tra,lab,rew:precision=17
Wallclock time: 103.162 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:44:12 GMT+01:00 2026
Hostname: n23m0250.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:explicit)...

Computing reachable states... 620 1335 2048 2770 3493 4216 4942 5669 6398 7126 7857 8583 9320 10070 10799 11523 12264 13007 13751 14498 15244 15993 16744 17500 18252 19003 19763 20523 21285 22047 22811 23579 24311 states
Reachable states exploration and model construction done in 98.941 secs.
Sorting reachable states list...

Time for model construction: 99.772 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model.trew"...
Time for exporting: 0.487 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model.tra:	Size of output file is 2192639 bytes
out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model.lab:	Size of output file is 54 bytes
out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model.srew:	Size of output file is 231975 bytes
out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model.trew:	Size of output file is 64 bytes
```



### Log file: prism_from-prism_to-tra_ex_oscillators.8-10-0.1-1-0.1-1.0_rep2.log

```
Command(s):
../bin/prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.tra,lab,rew:precision=17
Wallclock time: 101.229 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:42:08 GMT+01:00 2026
Hostname: n23m0313.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:explicit)...

Computing reachable states... 668 1424 2178 2941 3703 4465 5230 5997 6737 7478 8245 9017 9793 10571 11351 12133 12901 13683 14439 15194 15968 16733 17494 18285 19080 19878 20678 21481 22265 23033 23587 24090 24311 states
Reachable states exploration and model construction done in 97.412 secs.
Sorting reachable states list...

Time for model construction: 98.189 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.trew"...
Time for exporting: 0.433 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.tra:	Size of output file is 2192639 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.lab:	Size of output file is 54 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.srew:	Size of output file is 231975 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.trew:	Size of output file is 64 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-tra_ex_oscillators.8-10-0.1-1-0.1-1.0_rep3.log

```
Command(s):
../bin/prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.tra,lab,rew:precision=17
Wallclock time: 126.199 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:10 GMT+01:00 2026
Hostname: n23m0079.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:explicit)...

Computing reachable states... 490 1072 1664 2249 2839 3412 4007 4602 5196 5793 6387 6986 7584 8183 8781 9383 9979 10580 11184 11791 12391 12999 13603 14213 14824 15436 16045 16657 17266 17880 18494 19106 19724 20339 20954 21570 22194 22814 23432 24058 24311 states
Reachable states exploration and model construction done in 121.33 secs.
Sorting reachable states list...

Time for model construction: 122.275 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.trew"...
Time for exporting: 0.465 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.tra:	Size of output file is 2192639 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.lab:	Size of output file is 54 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.srew:	Size of output file is 231975 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.trew:	Size of output file is 64 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-tra_ex_oscillators.8-10-0.1-1-0.1-1.0_rep4.log

```
Command(s):
../bin/prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.tra,lab,rew:precision=17
Wallclock time: 154.961 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:26:58 GMT+01:00 2026
Hostname: r23m0198.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:explicit)...

Computing reachable states... 402 847 1363 1864 2365 2835 3280 3732 4200 4715 5231 5714 6155 6624 7170 7694 8200 8677 9108 9607 10124 10631 11091 11514 12039 12548 13057 13481 13931 14454 14960 15459 15875 16319 16769 17289 17810 18318 18773 19214 19758 20282 20801 21308 21770 22289 22818 23339 23824 24278 24311 states
Reachable states exploration and model construction done in 150.403 secs.
Sorting reachable states list...

Time for model construction: 151.363 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.trew"...
Time for exporting: 0.479 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.tra:	Size of output file is 2192639 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.lab:	Size of output file is 54 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.srew:	Size of output file is 231975 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.trew:	Size of output file is 64 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-tra_ex_oscillators.8-10-0.1-1-0.1-1.0_rep5.log

```
Command(s):
../bin/prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.tra,lab,rew:precision=17
Wallclock time: 170.815 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:12 GMT+01:00 2026
Hostname: n23m0227.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/oscillators.8-10-0.1-1-0.1-1.0/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/oscillators.8-10-0.1-1-0.1-1.0/model.prism"...

Type:        DTMC
Modules:     oscillator_population
Actions:     [step]
Variables:   k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9 k_10
Labels:      "target"
Rewards:     "time_to_synch"

Building model (engine:explicit)...

Computing reachable states... 386 831 1275 1719 2164 2606 3053 3499 3943 4390 4837 5282 5730 6178 6623 7064 7511 7957 8404 8854 9301 9750 10198 10635 11076 11519 11959 12401 12841 13277 13720 14155 14589 15025 15461 15898 16335 16772 17208 17645 18082 18520 18957 19395 19831 20267 20704 21140 21579 22018 22465 22908 23347 23786 24225 24311 states
Reachable states exploration and model construction done in 165.822 secs.
Sorting reachable states list...

Time for model construction: 166.815 seconds.

Type:        DTMC
States:      24311 (1 initial)
Transitions: 76623

Exporting model in plain text format to file "out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.trew"...
Time for exporting: 0.622 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.tra:	Size of output file is 2192639 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.lab:	Size of output file is 54 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.srew:	Size of output file is 231975 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_ex/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.trew:	Size of output file is 64 bytes
Removing output file to save space for repetition #5
```

