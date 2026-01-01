
# Receives the results, processes them and returns them
def display_results(query_results) -> tuple[str | None, str | None]:
    matches = query_results.get('matches', [])
    if not matches:
        print("No matches found.")
        return None, None
    text = None
    target_id = None
    for match in matches:
        match_id = match.get('id')
        score = match.get('score')
        print(f"ID: {match_id}, Score: {score}")

        metadata = match.get('metadata', {})
        if 'text' in metadata:
            print()
            #print(f"Text: {metadata['text']}")
        else:
            print("No metadata available.")

    # Get text and ID from the best match (first result)
    best_match = matches[0]
    target_id = best_match.get('id')
    metadata = best_match.get('metadata', {})
    text = metadata.get('text')
    return text, target_id