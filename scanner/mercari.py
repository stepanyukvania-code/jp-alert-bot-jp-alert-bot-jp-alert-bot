from playwright.sync_api import sync_playwright


def search(keyword, limit=20):
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(
            f"https://www.mercari.com/jp/search/?keyword={keyword}",
            timeout=60000
        )

        page.wait_for_timeout(5000)

        cards = page.query_selector_all("a")

        for c in cards:
            try:
                text = (c.inner_text() or "").strip()
                href = c.get_attribute("href")

                if not text or not href:
                    continue

                if "mercari" not in href:
                    continue

                results.append({
                    "title": text,
                    "url": href,
                    "price": ""
                })

                if len(results) >= limit:
                    break

            except:
                continue

        browser.close()

    return results
