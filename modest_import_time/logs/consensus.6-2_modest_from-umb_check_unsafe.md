# Log files for modest_from-umb_check_unsafe on model [consensus.6-2](../../models/consensus.6-2)

Parsed values: `[0.7, TO, TO, TO, TO]`



### Log file: modest_from-umb_check_unsafe_consensus.6-2_rep1.log

```
Command(s):
../bin/modest mcsta models/consensus.6-2/modest.model.umb models/consensus.6-2/modest.umb.properties.txt --unsafe -D --exhaustive
Wallclock time: 17.874 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.6-2/modest.model.umb models/consensus.6-2/modest.umb.properties.txt --unsafe -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.

Peak memory usage: 188 MB
Analysis results for UMB

+ State space (UMB)
  States:            1258240
  Choices:           5008128
  Branches:          6236736
  Time (decompress): 0.1 s
  Time (validate):   0.0 s
  Time (load):       0.6 s

+ Property disagree
  Probability: 0.36362422496221386
  Bounds:      [0.36362422496221386, 1]
  Time:        17.2 s

  + Value iteration
    Final error: 9.857326206509403E-07
    Iterations:  736
    Time:        17.2 s

```



### Log file: modest_from-umb_check_unsafe_consensus.6-2_rep2.log

```
Command(s):
../bin/modest mcsta models/consensus.6-2/modest.model.umb models/consensus.6-2/modest.umb.properties.txt --unsafe -D --exhaustive
Wallclock time: 7200.016 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.6-2/modest.model.umb models/consensus.6-2/modest.umb.properties.txt --unsafe -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.

##############################Output to stderr##############################
Fatal error. System.AccessViolationException: Attempted to read or write protected memory. This is often an indication that other memory is corrupt.
   at Modest.ModelChecking.ValueIteration.PerformUnboundedValueIteration(Modest.ModelChecking.PropertyAnalysisTask, Partition, System.Nullable`1<UInt64>, Modest.Modularity.LocationErrorHandler, System.Threading.CancellationToken, Boolean, Int64 ByRef, Double ByRef, Boolean ByRef)
   at Modest.ModelChecking.ValueIteration.PerformPartitionUnboundedValueIteration(Modest.ModelChecking.PropertyAnalysisTask, Partition, Int64, UnboundedValueIterationPartitionData, System.String, Modest.Modularity.LocationErrorHandler, Modest.Modularity.OperationState)
   at Modest.ModelChecking.ValueIteration+<>c__DisplayClass7_0.<IterateUnbounded>g__FixpointStep|1(Int32, Int32, Modest.Modularity.OperationState)
   at Modest.StateSpace.Helpers.IteratePartitions(Modest.StateSpace.StateSpace, System.Action`2<Int32,Modest.Modularity.OperationState>, System.Func`4<Int32,Int32,Modest.Modularity.OperationState,Boolean>, System.Action`2<Int32,Modest.Modularity.OperationState>, Modest.Modularity.OperationState)
   at Modest.ModelChecking.ValueIteration.IterateUnbounded(Modest.ModelChecking.PropertyAnalysisTask, Modest.StateSpace.StateSpace, Modest.Modularity.AnalysisDataSet, System.String, Modest.Modularity.LocationErrorHandler, Modest.Modularity.OperationState)
```



### Log file: modest_from-umb_check_unsafe_consensus.6-2_rep3.log

```
Command(s):
../bin/modest mcsta models/consensus.6-2/modest.model.umb models/consensus.6-2/modest.umb.properties.txt --unsafe -D --exhaustive
Wallclock time: 7200.005 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.6-2/modest.model.umb models/consensus.6-2/modest.umb.properties.txt --unsafe -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.
```



### Log file: modest_from-umb_check_unsafe_consensus.6-2_rep4.log

```
Command(s):
../bin/modest mcsta models/consensus.6-2/modest.model.umb models/consensus.6-2/modest.umb.properties.txt --unsafe -D --exhaustive
Wallclock time: 7200.005 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.6-2/modest.model.umb models/consensus.6-2/modest.umb.properties.txt --unsafe -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.
```



### Log file: modest_from-umb_check_unsafe_consensus.6-2_rep5.log

```
Command(s):
../bin/modest mcsta models/consensus.6-2/modest.model.umb models/consensus.6-2/modest.umb.properties.txt --unsafe -D --exhaustive
Wallclock time: 7200.015 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.6-2/modest.model.umb models/consensus.6-2/modest.umb.properties.txt --unsafe -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.

##############################Output to stderr##############################
Fatal error. System.AccessViolationException: Attempted to read or write protected memory. This is often an indication that other memory is corrupt.
```

