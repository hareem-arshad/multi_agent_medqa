# agents.py

def solver(question):
    return f"""
You are a medical reasoning assistant.

Solve step by step:

Question:
{question}

Provide reasoning and final answer.
"""


def critic(answer):
    return f"""
You are a strict medical reviewer.

Analyze this answer:
{answer}

List:
- logical errors
- missing steps
- incorrect assumptions
"""


def refiner(question, answer, feedback):
    return f"""
You are an expert medical assistant.

Improve the answer.

Question:
{question}

Original Answer:
{answer}

Critic Feedback:
{feedback}

Now give a corrected, improved answer.
"""