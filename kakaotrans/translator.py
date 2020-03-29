# -*- coding: utf-8 -*-
import requests

from kakaotrans.constants import LANGUAGES, DEFAULT_USER_AGENT, BASE_URL


class Translator(object):
    """ 
    Kakao Translate ajax API implemenation class

    You have to create an instance of Translator to use this API
    """

    def __init__(self, service_url=None, user_agent=DEFAULT_USER_AGENT):

        self.service_url = service_url or BASE_URL

        self.headers = {
            "Host": "translate.kakao.com",
            "Connection": "keep-alive",
            "Accept": "*/*",
            "Origin": "https://translate.kakao.com",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": user_agent,
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Referer": "https://translate.kakao.com/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6"
        }

    def translate(self, query, src='en', tgt='kr', separate_lines=False,
                  save_as_file=False, file_name=None):
        """
        Translate text from source language to target langauge

        :param query: The source text to be translated
        :param src: Source language. You can set as 'auto' for auto detecting the source language.
        :param tgt: Target Language
        :param separate_lines: If this is set as True, this function will return the list of translated sentences
        :param save_as_file: Whether save the translated result as file or not
        :param file_name: File name for saving the result. 
        :return: Translated Text
                 If separate_line==False, return the translated result in one sentence
                 If separate_line==True, return the list of multiple translated sentences

        Basic usage:
            >>> from kakaotrans import Translator
            >>> translator = Translator()
            >>> translator.translate("Try your best rather than be the best.")
            '최고가 되기보다는 최선을 다하라.'
        """
        # To replace multiple whitespace to single whitespace
        # This helps the translator to understand the query and split the sentences more clearly
        query = ' '.join(query.strip().split())

        # Assert language code
        if src != 'auto' and src not in LANGUAGES:
            raise ValueError('Invalid source language')
        if tgt not in LANGUAGES:
            raise ValueError('Invalid target language')
        if src == tgt:
            raise ValueError("Source language and Target language cannot be same")

        # Send the POST request
        params = {
            'queryLanguage': src,
            'resultLanguage': tgt,
            'q': query
        }
        response = requests.post(self.service_url, headers=self.headers, data=params)

        # Check whether the status code is 200
        if response.status_code != 200:
            raise Exception("Response Error")

        translated_lines = response.json()['result']['output'][0]

        # Save the result as file
        if save_as_file and not file_name:
            raise ValueError("You must specified the filename if you want to save the result as file.")

        if save_as_file:
            with open(file_name, 'w', encoding='utf-8') as f:
                for line in translated_lines:
                    f.write(line + '\n')

        if separate_lines:
            return translated_lines
        else:
            return ' '.join(translated_lines)
