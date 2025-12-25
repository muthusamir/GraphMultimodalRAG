import openai

class MultimodalGenerator:
    def generate(self, context, query):
        prompt = f"Context: {context}\nQuery: {query}\nAnswer:"
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
