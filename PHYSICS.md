# ElectriPy Physics :zap: 

This document explains the physics used for making ElectriPy, not its implementation with
Python. If you want to see how physics are implemented you can go to [electripy/physics](https://github.com/dylannalex/electripy/tree/master/electripy/physics) folder.

While following the logic and formulas mentioned below it is important to consider that all
charges are point charges (which means that their mass is negligible) and are at rest.

## :electric_plug: Electric force calculation:

### _Two point charges:_
Imagine we have a plane with two **point charges at rest**, $q_0$ and $q_1$:

<p align="center">
  <img width="400" height="400" src="../media/two_point_charges_and_electric_force.png">
</p>

$q_0$ exerts an electric force $\vec{\textbf{F}}_0$ on $q_1$,
and $q_1$ exerts an electric force $\vec{\textbf{F}}_1$ on $q_0$.
These electric forces have the same magnitude but opposite direction. We can calculate the
electric forces' magnitude with Coulomb's law:
$$F = \frac{1}{4\pi\varepsilon_0}\frac{\|q_0q_1\|}{r^2}$$

<!--
<p align="center">
  <img width="323" height="115" src="../media/electric_force_between_two_point_charges.png">
</p>
-->

Nevertheless, we need to find the electric forces vector, not only their magnitude. To
simplify our task we are going to analyze the electric force exerted only on $q_0$,
which is $\vec{\textbf{F}}_1$. Since we now have one force, we will call it 
$\vec{\textbf{F}}$. In other words, $\vec{\textbf{F}}_1$ = $\vec{\textbf{F}}$.

<p align="center">
  <img width="400" height="400" src="../media/two_point_charges_and_r_vector.png">
</p>

$\vec{\textbf{r}}$ is a vector that goes from $q_0$ to $q_1$. However is more useful to find
$\hat{\textbf{r}}$, which has the same direction as $\vec{\textbf{r}}$ but it is a unit vector. $\hat{\textbf{r}}$ can be easily
calculated by scaling $\vec{\textbf{r}}$ by the inverse of its norm: $$\hat{\textbf{r}}=\frac{\vec{\textbf{r}}}{\|\vec{\text{r}}\|}$$
<br>
In this scenario, $\vec{\textbf{F}}$ can be calculated as $F\hat{\textbf{r}}$. This
is not always the case though. What would happen if $q_1$ was a positive charge?:

<p align="center">
  <img width="400" height="400" src="../media/two_point_charges_and_r_vector_2.png">
</p>

Here the electric force has changed, it is now calculated as $\vec{\textbf{F}}=-F\hat{\textbf{r}}$.
As we see, the direction of $\vec{\textbf{F}}$ does not only depend on $q_0$ and
$q_1$ magnitude but also on their sign. By analyzing some other examples we can deduce 
that $\vec{\textbf{F}}$ is:
$$\vec{\textbf{F}}=-\frac{1}{4\pi\varepsilon_0}\frac{q_0q_1}{r^2}\hat{\textbf{r}}$$

<!--
<p align="center">
  <img width="323" height="115" src="../media/electric_force_vector_two_point_charges.png">
</p>
-->

### _Multiple point charges:_

Now let's imagine that we have three point charges:

<p align="center">
  <img width="400" height="400" src="../media/three_point_charges_and_electric_force.png">
</p>

If we look at $q_0$ we can observe that it suffers a force $\vec{\textbf{F}}_1$
exerted by $q_1$ and a force $\vec{\textbf{F}}_2$ exerted by $q_2$. The
net force exerted on $q_0$ is $\vec{\textbf{F}}$, which is the sum of $\vec{\textbf{F}}_1$
and $\vec{\textbf{F}}_2$. This is called the Principle of Superposition and it is fulfilled
for any charge distribution.
<br><br>
Given a distribution of **n** charges $\\{q_0,q_1,\ldots,q_n\\}$, the electric
force exerted on $q_0$ is $\vec{\textbf{F}}$ and can be calculated as:

$$\vec{\textbf{F}}=\sum_i\vec{\textbf{F}}_i$$

<!--
<p align="center">
  <img width="244" height="126" src="../media/electric_force_vector_n_point_charges_1.png">
</p>
-->

After replacing $\vec{\textbf{F}}_i$ by its value:
$$\vec{\textbf{F}}=\sum_i-\frac{1}{4\pi\varepsilon_0}\frac{q_0q_i}{r_i^2}\hat{\textbf{r}}_i$$

<!--
<p align="center">
  <img width="493" height="140" src="../media/electric_force_vector_n_point_charges_2.png">
</p>
-->

We can optimize this by taking the constants values outside of the summatory:
$$\vec{\textbf{F}}=-\frac{1}{4\pi\varepsilon_0}\sum_i\frac{q_0q_i}{r_i^2}\hat{\textbf{r}}_i$$

<!--
<p align="center">
  <img width="493" height="140" src="../media/electric_force_vector_n_point_charges_3.png">
</p>
-->

We have arrived to a formula for calculating the electric net force of a given charge on an electric
field distribution.


## :electric_plug: Electric field calculation:

The electric field is defined mathematically as a vector field that associates to each point in space
the force per unit of charge exerted on an infinitesimal positive test charge at rest at that point.
<br><br>
Given a test charge $q_0$ at a point $P(x,y)$ and a charge distribution $\\{q_1,q_2,\ldots,q_n\\}$, we can calculate the electric field at $P$ position as:

$$\vec{\textbf{E}}=\frac{\vec{\textbf{F}}}{q_0}$$

<!--
<p align="center">
  <img width="228" height="199" src="../media/electric_field_vector_n_point_charges_1.png">
</p>
-->

Where $\vec{\textbf{E}}$ is the electric field vector at position $P$, and
$\vec{\textbf{F}}$ is the electric force exerted on $q_0$ by the charge distribution. If we
replace $\vec{\textbf{F}}$ by its value we get the formula to calculate the electric field at any
point:
$$\vec{\textbf{E}}=-\frac{1}{4\pi\varepsilon_0}\sum_i\frac{q_i}{r_i^2}\hat{\textbf{r}}_i$$

<!--
<p align="center">
  <img width="515" height="175" src="../media/electric_field_vector_n_point_charges_2.png">
</p>
-->

Where $r_i$ is the distance from the point $P$ to the charge $q_i$ and $\hat{\textbf{r}}_i$
is the unit vector with the same direction as $\vec{\textbf{r}}_i$, the vector that goes from $P$ to
the charge $q_i$.
