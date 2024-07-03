# code_problems
两个.py脚本，分别是带有continuous batching功能的server，还有用LLM做的speculative decoding server，都是用vllm库做的。目前都能跑，安装环境后可以直接跑。

现在server跑完就自动结束了，我想把它变成永久的，然后在另一个.py文件里，可以开client随时访问。不需要优化或改变任何server内部代码和参数。只要让它永久开着就可以。
