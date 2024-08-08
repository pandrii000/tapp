# TAPP: Target Tracking with Python

## Overview

TAPP is a Python-based tool designed for tracking objects in real-time video streams using OpenCV and Pygame. This project is part of a drone-target tracking system and utilizes optical flow algorithms to follow objects across frames. It also includes keyboard controls to start and stop tracking.

## Features

- **Real-time video capture**: Utilizes the camera feed for live video processing.
- **Optical flow tracking**: Implements the Lucas-Kanade method for tracking points across video frames.
- **Keyboard controls**: Allows users to start (`1` key) and stop (`0` key) tracking, as well as exit the program (`ESC` key).
- **Pygame integration**: Displays the video feed and tracking points using Pygame.

## Installation

### Prerequisites

- Python 3.9
- Poetry for dependency management

### Dependencies

The following Python packages are required:

- `opencv-python < 4.8`
- `numpy < 2`
- `pynput ^1.7.7`
- `pygame ^2.6.0`

### Setup

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd drone-target-tracking/scripts/2024-08-08-test-task/tapp
    ```

2. Install dependencies using Poetry:

    ```bash
    poetry install
    ```

3. Ensure your camera is connected and working.

## Usage

1. Run the application:

    ```bash
    poetry run python main.py
    ```

2. Use the following keyboard controls:
   - Press `1` to start tracking.
   - Press `0` to stop tracking.
   - Press `ESC` to exit the application.

## Project Structure

- **main.py**: The entry point of the application, orchestrating the camera, tracker, streamer, and keyboard input.
- **tapp/camera.py**: Handles video capture from the camera.
- **tapp/keyboard_input.py**: Manages keyboard inputs to control tracking.
- **tapp/tracker.py**: Implements the optical flow tracking logic.
- **tapp/streamer.py**: Manages the display of video frames and tracking points using Pygame.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss potential changes.
