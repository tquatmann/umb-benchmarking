# Log files for prism_from-prism_to-umb_norewards on model [egl.10-2](../../models/egl.10-2)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_to-umb_norewards_egl.10-2_rep1.log

```
Command(s):
../bin/prism  models/egl.10-2/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/egl.10-2/model.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 3.233 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:32:31 GMT+01:00 2026
Hostname: n23m0110.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/egl.10-2/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/egl.10-2/model.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/egl.10-2/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Building model (engine:symbolic)...

Warning: Guard for command 11 of module "partyA" is never satisfied.

Warning: Guard for command 12 of module "partyA" is never satisfied.

Warning: Guard for command 13 of module "partyA" is never satisfied.

Warning: Guard for command 14 of module "partyA" is never satisfied.

Warning: Guard for command 15 of module "partyA" is never satisfied.

Warning: Guard for command 16 of module "partyA" is never satisfied.

Warning: Guard for command 17 of module "partyA" is never satisfied.

Warning: Guard for command 18 of module "partyA" is never satisfied.

Warning: Guard for command 19 of module "partyA" is never satisfied.

Warning: Guard for command 20 of module "partyA" is never satisfied.

Warning: Guard for command 31 of module "partyA" is never satisfied.

Warning: Guard for command 32 of module "partyA" is never satisfied.

Warning: Guard for command 33 of module "partyA" is never satisfied.

Warning: Guard for command 34 of module "partyA" is never satisfied.

Warning: Guard for command 35 of module "partyA" is never satisfied.

Warning: Guard for command 36 of module "partyA" is never satisfied.

Warning: Guard for command 37 of module "partyA" is never satisfied.

Warning: Guard for command 38 of module "partyA" is never satisfied.

Warning: Guard for command 39 of module "partyA" is never satisfied.

Warning: Guard for command 40 of module "partyA" is never satisfied.

Warning: Guard for command 51 of module "partyA" is never satisfied.

Warning: Guard for command 52 of module "partyA" is never satisfied.

Warning: Guard for command 53 of module "partyA" is never satisfied.

Warning: Guard for command 54 of module "partyA" is never satisfied.

Warning: Guard for command 55 of module "partyA" is never satisfied.

Warning: Guard for command 56 of module "partyA" is never satisfied.

Warning: Guard for command 57 of module "partyA" is never satisfied.

Warning: Guard for command 58 of module "partyA" is never satisfied.

Warning: Guard for command 59 of module "partyA" is never satisfied.

Warning: Guard for command 60 of module "partyA" is never satisfied.

Warning: Guard for command 11 of module "partyB" is never satisfied.

Warning: Guard for command 12 of module "partyB" is never satisfied.

Warning: Guard for command 13 of module "partyB" is never satisfied.

Warning: Guard for command 14 of module "partyB" is never satisfied.

Warning: Guard for command 15 of module "partyB" is never satisfied.

Warning: Guard for command 16 of module "partyB" is never satisfied.

Warning: Guard for command 17 of module "partyB" is never satisfied.

Warning: Guard for command 18 of module "partyB" is never satisfied.

Warning: Guard for command 19 of module "partyB" is never satisfied.

Warning: Guard for command 20 of module "partyB" is never satisfied.

Warning: Guard for command 31 of module "partyB" is never satisfied.

Warning: Guard for command 32 of module "partyB" is never satisfied.

Warning: Guard for command 33 of module "partyB" is never satisfied.

Warning: Guard for command 34 of module "partyB" is never satisfied.

Warning: Guard for command 35 of module "partyB" is never satisfied.

Warning: Guard for command 36 of module "partyB" is never satisfied.

Warning: Guard for command 37 of module "partyB" is never satisfied.

Warning: Guard for command 38 of module "partyB" is never satisfied.

Warning: Guard for command 39 of module "partyB" is never satisfied.

Warning: Guard for command 40 of module "partyB" is never satisfied.

Warning: Guard for command 51 of module "partyB" is never satisfied.

Warning: Guard for command 52 of module "partyB" is never satisfied.

Warning: Guard for command 53 of module "partyB" is never satisfied.

Warning: Guard for command 54 of module "partyB" is never satisfied.

Warning: Guard for command 55 of module "partyB" is never satisfied.

Warning: Guard for command 56 of module "partyB" is never satisfied.

Warning: Guard for command 57 of module "partyB" is never satisfied.

Warning: Guard for command 58 of module "partyB" is never satisfied.

Warning: Guard for command 59 of module "partyB" is never satisfied.

Warning: Guard for command 60 of module "partyB" is never satisfied.

Computing reachable states...

Reachability (BFS): 101 iterations in 0.08 seconds (average 0.000792, setup 0.00)

Time for model construction: 0.164 seconds.

Type:        DTMC
States:      66060286 (1 initial)
Transitions: 67108861

Transition matrix: 18729 nodes (3 terminal), 67108861 minterms, vars: 169r/169c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/egl.10-2/model.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at explicit.DTMCSimple.initialise(DTMCSimple.java:151)
	at explicit.DTMCSimple.<init>(DTMCSimple.java:67)
	at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:92)
	at prism.Prism.doExportBuiltModel(Prism.java:2838)
	at prism.Prism.exportBuiltModelTask(Prism.java:2804)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/egl.10-2/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_egl.10-2_rep2.log

```
Command(s):
../bin/prism  models/egl.10-2/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/egl.10-2/model_rep2.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 3.734 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:14:32 GMT+01:00 2026
Hostname: n23m0127.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/egl.10-2/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/egl.10-2/model_rep2.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/egl.10-2/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Building model (engine:symbolic)...

Warning: Guard for command 11 of module "partyA" is never satisfied.

Warning: Guard for command 12 of module "partyA" is never satisfied.

Warning: Guard for command 13 of module "partyA" is never satisfied.

Warning: Guard for command 14 of module "partyA" is never satisfied.

Warning: Guard for command 15 of module "partyA" is never satisfied.

Warning: Guard for command 16 of module "partyA" is never satisfied.

Warning: Guard for command 17 of module "partyA" is never satisfied.

Warning: Guard for command 18 of module "partyA" is never satisfied.

Warning: Guard for command 19 of module "partyA" is never satisfied.

Warning: Guard for command 20 of module "partyA" is never satisfied.

Warning: Guard for command 31 of module "partyA" is never satisfied.

Warning: Guard for command 32 of module "partyA" is never satisfied.

Warning: Guard for command 33 of module "partyA" is never satisfied.

Warning: Guard for command 34 of module "partyA" is never satisfied.

Warning: Guard for command 35 of module "partyA" is never satisfied.

Warning: Guard for command 36 of module "partyA" is never satisfied.

Warning: Guard for command 37 of module "partyA" is never satisfied.

Warning: Guard for command 38 of module "partyA" is never satisfied.

Warning: Guard for command 39 of module "partyA" is never satisfied.

Warning: Guard for command 40 of module "partyA" is never satisfied.

Warning: Guard for command 51 of module "partyA" is never satisfied.

Warning: Guard for command 52 of module "partyA" is never satisfied.

Warning: Guard for command 53 of module "partyA" is never satisfied.

Warning: Guard for command 54 of module "partyA" is never satisfied.

Warning: Guard for command 55 of module "partyA" is never satisfied.

Warning: Guard for command 56 of module "partyA" is never satisfied.

Warning: Guard for command 57 of module "partyA" is never satisfied.

Warning: Guard for command 58 of module "partyA" is never satisfied.

Warning: Guard for command 59 of module "partyA" is never satisfied.

Warning: Guard for command 60 of module "partyA" is never satisfied.

Warning: Guard for command 11 of module "partyB" is never satisfied.

Warning: Guard for command 12 of module "partyB" is never satisfied.

Warning: Guard for command 13 of module "partyB" is never satisfied.

Warning: Guard for command 14 of module "partyB" is never satisfied.

Warning: Guard for command 15 of module "partyB" is never satisfied.

Warning: Guard for command 16 of module "partyB" is never satisfied.

Warning: Guard for command 17 of module "partyB" is never satisfied.

Warning: Guard for command 18 of module "partyB" is never satisfied.

Warning: Guard for command 19 of module "partyB" is never satisfied.

Warning: Guard for command 20 of module "partyB" is never satisfied.

Warning: Guard for command 31 of module "partyB" is never satisfied.

Warning: Guard for command 32 of module "partyB" is never satisfied.

Warning: Guard for command 33 of module "partyB" is never satisfied.

Warning: Guard for command 34 of module "partyB" is never satisfied.

Warning: Guard for command 35 of module "partyB" is never satisfied.

Warning: Guard for command 36 of module "partyB" is never satisfied.

Warning: Guard for command 37 of module "partyB" is never satisfied.

Warning: Guard for command 38 of module "partyB" is never satisfied.

Warning: Guard for command 39 of module "partyB" is never satisfied.

Warning: Guard for command 40 of module "partyB" is never satisfied.

Warning: Guard for command 51 of module "partyB" is never satisfied.

Warning: Guard for command 52 of module "partyB" is never satisfied.

Warning: Guard for command 53 of module "partyB" is never satisfied.

Warning: Guard for command 54 of module "partyB" is never satisfied.

Warning: Guard for command 55 of module "partyB" is never satisfied.

Warning: Guard for command 56 of module "partyB" is never satisfied.

Warning: Guard for command 57 of module "partyB" is never satisfied.

Warning: Guard for command 58 of module "partyB" is never satisfied.

Warning: Guard for command 59 of module "partyB" is never satisfied.

Warning: Guard for command 60 of module "partyB" is never satisfied.

Computing reachable states...

Reachability (BFS): 101 iterations in 0.10 seconds (average 0.000990, setup 0.00)

Time for model construction: 0.248 seconds.

Type:        DTMC
States:      66060286 (1 initial)
Transitions: 67108861

Transition matrix: 18729 nodes (3 terminal), 67108861 minterms, vars: 169r/169c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/egl.10-2/model_rep2.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at explicit.DTMCSimple.initialise(DTMCSimple.java:151)
	at explicit.DTMCSimple.<init>(DTMCSimple.java:67)
	at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:92)
	at prism.Prism.doExportBuiltModel(Prism.java:2838)
	at prism.Prism.exportBuiltModelTask(Prism.java:2804)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/egl.10-2/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_egl.10-2_rep3.log

```
Command(s):
../bin/prism  models/egl.10-2/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/egl.10-2/model_rep3.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 3.413 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:32:55 GMT+01:00 2026
Hostname: n23m0165.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/egl.10-2/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/egl.10-2/model_rep3.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/egl.10-2/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Building model (engine:symbolic)...

Warning: Guard for command 11 of module "partyA" is never satisfied.

Warning: Guard for command 12 of module "partyA" is never satisfied.

Warning: Guard for command 13 of module "partyA" is never satisfied.

Warning: Guard for command 14 of module "partyA" is never satisfied.

Warning: Guard for command 15 of module "partyA" is never satisfied.

Warning: Guard for command 16 of module "partyA" is never satisfied.

Warning: Guard for command 17 of module "partyA" is never satisfied.

Warning: Guard for command 18 of module "partyA" is never satisfied.

Warning: Guard for command 19 of module "partyA" is never satisfied.

Warning: Guard for command 20 of module "partyA" is never satisfied.

Warning: Guard for command 31 of module "partyA" is never satisfied.

Warning: Guard for command 32 of module "partyA" is never satisfied.

Warning: Guard for command 33 of module "partyA" is never satisfied.

Warning: Guard for command 34 of module "partyA" is never satisfied.

Warning: Guard for command 35 of module "partyA" is never satisfied.

Warning: Guard for command 36 of module "partyA" is never satisfied.

Warning: Guard for command 37 of module "partyA" is never satisfied.

Warning: Guard for command 38 of module "partyA" is never satisfied.

Warning: Guard for command 39 of module "partyA" is never satisfied.

Warning: Guard for command 40 of module "partyA" is never satisfied.

Warning: Guard for command 51 of module "partyA" is never satisfied.

Warning: Guard for command 52 of module "partyA" is never satisfied.

Warning: Guard for command 53 of module "partyA" is never satisfied.

Warning: Guard for command 54 of module "partyA" is never satisfied.

Warning: Guard for command 55 of module "partyA" is never satisfied.

Warning: Guard for command 56 of module "partyA" is never satisfied.

Warning: Guard for command 57 of module "partyA" is never satisfied.

Warning: Guard for command 58 of module "partyA" is never satisfied.

Warning: Guard for command 59 of module "partyA" is never satisfied.

Warning: Guard for command 60 of module "partyA" is never satisfied.

Warning: Guard for command 11 of module "partyB" is never satisfied.

Warning: Guard for command 12 of module "partyB" is never satisfied.

Warning: Guard for command 13 of module "partyB" is never satisfied.

Warning: Guard for command 14 of module "partyB" is never satisfied.

Warning: Guard for command 15 of module "partyB" is never satisfied.

Warning: Guard for command 16 of module "partyB" is never satisfied.

Warning: Guard for command 17 of module "partyB" is never satisfied.

Warning: Guard for command 18 of module "partyB" is never satisfied.

Warning: Guard for command 19 of module "partyB" is never satisfied.

Warning: Guard for command 20 of module "partyB" is never satisfied.

Warning: Guard for command 31 of module "partyB" is never satisfied.

Warning: Guard for command 32 of module "partyB" is never satisfied.

Warning: Guard for command 33 of module "partyB" is never satisfied.

Warning: Guard for command 34 of module "partyB" is never satisfied.

Warning: Guard for command 35 of module "partyB" is never satisfied.

Warning: Guard for command 36 of module "partyB" is never satisfied.

Warning: Guard for command 37 of module "partyB" is never satisfied.

Warning: Guard for command 38 of module "partyB" is never satisfied.

Warning: Guard for command 39 of module "partyB" is never satisfied.

Warning: Guard for command 40 of module "partyB" is never satisfied.

Warning: Guard for command 51 of module "partyB" is never satisfied.

Warning: Guard for command 52 of module "partyB" is never satisfied.

Warning: Guard for command 53 of module "partyB" is never satisfied.

Warning: Guard for command 54 of module "partyB" is never satisfied.

Warning: Guard for command 55 of module "partyB" is never satisfied.

Warning: Guard for command 56 of module "partyB" is never satisfied.

Warning: Guard for command 57 of module "partyB" is never satisfied.

Warning: Guard for command 58 of module "partyB" is never satisfied.

Warning: Guard for command 59 of module "partyB" is never satisfied.

Warning: Guard for command 60 of module "partyB" is never satisfied.

Computing reachable states...

Reachability (BFS): 101 iterations in 0.08 seconds (average 0.000792, setup 0.00)

Time for model construction: 0.179 seconds.

Type:        DTMC
States:      66060286 (1 initial)
Transitions: 67108861

Transition matrix: 18729 nodes (3 terminal), 67108861 minterms, vars: 169r/169c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/egl.10-2/model_rep3.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at explicit.DTMCSimple.initialise(DTMCSimple.java:152)
	at explicit.DTMCSimple.<init>(DTMCSimple.java:67)
	at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:92)
	at prism.Prism.doExportBuiltModel(Prism.java:2838)
	at prism.Prism.exportBuiltModelTask(Prism.java:2804)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/egl.10-2/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_egl.10-2_rep4.log

```
Command(s):
../bin/prism  models/egl.10-2/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/egl.10-2/model_rep4.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 2.662 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:37:04 GMT+01:00 2026
Hostname: n23m0341.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/egl.10-2/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/egl.10-2/model_rep4.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/egl.10-2/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Building model (engine:symbolic)...

Warning: Guard for command 11 of module "partyA" is never satisfied.

Warning: Guard for command 12 of module "partyA" is never satisfied.

Warning: Guard for command 13 of module "partyA" is never satisfied.

Warning: Guard for command 14 of module "partyA" is never satisfied.

Warning: Guard for command 15 of module "partyA" is never satisfied.

Warning: Guard for command 16 of module "partyA" is never satisfied.

Warning: Guard for command 17 of module "partyA" is never satisfied.

Warning: Guard for command 18 of module "partyA" is never satisfied.

Warning: Guard for command 19 of module "partyA" is never satisfied.

Warning: Guard for command 20 of module "partyA" is never satisfied.

Warning: Guard for command 31 of module "partyA" is never satisfied.

Warning: Guard for command 32 of module "partyA" is never satisfied.

Warning: Guard for command 33 of module "partyA" is never satisfied.

Warning: Guard for command 34 of module "partyA" is never satisfied.

Warning: Guard for command 35 of module "partyA" is never satisfied.

Warning: Guard for command 36 of module "partyA" is never satisfied.

Warning: Guard for command 37 of module "partyA" is never satisfied.

Warning: Guard for command 38 of module "partyA" is never satisfied.

Warning: Guard for command 39 of module "partyA" is never satisfied.

Warning: Guard for command 40 of module "partyA" is never satisfied.

Warning: Guard for command 51 of module "partyA" is never satisfied.

Warning: Guard for command 52 of module "partyA" is never satisfied.

Warning: Guard for command 53 of module "partyA" is never satisfied.

Warning: Guard for command 54 of module "partyA" is never satisfied.

Warning: Guard for command 55 of module "partyA" is never satisfied.

Warning: Guard for command 56 of module "partyA" is never satisfied.

Warning: Guard for command 57 of module "partyA" is never satisfied.

Warning: Guard for command 58 of module "partyA" is never satisfied.

Warning: Guard for command 59 of module "partyA" is never satisfied.

Warning: Guard for command 60 of module "partyA" is never satisfied.

Warning: Guard for command 11 of module "partyB" is never satisfied.

Warning: Guard for command 12 of module "partyB" is never satisfied.

Warning: Guard for command 13 of module "partyB" is never satisfied.

Warning: Guard for command 14 of module "partyB" is never satisfied.

Warning: Guard for command 15 of module "partyB" is never satisfied.

Warning: Guard for command 16 of module "partyB" is never satisfied.

Warning: Guard for command 17 of module "partyB" is never satisfied.

Warning: Guard for command 18 of module "partyB" is never satisfied.

Warning: Guard for command 19 of module "partyB" is never satisfied.

Warning: Guard for command 20 of module "partyB" is never satisfied.

Warning: Guard for command 31 of module "partyB" is never satisfied.

Warning: Guard for command 32 of module "partyB" is never satisfied.

Warning: Guard for command 33 of module "partyB" is never satisfied.

Warning: Guard for command 34 of module "partyB" is never satisfied.

Warning: Guard for command 35 of module "partyB" is never satisfied.

Warning: Guard for command 36 of module "partyB" is never satisfied.

Warning: Guard for command 37 of module "partyB" is never satisfied.

Warning: Guard for command 38 of module "partyB" is never satisfied.

Warning: Guard for command 39 of module "partyB" is never satisfied.

Warning: Guard for command 40 of module "partyB" is never satisfied.

Warning: Guard for command 51 of module "partyB" is never satisfied.

Warning: Guard for command 52 of module "partyB" is never satisfied.

Warning: Guard for command 53 of module "partyB" is never satisfied.

Warning: Guard for command 54 of module "partyB" is never satisfied.

Warning: Guard for command 55 of module "partyB" is never satisfied.

Warning: Guard for command 56 of module "partyB" is never satisfied.

Warning: Guard for command 57 of module "partyB" is never satisfied.

Warning: Guard for command 58 of module "partyB" is never satisfied.

Warning: Guard for command 59 of module "partyB" is never satisfied.

Warning: Guard for command 60 of module "partyB" is never satisfied.

Computing reachable states...

Reachability (BFS): 101 iterations in 0.07 seconds (average 0.000693, setup 0.00)

Time for model construction: 0.164 seconds.

Type:        DTMC
States:      66060286 (1 initial)
Transitions: 67108861

Transition matrix: 18729 nodes (3 terminal), 67108861 minterms, vars: 169r/169c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/egl.10-2/model_rep4.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at explicit.DTMCSimple.initialise(DTMCSimple.java:152)
	at explicit.DTMCSimple.<init>(DTMCSimple.java:67)
	at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:92)
	at prism.Prism.doExportBuiltModel(Prism.java:2838)
	at prism.Prism.exportBuiltModelTask(Prism.java:2804)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/egl.10-2/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_norewards_egl.10-2_rep5.log

```
Command(s):
../bin/prism  models/egl.10-2/model.prism -exportmodel out/prism_from-prism_to-umb_norewards/egl.10-2/model_rep5.umb:states=false,obs=false,rewards=false,zip=false
Wallclock time: 3.516 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:30:20 GMT+01:00 2026
Hostname: n23m0250.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism models/egl.10-2/model.prism -exportmodel 'out/prism_from-prism_to-umb_norewards/egl.10-2/model_rep5.umb:states=false,obs=false,rewards=false,zip=false'

Parsing PRISM model file "models/egl.10-2/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Building model (engine:symbolic)...

Warning: Guard for command 11 of module "partyA" is never satisfied.

Warning: Guard for command 12 of module "partyA" is never satisfied.

Warning: Guard for command 13 of module "partyA" is never satisfied.

Warning: Guard for command 14 of module "partyA" is never satisfied.

Warning: Guard for command 15 of module "partyA" is never satisfied.

Warning: Guard for command 16 of module "partyA" is never satisfied.

Warning: Guard for command 17 of module "partyA" is never satisfied.

Warning: Guard for command 18 of module "partyA" is never satisfied.

Warning: Guard for command 19 of module "partyA" is never satisfied.

Warning: Guard for command 20 of module "partyA" is never satisfied.

Warning: Guard for command 31 of module "partyA" is never satisfied.

Warning: Guard for command 32 of module "partyA" is never satisfied.

Warning: Guard for command 33 of module "partyA" is never satisfied.

Warning: Guard for command 34 of module "partyA" is never satisfied.

Warning: Guard for command 35 of module "partyA" is never satisfied.

Warning: Guard for command 36 of module "partyA" is never satisfied.

Warning: Guard for command 37 of module "partyA" is never satisfied.

Warning: Guard for command 38 of module "partyA" is never satisfied.

Warning: Guard for command 39 of module "partyA" is never satisfied.

Warning: Guard for command 40 of module "partyA" is never satisfied.

Warning: Guard for command 51 of module "partyA" is never satisfied.

Warning: Guard for command 52 of module "partyA" is never satisfied.

Warning: Guard for command 53 of module "partyA" is never satisfied.

Warning: Guard for command 54 of module "partyA" is never satisfied.

Warning: Guard for command 55 of module "partyA" is never satisfied.

Warning: Guard for command 56 of module "partyA" is never satisfied.

Warning: Guard for command 57 of module "partyA" is never satisfied.

Warning: Guard for command 58 of module "partyA" is never satisfied.

Warning: Guard for command 59 of module "partyA" is never satisfied.

Warning: Guard for command 60 of module "partyA" is never satisfied.

Warning: Guard for command 11 of module "partyB" is never satisfied.

Warning: Guard for command 12 of module "partyB" is never satisfied.

Warning: Guard for command 13 of module "partyB" is never satisfied.

Warning: Guard for command 14 of module "partyB" is never satisfied.

Warning: Guard for command 15 of module "partyB" is never satisfied.

Warning: Guard for command 16 of module "partyB" is never satisfied.

Warning: Guard for command 17 of module "partyB" is never satisfied.

Warning: Guard for command 18 of module "partyB" is never satisfied.

Warning: Guard for command 19 of module "partyB" is never satisfied.

Warning: Guard for command 20 of module "partyB" is never satisfied.

Warning: Guard for command 31 of module "partyB" is never satisfied.

Warning: Guard for command 32 of module "partyB" is never satisfied.

Warning: Guard for command 33 of module "partyB" is never satisfied.

Warning: Guard for command 34 of module "partyB" is never satisfied.

Warning: Guard for command 35 of module "partyB" is never satisfied.

Warning: Guard for command 36 of module "partyB" is never satisfied.

Warning: Guard for command 37 of module "partyB" is never satisfied.

Warning: Guard for command 38 of module "partyB" is never satisfied.

Warning: Guard for command 39 of module "partyB" is never satisfied.

Warning: Guard for command 40 of module "partyB" is never satisfied.

Warning: Guard for command 51 of module "partyB" is never satisfied.

Warning: Guard for command 52 of module "partyB" is never satisfied.

Warning: Guard for command 53 of module "partyB" is never satisfied.

Warning: Guard for command 54 of module "partyB" is never satisfied.

Warning: Guard for command 55 of module "partyB" is never satisfied.

Warning: Guard for command 56 of module "partyB" is never satisfied.

Warning: Guard for command 57 of module "partyB" is never satisfied.

Warning: Guard for command 58 of module "partyB" is never satisfied.

Warning: Guard for command 59 of module "partyB" is never satisfied.

Warning: Guard for command 60 of module "partyB" is never satisfied.

Computing reachable states...

Reachability (BFS): 101 iterations in 0.08 seconds (average 0.000792, setup 0.00)

Time for model construction: 0.175 seconds.

Type:        DTMC
States:      66060286 (1 initial)
Transitions: 67108861

Transition matrix: 18729 nodes (3 terminal), 67108861 minterms, vars: 169r/169c

Exporting model in UMB format to file "out/prism_from-prism_to-umb_norewards/egl.10-2/model_rep5.umb"...

##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at explicit.DTMCSimple.initialise(DTMCSimple.java:152)
	at explicit.DTMCSimple.<init>(DTMCSimple.java:67)
	at symbolic.build.MTBDD2ExplicitModel.convertModel(MTBDD2ExplicitModel.java:92)
	at prism.Prism.doExportBuiltModel(Prism.java:2838)
	at prism.Prism.exportBuiltModelTask(Prism.java:2804)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2746)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_norewards/egl.10-2/model_rep5.umb:	File does not exist.
```

