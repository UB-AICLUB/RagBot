# Contribution Guidelines

### Prerequisites

## Architecture

The bot will be implemented using the following technologies:

- **Discord.py**: A Python library for interacting with the Discord API. [Discord.py Documentation](https://discordpy.readthedocs.io/en/stable/)
- **Text Embeddings**: Textual data will be converted into numerical representations for semantic analysis. [Introduction to Text Embeddings](https://stackoverflow.blog/2023/11/09/an-intuitive-introduction-to-text-embeddings/)
- **Vector Database**: Textual data will be stored in a vector database for efficient semantic search. [Vector Database](https://www.pinecone.io/learn/vector-database/)
- **FastAPI**: For building a web API to interface with the bot. [FastAPI Documentation](https://fastapi.tiangolo.com/)
- **Docker**: For containerization and deployment. [Docker Documentation](https://www.docker.com/)
- **Celery (Optional)**: For task queue management and asynchronous processing. [Celery Documentation](https://docs.celeryq.dev/en/stable/userguide/workers.html)
-- **RabbitMQ (Optional)**: Message broker for inter-component communication. [RabbitMQ Documentation](https://www.rabbitmq.com/tutorials)

We follow a 'learn as you do' motto, so don’t hesitate to pick up issues that interest you, even if you're unfamiliar with the details. Support is always available!

## Installation

### 1. **Clone the Repository**

```bash
git clone https://github.com/UB-AICLUB/RagBot.git
cd RagBot
```

### 2. Install Dependencies by Module
Each module has its own virtual environment and dependencies. You'll need to set up each environment individually based on the module you're working on.

####  API Module
Navigate to the API directory:

```bash
cd API
```
Create a virtual environment and install the necessary Python packages:


```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
pip install -r requirements.txt
```
Ensure that the .env file is set up with any required environment variables for the API.

#### Client Module
Navigate to the client directory:


```bash
cd client
```
Create a virtual environment and install the necessary Python packages:


```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
pip install -r requirements.txt
```

Set up your Discord bot token and any other necessary configuration by creating a .env file:

```env
DISCORD_TOKEN=your_discord_token
```
This file is required only if you want to test the bot on your server

#### Task Queue Module
If you're working with the task queue module, navigate to the directory:

```bash
cd task_queue
```

Set up the environment and install dependencies as needed following the pattern used for the other modules.

This will spin up all services, including the API and client components.

### Set Up Global Linting and Formatting
We use global linting and formatting rules across all modules. Make sure to follow them by running the linters and formatters from the root directory.

Install the necessary global dependencies:

```bash
pip install flake8 black
```

To check for linting issues:

```bash
flake8 .
```
To automatically format code:

```bash
black .
```

Ensure you follow these rules before making a pull request.

### Run the Modules
#### Running the API (FastAPI)

To run the FastAPI server for the API module, navigate to the API directory and run:

```bash
uvicorn main:app --reload
```

The API will now be available at http://127.0.0.1:8000.

#### Running the Discord Bot

To run the Discord bot, navigate to the client directory and execute:

```bash
python main.py
```
### To run the whole app(optional)

You can easily start the entire application using Docker Compose. This will launch all necessary services defined in your docker-compose.yaml file.

From the root directory, execute the following command:

```bash
docker-compose up --build
```
This command will build and start all services, including the API and client components, allowing you to run the application seamlessly.

Make sure you have Docker and Docker Compose installed on your machine before executing this command.
