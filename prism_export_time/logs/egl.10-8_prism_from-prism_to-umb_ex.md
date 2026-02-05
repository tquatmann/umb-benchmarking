# Log files

Tool configuration: prism_from-prism_to-umb_ex
Benchmark: [egl.10-8](../../models/egl.10-8)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_to-umb_ex_egl.10-8_rep1.log

```
Command(s):
../bin/prism -ex models/egl.10-8/model.prism -exportmodel out/prism_from-prism_to-umb_ex/egl.10-8/model.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 22.087 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:49:26 GMT+01:00 2026
Hostname: r23m0008.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/egl.10-8/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/egl.10-8/model.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/egl.10-8/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Building model (engine:explicit)...

Computing reachable states... 336012 648068 809838 831671 835261
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at explicit.DTMCSimple.addStates(DTMCSimple.java:181)
	at explicit.DTMCSimple.addState(DTMCSimple.java:173)
	at explicit.ConstructModel.constructModel(ConstructModel.java:302)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/egl.10-8/model.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_egl.10-8_rep2.log

```
Command(s):
../bin/prism -ex models/egl.10-8/model.prism -exportmodel out/prism_from-prism_to-umb_ex/egl.10-8/model_rep2.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 24.113 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:27:14 GMT+01:00 2026
Hostname: n23m0042.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/egl.10-8/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/egl.10-8/model_rep2.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/egl.10-8/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Building model (engine:explicit)...

Computing reachable states... 334066 652085 815305 830320 833910 837859
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.DTMCSimple.addToProbability(DTMCSimple.java:258)
	at explicit.ConstructModel.constructModel(ConstructModel.java:316)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/egl.10-8/model_rep2.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_egl.10-8_rep3.log

```
Command(s):
../bin/prism -ex models/egl.10-8/model.prism -exportmodel out/prism_from-prism_to-umb_ex/egl.10-8/model_rep3.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 20.148 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:22 GMT+01:00 2026
Hostname: n23m0204.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/egl.10-8/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/egl.10-8/model_rep3.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/egl.10-8/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Building model (engine:explicit)...

Computing reachable states... 393183 769010 826912 834092 836964
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at explicit.DTMCSimple.addStates(DTMCSimple.java:181)
	at explicit.DTMCSimple.addState(DTMCSimple.java:173)
	at explicit.ConstructModel.constructModel(ConstructModel.java:302)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/egl.10-8/model_rep3.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_egl.10-8_rep4.log

```
Command(s):
../bin/prism -ex models/egl.10-8/model.prism -exportmodel out/prism_from-prism_to-umb_ex/egl.10-8/model_rep4.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 24.748 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:29 GMT+01:00 2026
Hostname: n23m0006.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/egl.10-8/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/egl.10-8/model_rep4.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/egl.10-8/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Building model (engine:explicit)...

Computing reachable states... 335060 654376 816959 831130 834720 837951
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at explicit.DTMCSimple.addStates(DTMCSimple.java:181)
	at explicit.DTMCSimple.addState(DTMCSimple.java:173)
	at explicit.ConstructModel.constructModel(ConstructModel.java:302)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/egl.10-8/model_rep4.umb:	File does not exist.
```



### Log file: prism_from-prism_to-umb_ex_egl.10-8_rep5.log

```
Command(s):
../bin/prism -ex models/egl.10-8/model.prism -exportmodel out/prism_from-prism_to-umb_ex/egl.10-8/model_rep5.umb:states=false,obs=false,rewards=true,zip=false
Wallclock time: 21.999 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:09:59 GMT+01:00 2026
Hostname: n23m0043.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/egl.10-8/model.prism -exportmodel 'out/prism_from-prism_to-umb_ex/egl.10-8/model_rep5.umb:states=false,obs=false,rewards=true,zip=false'

Parsing PRISM model file "models/egl.10-8/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Building model (engine:explicit)...

Computing reachable states... 341081 660023 821420 834583 836043
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.DTMCSimple.addToProbability(DTMCSimple.java:259)
	at explicit.ConstructModel.constructModel(ConstructModel.java:316)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb_ex/egl.10-8/model_rep5.umb:	File does not exist.
```

