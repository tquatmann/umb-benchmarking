# Log files for prism_from-prism_to-umb-gz_norewards on model [polling.18-16](../../models/polling.18-16)

Parsed values: `[2418683097.0, 2418683097.0, 2418683097.0, 2418683097.0, 2418683097.0]`



### Log file: prism_from-prism_to-umb-gz_norewards_polling.18-16_rep1.log

```
Command(s):
../bin/prism  models/polling.18-16/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/polling.18-16/model.umb.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 28.148 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:22:13 GMT+01:00 2026
Hostname: n23m0128.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/polling.18-16/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/polling.18-16/model.umb.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 37 iterations in 0.04 seconds (average 0.001081, setup 0.00)

Time for model construction: 0.041 seconds.

Type:        CTMC
States:      7077888 (1 initial)
Transitions: 69599232

Rate matrix: 2745 nodes (4 terminal), 69599232 minterms, vars: 24r/24c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/polling.18-16/model.umb.gz"...
Time for exporting: 27.585 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/polling.18-16/model.umb.gz:	Size of output file is 2418683097 bytes
```



### Log file: prism_from-prism_to-umb-gz_norewards_polling.18-16_rep2.log

```
Command(s):
../bin/prism  models/polling.18-16/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/polling.18-16/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 33.795 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:29 GMT+01:00 2026
Hostname: n23m0220.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/polling.18-16/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/polling.18-16/model.umb_rep2.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 37 iterations in 0.03 seconds (average 0.000811, setup 0.00)

Time for model construction: 0.044 seconds.

Type:        CTMC
States:      7077888 (1 initial)
Transitions: 69599232

Rate matrix: 2745 nodes (4 terminal), 69599232 minterms, vars: 24r/24c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/polling.18-16/model.umb_rep2.gz"...
Time for exporting: 33.086 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/polling.18-16/model.umb_rep2.gz:	Size of output file is 2418683097 bytes
Removing output file to save space for repetition #2
```



### Log file: prism_from-prism_to-umb-gz_norewards_polling.18-16_rep3.log

```
Command(s):
../bin/prism  models/polling.18-16/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/polling.18-16/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 32.338 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:54:19 GMT+01:00 2026
Hostname: r23m0195.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/polling.18-16/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/polling.18-16/model.umb_rep3.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 37 iterations in 0.03 seconds (average 0.000811, setup 0.00)

Time for model construction: 0.054 seconds.

Type:        CTMC
States:      7077888 (1 initial)
Transitions: 69599232

Rate matrix: 2745 nodes (4 terminal), 69599232 minterms, vars: 24r/24c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/polling.18-16/model.umb_rep3.gz"...
Time for exporting: 31.612 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/polling.18-16/model.umb_rep3.gz:	Size of output file is 2418683097 bytes
Removing output file to save space for repetition #3
```



### Log file: prism_from-prism_to-umb-gz_norewards_polling.18-16_rep4.log

```
Command(s):
../bin/prism  models/polling.18-16/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/polling.18-16/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 29.841 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:37:12 GMT+01:00 2026
Hostname: n23m0157.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/polling.18-16/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/polling.18-16/model.umb_rep4.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 37 iterations in 0.06 seconds (average 0.001622, setup 0.00)

Time for model construction: 0.06 seconds.

Type:        CTMC
States:      7077888 (1 initial)
Transitions: 69599232

Rate matrix: 2745 nodes (4 terminal), 69599232 minterms, vars: 24r/24c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/polling.18-16/model.umb_rep4.gz"...
Time for exporting: 29.194 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/polling.18-16/model.umb_rep4.gz:	Size of output file is 2418683097 bytes
Removing output file to save space for repetition #4
```



### Log file: prism_from-prism_to-umb-gz_norewards_polling.18-16_rep5.log

```
Command(s):
../bin/prism  models/polling.18-16/model.prism -exportmodel out/prism_from-prism_to-umb-gz_norewards/polling.18-16/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true
Wallclock time: 34.373 seconds
Return code: 0
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:10 GMT+01:00 2026
Hostname: n23m0232.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/polling.18-16/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_norewards/polling.18-16/model.umb_rep5.gz:states=false,obs=false,rewards=false,zip=true'

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Building model (engine:symbolic)...

Computing reachable states...

Reachability (BFS): 37 iterations in 0.03 seconds (average 0.000811, setup 0.00)

Time for model construction: 0.072 seconds.

Type:        CTMC
States:      7077888 (1 initial)
Transitions: 69599232

Rate matrix: 2745 nodes (4 terminal), 69599232 minterms, vars: 24r/24c

Exporting model in plain text format to file "out/prism_from-prism_to-umb-gz_norewards/polling.18-16/model.umb_rep5.gz"...
Time for exporting: 33.251 seconds.


##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_norewards/polling.18-16/model.umb_rep5.gz:	Size of output file is 2418683097 bytes
Removing output file to save space for repetition #5
```

