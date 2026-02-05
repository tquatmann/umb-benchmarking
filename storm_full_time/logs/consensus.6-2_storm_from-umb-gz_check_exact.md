# Log files

Tool configuration: storm_from-umb-gz_check_exact
Benchmark: [consensus.6-2](../../models/consensus.6-2)
Parsed values: [TO, 7103.377, 6810.757, 6733.784, TO]



### Log file: storm_from-umb-gz_check_exact_consensus.6-2_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/consensus.6-2/storm.model.exact.umb.gz --prop models/consensus.6-2/property.props --exact
Wallclock time: 7203.065 seconds
Return code: None (timeout)
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:43:44 2026
Command line arguments: --timemem --buildfull --explicit-umb models/consensus.6-2/storm.model.exact.umb.gz --prop models/consensus.6-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.008s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.373s seconds.
Time for model construction: 3.415s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1258240
Transitions: 	6236736
Choices: 	5008128
Reward Models:  none
State Labels: 	4 labels
   * finished -> 384 item(s)
   * deadlock -> 0 item(s)
   * agree -> 114258 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "disagree": Pmax=? [F ("finished" & (!"agree"))] ...

##############################Output to stderr##############################
ERROR: The program received signal 15 and will be aborted in 3s.
Received signal 14
```



### Log file: storm_from-umb-gz_check_exact_consensus.6-2_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/consensus.6-2/storm.model.exact.umb.gz --prop models/consensus.6-2/property.props --exact
Wallclock time: 7103.377 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 02:51:46 2026
Command line arguments: --timemem --buildfull --explicit-umb models/consensus.6-2/storm.model.exact.umb.gz --prop models/consensus.6-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.020s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.329s seconds.
Time for model construction: 3.057s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1258240
Transitions: 	6236736
Choices: 	5008128
Reward Models:  none
State Labels: 	4 labels
   * finished -> 384 item(s)
   * deadlock -> 0 item(s)
   * agree -> 114258 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "disagree": Pmax=? [F ("finished" & (!"agree"))] ...
Result (for initial states): 37101798760906709/102027593703751680 (approx. 0.3636447496)
Time for model checking: 7100.025s.

Performance statistics:
  * peak memory usage: 3282MB
  * CPU time: 7077.953s
  * wallclock time: 7103.172s
```



### Log file: storm_from-umb-gz_check_exact_consensus.6-2_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/consensus.6-2/storm.model.exact.umb.gz --prop models/consensus.6-2/property.props --exact
Wallclock time: 6810.757 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:52:58 2026
Command line arguments: --timemem --buildfull --explicit-umb models/consensus.6-2/storm.model.exact.umb.gz --prop models/consensus.6-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.018s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.324s seconds.
Time for model construction: 2.976s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1258240
Transitions: 	6236736
Choices: 	5008128
Reward Models:  none
State Labels: 	4 labels
   * finished -> 384 item(s)
   * deadlock -> 0 item(s)
   * agree -> 114258 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "disagree": Pmax=? [F ("finished" & (!"agree"))] ...
Result (for initial states): 37101798760906709/102027593703751680 (approx. 0.3636447496)
Time for model checking: 6807.359s.

Performance statistics:
  * peak memory usage: 3282MB
  * CPU time: 6795.543s
  * wallclock time: 6810.434s
```



### Log file: storm_from-umb-gz_check_exact_consensus.6-2_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/consensus.6-2/storm.model.exact.umb.gz --prop models/consensus.6-2/property.props --exact
Wallclock time: 6733.784 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 02:58:57 2026
Command line arguments: --timemem --buildfull --explicit-umb models/consensus.6-2/storm.model.exact.umb.gz --prop models/consensus.6-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.009s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.335s seconds.
Time for model construction: 2.931s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1258240
Transitions: 	6236736
Choices: 	5008128
Reward Models:  none
State Labels: 	4 labels
   * finished -> 384 item(s)
   * deadlock -> 0 item(s)
   * agree -> 114258 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "disagree": Pmax=? [F ("finished" & (!"agree"))] ...
Result (for initial states): 37101798760906709/102027593703751680 (approx. 0.3636447496)
Time for model checking: 6730.606s.

Performance statistics:
  * peak memory usage: 3282MB
  * CPU time: 6706.913s
  * wallclock time: 6733.624s
```



### Log file: storm_from-umb-gz_check_exact_consensus.6-2_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/consensus.6-2/storm.model.exact.umb.gz --prop models/consensus.6-2/property.props --exact
Wallclock time: 7203.088 seconds
Return code: None (timeout)
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:25 2026
Command line arguments: --timemem --buildfull --explicit-umb models/consensus.6-2/storm.model.exact.umb.gz --prop models/consensus.6-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.006s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.379s seconds.
Time for model construction: 3.472s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1258240
Transitions: 	6236736
Choices: 	5008128
Reward Models:  none
State Labels: 	4 labels
   * finished -> 384 item(s)
   * deadlock -> 0 item(s)
   * agree -> 114258 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "disagree": Pmax=? [F ("finished" & (!"agree"))] ...

##############################Output to stderr##############################
ERROR: The program received signal 15 and will be aborted in 3s.
Received signal 14
```

