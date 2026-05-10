# Multi-Agent Clinical Reasoning System

A lightweight multi-agent AI framework that improves clinical reasoning by simulating an iterative expert review process using collaborative AI agents.

---

##  Overview

Traditional medical AI systems generate a single response without verification, which can lead to reasoning errors and inconsistent conclusions.  
This project solves that problem by introducing a **multi-agent reasoning pipeline** where multiple AI agents collaborate to solve, critique, and refine medical answers.

The system mimics real clinical workflows where multiple experts review and improve diagnostic reasoning before reaching a final decision.

---

## System Architecture

The system is built using three specialized AI agents:

###  Solver Agent
- Generates the initial clinical reasoning and diagnosis

###  Critic Agent
- Reviews the reasoning for logical errors, missing assumptions, or inconsistencies

###  Refiner Agent
- Improves the final answer using feedback from the critic

---

## Workflow
Medical Question
↓
Solver Agent (Initial Answer)
↓
Critic Agent (Error Detection)
↓
Refiner Agent (Final Improved Answer)


---

##  Dataset

The system is evaluated using the:

- MedQA (Medical Question Answering Dataset)
- This dataset contains medical exam-style questions designed to test clinical reasoning and diagnostic accuracy.
  Credits: https://huggingface.co/datasets/fzkuji/MedQA 
T
 
---

##  Technologies Used

- Python  
- CrewAI (Multi-agent orchestration)  
- Transformers (Hugging Face)  
- PyTorch  
- Gradio (UI for demo)  
- Qwen2.5-1.5B-Instruct (lightweight LLM)  
- TinyLlama-1.1B-Chat-v1.0 (lightweight LLM)  
- Google Colab  
- Hugging Face Datasets  

---

## Key Features

- Multi-agent collaborative reasoning system  
- Iterative critique-and-refinement pipeline  
- Lightweight open-source LLM integration  
- Medical QA evaluation workflow  
- Modular and scalable architecture  
- Cloud-ready deployment (Colab / Hugging Face Spaces)

---

## Example

**Input:**
> A 23-year-old pregnant woman at 22 weeks gestation presents with burning upon urination. She states it started 1 day ago and has been worsening despite drinking more water and taking cranberry extract. She otherwise feels well and is followed by a doctor for her pregnancy. Her temperature is 97.7°F (36.5°C), blood pressure is 122/77 mmHg, pulse is 80/min, respirations are 19/min, and oxygen saturation is 98% on room air. Physical exam is notable for an absence of costovertebral angle tenderness and a gravid uterus. Which of the following is the best treatment for this patient?

Options:
[{'key': 'A', 'value': 'Ampicillin'}, {'key': 'B', 'value': 'Ceftriaxone'}, {'key': 'C', 'value': 'Ciprofloxacin'}, {'key': 'D', 'value': 'Doxycycline'}, {'key': 'E', 'value': 'Nitrofurantoin'}] 

Answer:
The correct answer is E: Nitrofurantoin.

**Output Flow:**
- Solver: Generates initial diagnosis reasoning  
- Critic: Identifies missing clinical considerations  
- Refiner: Produces improved final clinical answer  

---

## Objective

To evaluate whether multi-agent AI systems can improve:

- Reasoning consistency  
- Diagnostic accuracy  
- Transparency in AI decision-making  
- Reliability in medical question answering  

---

## Deployment Options

- Google Colab (development & testing)  
- Hugging Face Spaces (live demo deployment)  

---

## Future Improvements

- Voting-based final decision system  
- Real-time agent interaction visualization  
- Faster inference optimization  
- Confidence scoring for medical outputs  
- Expanded dataset support  

---

##  Conclusion

This project demonstrates how collaborative multi-agent AI systems can significantly enhance the quality of clinical reasoning by simulating structured expert review workflows.

---
