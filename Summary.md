# Modelling Belief Dynamics and Misinformation Spread in Social Networks

## Project Overview

## Objectives
* To model how individual beliefs are shaped by peer influence and trust within a social network.
* To incorporate gender differences, trust levels and mechanisms for misinformation correction.
* To visualise the temporal evolution of collective beliefs through dynamic plots, emphasising fluctuations, convergence or polarisation.

## Methodology
* Network Construction: Utilised the NetworkX library to generate a small-world social network with 100 agents, reflecting realistic social connection patterns.
* Agent Attributes: Each agent is assigned a gender (female or male), an initial belief value (between 0.4 and 0.6) and a trust level (differing by gender).
* Belief Update Rules: At each time step, agents update their beliefs based on messages received from neighbors:
* Messages are classified as misinformation or corrections, influenced by a predefined misinformation rate.
* Beliefs are adjusted via a trust-weighted averaging process, with added stochastic noise to simulate real-world uncertainty.

## Visualisation
The average beliefs of female and male agents are plotted over time using matplotlib. These plots are saved at each timestep, creating a sequence of images that are compiled into an animated GIF to illustrate the evolving social dynamics.

## Mathematical Foundations of the Belief Dynamics Model
This simulation models how individual beliefs evolve through social influence, trust and misinformation using a formal mathematical framework.

Belief Update Rule

<img src="https://github.com/ihe-k/Beliefs/blob/main/B_eq.png?raw=true" width="200" />
