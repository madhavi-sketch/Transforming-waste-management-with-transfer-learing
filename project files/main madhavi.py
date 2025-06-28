from model.transfer_learning_model import build_model

if __name__ == "__main__":
    model = build_model(num_classes=5)  # Example: 5 classes
    model.summary()
