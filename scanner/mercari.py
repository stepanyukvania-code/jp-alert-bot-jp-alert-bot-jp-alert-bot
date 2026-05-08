from playwright.sync_api import sync_playwright


def search(keyword, limit=20):
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-blink-features=AutomationControlled"
            ]
        )

        page = browser.new_page()

        page.goto(
            f"https://www.mercari.com/jp/search/?keyword={keyword}",
            timeout=60000
        )

        page.wait_for_timeout(10000)

        html = page.content()

        if "Just a moment" in html or len(html) < 5000:
            print("BLOCKED OR EMPTY PAGE")
            return []

        links = page.query_selector_all("a")

        for a in links:
            try:
                href = a.get_attribute("href")
                text = (a.inner_text() or "").strip()

                if not href or not text:
                    continue

                if "/item/" not in href:
                    continue

                results.append({
                    "title": text,
                    "url": "https://www.mercari.com" + href
                })

                if len(results) >= limit:
                    break

            except:
                continue

        browser.close()

    return results
