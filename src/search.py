from duckduckgo_search import DDGS


def search_web(sport: str, max_results: int = 3):
    """
    Search DuckDuckGo for recent information related to the selected sport.

    Args:
        sport (str): Name of the sport.
        max_results (int): Maximum number of search results.

    Returns:
        list: A list of text snippets containing titles and summaries.
    """

    query = f"Latest {sport} news, facts, records, tournaments"

    snippets = []

    try:
        with DDGS() as ddgs:

            results = ddgs.text(
                query,
                max_results=max_results
            )

            for result in results:

                title = result.get("title", "").strip()
                body = result.get("body", "").strip()

                if title or body:
                    snippets.append(
                        f"{title}\n{body}"
                    )

    except Exception as e:
        print(f"DuckDuckGo Search Error: {e}")

    return snippets