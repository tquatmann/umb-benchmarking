# Log files

Tool configuration: modest_from-umb_check_unsafe-memory
Benchmark: [eajs.5-250-11](../../models/eajs.5-250-11)
Parsed values: [1.609, TO, TO, TO, TO]



### Log file: modest_from-umb_check_unsafe-memory_eajs.5-250-11_rep1.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/modest.model.umb models/eajs.5-250-11/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 1.609 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/modest.model.umb models/eajs.5-250-11/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.

Peak memory usage: 274 MB
Analysis results for UMB

+ State space (UMB)
  States:            3049471
  Choices:           4256193
  Branches:          6977654
  Time (decompress): 0.1 s
  Time (validate):   0.0 s
  Time (load):       0.5 s

+ Property ExpUtil
  Value:  10.032940688434891
  Bounds: [10.032940688434891, infinity)
  Time:   1.0 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.3 s
    Min. prob. 1 states:          3049471
    Time for min. prob. 1 states: 0.0 s

  + Value iteration
    Final error: 4.466131883374015E-08
    Iterations:  22
    Time:        0.7 s

```



### Log file: modest_from-umb_check_unsafe-memory_eajs.5-250-11_rep2.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/modest.model.umb models/eajs.5-250-11/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.037 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/modest.model.umb models/eajs.5-250-11/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.
```



### Log file: modest_from-umb_check_unsafe-memory_eajs.5-250-11_rep3.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/modest.model.umb models/eajs.5-250-11/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.028 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/modest.model.umb models/eajs.5-250-11/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.

##############################Output to stderr##############################
Fatal error. System.AccessViolationException: Attempted to read or write protected memory. This is often an indication that other memory is corrupt.
   at Modest.ModelChecking.ValueIteration.PerformUnboundedValueIteration(Modest.ModelChecking.PropertyAnalysisTask, Partition, System.Nullable`1<UInt64>, Modest.Modularity.LocationErrorHandler, System.Threading.CancellationToken, Boolean, Int64 ByRef, Double ByRef, Boolean ByRef)
   at Modest.ModelChecking.ValueIteration.PerformPartitionUnboundedValueIteration(Modest.ModelChecking.PropertyAnalysisTask, Partition, Int64, UnboundedValueIterationPartitionData, System.String, Modest.Modularity.LocationErrorHandler, Modest.Modularity.OperationState)
   at Modest.ModelChecking.ValueIteration+<>c__DisplayClass7_0.<IterateUnbounded>g__FixpointStep|1(Int32, Int32, Modest.Modularity.OperationState)
   at Modest.StateSpace.Helpers.IteratePartitions(Modest.StateSpace.StateSpace, System.Action`2<Int32,Modest.Modularity.OperationState>, System.Func`4<Int32,Int32,Modest.Modularity.OperationState,Boolean>, System.Action`2<Int32,Modest.Modularity.OperationState>, Modest.Modularity.OperationState)
   at Modest.ModelChecking.ValueIteration.IterateUnbounded(Modest.ModelChecking.PropertyAnalysisTask, Modest.StateSpace.StateSpace, Modest.Modularity.AnalysisDataSet, System.String, Modest.Modularity.LocationErrorHandler, Modest.Modularity.OperationState)
```



### Log file: modest_from-umb_check_unsafe-memory_eajs.5-250-11_rep4.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/modest.model.umb models/eajs.5-250-11/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.008 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/modest.model.umb models/eajs.5-250-11/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.
```



### Log file: modest_from-umb_check_unsafe-memory_eajs.5-250-11_rep5.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/modest.model.umb models/eajs.5-250-11/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.015 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/modest.model.umb models/eajs.5-250-11/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.
```

