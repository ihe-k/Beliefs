import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.lines import Line2D

def initialize_agents(n_agents):
    agents = []
    for i in range(n_agents):
        gender = 'female' if i < n_agents // 2 else 'male'
        belief = np.random.uniform(0.4, 0.6)
        trust = np.clip(
            np.random.normal(0.4 if gender == 'female' else 0.6, 0.05),
            0.1, 0.9
        )
        agents.append({'gender': gender, 'belief': belief, 'trust': trust})
    return agents

def simulate_belief_update(agents, G, misinformation_rate):
    new_beliefs = []
    for i, agent in enumerate(agents):
        messages = []
        for j in G.neighbors(i):
            nb = agents[j]['belief']
            if nb > 0.6:
                msg = 0.9 if np.random.rand() > misinformation_rate else 0.1
                messages.append(msg)
        if messages:
            m = np.mean(messages)
            update = agent['belief'] * (1 - agent['trust']) + m * agent['trust']
        else:
            update = agent['belief']
        update = np.clip(update + np.random.normal(0, 0.02), 0, 1)
        new_beliefs.append(update)
    for idx in range(len(agents)):
        agents[idx]['belief'] = new_beliefs[idx]

def main():
    n_agents = 100
    timesteps = 50
    misinformation_rate = 0.3
    intervention_step = 30  # when correction boost happens

    G = nx.watts_strogatz_graph(n_agents, 6, 0.2)
    agents = initialize_agents(n_agents)

    beliefs_female = []
    beliefs_male = []
    history = []

    for t in range(timesteps):
        rate = misinformation_rate if t < intervention_step else 0.1
        simulate_belief_update(agents, G, rate)
        history.append([a['belief'] for a in agents])
        beliefs_female.append(
            np.mean([a['belief'] for a in agents if a['gender'] == 'female']))
        beliefs_male.append(
            np.mean([a['belief'] for a in agents if a['gender'] == 'male']))

    arr = np.array(history)
    female_idx = [i for i, a in enumerate(agents) if a['gender'] == 'female']
    male_idx = [i for i, a in enumerate(agents) if a['gender'] == 'male']

    correction_line = Line2D([0], [0], color='red', lw=2, linestyle='--')

    # Female heatmap
    plt.figure(figsize=(14, 5))
    ax1 = sns.heatmap(arr[:, female_idx].T, cmap='viridis', cbar=True)
    ax1.invert_yaxis()  # Ensure Y-axis starts at 0 at bottom
    plt.title("Female Beliefs Over Time")
    plt.xlabel("Time Step")
    plt.ylabel("Agent Index")
    plt.axvline(intervention_step, color='red', linestyle='--', linewidth=2)
    plt.legend([correction_line], ["Correction Boost"], loc='upper left',
               borderpad=1.5, labelspacing=1.2)
    plt.tight_layout()
    plt.savefig("female_heatmap.png")
    plt.close()

    # Male heatmap
    plt.figure(figsize=(14, 5))
    ax2 = sns.heatmap(arr[:, male_idx].T, cmap='viridis', cbar=True)
    ax2.invert_yaxis()  # Ensure Y-axis starts at 0 at bottom
    plt.title("Male Beliefs Over Time")
    plt.xlabel("Time Step")
    plt.ylabel("Agent Index")
    plt.axvline(intervention_step, color='red', linestyle='--', linewidth=2)
    plt.legend([correction_line], ["Correction Boost"], loc='upper left',
               borderpad=1.5, labelspacing=1.2)
    plt.tight_layout()
    plt.savefig("male_heatmap.png")
    plt.close()

    # Group-averaged beliefs
    plt.figure(figsize=(10, 6))
    plt.plot(beliefs_female, label="Female Group", color='#003A6B')
    plt.plot(beliefs_male, label="Male Group", color='#1B5886')
    plt.axvline(intervention_step, color='red', linestyle='--', linewidth=2)
    plt.text(intervention_step + 1, 0.85, "Correction Boost",
             color='red', fontsize=12, va='top', ha='left')

    plt.legend(handles=[
        Line2D([], [], color='#003A6B', label='Female Group'),
        Line2D([], [], color='#1B5886', label='Male Group')
    ], loc='upper left', bbox_to_anchor=(0, 1), borderpad=1.5,
        labelspacing=1.2, handletextpad=1.0, fontsize=10)

    plt.xlabel("Time Step")
    plt.ylabel("Average Belief")
    plt.title("Group-Averaged Beliefs Over Time")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("group_beliefs_with_label.png", bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()
