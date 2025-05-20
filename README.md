
# Instrument Classifier App

A simple web app that identifies musical instruments in images using a deep learning model. Built with **Streamlit**, **FastAPI**, and **PyTorch**, this project showcases a full-stack AI-powered application — from model inference to a user-friendly UI.

---

## Features

- Upload an image of a musical instrument
- Get a prediction using a pre-trained ResNet model
- FastAPI backend for inference
- Streamlit frontend for clean user interaction
- Modular structure, Docker-ready (optional)

---

## Tech Stack

- **Frontend:** Streamlit
- **Backend:** FastAPI
- **Model:** PyTorch + torchvision (ResNet18)
- **Image Processing:** PIL, torchvision.transforms

---

## Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/Monique64/instrument-classifier.git
cd instrument-classifier
```

### 2. Install Dependencies

It's recommended to use a virtual environment:

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
./run.sh
```

This will start:
- FastAPI backend at `http://localhost:8000`
- Streamlit frontend at `http://localhost:8501`

---

## Project Structure

```
instrument-classifier/
├── app/
│   ├── main.py          # Streamlit UI
│   ├── api.py           # FastAPI backend
│   ├── model/
│   │   └── classifier.py  # PyTorch model logic
│   └── utils.py         # Utility functions (optional)
├── assets/              # Sample images, screenshots
├── requirements.txt     # Python dependencies
├── run.sh               # Script to run both frontend and backend
└── README.md
```

---

## Future Improvements

- Add real instrument dataset and fine-tune the model
- Add drag-and-drop UI and mobile support
- Deploy to Hugging Face Spaces or Heroku

---

## License

MIT License

---

## Author

Built with curiosity and code by **Monique64**  
GitHub: [@Monique64](https://github.com/Monique64)
