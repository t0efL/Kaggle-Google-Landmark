import torch

PATHTOLOAD = "/checkpoints/224_b0_cleaned/best.pt"
PATHTOSAVE = "/checkpoints/224_b0_cleaned/model.pt"

model = torch.load(PATHTOLOAD, map_location="cuda:0")["model"]
torch.save({"model": model}, PATHTOSAVE)
