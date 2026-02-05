# Log files for modest_from-umb_check_unsafe-memory on model [pacman.100](../../models/pacman.100)

Parsed values: `[TO, TO, TO, TO, TO]`



### Log file: modest_from-umb_check_unsafe-memory_pacman.100_rep1.log

```
Command(s):
../bin/modest mcsta models/pacman.100/modest.model.umb models/pacman.100/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.008 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.100/modest.model.umb models/pacman.100/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.
```



### Log file: modest_from-umb_check_unsafe-memory_pacman.100_rep2.log

```
Command(s):
../bin/modest mcsta models/pacman.100/modest.model.umb models/pacman.100/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.008 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.100/modest.model.umb models/pacman.100/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.

##############################Output to stderr##############################
Fatal error. System.AccessViolationException: Attempted to read or write protected memory. This is often an indication that other memory is corrupt.
   at Modest.ModelChecking.ValueIteration.PerformUnboundedValueIteration(Modest.ModelChecking.PropertyAnalysisTask, Partition, System.Nullable`1<UInt64>, Modest.Modularity.LocationErrorHandler, System.Threading.CancellationToken, Boolean, Int64 ByRef, Double ByRef, Boolean ByRef)
   at Modest.ModelChecking.ValueIteration.PerformPartitionUnboundedValueIteration(Modest.ModelChecking.PropertyAnalysisTask, Partition, Int64, UnboundedValueIterationPartitionData, System.String, Modest.Modularity.LocationErrorHandler, Modest.Modularity.OperationState)
```



### Log file: modest_from-umb_check_unsafe-memory_pacman.100_rep3.log

```
Command(s):
../bin/modest mcsta models/pacman.100/modest.model.umb models/pacman.100/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.013 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.100/modest.model.umb models/pacman.100/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.

##############################Output to stderr##############################
Fatal error. System.AccessViolationException: Attempted to read or write protected memory. This is often an indication that other memory is corrupt.
   at Modest.ModelChecking.ValueIteration.PerformUnboundedValueIteration(Modest.ModelChecking.PropertyAnalysisTask, Partition, System.Nullable`1<UInt64>, Modest.Modularity.LocationErrorHandler, System.Threading.CancellationToken, Boolean, Int64 ByRef, Double ByRef, Boolean ByRef)
   at Modest.ModelChecking.ValueIteration.PerformPartitionUnboundedValueIteration(Modest.ModelChecking.PropertyAnalysisTask, Partition, Int64, UnboundedValueIterationPartitionData, System.String, Modest.Modularity.LocationErrorHandler, Modest.Modularity.OperationState)
   at Modest.ModelChecking.ValueIteration+<>c__DisplayClass7_0.<IterateUnbounded>g__FixpointStep|1(Int32, Int32, Modest.Modularity.OperationState)
   at Modest.StateSpace.Helpers.IteratePartitions(Modest.StateSpace.StateSpace, System.Action`2<Int32,Modest.Modularity.OperationState>, System.Func`4<Int32,Int32,Modest.Modularity.OperationState,Boolean>, System.Action`2<Int32,Modest.Modularity.OperationState>, Modest.Modularity.OperationState)
   at Modest.ModelChecking.ValueIteration.IterateUnbounded(Modest.ModelChecking.PropertyAnalysisTask, Modest.StateSpace.StateSpace, Modest.Modularity.AnalysisDataSet, System.String, Modest.Modularity.LocationErrorHandler, Modest.Modularity.OperationState)
   at Modest.ModelChecking.MAModelChecker`1[[Modest.StateSpace.UnifiedBinaryFormat+UmbState, Modest.StateSpace, Version=3.1.0.0, Culture=neutral, PublicKeyToken=null]].CheckProperty(Modest.StateSpace.StateSpace, Modest.ModelChecking.ReachabilityPropertyInfo, System.String, System.String, Modest.StateSpace.StateSet`1<UmbState>, System.IDisposable ByRef, System.Func`3<Boolean,Boolean,Boolean>, System.String, Modest.Modularity.AnalysisDataSet, Modest.Modularity.OperationState, Modest.Modularity.ComponentErrorHandler)
   at Modest.ModelChecking.MAModelChecker`1[[Modest.StateSpace.UnifiedBinaryFormat+UmbState, Modest.StateSpace, Version=3.1.0.0, Culture=neutral, PublicKeyToken=null]].CheckProperties(Modest.StateSpace.StateSpace, Modest.StateSpace.StateSet`1<UmbState>, Boolean[], System.String, Modest.Modularity.OperationState, Modest.Modularity.ComponentErrorHandler)
   at Modest.ModelChecking.MAModelChecker`1[[Modest.StateSpace.UnifiedBinaryFormat+UmbState, Modest.StateSpace, Version=3.1.0.0, Culture=neutral, PublicKeyToken=null]].ModelCheck(System.String, Modest.Modularity.OperationState, Modest.Modularity.ComponentErrorHandler)
```



### Log file: modest_from-umb_check_unsafe-memory_pacman.100_rep4.log

```
Command(s):
../bin/modest mcsta models/pacman.100/modest.model.umb models/pacman.100/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.028 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.100/modest.model.umb models/pacman.100/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.
```



### Log file: modest_from-umb_check_unsafe-memory_pacman.100_rep5.log

```
Command(s):
../bin/modest mcsta models/pacman.100/modest.model.umb models/pacman.100/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive
Wallclock time: 7200.009 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.100/modest.model.umb models/pacman.100/modest.umb.properties.txt --unsafe -S Memory -D --exhaustive




UMB: warning: Skipping UMB file validation as requested. This is a security vulnerability when used with UMB files from untrusted sources.

##############################Output to stderr##############################
Fatal error. System.AccessViolationException: Attempted to read or write protected memory. This is often an indication that other memory is corrupt.
```

