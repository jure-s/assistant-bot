import pickle

FILENAME = "assistant_data.pkl"

def save_data(data):
    with open(FILENAME, "wb") as f:
        pickle.dump(data, f)
    print("Data saved.")

def load_data():
    try:
        with open(FILENAME, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {"contacts": {}, "notes": []}