# Log files

Tool configuration: prism_from-prism_to-tra_ex
Benchmark: [polling.18-16](../../models/polling.18-16)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: prism_from-prism_to-tra_ex_polling.18-16_rep1.log

```
Command(s):
../bin/prism -ex models/polling.18-16/model.prism -exportmodel out/prism_from-prism_to-tra_ex/polling.18-16/model.tra,lab,rew:precision=17
Wallclock time: 48.146 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Tue Jan 27 23:32:31 GMT+01:00 2026
Hostname: n23m0241.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/polling.18-16/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/polling.18-16/model.tra,lab,rew:precision=17'

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Building model (engine:explicit)...

Computing reachable states... 200367 409903 622572 831619 997079 1021879 1034180 1043409 1050085 1053893 1056747 1058084 1059418 1060559
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at explicit.DTMCSimple.addToProbability(DTMCSimple.java:258)
	at explicit.ConstructModel.constructModel(ConstructModel.java:319)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/polling.18-16/model.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/polling.18-16/model.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/polling.18-16/model.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/polling.18-16/model.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_polling.18-16_rep2.log

```
Command(s):
../bin/prism -ex models/polling.18-16/model.prism -exportmodel out/prism_from-prism_to-tra_ex/polling.18-16/model_rep2.tra,lab,rew:precision=17
Wallclock time: 41.871 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:26:01 GMT+01:00 2026
Hostname: n23m0134.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/polling.18-16/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/polling.18-16/model_rep2.tra,lab,rew:precision=17'

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Building model (engine:explicit)...

Computing reachable states... 233074 472706 715391 964203 1022172 1036082 1048085 1053423 1056657 1058375 1059518 1060849
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at parser.ast.Update.update(Update.java:215)
	at simulator.ChoiceListFlexi.computeTarget(ChoiceListFlexi.java:259)
	at simulator.ModulesFileModelGenerator.computeTransitionTarget(ModulesFileModelGenerator.java:664)
	at explicit.ConstructModel.constructModel(ConstructModel.java:295)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/polling.18-16/model_rep2.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/polling.18-16/model_rep2.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/polling.18-16/model_rep2.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/polling.18-16/model_rep2.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_polling.18-16_rep3.log

```
Command(s):
../bin/prism -ex models/polling.18-16/model.prism -exportmodel out/prism_from-prism_to-tra_ex/polling.18-16/model_rep3.tra,lab,rew:precision=17
Wallclock time: 49.964 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 09:15:07 GMT+01:00 2026
Hostname: r23m0071.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/polling.18-16/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/polling.18-16/model_rep3.tra,lab,rew:precision=17'

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Building model (engine:explicit)...

Computing reachable states... 196139 402652 614179 815639 980195 1020552 1033299 1042777 1049837 1054025 1056307 1057835 1058597 1059931
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.TreeMap.addEntry(TreeMap.java:801)
	at java.base/java.util.TreeMap.put(TreeMap.java:864)
	at java.base/java.util.TreeMap.put(TreeMap.java:570)
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
out/prism_from-prism_to-tra_ex/polling.18-16/model_rep3.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/polling.18-16/model_rep3.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/polling.18-16/model_rep3.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/polling.18-16/model_rep3.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_polling.18-16_rep4.log

```
Command(s):
../bin/prism -ex models/polling.18-16/model.prism -exportmodel out/prism_from-prism_to-tra_ex/polling.18-16/model_rep4.tra,lab,rew:precision=17
Wallclock time: 41.890 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 08:53:17 GMT+01:00 2026
Hostname: n23m0308.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/polling.18-16/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/polling.18-16/model_rep4.tra,lab,rew:precision=17'

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Building model (engine:explicit)...

Computing reachable states... 231930 473035 711486 962202 1023661 1037041 1047728 1052497 1055919 1058021 1059164 1060496
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.base/java.util.ArrayList.grow(ArrayList.java:240)
	at java.base/java.util.ArrayList.grow(ArrayList.java:245)
	at java.base/java.util.ArrayList.add(ArrayList.java:484)
	at java.base/java.util.ArrayList.add(ArrayList.java:497)
	at simulator.Updater.processUpdatesAndCreateNewChoice(Updater.java:379)
	at simulator.Updater.calculateTransitions(Updater.java:216)
	at simulator.ModulesFileModelGenerator.getTransitionListScalars(ModulesFileModelGenerator.java:827)
	at simulator.ModulesFileModelGenerator.getTransitionList(ModulesFileModelGenerator.java:814)
	at simulator.ModulesFileModelGenerator.getNumChoices(ModulesFileModelGenerator.java:513)
	at explicit.ConstructModel.constructModel(ConstructModel.java:273)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/polling.18-16/model_rep4.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/polling.18-16/model_rep4.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/polling.18-16/model_rep4.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/polling.18-16/model_rep4.trew:	File does not exist.
```



### Log file: prism_from-prism_to-tra_ex_polling.18-16_rep5.log

```
Command(s):
../bin/prism -ex models/polling.18-16/model.prism -exportmodel out/prism_from-prism_to-tra_ex/polling.18-16/model_rep5.tra,lab,rew:precision=17
Wallclock time: 43.098 seconds
Return code: 1
##############################
PRISM
=====

Version: 4.9.dev
Date: Thu Jan 29 07:36:54 GMT+01:00 2026
Hostname: n23m0191.hpc.itc.rwth-aachen.de
Memory limits: cudd=1g, java(heap)=1g
Command line: prism -ex models/polling.18-16/model.prism -exportmodel 'out/prism_from-prism_to-tra_ex/polling.18-16/model_rep5.tra,lab,rew:precision=17'

Parsing PRISM model file "models/polling.18-16/model.prism"...

Type:        CTMC
Modules:     server station1 station2 station3 station4 station5 station6 station7 station8 station9 station10 station11 station12 station13 station14 station15 station16 station17 station18
Actions:     [] [loop1a] [loop1b] [serve1] [loop2a] [loop2b] [serve2] [loop3a] [loop3b] [serve3] [loop4a] [loop4b] [serve4] [loop5a] [loop5b] [serve5] [loop6a] [loop6b] [serve6] [loop7a] [loop7b] [serve7] [loop8a] [loop8b] [serve8] [loop9a] [loop9b] [serve9] [loop10a] [loop10b] [serve10] [loop11a] [loop11b] [serve11] [loop12a] [loop12b] [serve12] [loop13a] [loop13b] [serve13] [loop14a] [loop14b] [serve14] [loop15a] [loop15b] [serve15] [loop16a] [loop16b] [serve16] [loop17a] [loop17b] [serve17] [loop18a] [loop18b] [serve18]
Variables:   s a s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18
Labels:      "serve_s2" "serve_s1"

Building model (engine:explicit)...

Computing reachable states... 231935 469254 700739 951378 1017366 1034269 1045095 1051005 1055001 1057287 1058432 1059576
##############################Output to stderr##############################
Picked up JAVA_TOOL_OPTIONS: -Xmx32g
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at parser.ast.Update.update(Update.java:215)
	at simulator.ChoiceListFlexi.computeTarget(ChoiceListFlexi.java:259)
	at simulator.ModulesFileModelGenerator.computeTransitionTarget(ModulesFileModelGenerator.java:664)
	at explicit.ConstructModel.constructModel(ConstructModel.java:295)
	at explicit.ConstructModel.constructModel(ConstructModel.java:150)
	at prism.Prism.doBuildModel(Prism.java:2303)
	at prism.Prism.buildModelIfRequired(Prism.java:2199)
	at prism.Prism.exportBuiltModelTasks(Prism.java:2740)
	at prism.PrismCL.doExports(PrismCL.java:868)
	at prism.PrismCL.run(PrismCL.java:381)
	at prism.PrismCL.go(PrismCL.java:227)
	at prism.PrismCL.main(PrismCL.java:3040)

############################## Output files ##############################
out/prism_from-prism_to-tra_ex/polling.18-16/model_rep5.tra:	File does not exist.
out/prism_from-prism_to-tra_ex/polling.18-16/model_rep5.lab:	File does not exist.
out/prism_from-prism_to-tra_ex/polling.18-16/model_rep5.srew:	File does not exist.
out/prism_from-prism_to-tra_ex/polling.18-16/model_rep5.trew:	File does not exist.
```

