import os
import typing as t

import openai
from _types import Message, Parameters, Role
from mistralai.client import MistralClient # type: ignore
from mistralai.models.chat_completion import ChatMessage # type: ignore
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam


def _chat_openai(
    client: OpenAI, messages: t.List[Message], parameters: Parameters
) -> Message:
    response = client.chat.completions.create(
        model=parameters.model,
        messages=t.cast(t.List[ChatCompletionMessageParam], messages),
        temperature=parameters.temperature,
        max_tokens=parameters.max_tokens,
        top_p=parameters.top_p,
    )

    response_message = response.choices[0].message
    return Message(
        role=Role(response_message.role), content=str(response_message.content)
    )


def chat_openai(messages: t.List[Message], parameters: Parameters) -> Message:
    return _chat_openai(OpenAI(), messages, parameters)


def chat_mistral(
    messages: t.List[Message], parameters: Parameters
) -> Message:
    client = MistralClient()
    messages = [
        ChatMessage(role=message.role, content=message.content) for message in messages
    ]

    response = client.chat(
        model=parameters.model,
        messages=messages,
        temperature=parameters.temperature,
        max_tokens=parameters.max_tokens,
        top_p=parameters.top_p,
    )
    response_message = response.choices[-1].message
    return Message(role=response_message.role, content=response_message.content)

def embed_mistral(contents: t.List[str]) -> t.List[t.List[float]]:
    client = MistralClient()
    response = client.embeddings('mistral-embed', contents)
    return [d.embedding for d in response.data]

def chat_together(messages: t.List[Message], parameters: Parameters) -> Message:
    client = openai.OpenAI(
        api_key=os.environ["TOGETHER_API_KEY"],
        base_url="https://api.together.xyz/v1",
    )

    return _chat_openai(client, messages, parameters)
