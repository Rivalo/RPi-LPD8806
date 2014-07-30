import wave
import pyaudio
from raspledstrip.LPD8806 import LPD8806SPI

led_strip = LPD8806SPI(36)

audio_file = wave.open('8k8bitpcm.wav', 'rb')
total_frames = audio_file.getnframes()
gamma = [0x80 | int(pow(float(i) / 255.0, 2.5) * 127.0 + 0.5) for i in range(256)]

display_buffer = [bytearray([0x00, 0x00, 0x00]) for i in xrange(36)]
byte_buffer = [0x00 for i in xrange(36*3)]
paudio = pyaudio.PyAudio()
audio_stream = paudio.open(
    format=paudio.get_format_from_width(audio_file.getsampwidth()),
    channels=audio_file.getnchannels(),
    rate=audio_file.getframerate(),
    output=True
)
def lpush(buffer, byte):
    def lpush_iter(buffer, pos, byte):
        if pos < len(buffer):
            current_byte = buffer[pos]
            buffer[pos] = byte
            lpush_iter(buffer, pos+1, current_byte)
        else:
            return buffer

    lpush_iter(buffer, 0, byte)

bytes = audio_file.readframes(8000)
while bytes:
    audio_stream.write(bytes)
    for byte in bytes:
        reduced_byte = gamma[ord(byte)]
        lpush(display_buffer, bytearray([reduced_byte, reduced_byte, reduced_byte]))
        #print str(display_buffer) + "\n"
        led_strip.update(display_buffer)
    bytes = audio_file.readframes(8000)







