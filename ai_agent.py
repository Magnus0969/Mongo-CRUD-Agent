import json
import os
from mongo_crud_tool import MongoCRUD
from ollama_llm import query_ollama
import re

crud = MongoCRUD(os.getenv("DB_NAME"))

# Prompt template for Mistral
AGENT_PROMPT_TEMPLATE = """
You are a MongoDB assistant agent.

Given an instruction from the user, extract a MongoDB operation and return a JSON response in the following format:

{
  "operation": "create" | "read" | "update" | "delete",
  "collection": "<collection_name>",
  "query": { ... },          // MongoDB filter query (can be empty for create)
  "data": { ... }            // Optional: For insert or update operations
}

Examples:
Instruction: "Add a user named Alice with age 30 to the users collection."
→ Output:
```json
{
  "operation": "create",
  "collection": "users",
  "query": {},
  "data": {
    "name": "Alice",
    "age": 30
  }
}
```

Instruction: "Find all users older than 25."
→ Output:
```json
{
  "operation": "read",
  "collection": "users",
  "query": {
    "age": { "$gt": 25 }
  },
  "data": {}
}
```

Now respond to this instruction:
Instruction: "{instruction}"

ONLY return valid JSON inside a markdown block like json ... with no explanation.

"""

def extract_json_from_markdown(text):
    """Extract JSON object from a markdown-formatted string with triple backticks."""
    if "```json" in text:
        start = text.index("```json") + len("```json")
        end = text.index("```", start)
        return text[start:end].strip()
    return text.strip()

def handle_user_input(instruction: str):
    prompt = instruction  # ← simplified since system prompt is in model
    raw_response = query_ollama(prompt)
    json_string = extract_json_from_markdown(raw_response)

    try:
        parsed = json.loads(json_string)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON from model:\n" + raw_response)

    operation = parsed.get("operation")
    collection = parsed.get("collection")
    query = parsed.get("query", {})
    data = parsed.get("data", {})

    if operation == "create":
        return crud.create(collection, data)
    elif operation == "read":
        return crud.read(collection, query)
    elif operation == "update":
        return crud.update(collection, query, data)
    elif operation == "delete":
        return crud.delete(collection, query)
    else:
        raise ValueError(f"Unknown operation: {operation}")
