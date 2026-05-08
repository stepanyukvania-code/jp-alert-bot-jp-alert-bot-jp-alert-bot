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

        page.wait_for_timeout(7000)

        cards = page.query_selector_all("[data-testid='item-cell']")

        for c in cards:
            try:
                title_el = c.query_selector("a")
                if not title_el:
                    continue

                title = title_el.inner_text().strip()
                href = title_el.get_attribute("href")

                price_el = c.query_selector("span")
                price = price_el.inner_text().strip() if price_el else ""

                if not title or not href:
                    continue

                results.append({
                    "title": title,
                    "url": "https://www.mercari.com" + href,
                    "price": price
                })

                if len(results) >= limit:
                    break

            except:
                continue

        browser.close()

    return results
