import torch
print(f"GPU count: {torch.cuda.device_count()}")
print(f"Current device id: {torch.cuda.current_device()}")
print(f"Name of the device: {torch.cuda.get_device_name(torch.cuda.current_device())}")
print(f"Is PyTorch using GPU: {torch.cuda.is_available()}")
