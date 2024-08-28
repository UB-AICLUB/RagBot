# RAG Discord Bot

Welcome to the RAG Discord Bot project! This document provides an overview of the project, its goals, and the technologies we'll be using.

## Project Overview

The RAG (Retrieve and Generate) Discord Bot aims to enhance our Discord server by providing intelligent responses based on our discussions and general club information. The project will span a month and is designed to be manageable within that timeframe.

### Use Cases

1. **Transcript Querying**: The bot will be able to refer to the transcripts of our discussions and answer questions based on them.
2. **General Club Information**: The bot will provide information about announcements and club resources.

## Architecture

The bot will be implemented using the following technologies:

- **Discord.py**: A Python library for interacting with the Discord API. [Discord.py Documentation](https://discordpy.readthedocs.io/en/stable/)
- **Text Embeddings**: Textual data will be converted into numerical representations for semantic analysis. [Introduction to Text Embeddings](https://stackoverflow.blog/2023/11/09/an-intuitive-introduction-to-text-embeddings/)
- **Vector Database**: Textual data will be stored in a vector database for efficient semantic search. [Vector Database](https://www.pinecone.io/learn/vector-database/)
- **FastAPI**: For building a web API to interface with the bot. [FastAPI Documentation](https://fastapi.tiangolo.com/)
- **Docker**: For containerization and deployment. [Docker Documentation](https://www.docker.com/)
- **Celery (Optional)**: For task queue management and asynchronous processing. [Celery Documentation](https://docs.celeryq.dev/en/stable/userguide/workers.html)

## Getting Started

### Prerequisites

- Python 3.x
- Basic understanding of Discord.py
- Familiarity with text embeddings and vector databases
- Knowledge of FastAPI and Docker (optional but recommended)

We also follow 'learn as you do' motto so dont be afraid to pick up issues that intrest you.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/UB-AICLUB/RagBot.git
   cd RagBot
   ```

2. **Install Dependencies**

   Create a virtual environment and install the necessary Python packages:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**

   Create a `.env` file and add your Discord bot token and other configuration details.

   ```env
   DISCORD_TOKEN=your_discord_token
   ```
   for obvious reasons, this will not be pushed into the repository. This is required only if you wanna test it in your own server.

4. **Run the Bot**

   ```bash
   python bot.py
   ```

## Development

During the first week of September, we will have an in-person discussion session to provide a basic overview of the tools and technologies involved.

## Contributions

Feel free to contribute to the project by submitting issues, suggestions, or pull requests. We encourage learning and collaboration throughout the development process.

## Contact

If you have any questions or doubts, please reach out to me at mohantej@buffalo.edu or ping us in the Discord server.

Looking forward to working with you all!
