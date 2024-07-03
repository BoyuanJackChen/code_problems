import json
from typing import List

from starlette.requests import Request
from starlette.responses import JSONResponse
from vllm import LLM, SamplingParams
from ray import serve


@serve.deployment(ray_actor_options={"num_gpus": 2})
class SpeculativeLLMServer:
    def __init__(self):
        pairs = ["facebook/opt-6.7b", "facebook/opt-125m",
         "lmsys/vicuna-7b-v1.5", "Jiayi-Pan/Tiny-Vicuna-1B"]
        self.llm = LLM(
            model="lmsys/vicuna-7b-v1.5",
            tensor_parallel_size=1,
            speculative_model="Jiayi-Pan/Tiny-Vicuna-1B",
            num_speculative_tokens=5,
            use_v2_block_manager=True,
        )

    async def __call__(self, request: Request) -> JSONResponse:
        request_dict = await request.json()
        prompts = request_dict.pop("prompts")
        sampling_params_dict = request_dict.pop("sampling_params")
        sampling_params = SamplingParams(**sampling_params_dict)

        outputs = self.llm.generate(prompts, sampling_params)
        results = []
        for output in outputs:
            prompt = output.prompt
            generated_text = output.outputs[0].text
            results.append({"prompt": prompt, "generated_text": generated_text})
        
        return JSONResponse(content={"results": results})

deployment = SpeculativeLLMServer.bind()
