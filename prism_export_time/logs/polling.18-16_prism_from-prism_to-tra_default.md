# Log files

Tool configuration: prism_from-prism_to-tra_default
Benchmark: [polling.18-16](../../models/polling.18-16)
Parsed values: [27.419, 33.19, 33.633, 28.572, 31.292]



### Log file: prism_from-prism_to-tra_default_polling.18-16_rep1.log

```
Command(s):
../bin/prism  models/polling.18-16/model.prism -exportmodel out/prism_from-prism_to-tra_default/polling.18-16/model.tra,lab,rew:precision=17
Wallclock time: 27.981 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:28:32 GMT+01:00 2026
Hostname: r23m0140.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/polling.18-16/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/polling.18-16/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 37 iterations in 0.04 seconds (average 0.001081, setup 0.00)

Time for model construction: 0.039 seconds.

Type:        CTMC
States:      7077888 (1 initial)
Transitions: 69599232

Rate matrix: 2745 nodes (4 terminal), 69599232 minterms, vars: 24r/24c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/polling.18-16/model.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/polling.18-16/model.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/polling.18-16/model.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/polling.18-16/model.trew"...
Time for exporting: 27.419 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/polling.18-16/model.tra:	Size of output file is 2481204441 bytes
out/prism_from-prism_to-tra_default/polling.18-16/model.lab:	Size of output file is 2621493 bytes
out/prism_from-prism_to-tra_default/polling.18-16/model.srew:	File does not exist.
out/prism_from-prism_to-tra_default/polling.18-16/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_polling.18-16_rep2.log

```
Command(s):
../bin/prism  models/polling.18-16/model.prism -exportmodel out/prism_from-prism_to-tra_default/polling.18-16/model_rep2.tra,lab,rew:precision=17
Wallclock time: 33.943 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:29 GMT+01:00 2026
Hostname: n23m0006.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/polling.18-16/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/polling.18-16/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 37 iterations in 0.04 seconds (average 0.001081, setup 0.00)

Time for model construction: 0.051 seconds.

Type:        CTMC
States:      7077888 (1 initial)
Transitions: 69599232

Rate matrix: 2745 nodes (4 terminal), 69599232 minterms, vars: 24r/24c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/polling.18-16/model_rep2.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/polling.18-16/model_rep2.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/polling.18-16/model_rep2.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/polling.18-16/model_rep2.trew"...
Time for exporting: 33.19 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/polling.18-16/model_rep2.tra:	Size of output file is 2481204441 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/polling.18-16/model_rep2.lab:	Size of output file is 2621493 bytes
Removing output file to save space for repetition #2
out/prism_from-prism_to-tra_default/polling.18-16/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_default/polling.18-16/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_polling.18-16_rep3.log

```
Command(s):
../bin/prism  models/polling.18-16/model.prism -exportmodel out/prism_from-prism_to-tra_default/polling.18-16/model_rep3.tra,lab,rew:precision=17
Wallclock time: 34.256 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:01 GMT+01:00 2026
Hostname: n23m0410.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/polling.18-16/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/polling.18-16/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 37 iterations in 0.04 seconds (average 0.001081, setup 0.00)

Time for model construction: 0.046 seconds.

Type:        CTMC
States:      7077888 (1 initial)
Transitions: 69599232

Rate matrix: 2745 nodes (4 terminal), 69599232 minterms, vars: 24r/24c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/polling.18-16/model_rep3.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/polling.18-16/model_rep3.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/polling.18-16/model_rep3.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/polling.18-16/model_rep3.trew"...
Time for exporting: 33.633 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/polling.18-16/model_rep3.tra:	Size of output file is 2481204441 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/polling.18-16/model_rep3.lab:	Size of output file is 2621493 bytes
Removing output file to save space for repetition #3
out/prism_from-prism_to-tra_default/polling.18-16/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_default/polling.18-16/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_polling.18-16_rep4.log

```
Command(s):
../bin/prism  models/polling.18-16/model.prism -exportmodel out/prism_from-prism_to-tra_default/polling.18-16/model_rep4.tra,lab,rew:precision=17
Wallclock time: 29.175 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:25:13 GMT+01:00 2026
Hostname: n23m0313.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/polling.18-16/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/polling.18-16/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 37 iterations in 0.04 seconds (average 0.001081, setup 0.00)

Time for model construction: 0.04 seconds.

Type:        CTMC
States:      7077888 (1 initial)
Transitions: 69599232

Rate matrix: 2745 nodes (4 terminal), 69599232 minterms, vars: 24r/24c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/polling.18-16/model_rep4.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/polling.18-16/model_rep4.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/polling.18-16/model_rep4.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/polling.18-16/model_rep4.trew"...
Time for exporting: 28.572 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/polling.18-16/model_rep4.tra:	Size of output file is 2481204441 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/polling.18-16/model_rep4.lab:	Size of output file is 2621493 bytes
Removing output file to save space for repetition #4
out/prism_from-prism_to-tra_default/polling.18-16/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_default/polling.18-16/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_default_polling.18-16_rep5.log

```
Command(s):
../bin/prism  models/polling.18-16/model.prism -exportmodel out/prism_from-prism_to-tra_default/polling.18-16/model_rep5.tra,lab,rew:precision=17
Wallclock time: 31.974 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:29 GMT+01:00 2026
Hostname: r23m0030.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/polling.18-16/model.prism -exportmodel 'out/prism_from-prism_to-tra_default/polling.18-16/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 37 iterations in 0.04 seconds (average 0.001081, setup 0.00)

Time for model construction: 0.046 seconds.

Type:        CTMC
States:      7077888 (1 initial)
Transitions: 69599232

Rate matrix: 2745 nodes (4 terminal), 69599232 minterms, vars: 24r/24c

Exporting model in plain text format to file "out/prism_from-prism_to-tra_default/polling.18-16/model_rep5.tra"...
Exporting labels and satisfying states in plain text format to file "out/prism_from-prism_to-tra_default/polling.18-16/model_rep5.lab"...
Exporting state rewards in plain text format to file "out/prism_from-prism_to-tra_default/polling.18-16/model_rep5.srew"...
Exporting transition rewards in plain text format to file "out/prism_from-prism_to-tra_default/polling.18-16/model_rep5.trew"...
Time for exporting: 31.292 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-tra_default/polling.18-16/model_rep5.tra:	Size of output file is 2481204441 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/polling.18-16/model_rep5.lab:	Size of output file is 2621493 bytes
Removing output file to save space for repetition #5
out/prism_from-prism_to-tra_default/polling.18-16/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_default/polling.18-16/model_rep5.trew:	File does not exist.
```

