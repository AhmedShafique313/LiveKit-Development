# LiveKit AI Voice Agent

## Project Overview

This project demonstrates the creation of a real-time AI voice agent using LiveKit, enabling natural and responsive voice interactions with users. It leverages a pipeline of Speech-to-Text (STT), Large Language Model (LLM), and Text-to-Speech (TTS) technologies to process voice input, generate intelligent responses, and deliver them back to the user in real-time. This architecture allows for versatile applications, including AI-powered customer service, interactive voice response (IVR) systems, virtual assistants, and more. The agent uses LiveKit for robust real-time audio streaming and management, ensuring low-latency and high-quality voice communication, crucial for a seamless user experience.

The primary goal of this project is to provide a reference implementation and a starting point for developers looking to build their own AI-powered voice agents with LiveKit. It showcases how to integrate various components like STT, LLM, and TTS services with LiveKit to create a functional and scalable voice agent.

## Features

*   **Real-time STT -> LLM -> TTS Pipeline:** The core of the project lies in its real-time voice processing pipeline. Speech from the user is converted to text using STT, the text is then processed by an LLM to generate a contextually relevant response, and finally, the LLM's text response is converted back to speech using TTS. This entire process occurs with minimal delay, enabling fluid and natural-sounding conversations.
*   **Low-Latency Communication with LiveKit:** LiveKit provides the underlying infrastructure for real-time audio streaming. Its optimized architecture minimizes latency and ensures high audio quality, which is critical for a responsive and engaging voice agent experience.
*   **Twilio Outbound Call Integration:** The agent can initiate outbound calls via Twilio, enabling proactive engagement with users. This feature allows for use cases such as automated customer outreach, appointment reminders, and more.
*   **Customizable Agent Logic:** The LLM component allows for customization of the agent's behavior and knowledge base. By fine-tuning the LLM or providing it with specific prompts and data, you can tailor the agent to specific use cases and domains.
*   **Scalable Architecture:** LiveKit's architecture allows for scaling the agent to handle multiple concurrent conversations. This scalability is essential for building voice agents that can handle a large volume of user interactions.

## Architecture

The following diagram illustrates the high-level architecture of the AI Voice Agent:

bash
    npm install -g livekit-cli
        Create a `.env` file in the root directory of your project. This file will store your API keys and credentials.

    > Replace the placeholder values with your actual API keys and credentials. The specific names and requirements for environment variables may vary depending on the STT, LLM, and TTS services you choose. Consult the documentation for each service for details.  For local development, consider using `ngrok` to expose your local server and use that URL in your Twilio configuration.

### Configuration

1.  **Configure LiveKit:**

    Ensure your LiveKit server is running and accessible. You can use [LiveKit Cloud](https://cloud.livekit.io/) or self-host a LiveKit server.

2.  **Configure Twilio (if using outbound calls):**

    *   Obtain your Account SID and Auth Token from the [Twilio website](https://www.twilio.com/).
    *   Purchase a Twilio phone number.
    *   Configure the Twilio phone number to point to your application's webhook URL.  This will likely involve setting up a TwiML application to handle incoming calls.

3.  **Configure STT, LLM, and TTS services:**

    *   Create accounts and obtain API keys for your chosen STT, LLM, and TTS services (e.g., Google Cloud Speech-to-Text, OpenAI, Google Cloud Text-to-Speech).
    *   Update the `.env` file with the appropriate API keys.
    *   Configure the necessary settings for each service, such as the language model, voice, and region.

## Usage

### Running the AI Voice Agent

1.  **Create a LiveKit room and start the agent:**

bash
    lk dispatch create --new-room --agent-name my-outbound-agent
        > The `lk dispatch create` command simplifies the process of creating a LiveKit room and launching an agent. The `--new-room` flag tells the CLI to create a new LiveKit room for the agent. The `--agent-name` flag assigns a name to the agent, which can be useful for identifying and managing multiple agents. Refer to the [LiveKit CLI documentation](https://github.com/livekit/livekit-cli) for more details on available options and customization.  For example, you might want to configure the room's audio codecs or participant limits.

2.  **Connect to the room:**

    Use a LiveKit client (e.g., JavaScript, Swift, or Android) to connect to the room. You can use the LiveKit example applications as a starting point or build your own client from scratch.  See the [LiveKit documentation](https://docs.livekit.io/) for client SDKs and examples.

3.  **Interact with the agent:**

    Once connected to the room, you can speak to the agent, and it will respond in real-time. The agent will process your speech, generate a response using the LLM, and speak the response back to you.

### Code Snippets

#### Example: Connecting to a LiveKit Room (JavaScript)

> Remember to replace `'ws://localhost:7880'` with your LiveKit server URL and `<your_livekit_token>` with a valid LiveKit token. You can generate tokens using the LiveKit API or the `livekit-cli`. Ensure that your LiveKit server is running and accessible before running this code. Also, remember to install the livekit-client library using npm or yarn.

## Contributing

> We welcome contributions to this project! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute.

## License

> This project is licensed under the [LICENSE](LICENSE) file.
