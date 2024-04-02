def get_last_vct_emea_match_id(team:str) -> str:
    import requests
    from config import Config

    vct_players = {
        "KC": "EIpD89iwA4-iKEFPJubyb6-nidT8q0-tHW4RHpE49Y2Krh6IMiC8Apr7vm1X8JBqFiwgKoCcdGAY9g",
        "TH": "QNmZT58DJT98C_dNlGGC-XRPk5xDr6gWfY1aodLgbSDfKYzXRCrWdwjAi9Cg-Uh0EwPc2XNJbDa3dA",
        "NAVI": "teY-1GL9BJVMEalg_MUtZRiMF5Bkxygt_fG5PA6Dsbjo9aUaBp36u9kMhLzB2wB8o7go1C6-k6Gw8Q",
        "FNC": "JJMgvLOzWVRmkJcBSFWhlbYBvdR_SxjQwSB8iXH4K_23eLOUSD_2njG_sZ2xXT0KqqgoxclWQrws9Q",
        "VIT": "VWAXBunM2S7Fwv73jlXPTF9Dddi7wcZU2Kk8vg2pTEzD1N7FNO5QD0j0wPsVzgSBXfeLant55qga3Q",
        "KOI": "o72AmRwLKq0OTwNFTCFyQzP2uAs5HhsHojWcbfRdIPNmDe6sHqKS-hLXG1AVB105G2JYoBcz0yrfXg",
        "FUT": "o6SEUhNKiUgpaDYFTP6to_JOvYs6JlhfV-21j0gffNTdt3WAA8zA_Qr7AjXqPEHKaCMC-7-DbhqwDw",
        "TL": "Q7emKsCKVbhsj7e9whb2urTI0ZMg83DrEKOo-0W49ubT76XmabKCene3cR64qBEfAJzJ8ZZGsqNtyw",
        "GX": "HIyicJ1Hx2MSTVZbyOqSofL-Kn1pk0g5yyBJzmAkpkwgNslKucQn1kTEVfyNW7NDBgskus7AvglM2A",
        "BBL": "95WKBTFKF_TYTS2lS8jfpq8m2qIP2mYt-HHIjHbyInYfw2rPqcL2zXu8gXW7xPaQhdm8hSurIU1u4w",
        "M8": "xjxtxg0qlYys9jh-v3ffVTulg-2ARiAs5SFVRvQa76naAbSX1NlZsbUj64SG5RmcwHlPQabr3z-mcg"
    }

    url = f"https://esports.api.riotgames.com/val/match/v1/matchlists/by-puuid/{vct_players[team]}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token": Config.RIOT_API_KEY
    }
    match_info = requests.get(url, headers=headers).json()["history"][0]
    return match_info