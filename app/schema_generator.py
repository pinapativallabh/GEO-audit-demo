def generate_schema(title, headings, url):
    title_lower = title.lower()

    if "product" in title_lower:
        return {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": title,
            "url": url
        }

    if "blog" in title_lower or "article" in title_lower:
        return {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": title,
            "url": url
        }

    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": title,
        "url": url
    }