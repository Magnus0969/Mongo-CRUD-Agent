import subprocess

def run_ai_instruction(instruction: str):
    print(f"\n🧠 Instruction: {instruction}")
    result = subprocess.run(
        ["python", "main.py", "ai", instruction],
        capture_output=True,
        text=True
    )
    if result.stdout:
        print("✅ Output:")
        print(result.stdout.strip())
    if result.stderr:
        print("❌ Error:")
        print(result.stderr.strip())

if __name__ == "__main__":
    print("🧪 Testing MongoAI Agent with Natural Language Prompts...")

    # 1. Create
    run_ai_instruction("Add a user named Alice with age 30 to the users collection")

    # 2. Read
    run_ai_instruction("Find all users named Alice")

    # 3. Update
    run_ai_instruction("Update age of Alice to 31")

    # 4. Read again to confirm update
    run_ai_instruction("Show me users named Alice")

    # 5. Delete
    run_ai_instruction("Remove user named Alice from the database")

    # 6. Final read to confirm deletion
    run_ai_instruction("List all users named Alice")
