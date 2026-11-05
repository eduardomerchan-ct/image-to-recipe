# Image to Recipe

A LangChain vision agent that looks at a photo of ingredients, works out what's in it, and searches the web for a recipe that uses only those ingredients.

## How it works

1. **Pick a photo:** a file picker opens (or you type a path) for a PNG, JPG or WebP image.
2. **Encode it:** `photo_decoder.py` turns the image into a base64 data URL and wraps it in a multimodal message.
3. **Run the agent:** a LangChain agent backed by Claude identifies the ingredients, then calls a `web_search` tool (Tavily) to find a matching recipe.
4. **Print the recipe:** the agent's final answer is printed to the terminal.

## Project layout

| File | Purpose |
|---|---|
| `main.py` | Entry point: builds the agent, picks the image, runs it |
| `photo_decoder.py` | File picker and image → message encoding |
| `tools.py` | `web_search` tool backed by the Tavily API |
| `prompt.py` | System and user prompts for the agent |

## Setup

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

Create a `.env` file with:

```
ANTHROPIC_API_KEY=...
TAVILY_API_KEY=...
```

Then run:

```bash
uv run main.py
```

## Tech stack

LangChain agents · Anthropic Claude (vision) · Tavily search API · uv
