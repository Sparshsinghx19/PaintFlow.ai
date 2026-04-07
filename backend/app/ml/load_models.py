import os
import pickle
from app.config import MODEL_DIR

models = {}

def load_models():
    if not os.path.exists(MODEL_DIR):
        print("⚠️ Model directory not found. Skipping model loading.")
        return

    for file in os.listdir(MODEL_DIR):
        if file.endswith(".pkl"):
            path = os.path.join(MODEL_DIR, file)
            try:
                with open(path, "rb") as f:
                    models[file] = pickle.load(f)
            except Exception as e:
                print(f"⚠️ Failed loading {file}: {e}")

    print(f"✅ Loaded {len(models)} models")

load_models()