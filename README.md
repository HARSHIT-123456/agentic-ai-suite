# Multi-Agent AI Assistant Suite

An LLM-powered application for analyzing YouTube videos and turning video content into summaries, timestamps, and key insights through an interactive interface.

## Overview

The Multi-Agent AI Assistant Suite is a Python-based Generative AI project built using Agno, LLM APIs, and YouTube transcript extraction tools. It is designed to simplify video-content analysis and help users access useful information without manually reviewing an entire video.

## Problem Statement

Long videos can take significant time to review. Finding important topics, understanding the main message, and locating relevant sections can be difficult.

This project explores how Large Language Models and AI tools can assist with video-content analysis and information retrieval.

## Key Features

- **LLM-powered analysis:** Uses supported LLM APIs to process and summarize video content.
- **Transcript extraction:** Retrieves available video transcript text using the project's transcript tools.
- **Video summaries:** Generates concise summaries and key insights.
- **Timestamped highlights:** Presents relevant video timestamps when supported by the available transcript and implementation.
- **Interactive interface:** Provides a Streamlit interface for users to interact with the application.
- **Tool integration:** Connects language models with external tools and APIs.

## Technology Stack

- **Language:** Python
- **Agent framework:** Agno
- **LLM providers:** Groq and/or OpenAI, depending on configuration
- **Video tools:** YouTube API and transcript extraction tools
- **Interface:** Streamlit

## How It Works

1. The user provides a supported YouTube video or video link.
2. The application retrieves available video information and transcript text.
3. The configured LLM processes the available content.
4. The application generates summaries, important insights, and supported timestamps.
5. Results are displayed through the Streamlit interface.

## Project Architecture

User Input → Video/Transcript Processing → LLM and Agent Workflow → Summary and Insights → Streamlit Interface

The exact execution flow depends on the agents, tools, and functions implemented in the source code.

## Getting Started

### Prerequisites

- Python installed
- Git
- API credentials required by the configured providers

### Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd YOUR_REPOSITORY_FOLDER
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add the required API keys using the environment variable names expected by your code.

Never commit API keys or secrets to GitHub.

### Run the Application

```bash
streamlit run app.py
```

Replace `app.py` with the actual Streamlit entry-point filename in your repository.

## Configuration

Configure the API credentials and other settings using the environment variables and configuration files supported by the project.

Do not publish real credentials in source code, screenshots, or documentation.

## Testing and Validation

Document the tests you have actually run, including:

- Application startup and dependency checks
- Transcript retrieval for supported videos
- LLM response generation
- Error handling for unavailable transcripts or invalid inputs
- Behaviour when API credentials are missing or a provider request fails

Add test commands and results after verifying them against the repository.

## Limitations

- Transcript availability and quality depend on the source video.
- Generated summaries can omit details or contain inaccuracies.
- API availability, rate limits, and usage costs depend on the configured provider.
- Timestamp accuracy depends on the transcript and the implemented timestamp-handling logic.
- The application should be evaluated on representative videos before relying on its outputs.

## Future Improvements

- Add automated tests for the main processing workflow.
- Improve handling of unavailable transcripts and API failures.
- Evaluate summary quality against a defined set of sample videos.
- Add source-linked insights and clearer error messages where supported.
- Improve reproducibility through documented configurations and example inputs.

## Security

- Keep API keys in environment variables.
- Exclude `.env` and other secret files from version control.
- Do not commit private user data or credentials.

