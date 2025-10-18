# OpenCV-RPi-Setup
Automated OpenCV installation for Raspberry Pi 4 &amp; 5 with all necessary dependencies. Includes a ready-to-use test script to verify installation.

Perfect! You already have a detailed setup guide. I can help you **convert this into a clean GitHub repo README.md** that’s well-formatted and professional. Here’s how it would look:

---

# **OpenCV Setup on Raspberry Pi **

Raspberry Pi leverages its computational capabilities and libraries like **OpenCV** to detect and recognize human faces, etc. It's an affordable and powerful platform for applications such as **security systems, access control, and attendance tracking**.

---

## **Setting Up OpenCV**

This guide provides **step-by-step instructions** to set up OpenCV from scratch on your Raspberry Pi.

---

### **1. Install Necessary Packages**

```bash
pip install picamera[array]
sudo apt-get update && sudo apt-get upgrade -y
sudo apt install cmake build-essential pkg-config git
sudo apt install libjpeg-dev libtiff-dev libjasper-dev libpng-dev libwebp-dev libopenexr-dev
sudo apt install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libdc1394-22-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev
sudo apt install libgtk-3-dev libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
sudo apt install libatlas-base-dev liblapacke-dev gfortran
sudo apt install libhdf5-dev libhdf5-103
sudo apt install python3-dev python3-pip python3-numpy
```

---

### **2. Expand the Swapfile**

Edit the swapfile configuration:

```bash
sudo nano /etc/dphys-swapfile
```

Change `CONF_SWAPSIZE` from **100** to **2048**, save, and exit.

Restart the swap service:

```bash
sudo systemctl restart dphys-swapfile
```

---

### **3. Clone OpenCV Repository**

Download the OpenCV zip file from [here](https://drive.google.com/drive/folders/15bBAxoo3BQorAz2CX8p6RiTv2jzRqhNv?usp=drive_link) and unzip it.

---

### **4. Build OpenCV**

Create a build directory:

```bash
mkdir ~/opencv/build
cd ~/opencv/build
```

---

### **5. CMake Configuration**

Install necessary dependencies and configure the build:

```bash
cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
      -D ENABLE_NEON=ON \
      -D ENABLE_VFPV3=ON \
      -D BUILD_TESTS=OFF \
      -D INSTALL_PYTHON_EXAMPLES=OFF \
      -D OPENCV_ENABLE_NONFREE=ON \
      -D CMAKE_SHARED_LINKER_FLAGS=-latomic \
      -D BUILD_EXAMPLES=OFF ..
```

Optional CMake file command:

```bash
cmake ..
```

---

### **6. Compile OpenCV**

This process will take over an hour and may appear frozen. Be patient:

```bash
make -j$(nproc)
```

---

### **7. Common Errors**

* **Error:** `fatal error: ImfChromaticities.h: No such file or directory`

```bash
sudo apt-get install libopenexr-dev
```

* **Error:** `fatal error: webp/decode.h: No such file or directory`

```bash
sudo apt-get install libwebp-dev
```

* **Update pip and setuptools**

```bash
pip install --upgrade pip setuptools
```

---

