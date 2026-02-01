Intelligent Floor Guided Parking

SoftDCar Hackathon – Computer Vision Challenge

Overview:

    This repository contains a computer vision–based autonomous parking solution developed during the SoftDCar Hackathon.

    The task focused on enabling an RC vehicle to navigate and park autonomously using visual cues embedded in an intelligent floor environment.

    The entire system is implemented as a single real-time Python script using a GStreamer-based camera pipeline.

Problem Description: 

    The vehicle was required to:

        1) Follow a green guidance path on the floor.

        2) Stop immediately when a red traffic signal is detected (red line in intelligent floor).

        3) Detect an ArUco marker and stop at a predefined distance in front of it.

        4) Operate using camera input only, without additional sensors.

System Approach: 

    1) Camera and Processing Pipeline:

        Real-time video streaming using GStreamer

        Frame-by-frame image processing in Python

    2) Path Following

        Color-based segmentation in HSV color space

        Detection of green floor markings

        Steering correction based on lateral deviation from the path

    3) Traffic Signal Detection

        Red color detection for traffic light recognition

        Immediate stop command when red signal is present

        Resume motion when signal condition is cleared

    4) ArUco Marker-Based Parking

        Detection of ArUco markers using OpenCV

        Distance estimation based on marker size

        Controlled stopping at a predefined safety distance

Implementation Details: 

    Entire logic implemented in a single Python file to ensure reliability under hackathon constraints

    Modular function structure inside the script for:

        Vision processing

        Decision logic

        Motion control commands

    Designed for low-latency real-time execution

Repository Structure:

intelligent-floor-guided-parking/
├── blackandWhiteFloor.py
├── README.md
└── media/
    ├── images/
    └── videos/

Tools and Technologies: 

    Python

    OpenCV

    GStreamer

    ArUco markers

    Real-time computer vision

Results:

    The system successfully demonstrated:

        Stable green path following

        Reliable stopping behavior at red traffic signals

        Accurate distance-based stopping using ArUco markers

        Real-time autonomous operation in an indoor environment

Limitations and Future Work:

    Introduce PID-based steering control

    Replace color thresholding with learning-based perception

    Modularize into ROS2 nodes

    Integrate additional sensors for robustness

Notes:

This project was developed as part of a time-constrained hackathon and prioritizes robustness, clarity, and real-time performance over architectural complexity.