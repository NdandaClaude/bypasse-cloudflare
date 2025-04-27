from src.cf_bypass import bypass_cloudflare

if __name__ == "__main__":
    # Remplacez ces valeurs par celles de votre cible
    bypass_cloudflare(
        url="https://EXEMPLE.com/chemin",
        iframe_prefix='@sre^https://challenges.cloudflare.com/cdn-cqf',
        element_selector='[data-testid="challenge-button"]',
        wait_time=5
    )
