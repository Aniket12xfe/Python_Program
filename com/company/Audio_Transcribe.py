import assemblyai as aai
aai.settings.api_key = "86e37e2173da469d88e8084f43efa839"
audio_url = "https://github.com/Aniket12xfe/ApiTesting/raw/main/Om%20deshmukh.mp4"

transcriber = aai.Transcriber()

transcript = transcriber.transcribe(audio_url)

print(transcript.text)
