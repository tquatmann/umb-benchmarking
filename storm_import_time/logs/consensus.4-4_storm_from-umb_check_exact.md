# Log files

Tool configuration: storm_from-umb_check_exact
Benchmark: [consensus.4-4](../../models/consensus.4-4)
Parsed values: [0.106, 0.109, 0.101, 0.116, 0.134]



### Log file: storm_from-umb_check_exact_consensus.4-4_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/consensus.4-4/storm.model.exact.umb --prop models/consensus.4-4/property.props --exact
Wallclock time: 4.071 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:46:20 2026
Command line arguments: --timemem --buildfull --explicit-umb models/consensus.4-4/storm.model.exact.umb --prop models/consensus.4-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.015s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.025s seconds.
Time for model construction: 0.106s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	43136
Transitions: 	144352
Choices: 	115840
Reward Models:  none
State Labels: 	4 labels
   * finished -> 64 item(s)
   * deadlock -> 0 item(s)
   * agree -> 9170 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "disagree": Pmax=? [F ("finished" & (!"agree"))] ...
Result (for initial states): 45666330762076479/292595849630842880 (approx. 0.156073064)
Time for model checking: 3.912s.

Performance statistics:
  * peak memory usage: 138MB
  * CPU time: 3.953s
  * wallclock time: 4.023s
```



### Log file: storm_from-umb_check_exact_consensus.4-4_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/consensus.4-4/storm.model.exact.umb --prop models/consensus.4-4/property.props --exact
Wallclock time: 4.293 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 02:56:55 2026
Command line arguments: --timemem --buildfull --explicit-umb models/consensus.4-4/storm.model.exact.umb --prop models/consensus.4-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.012s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.027s seconds.
Time for model construction: 0.109s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	43136
Transitions: 	144352
Choices: 	115840
Reward Models:  none
State Labels: 	4 labels
   * finished -> 64 item(s)
   * deadlock -> 0 item(s)
   * agree -> 9170 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "disagree": Pmax=? [F ("finished" & (!"agree"))] ...
Result (for initial states): 45666330762076479/292595849630842880 (approx. 0.156073064)
Time for model checking: 4.130s.

Performance statistics:
  * peak memory usage: 138MB
  * CPU time: 4.184s
  * wallclock time: 4.244s
```



### Log file: storm_from-umb_check_exact_consensus.4-4_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/consensus.4-4/storm.model.exact.umb --prop models/consensus.4-4/property.props --exact
Wallclock time: 3.943 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:06 2026
Command line arguments: --timemem --buildfull --explicit-umb models/consensus.4-4/storm.model.exact.umb --prop models/consensus.4-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.013s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.025s seconds.
Time for model construction: 0.101s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	43136
Transitions: 	144352
Choices: 	115840
Reward Models:  none
State Labels: 	4 labels
   * finished -> 64 item(s)
   * deadlock -> 0 item(s)
   * agree -> 9170 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "disagree": Pmax=? [F ("finished" & (!"agree"))] ...
Result (for initial states): 45666330762076479/292595849630842880 (approx. 0.156073064)
Time for model checking: 3.735s.

Performance statistics:
  * peak memory usage: 138MB
  * CPU time: 3.774s
  * wallclock time: 3.842s
```



### Log file: storm_from-umb_check_exact_consensus.4-4_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/consensus.4-4/storm.model.exact.umb --prop models/consensus.4-4/property.props --exact
Wallclock time: 4.384 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:03:31 2026
Command line arguments: --timemem --buildfull --explicit-umb models/consensus.4-4/storm.model.exact.umb --prop models/consensus.4-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.020s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.025s seconds.
Time for model construction: 0.116s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	43136
Transitions: 	144352
Choices: 	115840
Reward Models:  none
State Labels: 	4 labels
   * finished -> 64 item(s)
   * deadlock -> 0 item(s)
   * agree -> 9170 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "disagree": Pmax=? [F ("finished" & (!"agree"))] ...
Result (for initial states): 45666330762076479/292595849630842880 (approx. 0.156073064)
Time for model checking: 4.197s.

Performance statistics:
  * peak memory usage: 138MB
  * CPU time: 4.248s
  * wallclock time: 4.334s
```



### Log file: storm_from-umb_check_exact_consensus.4-4_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/consensus.4-4/storm.model.exact.umb --prop models/consensus.4-4/property.props --exact
Wallclock time: 3.871 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:11:45 2026
Command line arguments: --timemem --buildfull --explicit-umb models/consensus.4-4/storm.model.exact.umb --prop models/consensus.4-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.018s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.054s seconds.
Time for model construction: 0.134s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	43136
Transitions: 	144352
Choices: 	115840
Reward Models:  none
State Labels: 	4 labels
   * finished -> 64 item(s)
   * deadlock -> 0 item(s)
   * agree -> 9170 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "disagree": Pmax=? [F ("finished" & (!"agree"))] ...
Result (for initial states): 45666330762076479/292595849630842880 (approx. 0.156073064)
Time for model checking: 3.681s.

Performance statistics:
  * peak memory usage: 137MB
  * CPU time: 3.726s
  * wallclock time: 3.833s
```

