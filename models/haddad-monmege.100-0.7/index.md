 # haddad-monmege.100-0.7
       
##### Download
[model.prism](model.prism) [property.props](property.props) [model.jani](model.jani)

##### Origin

Taken from [QVBS](https://qcomp.org/benchmarks/#haddad-monmege) (January 2026).
The provided parameter instantiation and property have been considered in QComp 2019 and QComp 2020.

Original Prism model and property files have been adapted for compatibility and simplicity:
- Constants: All open constants are now explicitly set within model.prism (no need to set them via command line)
- Properties: The properties only refer to labels and rewards as defined in the model.prism file. No variables or constants are used in the property.
- Formulas: some PRISM formula declarations have been renamed so that their identify does not crash with a label.


##### model.prism

```
// Toy example on which standard value iteration yields wrong results
// This model originates from Haddad, Monmege: Reachability in MDPs: Refining Convergence of Value Iteration

dtmc

const int N=100;
const double p=0.7;
const double q = 0.5;

module main
	x : [0..2*N] init N;
	[] x=N -> p : (x'=N-1) + (1-p) : (x'=N+1);
	[] x>0 & x<N -> q : (x'=x-1) + (1-q) : (x'=N);
	[] x>N & x<2*N -> q : (x'=x+1) + (1-q) : (x'=N);
	[] x=0 | x=2*N -> 1 : true;
endmodule

label "Target" = x=0;

``` 

##### property.props

```
// Probability to reach the target state
"target": P=? [F "Target"];

```
