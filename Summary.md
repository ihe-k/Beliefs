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

## Mathematical Foundations of the Belief Dynamics Model
This simulation models how individual beliefs evolve through social influence, trust and misinformation using a formal mathematical framework.

<ins>Belief Update Rule</ins>

<img src="https://github.com/ihe-k/Beliefs/blob/main/B_eq.png?raw=true" width="200" />

where:

<img src="https://github.com/ihe-k/Beliefs/blob/main/B_2_eq.png?raw=true" width="200" />

<ins>Modelling Neighbour Messages</ins>  
Each neighbour *j* send a message M*j*<sup>(*t*)</sup> that reflects their belief and the nature of the information (misinformation or correction).  It is probablistically determined based on their belief:

<img src="https://github.com/ihe-k/Beliefs/blob/main/B_3_eq.png?raw=true" width="200" />

The likelihood of misinformation against correction depends on the misinformation rate and the neighbour's current belief.

The average message received by agent *i* is:

<img src="https://github.com/ihe-k/Beliefs/blob/main/B_4_eq.png?raw=true" width="400" />

where:

<img src="https://github.com/ihe-k/Beliefs/blob/main/B_5_eq.png?raw=true" width="200" />

<ins>Incorporating uncertainty</ins>  
To emulate real-world variability, a small Gaussian node with a mean of 0 and a standard deviation of 0.02 is added:

<img src="https://github.com/ihe-k/Beliefs/blob/main/B_6_eq.png?raw=true" width="400" />

This stochastic component ensures that beliefs may fluctuate and prevents deterministic convergence as well as capturing the variability inherent in social opinion dynamics.

## Results & Insights
The average beliefs of female and male agents are plotted over time using matplotlib ('male_heatmap.png' and 'female_heatmap.png'). A plot ('create_misinfo_gif) highlighting corrective actions to address misinformation is saved at each timestep, creating a sequence of images that are compiled into an animated GIF to illustrate the evolving social dynamics.

### Beliefs Heatmap ('female_heatmap.png')
This heatmap visualises the beliefs of female agents over the course of 50 time steps. Each row corresponds to one female agent and each column represents a time step.

<ins>Key Features:</ins>
* Colour Representation: The color intensity represents the belief value of each agent, with the 'viridis' colormap mapping belief values (ranging from 0 to 1) to different shades.
* Vertical Red Line: This indicates the intervention step (Step 30), where a corrective action (like a correction boost) is applied to reduce the misinformation rate. Before this step, misinformation is more likely, while after it, the rate drops to 0.1, making belief updates more aligned with corrections.
* Y-Axis: The y-axis corresponds to the index of female agents (from top to bottom). In this exmaple, agent belief values evolve over time.

Before the intervention (step 30) male and female agents are exposed to misinformation and correction messages. However, female agents, due to their typically lower trust values, may be more resistant to adopting beliefs that come from others.  Whereas male agents appear more susceptible to adopting the beliefs of their neighbours, even if the information is misleading possibly due to higher trust values on average than female agents.  After step 30, the misinformation rate drops, there is a convergence in beliefs across both genders. The correction boost reduces the likelihood of misinformation spreading.

The 'lightness' of the female heatmap in comparison to their counterparts suggests that female agents have beliefs that are closer to 1 (the maximum belief) possibly because of how initial beliefs and belief update rules interact differently for males and females.  As  belief update rules take into account messages from neighbours and misinformation, females might adjust more quickly or more aggressively toward higher beliefs due to these dynamics (which could be related to the trust or influence the agents have on each other).  It may also indicate that their beliefs remain closer to their starting point after corrective actions comparen to females who appear more resistant to misinformation due to lower initial trust values.  This suggests that females may stabilise at hgher belief values over times while males experience greater fluctuation, possibly due to their greater higher initial trust levels, which may lead them to being more influenced by misinformation from neighbours.

### Group Beliefs
The correction boost in the 'group_beliefs' plot highlights that the introduction of an intervention reduces misinformation, causing a sharp reduction in belief fluctuations after time step 30. Both male and female groups are likely to show increased alignment with the truth as the misinformation rate drops.  

Similarly, the area plot animation that shows how different components of misinformation evolve over time, including various interventions like user corrections, fact-checking, and official corrections illustrates the way misinformation that is spread over phases may be countered.   To make the visualisation cleaner, each of the component data is smoothed using B-splines, which ensure that the data curves are continuous and aesthetically appealing. This is done using the make_interp_spline function from scipy.  Each time slice of the data (misinformation, fact-checking, user corrections and official corrections) is stacked on top of the others to show how different components contribute to the total belief at each timestep.  The timeline is divided into three phases: preparation, development and escalation. 

During the preparation phase, misinformation is the dominant factor.  As fact-checking and user corrections begin in the development phase, misinformation drops and these corrective actions garner prominence. As more official corrections are released to stabilise the belief system and manage misinformation spread, layers shift and misinformation shrinks in the escalation phase.

### Sensitivity Analysis
The code runs simulations with different trust levels (from 0.1 to 0.9). By varying the trust parameter from low to high, I analyse the way the final average belief b<sub>*final*</sub> depends on trust:

<img src="https://github.com/ihe-k/Beliefs/blob/main/B_7_eq.png?raw=true" width="200" />

where *T* represents the total number of time steps.

For each trust level, the agent interactions are simulated for 50 time steps and the average beliefs for females and males are tracked over time.

The plot shows a positive correlation between trust and the final average belief. As trust increases, agents become more willing to update their beliefs based on their neighbours.  As a result, there is faster convergence toward a consensus (correct belief).  At low trust levels (e.g., trust = 0.1 or 0.2), agents are more resistant to belief changes. Their beliefs might stay more divergent, and the overall final belief may be lower, reflecting greater uncertainty or spread of misinformation.  At high trust levels (e.g., trust = 0.8 or 0.9), agents tend to adopt beliefs more quickly, and the final belief across the group is likely to be more aligned with the truth (closer to 1.0), as agents trust their neighbours' corrections more.

## Further Development
* Study effects of misinformation rates
* Incorporate more complex belief update rules
* Use real social network data
* Explore different network topologies
