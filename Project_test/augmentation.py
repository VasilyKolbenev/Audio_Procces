from pydub import AudioSegment

def modify_audio(file_path, speed_factor=1.0, volume_change=0.0):
    audio = AudioSegment.from_file(file_path, format="wav")

    # Изменение скорости воспроизведения
    new_audio = audio.speedup(playback_speed=speed_factor)

    # Изменение громкости
    new_audio = new_audio + volume_change

    # Сохранение измененного файла
    modified_file_path = file_path.replace(".wav", "_modified.wav")
    new_audio.export(modified_file_path, format="wav")
    print(f"Modified audio saved at: {modified_file_path}")

# Пример вызова функции:
modify_audio('/home/vasily/Загрузки/Project_test/Project_test/splin.wav', speed_factor=2.0, volume_change=10)