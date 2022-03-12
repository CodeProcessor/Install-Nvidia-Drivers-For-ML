import torch

print(f"GPU count\t\t: {torch.cuda.device_count()}")
print(f"Device list\t\t: {list(range(torch.cuda.device_count()))}")
print(f"Current device id\t: {torch.cuda.current_device()}")
print(f"Name of the device\t: {torch.cuda.get_device_name(torch.cuda.current_device())}")
print(f"Is PyTorch using GPU\t: {torch.cuda.is_available()}")
print("Memory Usage:")
print(f"\tAllocated: {torch.cuda.memory_allocated(device=torch.cuda.current_device())}")
print(f"\tCached: {torch.cuda.memory_allocated(device=torch.cuda.current_device())}")
print(f"\tMax Allocated: {torch.cuda.max_memory_allocated(device=torch.cuda.current_device())}")
print(f"\tMax Cached: {torch.cuda.memory_reserved(device=torch.cuda.current_device())}")

