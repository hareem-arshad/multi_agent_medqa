# Multi-Agent Clinical Reasoning System

## Overview
A multi-agent AI framework that improves LLM reasoning using iterative feedback loops.

## Dataset
MedQA benchmark dataset (Jin et al., 2020)

## System
- Solver Agent
- Critic Agent
- Refiner Agent

## Method
We evaluate whether iterative feedback improves reasoning quality.

## Result
Multi-agent system improves reasoning consistency compared to baseline.

## Tech Stack
Python, Streamlit, LLM APIs, MedQA dataset

User Input
   ↓
Solver Agent
   ↓
Critic Agent
   ↓
Refiner Agent
   ↓
Final Answer
   ↓
Evaluation
   ↓
AMD Batch Benchmark (optional)