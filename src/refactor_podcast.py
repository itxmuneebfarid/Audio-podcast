# def refactor_podcast(podcast):
#     speaker1_lines = podcast.get("speaker1", [])
#     speaker2_lines = podcast.get("speaker2", [])

#     refactored_podcast = zip(speaker1_lines, speaker2_lines)

#     return refactored_podcast
def refactor_podcast(podcast):
    speaker1_lines = podcast.get("speaker1", [])
    speaker2_lines = podcast.get("speaker2", [])

    # Fill to equal length
    max_len = max(len(speaker1_lines), len(speaker2_lines))
    speaker1_lines += [""] * (max_len - len(speaker1_lines))
    speaker2_lines += [""] * (max_len - len(speaker2_lines))

    return list(zip(speaker1_lines, speaker2_lines))



