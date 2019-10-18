import requests
import urllib.request

def getauthentication():
    """fetch a session key from WikiArt"""
    params = {}
    params['accessCode'] = 'b30313a21b6a4d36'
    params['secretCode'] = '85596c6bdea12adf'
    url = 'https://www.wikiart.org/en/Api/2/login'

    try:
        response = requests.get(url,
                                params=params,
                                timeout=120)
        response.raise_for_status()
        data = response.json()
        return data['SessionKey']

    except Exception as error:
        #Logger.write('Error %s' % str(error))
        print('rip, chip')

def getArtistList():


def copy_everything(self):
    """Download A Copy of Every Single Painting."""
    Logger.write('\nCopying paintings:')
    if not self.painting_groups:
        raise RuntimeError('Painting groups not found. Cannot continue.')

    show_progress_at = max(1, int(.1 * len(self.painting_groups)))

    # Retrieve copies of every artist's painting.
    for i, group in enumerate(self.painting_groups):
        for painting in group:
            self.download_hard_copy(painting)

        if i % show_progress_at == 0:
            Logger.info('%i%% done' % (100 * (i + 1) // len(self.painting_groups)))

    return self


print(getauthentication())