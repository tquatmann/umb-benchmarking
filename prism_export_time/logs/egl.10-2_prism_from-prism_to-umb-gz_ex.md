# Log files for prism_from-prism_to-umb-gz_ex on model [egl.10-2](../../models/egl.10-2)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: prism_from-prism_to-umb-gz_ex_egl.10-2_rep1.log

```
Command(s):
../bin/prism -ex models/egl.10-2/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/egl.10-2/model.umb.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 22.428 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:44:44 GMT+01:00 2026
Hostname: r23m0008.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/egl.10-2/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/egl.10-2/model.umb.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/egl.10-2/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Building model (engine:explicit)...

Computing reachable states... 333099 643274 809628 831431 834951
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
out/prism_from-prism_to-umb-gz_ex/egl.10-2/model.umb.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_egl.10-2_rep2.log

```
Command(s):
../bin/prism -ex models/egl.10-2/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/egl.10-2/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 82.036 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:07 GMT+01:00 2026
Hostname: r23m0217.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/egl.10-2/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/egl.10-2/model.umb_rep2.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/egl.10-2/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Building model (engine:explicit)...

Computing reachable states... 87490 179825 260818 348371 428490 511160 588818 670807 750199 774620 805397 821422 829333 832564 834000 834718 836872 837949
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.lang.Integer.valueOf(Integer.java:1019)
	at explicit.IndexedSet.add(IndexedSet.java:72)
	at explicit.ConstructModel.constructModel(ConstructModel.java:297)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/egl.10-2/model.umb_rep2.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_egl.10-2_rep3.log

```
Command(s):
../bin/prism -ex models/egl.10-2/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/egl.10-2/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 21.772 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:20 GMT+01:00 2026
Hostname: r23m0090.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/egl.10-2/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/egl.10-2/model.umb_rep3.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/egl.10-2/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Building model (engine:explicit)...

Computing reachable states... 378979 713889 821573 833824 835619
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.lang.Integer.valueOf(Integer.java:1019)
	at explicit.IndexedSet.add(IndexedSet.java:72)
	at explicit.ConstructModel.constructModel(ConstructModel.java:297)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-umb-gz_ex/egl.10-2/model.umb_rep3.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_egl.10-2_rep4.log

```
Command(s):
../bin/prism -ex models/egl.10-2/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/egl.10-2/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 24.423 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:26 GMT+01:00 2026
Hostname: n23m0167.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/egl.10-2/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/egl.10-2/model.umb_rep4.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/egl.10-2/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Building model (engine:explicit)...

Computing reachable states... 352974 689853 820674 832566 834361 838310
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
out/prism_from-prism_to-umb-gz_ex/egl.10-2/model.umb_rep4.gz:	File does not exist.
```



### Log file: prism_from-prism_to-umb-gz_ex_egl.10-2_rep5.log

```
Command(s):
../bin/prism -ex models/egl.10-2/model.prism -exportmodel out/prism_from-prism_to-umb-gz_ex/egl.10-2/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true
Wallclock time: 23.670 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:25:18 GMT+01:00 2026
Hostname: n23m0060.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/egl.10-2/model.prism -exportmodel 'out/prism_from-prism_to-umb-gz_ex/egl.10-2/model.umb_rep5.gz:states=false,obs=false,rewards=true,zip=true'

Parsing PRISM model file "models/egl.10-2/model.prism"...

Type:        DTMC
Modules:     counter partyA partyB
Actions:     [] [receiveB] [receiveA]
Variables:   b n phase party b0 b20 b1 b21 b2 b22 b3 b23 b4 b24 b5 b25 b6 b26 b7 b27 b8 b28 b9 b29 b10 b30 b11 b31 b12 b32 b13 b33 b14 b34 b15 b35 b16 b36 b17 b37 b18 b38 b19 b39 a0 a20 a1 a21 a2 a22 a3 a23 a4 a24 a5 a25 a6 a26 a7 a27 a8 a28 a9 a29 a10 a30 a11 a31 a12 a32 a13 a33 a14 a34 a15 a35 a16 a36 a17 a37 a18 a38 a19 a39
Labels:      "knowB" "knowA"

Building model (engine:explicit)...

Computing reachable states... 357578 692741 821123 833015 835528
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
out/prism_from-prism_to-umb-gz_ex/egl.10-2/model.umb_rep5.gz:	File does not exist.
```

