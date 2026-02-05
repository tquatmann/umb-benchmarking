# Log files

Tool configuration: storm_from-umb-gz_check_exact
Benchmark: [consensus.4-4](../../models/consensus.4-4)
Parsed values: [4.108, 4.782, 4.04, 3.936, 3.803]



### Log file: storm_from-umb-gz_check_exact_consensus.4-4_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/consensus.4-4/storm.model.exact.umb.gz --prop models/consensus.4-4/property.props --exact
Wallclock time: 4.108 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:55:09 2026
Command line arguments: --timemem --buildfull --explicit-umb models/consensus.4-4/storm.model.exact.umb.gz --prop models/consensus.4-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.020s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.026s seconds.
Time for model construction: 0.108s.

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
Time for model checking: 3.633s.

Performance statistics:
  * peak memory usage: 138MB
  * CPU time: 3.674s
  * wallclock time: 3.781s
```



### Log file: storm_from-umb-gz_check_exact_consensus.4-4_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/consensus.4-4/storm.model.exact.umb.gz --prop models/consensus.4-4/property.props --exact
Wallclock time: 4.782 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:23:25 2026
Command line arguments: --timemem --buildfull --explicit-umb models/consensus.4-4/storm.model.exact.umb.gz --prop models/consensus.4-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.011s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.033s seconds.
Time for model construction: 0.119s.

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
Time for model checking: 4.580s.

Performance statistics:
  * peak memory usage: 137MB
  * CPU time: 4.626s
  * wallclock time: 4.704s
```



### Log file: storm_from-umb-gz_check_exact_consensus.4-4_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/consensus.4-4/storm.model.exact.umb.gz --prop models/consensus.4-4/property.props --exact
Wallclock time: 4.040 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 02:56:24 2026
Command line arguments: --timemem --buildfull --explicit-umb models/consensus.4-4/storm.model.exact.umb.gz --prop models/consensus.4-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.012s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.025s seconds.
Time for model construction: 0.100s.

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
Time for model checking: 3.660s.

Performance statistics:
  * peak memory usage: 137MB
  * CPU time: 3.696s
  * wallclock time: 3.781s
```



### Log file: storm_from-umb-gz_check_exact_consensus.4-4_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/consensus.4-4/storm.model.exact.umb.gz --prop models/consensus.4-4/property.props --exact
Wallclock time: 3.936 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:25 2026
Command line arguments: --timemem --buildfull --explicit-umb models/consensus.4-4/storm.model.exact.umb.gz --prop models/consensus.4-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.015s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.028s seconds.
Time for model construction: 0.107s.

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
Time for model checking: 3.733s.

Performance statistics:
  * peak memory usage: 138MB
  * CPU time: 3.767s
  * wallclock time: 3.848s
```



### Log file: storm_from-umb-gz_check_exact_consensus.4-4_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/consensus.4-4/storm.model.exact.umb.gz --prop models/consensus.4-4/property.props --exact
Wallclock time: 3.803 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:25:39 2026
Command line arguments: --timemem --buildfull --explicit-umb models/consensus.4-4/storm.model.exact.umb.gz --prop models/consensus.4-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.013s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.024s seconds.
Time for model construction: 0.099s.

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
Time for model checking: 3.656s.

Performance statistics:
  * peak memory usage: 138MB
  * CPU time: 3.701s
  * wallclock time: 3.760s
```

