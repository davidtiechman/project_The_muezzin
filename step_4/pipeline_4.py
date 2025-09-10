from decoding_and_processing_a_word_list.decryption_encrypted import decrypt_base64
from decoding_and_processing_a_word_list.generates_related_words import generate_related_words
from decoding_and_processing_a_word_list.processing_word_list import clean_list_word
from text_classification.connects_related_words import connect_words
from text_classification.hazard_calculation import hazard_calculation
from text_classification.hazard_level_calculation import hazard_level_calculation
from text_classification.processor import process_text
from text_classification.score_text import get_score


def added_score_filed(audio_text):
    list_host = decrypt_base64('R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT')
    list_not_host = decrypt_base64('RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ==')
    list_host = clean_list_word(str(list_host))
    list_not_host = clean_list_word(str(list_not_host))
    list_of_related_words_host = generate_related_words(list_host)
    list_of_related_words_not_host = generate_related_words(list_not_host)
    cleaning_audio_text = process_text(audio_text)
    connect_audio_text = connect_words(cleaning_audio_text,list_of_related_words_host)
    connect_audio_text = connect_words(connect_audio_text,list_of_related_words_not_host)
    bds_percent = get_score(connect_audio_text,list_host,list_not_host)
    is_bds = hazard_calculation(bds_percent)
    bds_threat_level = hazard_level_calculation(is_bds)
    return is_bds, bds_percent, bds_threat_level
