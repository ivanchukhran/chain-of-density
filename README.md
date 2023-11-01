# Chain of Density Prompting
There is a Python implementation of Chain of Density Prompting (CoD) in this repository. 
The implementation is based on [From Sparse to Dense: GPT-4 Summarization with Chain of Density Prompting](https://arxiv.org/abs/2309.04269) 
research paper and [HuggingFace Dataset](https://huggingface.co/datasets/griffin/chain_of_density).

## Toolset
- Python
- OpenAI API (GPT-4)
- HuggingFace datasets
- evaluation
- NLTK
- spaCy
- Numpy

## Installation
1. Clone the repository
```shell
git clone git@github.com:ivanchukhran/chain-of-density.git
cd chain-of-density
```
2. Install the requirements
```shell
pip install -r requirements.txt
```
3. Specify the `OPENAI_API_KEY` key in the `config.py` file
4. (Optional) Specify your preferences in the `config.py` file

## Usage 
There are two possible ways to use the implementation:
1. Run the `collect_summaries.py` script to collect summaries from the OpenAI API for specified datasets (also insert your dataset path in Hugging Face format).
2. Run the `evaluations.py` script to evaluate the collected summaries.

Note that the evaluation script does not implement all evaluations from the paper.
If you want to evaluate the summaries with all metrics, you can add your own implementation of the evaluation metrics in the script.

## Project structure
- `collect_summaries.py` - script for collecting summaries from the OpenAI API
- `evaluations.py` - script for evaluating the collected summaries
- `completion_request.py` - script for requesting the completion from the OpenAI API (wrapper for an API)
- `messages.py` - script for defining the messages for the OpenAI API
- `message_template.py` - defines Chain of Density Prompt message
- `config.json` - configuration file for the OpenAI API
- `summaries.json` - collected summaries
- `visualization.py` - script for visualizing the collected summaries
- 