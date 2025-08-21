# Modelling Belief Dynamics and Misinformation Spread in Social Networks

## Project Overview
This repository encapsulates modelling on the evolution of group beliefs over time, focusing on the impact of interventions such as "Correction Boosts." Utilising agent-based modelling and network science, the project simulates belief propagation within social networks, offering insights into how interventions can influence collective belief systems.

## Objectives
* Modelling Belief Dynamics: Develop agent-based models to simulate belief formation and evolution within groups.
* Intervention Analysis: Assess the effectiveness of various interventions, including misinformation correction strategies on altering group beliefs.
* Visualisation: Create dynamic visualisations to illustrate belief changes and intervention impacts over time.

## Methodology
* Agent-Based Modelling: Implemented using Python and NetworkX to simulate interactions and belief updates among agents within a network.
* Intervention Strategies: Introduced "Correction Boosts" at specific time steps to evaluate their influence on belief trajectories.
* Data Visualisation: Employed Matplotlib and Seaborn to generate heatmaps and line plots, visualising belief distributions and the effects of interventions.

## Visualisation
The average beliefs of female and male agents are plotted over time using matplotlib. A plot highlighting corrective actions to address misinformation is saved at each timestep, creating a sequence of images that are compiled into an animated GIF to illustrate the evolving social dynamics.

## Mathematical Foundations of the Belief Dynamics Model
This simulation models how individual beliefs evolve through social influence, trust and misinformation using a formal mathematical framework.

<ins>Belief Update Rule</ins>

<img src="https://github.com/ihe-k/Beliefs/blob/main/B_eq.png?raw=true" width="200" />

where:

<img src="https://github.com/ihe-k/Beliefs/blob/main/B_2_eq.png?raw=true" width="200" />

<ins>Modelling Neighbour Messages</ins> 
Each neighbour *j* send a message M*j*<sup>(*t*) that reflects their belief and the nature of the information (misinformation or correction).  It is probablistically determined based on their belief:

<img src="https://github.com/ihe-k/Beliefs/blob/main/B_3_eq.png?raw=true" width="200" />

The likelihood of misinformation against correction depends on the misinformation rate and the neighbour's current belief.

The average message received by agent *i* is:

<img src="https://github.com/ihe-k/Beliefs/blob/main/B_4_eq.png?raw=true" width="200" />

where:

<img src="https://github.com/ihe-k/Beliefs/blob/main/B_5_eq.png?raw=true" width="200" />

<ins>Incorporating uncertainty</ins>
To emulate real-world variability, a small Gaussian node with a mean of 0 and a standard deviation of 0.02 is added:

<img src="https://github.com/ihe-k/Beliefs/blob/main/B_6_eq.png?raw=true" width="200" />

This stochastic component ensures that beliefs may fluctuate and prevents deterministic convergence as well as capturing the variability inherent in social opinion dynamics.

## Skills Demonstrated
* Network modelling and simulation with NetworkX.
* Implementation of agent-based models incorporating probabilistic messaging and belief updating.
* Advanced data visualisation, including animated plots, using matplotlib and external tools (ImageMagick).
* Modular, well-documented Python scripting for reproducibility and future extensions.

## Results & Insights
The generated animation vividly demonstrates how beliefs fluctuate as a result of social influence and misinformation.
The dynamic visualisation provides insights into the conditions that foster belief convergence or polarisation.
The approach is adaptable to more complex scenarios, such as multiple misinformation sources or evolving network structures.

