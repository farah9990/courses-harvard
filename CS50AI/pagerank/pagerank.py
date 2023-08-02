import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    s = {}

    # k => link
    if len(corpus[page]) == 0:
        for k in corpus:
            s[k] = 1 / len(corpus)
    else:
        for k in corpus:
            s[k] = (1 - damping_factor) / len(corpus)

        for k in corpus[page]:
            s[k] += damping_factor / len(corpus[page])
    # Return a probability distribution
    return s


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    s = {}
    for page in corpus:
        s[page] = 0
    # page choice is picked at random:
    page = random.choice(list(corpus.keys()))

    for i in range(1, n):
        distribution = transition_model(corpus, page, damping_factor)
        for page in s:
            s[page] = ((i-1) * s[page] + distribution[page]) / i

        page = random.choices(list(s.keys()), list(s.values()), k=1)[0]
    # Return a dictionary
    return s


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    r = {}
    # calculate
    for key in corpus:
        r[key] = 1 / len(corpus)
    # if false condation stop
    while True:
        count = 0
        for key in corpus:
            new = (1 - damping_factor) / len(corpus)
            sigma = 0
            for page in corpus:
                if key in corpus[page]:
                    num_links = len(corpus[page])
                    sigma = sigma + r[page] / num_links

            sigma = damping_factor * sigma
            new += sigma
            if abs(r[key] - new) < 0.001:
                count += 1
            r[key] = new

        if count == len(corpus):
            break
    # Return a dictionary
    return r
# end metnods


if __name__ == "__main__":
    main()