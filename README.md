# RAG Discord Bot

Welcome to the RAG Discord Bot project! This document provides an overview of the project, its goals, and the technologies we'll be using.

## Project Overview

The RAG (Retrieve and Generate) Discord Bot aims to enhance our Discord server by providing intelligent responses based on our discussions and general club information. The project will span a month and is designed to be manageable within that timeframe.


![image](https://github.com/user-attachments/assets/175d2671-3920-461c-903c-d868dd7749ad)


### Use Cases

1. **Transcript Querying**: The bot will be able to refer to the transcripts of our discussions and answer questions based on them.
2. **General Club Information**: The bot will provide information about announcements and club resources.

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

Feel free to contribute to the project by submitting issues, suggestions, or pull requests. We encourage learning and collaboration throughout the development process. Please go through our [Contribution Guideline](./CONTRIBUTION.MD) before contributing in our code base.

## Contact

If you have any questions or doubts, please reach out to me at mohantej@buffalo.edu or ping us in the Discord server.

Looking forward to working with you all!
