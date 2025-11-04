# Voice Assistant Project

This project is a **Python-based voice assistant** capable of performing various tasks such as playing songs on YouTube, telling the current time, searching Wikipedia, telling jokes, and answering basic questions about itself.

---

## Features

* **Play YouTube videos**: Say a command like `partner play <song name>` and it will open YouTube and play the requested song.
* **Check the current time**: Say `partner time` and the assistant will respond with the current time.
* **Search Wikipedia**: Say `partner search <topic>` to get a brief summary from Wikipedia.
* **Jokes**: Say `partner joke` to hear a random joke using `pyjokes`.
* **Personalized answers**: Responds to questions like:

  * `who is your creator`
  * `what can you do`
  * `who are you`

---

## Requirements

* Python 3.x
* Libraries:

  * `speechrecognition`
  * `pyttsx3`
  * `pywhatkit`
  * `wikipedia`
  * `pyjokes`
  * `pyaudio` (for microphone input)

You can install the required libraries using pip:

```bash
pip install SpeechRecognition pyttsx3 pywhatkit wikipedia pyjokes pyaudio
```

---

## How to Run

1. Clone or download the project.
2. Make sure your microphone is set up and working.
3. Run the Python script:

```bash
python voice_assistant.py
```

4. Speak commands starting with the wake word `partner`. For example:

* `partner play Shape of You`
* `partner time`
* `partner search Python programming`
* `partner joke`
* `partner who is your creator`

---

## Notes

* The assistant uses **Google Speech Recognition** for converting speech to text.
* The wake word is currently set as `"partner"`. You can replace it with any other name by modifying the `take_command()` function.
* The assistant responds via **text-to-speech** using `pyttsx3`.
* Ensure you have an active internet connection for YouTube and Wikipedia searches.

---

## Customization

To change the wake word from `partner` to something else:

```python
if 'buddy' in command:  # replace 'buddy' with your desired name
    command = command.replace('buddy', '')
```

You can also customize the responses in the `run_partner()` function to make it more interactive or professional.

---

## Author

Created by **Praveen** as a simple voice assistant project to demonstrate speech recognition and text-to-speech capabilities in Python.

---

## License

This project is open source and free to use for learning and personal projects.
