# Log files

Tool configuration: storm_from-prism_check_exact
Benchmark: [consensus.6-2](../../models/consensus.6-2)
Parsed values: [6853.557, TO, 6720.788, 6742.803, TO]



### Log file: storm_from-prism_check_exact_consensus.6-2_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/consensus.6-2/model.prism --prismcompat --prop models/consensus.6-2/property.props --exact
Wallclock time: 6853.557 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:24:30 2026
Command line arguments: --timemem --buildfull --prism models/consensus.6-2/model.prism --prismcompat --prop models/consensus.6-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.146s.

Time for model construction: 10.070s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1258240
Transitions: 	6236736
Choices: 	5008128
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * finished -> 384 item(s)
   * agree -> 114258 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "disagree": Pmax=? [F ("finished" & (!"agree"))] ...
Result (for initial states): 37101798760906709/102027593703751680 (approx. 0.3636447496)
Time for model checking: 6842.997s.

Performance statistics:
  * peak memory usage: 3328MB
  * CPU time: 6833.615s
  * wallclock time: 6853.329s
```



### Log file: storm_from-prism_check_exact_consensus.6-2_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/consensus.6-2/model.prism --prismcompat --prop models/consensus.6-2/property.props --exact
Wallclock time: 7203.022 seconds
Return code: None (timeout)
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:51:33 2026
Command line arguments: --timemem --buildfull --prism models/consensus.6-2/model.prism --prismcompat --prop models/consensus.6-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.036s.

Time for model construction: 45.451s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1258240
Transitions: 	6236736
Choices: 	5008128
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * finished -> 384 item(s)
   * agree -> 114258 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "disagree": Pmax=? [F ("finished" & (!"agree"))] ...

##############################Output to stderr##############################
ERROR: The program received signal 15 and will be aborted in 3s.
Received signal 14
```



### Log file: storm_from-prism_check_exact_consensus.6-2_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/consensus.6-2/model.prism --prismcompat --prop models/consensus.6-2/property.props --exact
Wallclock time: 6720.788 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:03 2026
Command line arguments: --timemem --buildfull --prism models/consensus.6-2/model.prism --prismcompat --prop models/consensus.6-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.004s.

Time for model construction: 10.079s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1258240
Transitions: 	6236736
Choices: 	5008128
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * finished -> 384 item(s)
   * agree -> 114258 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "disagree": Pmax=? [F ("finished" & (!"agree"))] ...
Result (for initial states): 37101798760906709/102027593703751680 (approx. 0.3636447496)
Time for model checking: 6709.794s.

Performance statistics:
  * peak memory usage: 3328MB
  * CPU time: 6702.506s
  * wallclock time: 6719.972s
```



### Log file: storm_from-prism_check_exact_consensus.6-2_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/consensus.6-2/model.prism --prismcompat --prop models/consensus.6-2/property.props --exact
Wallclock time: 6742.803 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:37:39 2026
Command line arguments: --timemem --buildfull --prism models/consensus.6-2/model.prism --prismcompat --prop models/consensus.6-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 9.867s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1258240
Transitions: 	6236736
Choices: 	5008128
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * finished -> 384 item(s)
   * agree -> 114258 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "disagree": Pmax=? [F ("finished" & (!"agree"))] ...
Result (for initial states): 37101798760906709/102027593703751680 (approx. 0.3636447496)
Time for model checking: 6732.466s.

Performance statistics:
  * peak memory usage: 3328MB
  * CPU time: 6720.465s
  * wallclock time: 6742.467s
```



### Log file: storm_from-prism_check_exact_consensus.6-2_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/consensus.6-2/model.prism --prismcompat --prop models/consensus.6-2/property.props --exact
Wallclock time: 7203.021 seconds
Return code: None (timeout)
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:07:34 2026
Command line arguments: --timemem --buildfull --prism models/consensus.6-2/model.prism --prismcompat --prop models/consensus.6-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.004s.

Time for model construction: 9.933s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1258240
Transitions: 	6236736
Choices: 	5008128
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * finished -> 384 item(s)
   * agree -> 114258 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "disagree": Pmax=? [F ("finished" & (!"agree"))] ...

##############################Output to stderr##############################
ERROR: The program received signal 15 and will be aborted in 3s.
Received signal 14
```

