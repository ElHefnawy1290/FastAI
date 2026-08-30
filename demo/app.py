import gradio as gr
import spaces
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
zero = torch.Tensor([0]).to(device)
print(zero.device)

@spaces.GPU
def greet(n):
    print(zero.device)
    return f"Hello {zero + n} Tensor"

demo = gr.Interface(fn=greet, inputs=gr.Number(), outputs=gr.Text())
demo.launch()