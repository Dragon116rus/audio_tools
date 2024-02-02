import librosa
import soundfile as sf
import argparse

def modify_audio(input_file: str, output_file: str, speed_factor: float = 1.0, volume_factor: float = 1.0) -> None:
    """
    Modify the speed and volume of an audio file and save the result.

    Parameters:
        - input_file (str): Path to the input audio file.
        - output_file (str): Path to save the modified audio file.
        - speed_factor (float, optional): Factor to modify the speed of the audio (default is 1.0).
        - volume_factor (float, optional): Factor to modify the volume of the audio (default is 1.0).

    Returns:
        None
    """
    # Load audio file
    data, sampling_rate = librosa.load(input_file)

    # Modify speed
    data = librosa.effects.time_stretch(data, rate=speed_factor)

    # Modify volume
    data = data * volume_factor

    # Write the modified audio to a new file
    sf.write(output_file, data, sampling_rate)

def main():
    parser = argparse.ArgumentParser(description="Modify the speed and volume of an audio file.")
    parser.add_argument("--input_file", type=str, help="Path to the input audio file.", required=True)
    parser.add_argument("--output_file", type=str, help="Path to save the modified audio file.", default="output.wav")
    parser.add_argument("--speed_factor", type=float, default=1.0, help="Factor to modify the speed of the audio (default is 1.0).")
    parser.add_argument("--volume_factor", type=float, default=1.0, help="Factor to modify the volume of the audio (default is 1.0).")

    args = parser.parse_args()
    modify_audio(args.input_file, args.output_file, args.speed_factor, args.volume_factor)

if __name__ == "__main__":
    main()