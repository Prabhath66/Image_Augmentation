# 🖼️ Image Augmentation App

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=flat-square&logo=opencv&logoColor=white)](https://opencv.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Matrix%20Ops-013243?style=flat-square&logo=numpy&logoColor=white)](https://numpy.org/)
[![Live Demo](https://img.shields.io/badge/🤗%20Hugging%20Face-Live%20Demo-yellow?style=flat-square)](https://huggingface.co/spaces/Prabhath6/Image_Augmentation)

> **A real-time, browser-based image augmentation platform built with Python, OpenCV, and Streamlit — designed to supercharge AI and Computer Vision dataset preparation.**

🌐 **[Live Demo → Try it on Hugging Face Spaces](https://huggingface.co/spaces/Prabhath6/Image_Augmentation)**

---

## 📖 Table of Contents

- [About the Project](#-about-the-project)
- [Why Image Augmentation?](#-why-image-augmentation)
- [Features](#-features)
- [Augmentation Techniques](#-augmentation-techniques)
- [Demo](#-demo)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [How to Use](#-how-to-use)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🧠 About the Project

The **Image Augmentation App** is an interactive web application that lets you upload any image and instantly generate a batch of augmented variants using a wide range of geometric and photometric transformations — all from your browser, with zero code required.

It's built for **ML engineers**, **data scientists**, and **computer vision practitioners** who need to quickly expand training datasets, test model robustness, or simply visualize the effect of different transformations on an image.

Upload an image → choose your augmentations → set the count → download a ZIP. That's it.

---

## 💡 Why Image Augmentation?

Training deep learning models requires large, diverse datasets. Image augmentation artificially expands your dataset by creating realistic variations of existing images — improving:

- 📈 **Model generalization** — prevents overfitting on small datasets
- 🔄 **Data diversity** — introduces variance in angle, scale, brightness, and orientation
- ⚡ **Training efficiency** — more data without manual collection or labeling
- 🛡️ **Robustness** — trains models to handle real-world variability

This tool makes that process visual, fast, and accessible to anyone.

---

## ✨ Features

- 📤 **Image Upload** — supports JPG, JPEG, and PNG formats
- 🎛️ **Multi-select Augmentation Panel** — pick one or more techniques from the sidebar
- 🔢 **Batch Size Control** — generate anywhere from 1 to 100 augmented images in one click
- 🖼️ **Live Preview** — instantly preview the first 3 augmented images before downloading
- 📦 **ZIP Download** — all generated images packaged into a single downloadable ZIP file
- 🎲 **Randomized Parameters** — each augmented image uses randomly sampled transformation values for natural variety
- ⚡ **Real-time Processing** — powered by OpenCV for fast, in-memory transformation with no server-side storage

---

## 🔧 Augmentation Techniques

The app supports **11 augmentation operations**, including powerful combinations:

| # | Technique | Description |
|---|---|---|
| 1 | **Translation** | Randomly shifts the image along X and Y axes (±60px) |
| 2 | **Rotation** | Rotates the image by a random angle between -180° and +180° |
| 3 | **Scaling** | Randomly scales the image between 0.5× and 1.5× |
| 4 | **Shearing** | Applies random shear distortion along both axes |
| 5 | **Cropping** | Randomly crops a region and resizes it back to the original dimensions |
| 6 | **Brightness** | Randomly increases or decreases brightness by adding/subtracting pixel values |
| 7 | **Grayscale** | Converts the image to grayscale while keeping the 3-channel shape |
| 8 | **Flip Horizontally** | Mirrors the image left-to-right |
| 9 | **Flip Vertically** | Flips the image upside-down |
| 10 | **Translation + Scaling + Shearing** | Applies all three geometric transforms in a single affine matrix |
| 11 | **Translation + Rotation** | Combines rotation and translation via homogeneous matrix composition |

> All transformations use **affine/warp operations** with `BORDER_REFLECT` padding to avoid black border artifacts.

---

## 🎥 Demo

> 🔗 **[Launch the Live App](https://huggingface.co/spaces/Prabhath6/Image_Augmentation)**

No installation needed — the app is live on Hugging Face Spaces. Upload your image, select augmentation types, set the batch size, and download your augmented dataset as a ZIP in seconds.

---

## 🛠️ Tech Stack

| Technology | Role |
|---|---|
| **Python 3.9+** | Core language |
| **Streamlit** | Web UI framework |
| **OpenCV (`cv2`)** | Image transformations and processing |
| **NumPy** | Matrix operations for affine transforms |
| **io + zipfile** | In-memory ZIP packaging for batch download |

---

## 📁 Project Structure

```
Image_Augmentation/
│
├── app.py              # Main application — UI, augmentation logic, download handler
└── requirements.txt    # Python dependencies
```

### Core Functions in `app.py`

| Function | What it Does |
|---|---|
| `trans_rotat_scale()` | Applies translation, scaling, and shearing via a single affine matrix |
| `trans_rotation()` | Combines rotation and translation using homogeneous coordinates |
| `cropping()` | Random-crops and resizes back to original dimensions |
| `brightness()` | Randomly brightens or darkens using `cv2.add` / `cv2.subtract` |
| `grayscale()` | Converts to grayscale and back to BGR for channel consistency |
| `flip_horizontally()` | Horizontal flip via `cv2.flip(..., 1)` |
| `flip_vertically()` | Vertical flip via `cv2.flip(..., 0)` |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Prabhath66/Image_Augmentation.git
   cd Image_Augmentation
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   streamlit run app.py
   ```

5. Open your browser at `http://localhost:8501`

---

## 📌 How to Use

1. **Upload an Image** — Click "Choose an image" and upload a JPG, JPEG, or PNG file. The original image is displayed immediately.

2. **Select Augmentation Types** — In the left sidebar, use the multiselect dropdown to choose one or more augmentation techniques (e.g., Rotation, Brightness, Flip Horizontally).

3. **Set Batch Size** — Use the slider to choose how many augmented images you want to generate (1–100). Each image gets a randomly sampled variant of your selected transformations.

4. **Generate** — Click the **"Generate Augmented Images"** button. A live preview of 3 augmented images appears instantly.

5. **Download** — Click **"📁 Download Augmented Images ZIP file"** to save all generated images as a ZIP archive (`Augmented_images.zip`).

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repo
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add: your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

### Ideas for Contributions

- 🌀 Add noise augmentation (Gaussian, salt & pepper)
- 🎨 Add color jitter (hue, saturation, contrast shifts)
- 🔲 Add cutout / random erasing augmentation
- 📐 Add perspective/projective transform
- 🖼️ Support batch upload (multiple images at once)
- 📊 Show a histogram comparison of original vs augmented image
- 🧪 Add augmentation pipeline presets (e.g., "Object Detection Ready", "Classification Ready")

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

Made with ❤️ and 🖼️ by [Prabhath66](https://github.com/Prabhath66)

⭐ **If this project helped you, drop a star!** ⭐
