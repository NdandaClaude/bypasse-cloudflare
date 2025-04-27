from time import sleep
from DrissionPage import ChromiumPage

def bypass_cloudflare(url, iframe_prefix, element_selector, wait_time=5):
    """
    Automate the browser to interact with an element inside a Cloudflare iframe.
    Arguments:
    - url: The URL to visit.
    - iframe_prefix: The prefix to identify the Cloudflare iframe.
    - element_selector: The CSS selector or identifier for the element to click.
    - wait_time: Seconds to wait before interaction.
    """
    P = ChromiumPage()
    p = P.get(url)

    i = P.get_frame(iframe_prefix)
    if not i:
        print("[ERROR] Iframe introuvable. Vérifiez l'URL ou le sélecteur d'iframe.")
        return

    e = i.find_element(element_selector)
    if not e:
        print("[ERROR] Élément à cliquer introuvable dans l'iframe.")
        return

    print(f"Attente de {wait_time} secondes avant de cliquer...")
    sleep(wait_time)
    e.click()
    print("Clic effectué sur l'élément cible.")

if __name__ == '__main__':
    # Exemple d'utilisation
    bypass_cloudflare(
        url="https://EXEMPLE.com/chemin",               # À personnaliser !
        iframe_prefix='@sre^https://challenges.cloudflare.com/cdn-cqf',
        element_selector='[data-testid="challenge-button"]',  # À personnaliser !
        wait_time=5
    )
