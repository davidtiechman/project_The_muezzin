from audio_transcription.transcription_audio_to_text import Transcription
from decoding_and_processing_a_word_list.decryption_encrypted import decrypt_base64
from decoding_and_processing_a_word_list.processing_word_list import clean_list_word

trna = Transcription()
# text = trna.transcribe('audio_transcription/download (1).wav')
# print(text)
list_host = decrypt_base64('R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT')
list_not_host = decrypt_base64('RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ==')
list_host = clean_list_word(str(list_host))
list_not_host = clean_list_word(str(list_not_host))
list_of_related_words_host = []
list_of_related_words_not_host = []
# list_words = clean_list_word(text)
# print(list_words)
# def connecting_related_words(text,list_word):
#     for i in range(len(text)-1):
#         if text[i] + text[i+1] in list_word:
#             text[i] = text[i] + text[i+1]
#     return text

print(list_host)
print(list_not_host)
for word in list_host:
    if " " in word:
        list_of_related_words_host.append(word)
print(list_of_related_words_host)
for word in list_not_host:
    if " " in word:
        list_of_related_words_not_host.append(word)
print(list_of_related_words_not_host)
