

import pickle
import os
from app.config import MODEL_DIR

models = {}

def load_all_models():
    global models
    for file in os.listdir(MODEL_DIR):
        if file.endswith(".pkl"):
            path = os.path.join(MODEL_DIR, file)
            with open(path, "rb") as f:
                models[file] = pickle.load(f)

    print(f"✅ Loaded {len(models)} models")

load_all_models()