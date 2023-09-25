
import json
import os
import requests
from dotenv import load_dotenv
load_dotenv()


def scrape_profile(profile_url: str):
    """
    scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile
    """

    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    response = requests.get(
        api_endpoint,
        params={
            'url': profile_url,
            'fallback_to_cache': 'on-error',
            'use_cache': 'if-present',
            'skills': 'include',
            'inferred_salary': 'include',
            'personal_email': 'include',
            'personal_contact_number': 'include',
            'twitter_profile_id': 'include',
            'facebook_profile_id': 'include',
            'github_profile_id': 'include',
            'extra': 'include',
        },
        headers=header_dic
    )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None) and k not in ["people_also_viewed", "similarly_named_profiles"]
    }

    return data


def create_json(profile):

    # run the LinkedIn scraper
    # profile = 'https://www.linkedin.com/in/patrickwalsh6079/'
    name = profile.split('/')[-2]
    # print(name)
    linkedin_scraper = scrape_profile(profile_url=profile)


    # save to file
    # Serializing json
    json_object = json.dumps(linkedin_scraper, indent=4)

    # Writing to JSON file
    with open(f"./data/{name}.json", "w") as outfile:
        outfile.write(json_object)

    print('Successfully scraped LinkedIn profile!')
