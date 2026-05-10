# =========================
# 1. INSTALL
# =========================
!pip install crewai transformers accelerate torch datasets -q

# =========================
# 2. IMPORTS
# =========================
import os
from transformers import pipeline
from crewai import Agent, Task, Crew
from datasets import load_dataset

os.environ["OPENAI_API_KEY"] = "dummy"

# =========================
# 3. MODELS (LIGHTWEIGHT)
# =========================
solver_pipe = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-1.5B-Instruct",
    device_map="auto",
    max_new_tokens=200
)

critic_pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    device_map="auto",
    max_new_tokens=200
)

refiner_pipe = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-1.5B-Instruct",
    device_map="auto",
    max_new_tokens=200
)

# =========================
# 4. MEDQA DATASET
# =========================
dataset = load_dataset("fzkuji/MedQA", split="train")

def get_sample(i=0):
    item = dataset[i]
    q = item["question"]
    opts = item["options"]
    ans = item["answer"]

    return f"Question:\n{q}\n\nOptions:\n{opts}", ans

# =========================
# 5. AGENTS (NO LLM PARAMETER!)
# =========================
solver_agent = Agent(
    role="Solver",
    goal="Solve medical questions",
    backstory="Medical expert",
    verbose=True
)

critic_agent = Agent(
    role="Critic",
    goal="Find mistakes",
    backstory="Medical reviewer",
    verbose=True
)

refiner_agent = Agent(
    role="Refiner",
    goal="Improve answers",
    backstory="Medical improver",
    verbose=True
)

# =========================
# 6. TASKS (IMPORTANT FIX)
# =========================
def create_tasks(question):

    return [
        Task(
            description=f"Solve this:\n\n{question}",
            expected_output="Final diagnosis + reasoning"
        ),
        Task(
            description=f"Critique this:\n\n{question}",
            expected_output="List of errors"
        ),
        Task(
            description=f"Refine answer:\n\n{question}",
            expected_output="Improved final answer"
        )
    ]

# =========================
# 7. RUN SYSTEM (MANUAL PIPELINE)
# =========================
def run_system(question):

    solver_out = solver_pipe(question)[0]["generated_text"]
    critic_out = critic_pipe(question)[0]["generated_text"]
    refiner_input = solver_out + "\n" + critic_out
    final_out = refiner_pipe(refiner_input)[0]["generated_text"]

    return {
        "solver": solver_out,
        "critic": critic_out,
        "final": final_out
    }

# =========================
# 8. TEST
# =========================
q, gold = get_sample(0)

result = run_system(q)

print("\n===== SOLVER =====\n", result["solver"])
print("\n===== CRITIC =====\n", result["critic"])
print("\n===== FINAL =====\n", result["final"])
print("\n===== GROUND TRUTH =====\n", gold)