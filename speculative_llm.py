from vllm import LLM, SamplingParams

prompts = [
    "The future of AI is",
]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

pairs = ["facebook/opt-6.7b", "facebook/opt-125m",
         "lmsys/vicuna-7b-v1.5", "Jiayi-Pan/Tiny-Vicuna-1B"]

llm = LLM(
    model="lmsys/vicuna-7b-v1.5",
    tensor_parallel_size=1,
    speculative_model="Jiayi-Pan/Tiny-Vicuna-1B",
    num_speculative_tokens=5,
    use_v2_block_manager=True,
)
outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")