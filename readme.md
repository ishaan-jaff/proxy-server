
# liteLLM Proxy Server: 50+ LLM Models, Error Handling, Caching
### Azure, Llama2, OpenAI, Claude, Hugging Face, Replicate Models
[![PyPI Version](https://img.shields.io/pypi/v/litellm.svg)](https://pypi.org/project/litellm/)
[![PyPI Version](https://img.shields.io/badge/stable%20version-v0.1.345-blue?color=green&link=https://pypi.org/project/litellm/0.1.1/)](https://pypi.org/project/litellm/0.1.1/)
![Downloads](https://img.shields.io/pypi/dm/litellm)
[![litellm](https://img.shields.io/badge/%20%F0%9F%9A%85%20liteLLM-OpenAI%7CAzure%7CAnthropic%7CPalm%7CCohere%7CReplicate%7CHugging%20Face-blue?color=green)](https://github.com/BerriAI/litellm)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/_YF4Qj?referralCode=t3ukrU)

# What does liteLLM proxy do
- One server to make requests to all your LLM APIs: **Azure, OpenAI, Replicate, Anthropic, Hugging Face.** Support for 50+ models
- **Consistent Input/Output** Format
- **Error Handling** Using Model Fallbacks (if `GPT-4` fails, try `llama2`)
- **Logging** - Log Requests, Responses and Errors to Supabase, Posthog, Mixpanel, Sentry, Helicone (Any of the supported providers)
- **Token Usage & Spend** - Track Input + Completion tokens used + Spend/model
- **Caching** - Implementation of Semantic Caching
- **Key Management** - One Server for all your API Keys (use a `.env` or a secret manager here)
- **Streaming & Async Support** - Return generators to stream text responses


## API Endpoints

### `/chat/completions` (POST)

This endpoint is used to generate chat completions for 50+ support LLM API Models. Use llama2, GPT-4, Claude2 etc

#### Input
This API endpoint accepts all inputs in raw JSON and expects the following inputs
- `model` (string, required): ID of the model to use for chat completions. Refer to the model endpoint compatibility table for supported models.
 eg `gpt-3.5-turbo`, `gpt-4`, `claude-2`, `command-nightly`, `stabilityai/stablecode-completion-alpha-3b-4k`
- `messages` (array, required): A list of messages representing the conversation context. Each message should have a `role` (system, user, assistant, or function), `content` (message text), and `name` (for function role).
- Additional Optional parameters: `temperature`, `functions`, `function_call`, `top_p`, `n`, `stream`. See the full list of supported inputs here: https://litellm.readthedocs.io/en/latest/input/


##### example json
```
{
    "model": "gpt-3.5-turbo",
    "messages": [
                    { 
                        "content": "Hello, whats the weather in San Francisco??",
                        "role": "user"
                    }
                ]
    
}
```

#### Making an API request
```python
import requests
import json

# TODO: use your URL 
url = "http://localhost:5000/chat/completions"

payload = json.dumps({
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "content": "Hello, whats the weather in San Francisco??",
      "role": "user"
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)

```

### Output [Response Format]
Responses from the server are given in the following format. 
All responses from the server are returned in the following format (for all LLM models)
```
{
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "message": {
                "content": "I'm sorry, but I don't have the capability to provide real-time weather information. However, you can easily check the weather in San Francisco by searching online or using a weather app on your phone.",
                "role": "assistant"
            }
        }
    ],
    "created": 1691790381,
    "id": "chatcmpl-7mUFZlOEgdohHRDx2UpYPRTejirzb",
    "model": "gpt-3.5-turbo-0613",
    "object": "chat.completion",
    "usage": {
        "completion_tokens": 41,
        "prompt_tokens": 16,
        "total_tokens": 57
    }
}
```


### Supported models

OpenAI Chat Completion Models:
gpt-4
gpt-4-0613
gpt-4-32k

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



