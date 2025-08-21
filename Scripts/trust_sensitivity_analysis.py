import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import os
import subprocess

def initialize_agents(n_agents):
    """Initialize agents with gender, belief, and trust."""
    agents = []
    for i in range(n_agents):
        gender = 'female' if i < n_agents // 2 else 'male'
        belief = np.random.uniform(0.4, 0.6)
        trust = np.clip(np.random.normal(0.4 if gender=='female' else 0.6, 0.05), 0.1, 0.9)
        agents.append({'gender': gender, 'belief': belief, 'trust': trust})
    return agents

def simulate_belief_update(agents, G, misinformation_rate, trust):
    """Update agents' beliefs based on neighbors' messages influenced by trust."""
    new_beliefs = []
    for i, agent in enumerate(agents):
        neighbors = list(G.neighbors(i))
        if not neighbors:
            new_beliefs.append(agent['belief'])
            continue
        messages = []
        for j in neighbors:
            neighbor_belief = agents[j]['belief']
            if neighbor_belief > 0.6:
                msg_type = 'correction' if np.random.rand() > misinformation_rate else 'misinfo'
                messages.append(0.9 if msg_type=='correction' else 0.1)
        if messages:
            m = np.mean(messages)
            belief_update = (agent['belief'] * (1 - trust)) + (m * trust)
        else:
            belief_update = agent['belief']
        # Add some randomness
        belief_update += np.random.normal(0, 0.02)
        belief_update = np.clip(belief_update, 0, 1)
        new_beliefs.append(belief_update)
    # Assign updated beliefs
    for i in range(len(agents)):
        agents[i]['belief'] = new_beliefs[i]

def create_animation(frames_dir, output_gif):
    """Create GIF from frames using ImageMagick."""
    try:
        subprocess.run([
            "convert",
            "-delay", "20",
            "-loop", "0",
            os.path.join(frames_dir, "beliefs_trust_*.png"),
            output_gif
        ], check=True)
        print(f"GIF successfully saved as '{output_gif}'")
    except Exception as e:
        print("Error creating GIF:", e)

def main():
    n_agents = 100
    timesteps = 50
    misinformation_rate = 0.3

    # Define trust levels to test
    trust_levels = np.linspace(0.1, 0.9, 9)  # e.g., from 0.1 to 0.9

    # Store results
    results = []

    # Create directory for frames
    frames_dir = "trust_sensitivity_frames"
    os.makedirs(frames_dir, exist_ok=True)

    for trust in trust_levels:
        # Initialize network and agents for each trust level
        G = nx.watts_strogatz_graph(n=n_agents, k=6, p=0.2)
        agents = initialize_agents(n_agents)

        beliefs_female = []
        beliefs_male = []

        # Run simulation
        for t in range(timesteps):
            simulate_belief_update(agents, G, misinformation_rate, trust)
            female_beliefs = [a['belief'] for a in agents if a['gender']=='female']
            male_beliefs = [a['belief'] for a in agents if a['gender']=='male']
            beliefs_female.append(np.mean(female_beliefs))
            beliefs_male.append(np.mean(male_beliefs))
            # Save plot at each timestep
            plt.figure(figsize=(8,4))
            plt.plot(beliefs_female, label='Female', color='#003A6B')  # dark blue
            plt.plot(beliefs_male, label='Male', color='#3776A1')    # lighter blue
            plt.xlabel('Time Step')
            plt.ylabel('Average Belief')
            plt.title(f'Belief Evolution at Step {t} (Trust={trust:.2f})')
            plt.legend()
            plt.ylim(0,1)
            plt.tight_layout()
            plt.savefig(f"{frames_dir}/beliefs_trust_{trust:.2f}_step_{t:03d}.png")
            plt.close()

        # Record final belief
        final_avg_belief = np.mean([beliefs_female[-1], beliefs_male[-1]])
        results.append({'trust': trust, 'final_belief': final_avg_belief})

    # Plot final belief vs trust
    plt.figure(figsize=(8,6))
    plt.plot([r['trust'] for r in results], [r['final_belief'] for r in results], marker='o', color='#003A6B')
    plt.xlabel('Trust Level')
    plt.ylabel('Final Average Belief')
    plt.title('Final Belief as a Function of Trust Level')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('final_belief_vs_trust.jpg')  # Save as JPEG
    plt.close()

    # Show the plot
    plt.show()

    # Create GIF animation from frames
    create_animation(frames_dir, "trust_sensitivity.gif")

if __name__ == "__main__":
    main()