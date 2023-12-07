# Natural-Pattern-Adaptation-CA
Research on Natural Pattern Adaptation using Cellular Automata Model: A repository for the final project in our MathBio class, exploring the dynamics of natural pattern adaptation through the lens of a cellular automata model. Contains code, documentation, and resources related to the project.


# Cellular Automata Approaches to Biological Modeling: Extensions to biological pattern adaptation

# Presented by Yogesh Phalak and Jonathan Zelaya

![](img/Cellular%20Automata%2020.png)

# Last time…

Reaction\-diffusion kinetics

Coupled set of ODEs

Activation parameter

Threshold parameter

![](img/Cellular%20Automata%2021.gif)

![](img/Cellular%20Automata%2022.png)

![](img/Cellular%20Automata%2023.png)

# Cellular Automata

Reduced\-order model

Discrete Lattices

Simple rules for lattice state point value

__e\.g\. Conway's Game of Life__

![](img/Cellular%20Automata%2024.png)

![](img/Cellular%20Automata%2025.gif)

__Source: Wikipedia__

# Deterministic Automata

![](img/Cellular%20Automata%2026.gif)

![](img/Cellular%20Automata%2027.gif)

Population

Immunology

Developmental\*

![](img/Cellular%20Automata%2028.png)

__Reproduced Results__

__Spiral wave pair \(100 x 100 grid\) __

__Autumn colormap \{0 \- 5\}__

__The Belousov\-__  __Zhabotinsky__  __ \(BZ\) reaction__

![](img/Cellular%20Automata%2029.png)

# Population Biology | parasites

![](img/Cellular%20Automata%20210.gif)

![](img/Cellular%20Automata%20211.gif)

__Host\-parasite model__

9 state model

0 \- empty cell

1 \- mature host

\(2\-3\) \- dying host

5 \- mature parasite

\(6\-8\) \- dying parasite

__Reproduced Results__

![](img/Cellular%20Automata%20212.png)

__Host\-Parasite Automata \(300 x 300 grid\)  Hot colormap \{A \- I\}__

![](img/Cellular%20Automata%20213.png)

# Population Biology | sharks and minnows gets mathy

![](img/Cellular%20Automata%20214.gif)

__Predator\-prey model__

8 state model

0 \- empty cell

1 \- prey

\(2\-6\) stages of shark development

7 \- reproducing shark

Oscillatory behavior

![](img/Cellular%20Automata%20215.png)

![](img/Cellular%20Automata%20216.png)

__Reproduced Results__

![](img/Cellular%20Automata%20217.png)

# Immunology

![](img/Cellular%20Automata%20218.png)

__Shape\-space simulations of the immune system__

Shape \- \{Binding properties of antigens\, antibodies\, receptors\}

16\-state model of ‘B\-cells’

Complementary cell interaction

![](img/Cellular%20Automata%20219.png)

![](img/Cellular%20Automata%20220.png)

__Reproduced Result__

![](img/Cellular%20Automata%20221.png)

![](img/Cellular%20Automata%20222.png)

# Developmental* | Animal Coat Patterns

Young’s Model

2 state model \(0\,1\)

Lateral inhibition

Threshold \- Weight Matrix\, Heaviside function

![](img/Cellular%20Automata%20223.png)

![](img/Cellular%20Automata%20224.png)

![](img/Cellular%20Automata%20225.png)

![](img/Cellular%20Automata%20226.png)

![](img/Cellular%20Automata%20227.png)

# Paper’s result

50 x 50 grid\, 0 \- white\, 1 \- black

![](img/Cellular%20Automata%20228.png)

![](img/Cellular%20Automata%20229.png)

![](img/Cellular%20Automata%20230.png)

![](img/Cellular%20Automata%20231.png)

![](img/Cellular%20Automata%20232.png)

# Our results

![](img/Cellular%20Automata%20233.png)

![](img/Cellular%20Automata%20234.png)

![](img/Cellular%20Automata%20235.png)

![](img/Cellular%20Automata%20236.png)

![](img/Cellular%20Automata%20237.png)

# Extension | Pattern Adaptation

![](img/Cellular%20Automata%20238.png)

__Key Observations: __

Young's Cellular automata algorithm generates infinite patterns based on diverse parameters and initial conditions\.

Distinct but visually similar patterns emerge with varied initial conditions\, characterized by a fixed weight function \(Wij\)\.

__Weight tensor in Young's Model__

![](img/Cellular%20Automata%20239.gif)

__Reinterpretation of the Young's CA as a convolution with a weight tensor\, is analogous to a kernel in image processing\.__

__Is it possible to derive this weight tensor from the patterns observed in nature?__

__Source: Towards Data Science__

# Methodology

![](img/Cellular%20Automata%20240.jpg)

![](img/Cellular%20Automata%20241.jpg)

![](img/Cellular%20Automata%20242.jpg)

![](img/Cellular%20Automata%20243.jpg)

![](img/Cellular%20Automata%20244.jpg)

![](img/Cellular%20Automata%20245.png)

![](img/Cellular%20Automata%20246.gif)

# Free indices parameter

![](img/Cellular%20Automata%20247.png)

![](img/Cellular%20Automata%20248.png)

# Results | Zebra

![](img/Cellular%20Automata%20249.jpg)

![](img/Cellular%20Automata%20250.jpg)

![](img/Cellular%20Automata%20251.jpg)

![](img/Cellular%20Automata%20252.jpg)

![](img/Cellular%20Automata%20253.jpg)

__Weight tensor for Zebra Pattern__

# Results | Leopard

![](img/Cellular%20Automata%20254.jpg)

![](img/Cellular%20Automata%20255.jpg)

![](img/Cellular%20Automata%20256.jpg)

Results | Leopard

![](img/Cellular%20Automata%20257.png)

![](img/Cellular%20Automata%20258.png)

__Weight tensor for Leopard Pattern__

# Results | Tiger

![](img/Cellular%20Automata%20259.jpg)

![](img/Cellular%20Automata%20260.jpg)

![](img/Cellular%20Automata%20261.jpg)

![](img/Cellular%20Automata%20262.jpg)

![](img/Cellular%20Automata%20263.png)

__Weight tensor in Tiger Pattern__

# Radial function parameter

![](img/Cellular%20Automata%20264.png)

![](img/Cellular%20Automata%20265.png)

![](img/Cellular%20Automata%20266.png)

![](img/Cellular%20Automata%20267.png)

![](img/Cellular%20Automata%20268.png)

![](img/Cellular%20Automata%20269.png)

__Radially symmetric Weight tensors __

Results | Fingerprint like patterns

![](img/Cellular%20Automata%20270.png)

![](img/Cellular%20Automata%20271.png)

![](img/Cellular%20Automata%20272.png)

![](img/Cellular%20Automata%20273.png)

![](img/Cellular%20Automata%20274.jpg)

# Future Directions

__Explaining Coat Patterns in an Evolutionary Perspective__

__Exploring Dynamic Pattern Adaptation__

__Compressing Large Datasets of Biological Systems__

![](img/Cellular%20Automata%20275.gif)

__source: worldpress\.com__

<span style="color:#FFFFFF"> __source: deepoceannews\.com__ </span>

![](img/Cellular%20Automata%20276.jpg)

![](img/Cellular%20Automata%20277.gif)

![](img/Cellular%20Automata%20278.png)

__source: __  __GeeksforGeeks__

__source: Saponara et\. Al\. 2021__

![](img/Cellular%20Automata%20279.png)

# Thank You !Questions ?

