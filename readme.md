
# liteLLM Proxy Server: 50+ LLM Models, Error Handling, Caching
### Azure, Llama2, OpenAI, Claude, Hugging Face, Replicate Models
[![PyPI Version](https://img.shields.io/pypi/v/litellm.svg)](https://pypi.org/project/litellm/)
[![PyPI Version](https://img.shields.io/badge/stable%20version-v0.1.345-blue?color=green&link=https://pypi.org/project/litellm/0.1.1/)](https://pypi.org/project/litellm/0.1.1/)
![Downloads](https://img.shields.io/pypi/dm/litellm)
[![litellm](https://img.shields.io/badge/%20%F0%9F%9A%85%20liteLLM-OpenAI%7CAzure%7CAnthropic%7CPalm%7CCohere%7CReplicate%7CHugging%20Face-blue?color=green)](https://github.com/BerriAI/litellm)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/_YF4Qj?referralCode=t3ukrU)

# What does this Repo do
- One server to make requests to all your LLM APIs: Azure, OpenAI, Replicate, Hugging Face. Support for 50+ models
- Consistent Input/Output Format
- Error Handling Using Model Fallbacks (if `GPT-4` fails, try `llama2`)
- Logging - Log Requests, Responses and Errors to Supabase, Posthog, Mixpanel, Sentry, Helicone (Any of the supported providers)
- Caching - Implementation of Semantic Caching


## API Endpoints

### `/chat/completions` (POST)

This endpoint is used to generate chat completions. It takes in JSON data with the following parameters:

- `model` (string, required): ID of the model to use for chat completions. Refer to the model endpoint compatibility table for supported models.
- `messages` (array, required): A list of messages representing the conversation context. Each message should have a `role` (system, user, assistant, or function), `content` (message text), and `name` (for function role).
- Additional parameters for controlling completions, such as `temperature`, `top_p`, `n`, etc.

Example JSON payload:

```json
{
"model": "gpt-3.5-turbo",
"messages": [
 {"role": "system", "content": "You are a helpful assistant."},
 {"role": "user", "content": "Knock knock."},
 {"role": "assistant", "content": "Who's there?"},
 {"role": "user", "content": "Orange."}
],
"temperature": 0.8
}
```


## Input Parameters
model: ID of the language model to use.
messages: An array of messages representing the conversation context.
role: The role of the message author (system, user, assistant, or function).
content: The content of the message.
name: The name of the author (required for function role).
function_call: The name and arguments of a function to call.
functions: A list of functions the model may generate JSON inputs for.
Various other parameters for controlling completion behavior.
Supported Models
The proxy server supports the following models:

OpenAI Chat Completion Models:
gpt-4
gpt-4-0613
gpt-4-32k
...
OpenAI Text Completion Models:
text-davinci-003
Cohere Models:
command-nightly
command
...
Anthropic Models:
claude-2
claude-instant-1
...
Replicate Models:
replicate/
OpenRouter Models:
google/palm-2-codechat-bison
google/palm-2-chat-bison
...
Vertex Models:
chat-bison
chat-bison@001

Refer to the model endpoint compatibility table for more details.

Refer to the model endpoint compatibility table for more details.

