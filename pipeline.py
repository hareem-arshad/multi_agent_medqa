# pipeline.py

from agents import solver, critic, refiner

# SIMPLE MOCK LLM (replace later if needed)
def llm(prompt):
    return "🧠 " + prompt[:400] + "\n\n[MODEL OUTPUT SIMULATION]"


def run_pipeline(question):

    # Step 1: Solve
    initial_prompt = solver(question)
    initial = llm(initial_prompt)

    # Step 2: Critic
    critic_prompt = critic(initial)
    feedback = llm(critic_prompt)

    # Step 3: Refiner
    refiner_prompt = refiner(question, initial, feedback)
    final = llm(refiner_prompt)

    return initial, feedback, final