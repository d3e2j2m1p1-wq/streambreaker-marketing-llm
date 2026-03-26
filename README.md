# StreamBreaker AI — Marketing Strategy Generator
> **Model 3 of the StreamBreaker AI Capstone Pipeline** · MS Business Analytics, Cal State East Bay · April 2026

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5--turbo-412991?style=flat&logo=openai&logoColor=white)](https://openai.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## What It Does

StreamBreaker AI is a multi-model AI pipeline built to help **independent music artists** break through in a saturated streaming market. This repo contains **Model 3: the Marketing Strategy Generator** — a GPT-3.5-turbo powered module that takes an artist's profile, genre, and goals as input and produces a structured, audience-segmented marketing strategy as output.

The full pipeline (4 models total, built by a team of 4) covers audience analysis, trend forecasting, marketing strategy generation, and performance tracking. This module owns the marketing strategy layer.

---

## How It Works

```
User Input (artist profile, genre, target audience, goals)
        ↓
Multi-step Prompt Chain (prompts.py)
        ↓
OpenAI GPT-3.5-turbo API
        ↓
Structured Marketing Strategy Output
        ↓
Pipeline API Contract → downstream models
```

The prompt engineering uses a **chain-of-thought approach** — breaking the strategy generation into sequential reasoning steps (audience segmentation → platform prioritization → content calendar → budget allocation) rather than asking the model to produce everything in one shot. This significantly improves output quality and consistency.

---

## Project Structure

```
streambreaker-marketing-llm/
├── main.py                  # Entry point — runs the full strategy generation flow
├── prompts.py               # Prompt templates and chain logic
├── app_demo.py              # Interactive demo mode
├── test_integration.py      # Integration tests with the broader pipeline
├── CASE_STUDIES.md          # Sample outputs and real-world test cases
├── TEAM_INTEGRATION.md      # API contract docs for team pipeline integration
└── TEST_RESULTS.md          # Evaluation results and output quality metrics
```

---

## Getting Started

**Prerequisites**
- Python 3.10+
- OpenAI API key

**Install dependencies**
```bash
pip install openai python-dotenv
```

**Set your API key**
```bash
# Create a .env file
echo "OPENAI_API_KEY=your_key_here" > .env
```

**Run the demo**
```bash
python app_demo.py
```

**Run the full strategy generator**
```bash
python main.py
```

---

## Example Output

Given an input like:
> *Artist: indie-pop duo, 5K monthly Spotify listeners, target: 18–28 urban demographic, goal: grow to 50K listeners in 6 months*

The model generates a multi-section strategy covering platform focus, content cadence, collaboration targets, playlist pitching approach, and a 30/60/90-day action plan.

See [`CASE_STUDIES.md`](CASE_STUDIES.md) for full sample outputs.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language Model | OpenAI GPT-3.5-turbo |
| Prompt Engineering | Multi-step chain-of-thought |
| Language | Python 3.10 |
| Pipeline Integration | REST API contract (see TEAM_INTEGRATION.md) |
| Testing | Custom integration test suite |

---

## Team & Context

This module was developed as part of a 4-person MS Business Analytics capstone at **California State University, East Bay**. Each team member owned one model in the pipeline. This repo covers Model 3 (Marketing Strategy Generation).

---

## Author

**Miguel Angel Davila Carrasco**  
MS Business Analytics · Cal State East Bay  
[github.com/d3e2j2m1p1-wq](https://github.com/d3e2j2m1p1-wq)
