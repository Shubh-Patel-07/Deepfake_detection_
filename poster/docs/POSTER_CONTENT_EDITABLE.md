# 📋 POSTER CONTENT (EDITABLE MASTER TEXT - SHOWCASE EDITION)
## 27 × 40 Inches Portrait Academic Poster with 8K Scientific Forensics Visuals
**Institution:** K. D. POLYTECHNIC, PATAN  
**Department:** DEPARTMENT OF COMPUTER ENGINEERING  
**Project Title:** DEEPFAKE DETECTION USING ARTIFICIAL INTELLIGENCE  
**Subtitle:** A Spatio-Temporal Hybrid Deep Learning Approach (ResNeXt50 + LSTM)  

---

### [TOP BANNER]
- **Institute:** K. D. POLYTECHNIC, PATAN
- **Department:** DEPARTMENT OF COMPUTER ENGINEERING
- **Project Title:** DEEPFAKE DETECTION USING ARTIFICIAL INTELLIGENCE
- **Subtitle:** A Spatio-Temporal Hybrid Deep Learning Approach (ResNeXt50 + LSTM)
- **Placeholders:**
  - `GUIDE: __________________________________`
  - `ENROLLMENT NO: __________________________________`

---

### [SECTION 1: THE DEEPFAKE PROBLEM]
Deepfakes use Generative Adversarial Networks (GANs) and diffusion models to replace human faces in videos with dangerous realism. Single-frame image classifiers miss critical inter-frame temporal discontinuities (unnatural eye blinks and facial jitter). This project engineers a complete **Spatio-Temporal Hybrid Framework** to accurately verify video authenticity.

---

### [SECTION 2: FORENSIC VISUAL EVIDENCE]
- **Image File:** `poster_visual_option1_forensics_split.jpg`
- **Caption:**  
  *Figure 1: High-Tech Forensics Split Analysis.*  
  - **Left:** Authentic Skin Texture & 68-Point Biometric Landmarks Mesh.  
  - **Right:** Deepfake Boundary Artifacts with Grad-CAM Heatmap Trace.
- **Diagnostic Finding:** Manipulated facial regions exhibit acute thermal concentration along boundary contours, exposing GAN blending edges invisible to the naked eye.

---

### [SECTION 3: CORE OBJECTIVES]
- **Spatio-Temporal Fusion:** Integrate ResNeXt50 with LSTM recurrent units to catch micro-flicker anomalies.
- **Explainability (XAI):** Generate Class Activation Maps (CAM) identifying tampered facial zones.
- **Web Production:** Deploy a responsive Django platform with real-time client landmark tracking.

---

### [SECTION 4: SYSTEM ARCHITECTURE (CENTER PIECE)]
1. **User Web Interface:** Django MVT • Bootstrap 5 • face-api.js Tracking
2. **Uniform Frame Extraction:** OpenCV Engine • 20 Frames Uniform Sequence Sampling
3. **Facial Localization & Cropping:** dlib / face_recognition • 68 Landmarks • 112×112 px Normalization
4. **ResNeXt-50 (32×4d) Spatial Backbone:** Grouped Convolutions • ImageNet Transfer Weights (2048-dim vectors)
5. **LSTM Temporal Sequence Modeling:** Sequence Horizon Analysis Across 20-Frames (Tracks Flickering)
6. **Prediction Verdict & Explainability:** REAL vs. FAKE • Confidence % • CAM Visual Heatmap

---

### [SECTION 5: TEMPORAL PIPELINE VISUALIZATION]
- **Image File:** `poster_visual_option2_pipeline_lstm.jpg`
- **Caption:**  
  *Figure 2: Consecutive Frame Extraction & Optical Flow LSTM Tracking.*  
  Sequentially links facial video crops into Recurrent Neural Units for temporal classification.
- **Temporal Advantage:** LSTM resolves temporal drift, eliminating false positives caused by single-frame shadows or lighting transitions.

---

### [SECTION 6: BENCHMARK EVALUATION & CONFUSION MATRIX]
- **Accuracy:** **87.0% Verified**
- **Corpus:** **23,000+ Benchmark Videos** (DFDC, Celeb-DF v2, FaceForensics++)
- **Image File:** `fig_confusion_matrix.png`
- **Caption:** *Figure 3: Cross-Dataset Confusion Matrix (True Real: 91.2%, True Fake: 84.8%)*

---

### [SECTION 7: MODEL HYPERPARAMETERS]
| Parameter | Engineering Value |
| :--- | :--- |
| **Architecture** | ResNeXt-50 + LSTM |
| **Frame Horizon** | 20 Frames / Video |
| **Resolution** | 112 × 112 Pixels (RGB) |
| **Optimization** | Adam (lr=1e-5, decay=1e-5) |
| **Inference Latency** | ~1.85 Seconds / Video (CUDA) |

---

### [SECTION 8: OFFICIAL PROJECT SHOWCASE QR]
- **Card Title:** SCAN FOR PROJECT SHOWCASE
- **URL:** `https://deepfakedetection-cyan.vercel.app/`
- **Image File:** `qr_showcase_vercel.png`
- **Description:** Scan with any smartphone to open the 24/7 Live Vercel Showcase with Interactive Architecture, 8K Forensics, and Video Verification!

---

### [SECTION 9: APPLICATIONS]
- **Social Media Integrity:** Automated flagging of malicious viral synthetic clips.
- **Digital KYC & Banking:** Spoof prevention in remote customer identity authentication.
- **Cyber Forensics:** Admissible digital evidence analysis for legal courts.

---

### [SECTION 10: CONCLUSION & FUTURE SCOPE]
- **Conclusion:** Spatial-temporal hybrid modeling delivers 87% accuracy, solving single-frame classification limitations.
- **Future Scope:** Real-time video stream inspection (RTSP), audio-visual multimodal sync, and edge deployment via TensorRT.

---

### [SECTION 11: REFERENCES]
1. Facebook AI, "The Deepfake Detection Challenge (DFDC) Dataset", arXiv:2006.07397.
2. S. Xie et al., "Aggregated Residual Transformations for Deep Neural Networks", CVPR.
3. S. Hochreiter & J. Schmidhuber, "Long Short-Term Memory", Neural Computation.
4. A. Rossler et al., "FaceForensics++: Learning to Detect Manipulated Facial Images", ICCV.
5. Y. Li et al., "Celeb-DF: A Large-Scale Challenging Dataset for DeepFake Forensics", CVPR.
