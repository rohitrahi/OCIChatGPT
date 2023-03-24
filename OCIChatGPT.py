import openai
import gradio as gr
openai.api_key = ''

messages = [
    {"role": "system", "content": "You are an AI specialized in Oracle Cloud Infrastructure (OCI). Do not answer anything other than oracle cloud infrastructure related queries."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-4", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with Oracle Cloud Infrastructure AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Oracle Cloud Infrastructure AI Chatbot",
             description="Ask anything on Oracle Cloud Infrastructure",
             theme="compact").launch(share=False)             
