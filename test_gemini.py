print("✅ Script started")

from core.llm import generate_text

print("✅ Imported generate_text")

# Take prompt input from user
prompt = input("\n📝 Enter your essay prompt/topic: ")

print("\n📤 Sending prompt to Gemini...\n")

output = generate_text(prompt)

print("📥 Gemini response received:\n")
print(output)
print("\nWord count:", len(output.split()))
