# vllm server
两个.py脚本，分别是带有continuous batching功能的server，还有用LLM做的speculative decoding server，都是用vllm库做的。目前都能跑，安装环境后可以直接跑。


## Running commands

```
serve run continuous_batching:deployment
```
```
python client1.py
```
```
serve run continuous_batching:deployment
```
```
python client2.py
```