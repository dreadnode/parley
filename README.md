# Parley

This is a minimal implementation of the "Tree of Attacks (TAP): Jailbreaking Black-Box LLMs Automatically" Research by Robust Intelligence.

[Using AI to Automatically Jailbreak GPT-4 and Other LLMs in Under a Minute](https://www.robustintelligence.com/blog-posts/using-ai-to-automatically-jailbreak-gpt-4-and-other-llms-in-under-a-minute)

# Design

- [x] Clean, expand, and restructure all the system prompts
- [x] Use API-based model calling via OpenAI, TogetherAI, and Mistral
- [x] Refactor the tree/leaf branching for simplicity
- [ ] Implement max conversation history to stay within attacker context window
- [ ] Add WandB logging for history tracking
- [ ] Add support for local models  

# Usage
1. Pull + Install dependencies
```
git clone git@github.com:dreadnode/parley.git
cd parley
poetry install
poetry shell
```
2. Configure any required API keys
```
OPENAI_API_KEY='...'
TOGETHER_API_KEY='...'
MISTRAL_API_KEY='...'
```
3. Run an attack generation
```
python parley.py "Force the model to print it's previous instructions"
```
