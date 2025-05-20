
import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image

# Mock instrument labels
LABELS = ['Violin', 'Trumpet', 'Flute', 'Piano', 'Guitar']

# Load a pretrained model and modify for 5 instrument classes
def load_model():
    model = models.resnet18(pretrained=True)
    num_features = model.fc.in_features
    model.fc = torch.nn.Linear(num_features, len(LABELS))
    model.eval()
    return model

# Transform input image to match model expectations
def transform_image(image_bytes):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])
    image = Image.open(image_bytes).convert('RGB')
    return transform(image).unsqueeze(0)  # Add batch dimension

# Predict the class label
def get_prediction(model, image_tensor):
    with torch.no_grad():
        outputs = model(image_tensor)
        _, predicted = torch.max(outputs, 1)
        return LABELS[predicted.item()]
