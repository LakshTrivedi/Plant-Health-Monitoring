# 🌿 Plant Health Monitoring System

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Issues](https://img.shields.io/github/issues/LakshTrivedi/Plant-Health-Monitoring)](https://github.com/LakshTrivedi/Plant-Health-Monitoring/issues)
[![Forks](https://img.shields.io/github/forks/LakshTrivedi/Plant-Health-Monitoring)](https://github.com/LakshTrivedi/Plant-Health-Monitoring/network/members)
[![Stars](https://img.shields.io/github/stars/LakshTrivedi/Plant-Health-Monitoring)](https://github.com/LakshTrivedi/Plant-Health-Monitoring/stargazers)

A smart machine learning-powered application that predicts the health of plants based on key environmental and physiological parameters. It provides real-time insights to help farmers and researchers monitor and optimize plant health, prevent stress, and enhance crop productivity.

---

## 🧠 How It Works

1. Collects environmental and soil data (e.g., nitrogen, potassium, humidity, chlorophyll).
2. Applies a trained machine learning model to classify the plant health as:
   - Healthy 🌱
   - Moderate Stress 🌾
   - Stressed 🥀
3. Displays predictions in a simple web interface built with Flask.

---

## 🏗️ System Architecture

```mermaid
graph TD;
    User -->|Input Parameters| WebApp[Flask Web Interface]
    WebApp -->|Send Data| Model[Trained ML Model]
    Model -->|Health Status| WebApp
    WebApp -->|Display Results| User
