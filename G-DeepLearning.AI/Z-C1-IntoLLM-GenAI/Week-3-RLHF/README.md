# Week 3 - Agents & RLHF 
RLHF:
- Reinforcement learning from human feedback (RLHF) helps align LLMs to human values and reduce harmful content.
- RLHF uses human feedback and reinforcement learning to shape LLM behavior. Helps make models more honest, hopeful, harmless.

<br><br>

Agents: 
- LLMs can be used as reasoning engines by allowing them to take actions like web searches, addressing limitations.
- Reasoning engine approaches like RAG let LLMs incorporate external info like databases, taking actions.

### RLHF - Reinforcement Learning from Human Feedback

Sometime LLM Models behave badly
- toxic language 
- aggressive responses
- providing dangerous information 
- Incorrect response (hallucination)
<br>

Responsible use of AI Principle HHH
- Helpful 
- Honest 
- Harmless
<br>

[Learning to summarize from Human Feedback](https://arxiv.org/abs/2009.01325) research paper by OpenAI, 2020
- Here you can see that a model fine-tuned on human feedback produced better responses than a pretrained model, an instruct fine-tuned model, and even the reference human baseline.
<br>

Reinforcement Learning 
- Reinforcement learning is a type of machine learning in which an agent learns to make decisions related to a specific goal by taking actions in an environment, with the objective of maximizing some notion of a cumulative reward.
- In this framework, the agent continually learns from its experiences by taking actions, observing the resulting changes in the environment, and receiving rewards or penalties, based on the outcomes of its actions. 
- By iterating through this process, the agent gradually refines its strategy or policy to make better decisions and increase its chances of success.
- Agent - who plays tic-tac-toe
    - Model - RL Policy
- Objective - win the game 
    - Goal - The goal of reinforcement learning is for the agent to learn the optimal policy for a given environment that maximizes their rewards.
- Environment - the game board, current configuration
- Action Space - All the possible actions
- Playout/ Rollout - The series of actions and corresponding states form a playout.
- We can use this same approach with LLMs. 
    - Reward model: Evaluating individual tokens by human can be time consuming Nd expensive. So, we could build a Reward Model. 
    - Roolout and not playout

#### RLHF: Obtaining feedback from Humans 
- To fine-tune an LLM with RLHF:
    - Select a capable base LLM and generate completions for a prompt dataset
- Gather human feedback:
    - Define a criteria (e.g. helpfulness, harmless, honest) for humans to evaluate completions
    - Have humans rank multiple completions for each prompt
- Convert rankings to pairwise comparisons:
    - Take all possible pairs of completions
    - Label preferred option in pair as 1, other as 0
    - Reorder so preferred option is first
- Train a reward model on human feedback
    - Will predict reward in place of humans during RL finetuning
- Provide clear instructions to get high quality labels:
    - Explain criteria and task in detail
    - Guide decisions and edge cases
- Ranked feedback gives more data than thumbs up/down
The key steps are generating completions, getting ranked human assessments, converting to pairwise format, and training a reward model for reinforcement learning.

#### RLHF: Train reward model
the reward model is trained on human preferences to predict reward values that can guide the LLM during reinforcement learning.
- The reward model for RLHF is usually a language model:
    - Trained on human ranked prompt-completion pairs
- Learns to favor human preferred completion 
    - by Minimizes loss on reward difference 
    - loss = log( *sigma* (r_j - r_k) )
    - Human preferred option y_j is always ranked first
    - Can then provide logits for positive and negative classes
    - E.g. non-toxic (positive) and toxic (negative) for detoxification
- Largest logit for positive class is the reward value
- Apply softmax to logits to get probabilities
- Reward model provides tool to align LLM via RL process

#### RLHF: Fine-tuning with reinforcement learning
The iterative RLHF process uses the reward model and PPO to gradually update the LLM to produce more human aligned responses over time.
- The reward model is used in RLHF to update the LLM weights towards human alignment
- Process:
    - Pass prompt to instruct LLM to generate completion
    - Send completion + prompt to reward model to get reward value
    - Use reward value to update LLM weights via RL algorithm
- Higher reward = more aligned response
- Iterative process continues for defined number of epochs
- Reward should improve each iteration as LLM alignment increases
- Continue until LLM reaches alignment criteria (e.g. helpfulness threshold)
- Popular RL algorithm is PPO (proximal policy optimization)
- PPO uses reward model outputs to update LLM weights
- Understanding PPO can help troubleshoot implementation issues

#### Proximal Policy Optimization
- PPO (Proximal Policy Optimization) is an algorithm for reinforcement learning.
- PPO optimizes the LLM policy to align with human preferences over iterations.
- It makes small updates within a bounded region to maintain stability.
- The goal is to maximize rewards based on human feedback.
<br>

**How does PPO work**:
- PPO operates in two phases: 
    - Phase I (LLM generates completions)  
    - Phase II (update LLM with rewards).
- The value function estimates expected total rewards for a given state.
- Value loss minimizes the difference between actual rewards and value estimates.

- PPO keeps model updates within a trust region to ensure stability.
- The PPO policy objective aims to maximize expected rewards by updating LLM weights.
- Advantage estimation helps identify better and worse token choices.
- The policy objective includes entropy to balance alignment and creativity.
- c1 and c2 are hyperparameters in the PPO objective.
    - Loss(PPO) = L(Policy) + c1 L_VF + c2 L_ENT
    - L(Policy) Policy Loss
    - c1 L_VF Value Loss
    - c2 L_ENT Entropy Loss 
- Multiple iterations of PPO lead to a human-aligned LLM.

- Alternates to RL technique for LLM fine-tuning:
    - Q-learning 
    - direct preference optimization

#### RLHF: Reward Hacking
- An interesting problem that can emerge in reinforcement learning is known as reward hacking, where the agent learns to cheat the system by favoring actions that maximize the reward received even if those actions don't align well with the original objective. Examples: 
    - It might exaggerate things (garbage turns to very beautiful)
    - nonsensical, grammatically incorrect text (Beautiful love and world peace all around)
- **Avoiding Reward Haking**
    - Model 1
        - Use initial instruct LLM as frozen reference model
        - Reference model weights are not updated during RLHF
        - Maintains consistent baseline for comparison
    - Pass prompt to reference LLM and updated LLM to generate completions
    - Calculate KL divergence between the two completions
    - KL divergence measures difference between probability distributions to compare updated LLM to reference LLM (Modle 1)
    - KL divergence calculated for each token across vocabulary
    - Add KL divergence as penalty term to reward calculation
    - Penalizes updated LLM if it shifts too far from reference
    - Need two copies of LLM - frozen reference and PPO updated LLM
    - Can use PEFT adapter-based fine-tuning to reuse same base LLM (less momory footprint)
- **Evaluate the human-aligned LLM**
     - use a reward model that can generate a Toxicity score 

#### Scaling human feedback
Constitutional AI is a method to scale supervision and address unintended consequences by training models to comply with predefined rules and principles.
    - Scaling human feedback for RLHF is challenging, requires large labeling teams
    - Constitutional AI uses principles and rules to govern model behavior
    - Trains models to self-critique and revise responses to comply with principles
    - Addresses unintended consequences like models revealing harmful info
    - Two stages for RLAIF:
        - Supervised pretraining to generate constitutional responses
        - Reinforcement learning with model-generated preferences as reward
    - Examples:
        - Model gives harmful helpful response (e.g. hacking wifi)
        - Ask model to critique per constitution and generate new response
    - Creates training data of harmful and constitutional pairs
    - Fine-tune model with this data to learn constitutional responses
    - Then use fine-tuned model to generate preferences for reward model
    - Reward model used in RL stage to further align model
- Ref: [Constitutional AI: Harmlessness from AI Feedback, 2022](https://arxiv.org/abs/2212.08073)
    - 