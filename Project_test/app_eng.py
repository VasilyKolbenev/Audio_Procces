from vosk import Model, KaldiRecognizer
import wave
import json
import os

def transcribe_audio_vosk(audio_path, model_path, json_path):
    # Загрузка модели Vosk
    model = Model(model_path)
    
    # Открытие аудиофайла
    with wave.open(audio_path, "rb") as wf:
        # Проверка соответствия параметров аудио для Vosk
        if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
            print("Audio file must be WAV format with mono PCM.")
            return

        # Создание распознавателя с использованием модели
        recognizer = KaldiRecognizer(model, wf.getframerate())

        # Распознавание аудио
        results = []
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                results.append(json.loads(recognizer.Result()))

        # Добавление последнего частичного результата
        results.append(json.loads(recognizer.FinalResult()))

    # Сохранение результатов в JSON-файл
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4)

    # Вывод распознанного текста
    for result in results:
        if result is not None and 'text' in result:
            print(result['text'])

# Путь к вашему аудиофайлу и модели
audio_path = "/home/vasily/Загрузки/Project_test/Project_test/harvard_re.wav"
model_path = "/home/vasily/Загрузки/Project_test/vosk-model-small-en-us-0.15"
json_path = "/home/vasily/Загрузки/Project_test/Project_test/transcription_en.json" 

transcribe_audio_vosk(audio_path, model_path, json_path)