from pydub import AudioSegment

def optimize_audio(file_path, target_path):
    # Загрузка исходного аудиофайла
    audio = AudioSegment.from_file(file_path)

    # Преобразование аудио в моно
    audio = audio.set_channels(1)

    # Установка частоты дискретизации 16000 Гц
    audio = audio.set_frame_rate(16000)

    # Экспорт аудио в формате WAV с параметрами кодирования PCM 16 бит
    audio.export(target_path, format="wav", codec="pcm_s16le")

# Путь к исходному аудиофайлу
file_path = '/home/vasily/Загрузки/Project_test/Project_test/archive/harvard.wav'

# Путь, куда будет сохранён оптимизированный файл
target_path = '/home/vasily/Загрузки/Project_test/Project_test/harvard_re.wav'

optimize_audio(file_path, target_path)