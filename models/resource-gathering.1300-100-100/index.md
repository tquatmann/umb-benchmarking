# resource-gathering.1300-100-100
       
##### Download
[model.prism](model.prism) [property.props](property.props) [model.jani](model.jani)

##### Origin

Taken from [QVBS](https://qcomp.org/benchmarks/#resource-gathering) (January 2026).
The provided parameter instantiation and property have been considered in QComp 2019 and QComp 2020.

Original Prism model and property files have been adapted for compatibility and simplicity:
- Constants: All open constants are now explicitly set within model.prism (no need to set them via command line)
- Properties: The properties only refer to labels and rewards as defined in the model.prism file. No variables or constants are used in the property.
- Formulas: some PRISM formula declarations have been renamed so that their identify does not crash with a label.


##### model.prism

```
mdp

const int WIDTH = 5;
const int HEIGHT = 5;
const int XINIT = 3;
const int YINIT = 1;

const int GOLD_TO_COLLECT=100; // Set to 0 to avoid unfolding
const int GEM_TO_COLLECT=100; // Set to 0 to avoid unfolding
const int B=1300;

const double pAttack = 1/10;

formula left_of_gold = x=2 & y=5;
formula right_of_gold = x=4 & y=5;
formula below_of_gold = (x=3 & y=4);
formula above_of_gold = false;
formula left_of_gem = (x=4 & y=4);
formula right_of_gem = false;
formula below_of_gem = (x=5 & y=3);
formula above_of_gem = (x=5 & y=5);
formula left_of_home = x=2 & y=1;
formula right_of_home = x=4 & y=1;
formula above_of_home = x=3 & y=2;
formula below_of_home = false;
formula left_of_enemy = (x=3 & y=5) | (x=2 & y=4);
formula right_of_enemy = (x=5 & y=5) | (x=4 & y=4);
formula above_of_enemy = x=3 & y=5;
formula below_of_enemy = (x=3 & y=3) | (x=4 & y=4);

module robot

	gold : bool init false;
	gem : bool init false;
	attacked : bool init false;

	x : [1..WIDTH] init XINIT;
	y : [1..HEIGHT] init YINIT;

	[right] !left_of_enemy & x<WIDTH ->  (attacked'=false) & (x'=x+1) & (gold' = (gold & !left_of_home) | left_of_gold)   &  (gem' =  (gem & !left_of_home) | left_of_gem);
	[left] !right_of_enemy & x>1 ->      (attacked'=false) & (x'=x-1) & (gold' = (gold & !right_of_home) | right_of_gold) & (gem' =  (gem & !right_of_home) | right_of_gem);
	[top] !below_of_enemy & y<HEIGHT ->  (attacked'=false) & (y'=y+1) & (gold' = (gold & !below_of_home) | below_of_gold) & (gem' =  (gem & !below_of_home) | below_of_gem);
	[down] !above_of_enemy & y>1 ->      (attacked'=false) & (y'=y-1) & (gold' = (gold & !above_of_home) | above_of_gold) & (gem' =  (gem & !above_of_home) | above_of_gem);

	[right] left_of_enemy & x<WIDTH -> pAttack : (attacked'=true) & (x'=XINIT) & (y'=YINIT) & (gold'=false) & (gem'=false) + (1-pAttack) : (attacked'=false) & (x'=x+1) & (gold' = (gold & !left_of_home) | left_of_gold) & (gem' =  (gem & !left_of_home) | left_of_gem);
	[left] right_of_enemy & x>1 ->     pAttack : (attacked'=true) & (x'=XINIT) & (y'=YINIT) & (gold'=false) & (gem'=false) + (1-pAttack) : (attacked'=false) & (x'=x-1) & (gold' = (gold & !right_of_home) | right_of_gold) & (gem' =  (gem & !right_of_home) | right_of_gem);
	[top] below_of_enemy & y<HEIGHT -> pAttack : (attacked'=true) & (x'=XINIT) & (y'=YINIT) & (gold'=false) & (gem'=false) + (1-pAttack) : (attacked'=false) & (y'=y+1) & (gold' = (gold & !below_of_home) | below_of_gold) & (gem' =  (gem & !below_of_home) | below_of_gem);
	[down] above_of_enemy & y>1 ->     pAttack : (attacked'=true) & (x'=XINIT) & (y'=YINIT) & (gold'=false) & (gem'=false) + (1-pAttack) : (attacked'=false) & (y'=y-1) & (gold' = (gold & !above_of_home) | above_of_gold) & (gem' =  (gem & !above_of_home) | above_of_gem);
endmodule

module goldcounter

	required_gold : [0..GOLD_TO_COLLECT] init GOLD_TO_COLLECT;
	
	[right] true -> (required_gold'=max(0, required_gold - (left_of_home & gold  ? 1: 0)));
	[left] true -> (required_gold'=max(0, required_gold - (right_of_home & gold ? 1 : 0)));
	[top] true -> (required_gold'=max(0, required_gold - (below_of_home & gold ? 1 : 0)));
	[down] true -> (required_gold'=max(0, required_gold - (above_of_home & gold ? 1 : 0)));
endmodule

module gemcounter

	required_gem : [0..GEM_TO_COLLECT] init GEM_TO_COLLECT;

	[right] true -> (required_gem'=max(0, required_gem - (left_of_home & gem  ? 1: 0)));
	[left] true -> (required_gem'=max(0, required_gem - (right_of_home & gem ? 1 : 0)));
	[top] true -> (required_gem'=max(0, required_gem - (below_of_home & gem ? 1 : 0)));
	[down] true -> (required_gem'=max(0, required_gem - (above_of_home & gem ? 1 : 0)));
endmodule

label "success" = required_gold=0 & required_gem=0;

``` 

##### property.props

```
"prgoldgem": Pmax=? [F<=1300 "success"];

```
