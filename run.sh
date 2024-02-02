#!/bin/bash

# Set the path to the Python interpreter
PYTHON_INTERPRETER=python

# Set the path to the scripts
AUDIO_MODIFIER_SCRIPT=audio_modifier.py
SPEECH_TO_TEXT_SCRIPT=speech_to_text_converter.py

# Function to display usage instructions
usage() {
    echo "Usage: $0 [options]"
    echo "Options:"
    echo "  -a, --audio-modifier    Run audio modifier script with parameters"
    echo "  -s, --speech-to-text    Run speech to text converter script with parameters"
    echo "  -h, --help              Display this help message"
    exit 1
}

# Check if at least one argument is provided
if [ "$#" -lt 1 ]; then
    usage
fi

# Parse command-line options
while [ "$#" -gt 0 ]; do
    case "$1" in
        -a|--audio-modifier)
            shift
            $PYTHON_INTERPRETER $AUDIO_MODIFIER_SCRIPT "$@"
            exit 0
            ;;
        -s|--speech-to-text)
            shift
            $PYTHON_INTERPRETER $SPEECH_TO_TEXT_SCRIPT "$@"
            exit 0
            ;;
        -h|--help)
            usage
            ;;
        *)
            echo "Unknown option: $1"
            usage
            ;;
    esac
done

# If no valid options are provided, display usage instructions
usage