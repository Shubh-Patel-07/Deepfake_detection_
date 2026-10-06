# 🛡️ AI-Powered Deepfake Video Detection System
> **A Spatio-Temporal Hybrid Deep Learning Framework using ResNeXt50 + LSTM**  
> *Developed for Academic & Technical Research — K. D. Polytechnic, Patan*

[![Python Version](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python)](https://python.org)
[![Deep Learning Framework](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?logo=pytorch)](https://pytorch.org)
[![Web Framework](https://img.shields.io/badge/Django-4.2+-092E20?logo=django)](https://djangoproject.com)
[![Model Accuracy](https://img.shields.io/badge/Accuracy-87%25-success)](https://github.com/Shubh-Patel-07/Deepfake_detection_)
[![Live Showcase](https://img.shields.io/badge/Showcase-Vercel-black?logo=vercel)](https://deepfakedetection-cyan.vercel.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🌐 Live Demonstrations & Links

- **🚀 Interactive Project Showcase:** [https://deepfakedetection-cyan.vercel.app/](https://deepfakedetection-cyan.vercel.app/)
- **⚡ Live AI Detection Engine (Ngrok Tunnel):** [https://petite-discover-precut.ngrok-free.dev/](https://petite-discover-precut.ngrok-free.dev/)
- **📦 GitHub Repository:** [https://github.com/Shubh-Patel-07/Deepfake_detection_](https://github.com/Shubh-Patel-07/Deepfake_detection_)

---

## 📌 Executive Summary

With the rapid emergence of high-fidelity Generative Adversarial Networks (GANs), autoencoders, and diffusion synthesis tools, malicious deepfakes have become nearly indistinguishable to the human eye. Most conventional detection models evaluate isolated frames, missing critical inter-frame temporal inconsistencies like micro-jitter, abnormal blink intervals, and illumination phase shifts.

This project introduces a **Spatio-Temporal Hybrid Deep Learning Architecture**:
1. **ResNeXt-50 (32×4d Backbone):** Extracts 2048-dimensional spatial representations and blending boundary anomalies from individual face crops.
2. **LSTM (Long Short-Term Memory Network):** Evaluates sequential time-series dynamics across a 20-frame continuous horizon to capture temporal incoherence.
3. **Class Activation Mapping (CAM):** Generates transparent heatmaps highlighting manipulated facial segments for explainable AI (XAI).

---

## 🏗️ System Architecture & Workflow

```
[ User Video Upload (MP4 / AVI) ]
                │
                ▼
[ Uniform Frame Extraction: OpenCV ] ──> Extracts 20 Sequence Frames
                │
                ▼
[ Facial Localization: dlib / face_recognition ] ──> 68 Landmark Bounding Box
                │
                ▼
[ Preprocessing & Normalization ] ──> Crop to 112×112 px & ImageNet Standard
                │
                ▼
[ Spatial Feature Extraction: ResNeXt-50 (32×4d) ] ──> 2048-dim Latent Vectors
                │
                ▼
[ Temporal Modeling: LSTM Network ] ──> Inter-Frame Transition Analysis
                │
                ▼
[ Classification Head ] ──> Dropout(0.4) + Dense Layer + Sigmoid
                │
                ▼
[ Final Decision Output: REAL / FAKE + Confidence % + CAM Heatmap ]
```

---

## 📊 Benchmark Datasets & Performance

The model is trained and cross-evaluated on three premier forensic benchmarks:
- **DFDC (Deepfake Detection Challenge by Meta / Facebook AI):** 100,000+ total video clips.
- **Celeb-DF (v2):** 5,639 high-definition celebrity deepfake videos.
- **FaceForensics++ (FF++):** Diverse manipulation methods (Deepfakes, FaceSwap, Face2Face).

### 📈 Comparative Metrics
| Metric | Baseline ResNet-50 | Our ResNeXt-50 + LSTM Model | Improvement |
| :--- | :--- | :--- | :--- |
| **Accuracy** | 78.4% | **87.0%** | **+8.6%** |
| **Precision** | 79.1% | **88.2%** | **+9.1%** |
| **Recall** | 76.8% | **85.9%** | **+9.1%** |
| **F1-Score** | 77.9% | **87.0%** | **+9.1%** |
| **False Positive Rate**| 21.6% | **12.4%** | **-9.2%** |

---

## ⚙️ Model Hyperparameters

| Hyperparameter | Value | Rationale |
| :--- | :--- | :--- |
| **Backbone CNN** | `resnext50_32x4d` | Grouped convolutions capture high-cardinality boundary artifacts |
| **Sequence Length** | 20 Frames | Statistically optimal for temporal blinks with sub-2s latency |
| **Input Resolution** | 112 × 112 RGB | Minimizes memory footprint by 75% compared to 224×224 |
| **Optimizer** | Adam (`lr=1e-5`, `decay=1e-5`) | Stable convergence without gradient explosion |
| **Loss Function** | Binary Cross-Entropy (`BCEWithLogitsLoss`) | Optimal penalty for probabilistic binary classifications |
| **Regularization** | Dropout (`p=0.4`) | Prevents overfitting to specific GAN artifacts |

---

## 💻 Tech Stack

- **Deep Learning:** PyTorch, torchvision, CUDA Toolkit
- **Computer Vision:** OpenCV (`cv2`), `dlib`, `face_recognition`, `face-api.js`
- **Backend Architecture:** Python 3.12, Django 4.2+ (MVT Pattern)
- **Frontend Interface:** Bootstrap 5, Modern Vanilla JS, HTML5 Canvas
- **Deployment & Production:** Docker, Gunicorn, Nginx, Ngrok Tunneling

---

## 🚀 Quickstart Guide (Local Installation)

### 1. Clone the Repository
```bash
git clone https://github.com/Shubh-Patel-07/Deepfake_detection_.git
cd Deepfake_detection_
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux / macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r "Django Application\requirements.txt"
```

### 4. Run Migrations & Start Django Server
```bash
cd "Django Application"
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```
Visit `http://localhost:8000/` in your browser.

---

## 🌍 Exposing to Live Mobile Demo via Ngrok

To allow external judges or mobile devices to test live video inference:
```bash
# In a separate terminal:
ngrok http 8000
```
Update `ALLOWED_HOSTS` in `Django Application/project_settings/settings.py` or use your current public ngrok domain.

---

## 📁 Repository Directory Structure

```
Deepfake_detection_/
├── Django Application/             # Production Web Application
│   ├── ml_app/                    # Core inference engine & templates
│   │   ├── views.py               # Video processing & PyTorch inference
│   │   ├── templates/             # HTML interface & result pages
│   │   └── models/                # Pretrained model weights
│   ├── project_settings/          # Django configuration & routes
│   ├── static/                    # Stylesheets, JS scripts, and brand assets
│   ├── Dockerfile                 # Containerized deployment spec
│   └── requirements.txt           # Python dependency manifest
├── Model Creation/                 # Training notebooks & dataset scripts
│   ├── Model_and_train_csv.ipynb  # PyTorch model training pipeline
│   ├── Predict.ipynb              # Test inference verification
│   └── Helpers/                   # Dataset balancing and filtering utilities
├── poster/                        # Competition Poster Templates
│   └── poster.html                # 27x40 inch portrait academic poster
├── website/                       # Static showcase portal source code
├── TESTING VIDEO/                 # Real & Fake benchmark test videos
└── README.md                      # Primary project documentation
```

---

## 👥 Authors & Academic Affiliation

- **Lead Developer:** Shubh Patel ([GitHub](https://github.com/Shubh-Patel-07) • [LinkedIn](https://www.linkedin.com/in/gjcompshubh123/))
- **Institution:** K. D. Polytechnic, Patan
- **Department:** Department of Computer Engineering
