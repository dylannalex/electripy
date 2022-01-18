# ElectriPy Physics :zap: 

This document explains the physics used for making ElectriPy, not its implementation with
Python. If you want to see how physics are implemented you can go to [electripy/physics](https://github.com/dylannalex/electripy/tree/master/electripy/physics) folder.

While following the logic and formulas mentioned below it is important to consider that all
charges are point charges (which means that their mass is negligible) and are at rest.

## :electric_plug: Electric force calculation:

### _Two point charges:_
Imagine we have a plane with two **point charges at rest**, q<sub>0</sub> and q<sub>1</sub>:

<p align="center">
  <img width="400" height="400" src="../media/two_point_charges_and_electric_force.png">
</p>

q<sub>0</sub> exerts an electric force F<sup>&#8407;</sup><sub>0</sub> on q<sub>1</sub>,
and q<sub>1</sub> exerts an electric force F<sup>&#8407;</sup><sub>1</sub> on q<sub>0</sub>.
These electric forces have the same magnitude but opposite direction. We can calculate the
electric forces' magnitude with Coulomb's law:  

<p align="center">
  <img width="323" height="115" src="../media/electric_force_between_two_point_charges.png">
</p>

Nevertheless, we need to find the electric forces vector, not only their magnitude. To
simplify our task we are going to analyze the electric force exerted only on q<sub>0</sub>,
which is F<sup>&#8407;</sup><sub>1</sub>. Since we now have one force, we will call it 
F<sup>&#8407;</sup>. In other words, F<sup>&#8407;</sup><sub>1</sub> = F<sup>&#8407;</sup>.

<p align="center">
  <img width="400" height="400" src="../media/two_point_charges_and_r_vector.png">
</p>

r&#8407; is a vector that goes from q<sub>0</sub> to q<sub>1</sub>. However is more useful to find
r&#770;, which has the same direction as r&#8407; but it is a unit vector. r&#770; can be easily
calculated by scaling r&#8407; by the inverse of its norm: r&#770; = r<sup>-1</sup> r&#8407;.
<br>
In this scenario, F<sup>&#8407;</sup> can be calculated as F r&#770;. This
is not always the case though. What would happen if q<sub>1</sub> was a positive charge?:

<p align="center">
  <img width="400" height="400" src="../media/two_point_charges_and_r_vector_2.png">
</p>

Here the electric force has changed, it is now calculated as F<sup>&#8407;</sup> = -F r&#770;.
As we see, the direction of F<sup>&#8407;</sup> does not only depend on q<sub>0</sub> and
q<sub>1</sub> magnitude but also on their sign. By analyzing some other examples we can deduce 
that F<sup>&#8407;</sup> is:

<p align="center">
  <img width="323" height="115" src="../media/electric_force_vector_two_point_charges.png">
</p>

### _Multiple point charges:_

Now let's imagine that we have three point charges:

<p align="center">
  <img width="400" height="400" src="../media/three_point_charges_and_electric_force.png">
</p>

If we look at q<sub>0</sub> we can observe that it suffers a force F<sup>&#8407;</sup><sub>1</sub>
exerted by q<sub>1</sub> and a force F<sup>&#8407;</sup><sub>2</sub> exerted by q<sub>2</sub>. The
net force exerted on q<sub>0</sub> is F<sup>&#8407;</sup>, which is the sum of F<sup>&#8407;</sup><sub>1</sub>
and F<sup>&#8407;</sup><sub>2</sub>. This is called the Principle of Superposition and it is fulfilled
for any charge distribution.
<br><br>
Given a distribution of **n** charges {q<sub>0</sub>, q<sub>1</sub>, ..., q<sub>n</sub>}, the electric
force exerted on q<sub>0</sub> is F<sup>&#8407;</sup> and can be calculated as:

<p align="center">
  <img width="244" height="126" src="../media/electric_force_vector_n_point_charges_1.png">
</p>

After replacing F<sup>&#8407;</sup><sub>i</sub> by its value:

<p align="center">
  <img width="493" height="140" src="../media/electric_force_vector_n_point_charges_2.png">
</p>

We can optimize this by taking the constants values outside of the summatory:

<p align="center">
  <img width="493" height="140" src="../media/electric_force_vector_n_point_charges_3.png">
</p>

We have arrived to a formula for calculating the electric net force of a given charge on an electric
field distribution.


## :electric_plug: Electric field calculation:

The electric field is defined mathematically as a vector field that associates to each point in space
the force per unit of charge exerted on an infinitesimal positive test charge at rest at that point.
<br><br>
Given a test charge q<sub>0</sub> at a point **P(x, y)** and a charge distribution {q<sub>1</sub>,
q<sub>2</sub>, ...,q<sub>n</sub>}, we can calculate the electric field at **P** position as:

<p align="center">
  <img width="228" height="199" src="../media/electric_field_vector_n_point_charges_1.png">
</p>

Where E<sup>&#8407;</sup> is the electric field vector at q<sub>0</sub> position (**P**), and
F<sup>&#8407;</sup> is the electric force exerted on q<sub>0</sub> by the charge distribution. If we
replace F<sup>&#8407;</sup> by its value we get the formula to calculate the electric field at any
point:

<p align="center">
  <img width="515" height="175" src="../media/electric_field_vector_n_point_charges_2.png">
</p>

Where r<sub>i</sub> is the distance from the point **P** to the charge q<sub>i</sub> and r&#770;<sub>i</sub>
is the unit vector with the same direction as r&#8407;<sub>i</sub>, the vector that goes from **P** to
the charge q<sub>i</sub>.
