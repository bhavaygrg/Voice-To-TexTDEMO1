# VoiceNotes++

## 🎙️ About VoiceNotes++

VoiceNotes++ is your friendly companion in the world of online learning and lectures. It's not just another transcription tool; it's your study buddy, making online classes more accessible, productive, and fun!

## 🌟 Key Features

- **Instant Transcription:** Effortlessly convert spoken words into text in real-time.
- **Enhanced Productivity:** Focus on learning while VoiceNotes++ takes care of the note-taking.
- **User-Friendly:** Intuitive and easy-to-use interface for students and educators.
- **Aesthetic Appeal:** Beautiful NFTs and graphics for an enjoyable experience.
- **GitHub Integration:** Automatically push your transcriptions to your GitHub repository.

## 🚀 Getting Started

1. Clone this repository.
2. Install the necessary dependencies (Python, FFmpeg, and required Python libraries).
3. use ```
4.       ffmpeg -i <Your_Video_name> -vn -acodec pcm_s16le -ar 44100 -ac 2 sample_audio.wav
5.       python final_text.py , now a markdown file will be created for the ouput.
6.       python git_push.py
7. Your transcriptions will be automatically pushed to your GitHub repository.

## Inspiration
VoiceNotes++ was inspired by the challenges students and educators faced during the shift to online classes. As the demand for effective note-taking and transcription solutions grew, this project emerged to simplify capturing spoken content during virtual lectures. Its mission is to enhance accessibility and productivity in online education, providing students with a valuable tool to transcribe lectures, create study materials, and improve their overall learning experience.

## What it does
VoiceNotes++ is a voice-to-text transcription tool designed to simplify the process of converting spoken content into written text. It empowers students and educators during online classes by allowing them to effortlessly transcribe lectures, discussions, and presentations. Users can create study notes, review lecture content, and enhance their overall learning experience. VoiceNotes++ streamlines the capture of spoken information, making it a valuable asset for remote education and improving accessibility and productivity in the online learning environment.

## How we built it
For the development of VoiceNotes++, we primarily utilized Python as the core programming language, leveraged FFmpeg for audio handling and manipulation, employed the SpeechRecognition library for voice-to-text transcription, integrated pydub for audio processing, harnessed OpenCV for computer vision tasks, and managed version control and collaboration through GitHub and the PyGithub library, ultimately creating an efficient and accessible voice-to-text transcription tool for online classes and lectures.

## Challenges we ran into
- Ensuring accurate transcription across varying audio qualities, including background noise and different accents, required robust audio preprocessing and recognition techniques.
- Handling large audio files efficiently to prevent performance issues and long processing times was a technical hurdle.
- Optimizing the tool for both speed and accuracy in transcription, especially when dealing with longer audio recordings, required fine-tuning.

## Accomplishments that we're proud of
- Shobhit is proud of completing his first python based project.
- Bhavay is proud of handling audio quality variations and optimizing the project.
- Shobhit is proud of our project's technical achievements and its role in enhancing accessibility and 
   productivity in education.
- Both of us take pride in how our project effectively addresses real-world problems in real-time.

## What we learned
- Projects that solve real-life problems are the most fulfilling and enjoyable to build.
- Collaboration is the key.
- Innovation Sparks in Constraints: Innovation thrives under constraints, as tight deadlines encourage creative thinking.

## What's next for VoiceNotes++
- We are planning to enhance the project as a whole and then publish it as a browser extension.
- Better way of using this it in real-time.
- Hosting VoiceNotes++ independently


## 🌐 Collaborate and Contribute

We welcome collaborators and contributors! Feel free to fork this repository and submit your contributions via pull requests. Let's make online learning better together.

## 📜 License

This project is licensed under the [MIT License](LICENSE), so feel free to use, modify, and share it as you see fit.

## 📧 Contact

Have questions, suggestions, or just want to chat? Reach out to us at [Bhavay](mailto:gargbhavay78@gmail.com).

Happy Learning with VoiceNotes++! 📚🎉
