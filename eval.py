# eval.py

def evaluate(initial, final):

    return {
        "initial_length": len(initial),
        "final_length": len(final),
        "improvement": len(final) > len(initial)
    }