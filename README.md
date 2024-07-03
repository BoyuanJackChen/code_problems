# vllm server
Two servers implemented from vllm, one can do continuous batching; the other can do speculative decoding. Install the requirements and run the commands right away. 

## TODO:
The server only uses 1 gpu at a time... Need to fix this.

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