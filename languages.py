import os
import json
import logging

languages_map = {}

def __parse_languages_map():
    try:
        langs_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'languages.json')
        logging.debug('Loading languages from ' + langs_file_path)
        fp = open(langs_file_path)
        globals()['languages_map'] = json.load(fp)
        fp.close()
    except BaseException:
        raise 

def langs():
    if globals()['languages_map'] == None or len(globals()['languages_map']) == 0:
        __parse_languages_map()

    return globals()['languages_map']

# returns apple language id (i.e. 'French_CA') for language name (i.e. 'Canadian French') or code (i.e. 'fr-CA')
def appleLangIdForLanguage(languageString):
    lang = langs().get(languageString)
    if lang != None:
        if type(lang) is dict:
            return lang['name']

        return lang

    for langId in langs():
        lang = langs()[langId]
        if type(lang) is dict:
            if lang['name'] == languageString:
                return lang['id']
        else:
            if lang == languageString:
                return lang
                
    return None

# returns language code (i.e. 'fr-CA') for language name (i.e. 'Canadian French') or apple language id (i.e. 'French_CA')
def langCodeForLanguage(languageString):
    for langId in langs():
        lang = langs()[langId]
        if type(lang) is dict:
            if (lang['name'] == languageString) or (lang['id'] == languageString):
                return langId
        else:
            if lang == languageString:
                return langId
                
    return None

def languageNameForId(languageId):
    lang = langs()[languageId]
    if type(lang) is dict:
        return lang['name']

    return lang
