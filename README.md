# 😴 Drowsiness Detector with Eye Aspect Ratio (EAR)

A **real-time drowsiness detection system** using Eye Aspect Ratio (EAR) to monitor eye closure and alert users immediately when prolonged eye closure is detected, helping prevent accidents due to sleepiness while driving or working.

---

## 🎯 Features

✅ Real-time video feed monitoring  
✅ Calculates Eye Aspect Ratio (EAR) for eye closure detection  
✅ Instant alert (sound/beep) on drowsiness detection  
✅ Lightweight and fast implementation  
✅ Easy to integrate with vehicle monitoring systems or personal productivity setups

---

## 🛠 Tech Stack

- **Python**
- **OpenCV** for real-time video processing
- **dlib / Mediapipe** for facial landmark detection
- **Pygame / playsound** for alert sounds

---

⚙️ How It Works
Uses facial landmark detection to locate eye coordinates.

Calculates Eye Aspect Ratio (EAR) to measure eye openness.

If EAR drops below a set threshold for a specified time, an alert is triggered.

📈 Future Enhancements
SMS/email alerts on drowsiness detection

Integration with vehicle hardware for ignition cut-off or seat vibration

Sleepiness scoring dashboard for analysis

Model optimization for low-power edge devices (Raspberry Pi)

🤝 Contributing
Contributions are welcome! Feel free to fork the repo, open issues, or submit pull requests to enhance functionality.

📧 Contact
For collaboration, suggestions, or queries:

GitHub: Om-Singh-45



🛡 License
This project is licensed under the MIT License.
