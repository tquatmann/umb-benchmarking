# Log files for storm_from-umb_check_exact on model [consensus.6-2](../../models/consensus.6-2)

Parsed values: `[3.289, 3.304, 2.746, 2.896, 3.286]`



### Log file: storm_from-umb_check_exact_consensus.6-2_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/consensus.6-2/storm.model.exact.umb --prop models/consensus.6-2/property.props --exact
Wallclock time: 7203.084 seconds
Return code: None (timeout)
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:48:25 2026
Command line arguments: --timemem --buildfull --explicit-umb models/consensus.6-2/storm.model.exact.umb --prop models/consensus.6-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.017s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.206s seconds.
Time for model construction: 3.289s.

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



### Log file: storm_from-umb_check_exact_consensus.6-2_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/consensus.6-2/storm.model.exact.umb --prop models/consensus.6-2/property.props --exact
Wallclock time: 7203.084 seconds
Return code: None (timeout)
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 02:51:45 2026
Command line arguments: --timemem --buildfull --explicit-umb models/consensus.6-2/storm.model.exact.umb --prop models/consensus.6-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.013s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.168s seconds.
Time for model construction: 3.304s.

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



### Log file: storm_from-umb_check_exact_consensus.6-2_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/consensus.6-2/storm.model.exact.umb --prop models/consensus.6-2/property.props --exact
Wallclock time: 6694.024 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:05 2026
Command line arguments: --timemem --buildfull --explicit-umb models/consensus.6-2/storm.model.exact.umb --prop models/consensus.6-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.013s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.153s seconds.
Time for model construction: 2.746s.

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
Time for model checking: 6691.051s.

Performance statistics:
  * peak memory usage: 3284MB
  * CPU time: 6681.687s
  * wallclock time: 6693.894s
```



### Log file: storm_from-umb_check_exact_consensus.6-2_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/consensus.6-2/storm.model.exact.umb --prop models/consensus.6-2/property.props --exact
Wallclock time: 7203.073 seconds
Return code: None (timeout)
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:00 2026
Command line arguments: --timemem --buildfull --explicit-umb models/consensus.6-2/storm.model.exact.umb --prop models/consensus.6-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.021s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.165s seconds.
Time for model construction: 2.896s.

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



### Log file: storm_from-umb_check_exact_consensus.6-2_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/consensus.6-2/storm.model.exact.umb --prop models/consensus.6-2/property.props --exact
Wallclock time: 7203.089 seconds
Return code: None (timeout)
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:36:41 2026
Command line arguments: --timemem --buildfull --explicit-umb models/consensus.6-2/storm.model.exact.umb --prop models/consensus.6-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.021s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.169s seconds.
Time for model construction: 3.286s.

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

